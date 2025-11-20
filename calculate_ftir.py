#!/usr/bin/env python3
"""
FTIR Spectrum Calculator for MOL2 files
Calculates approximate FTIR spectrum based on functional groups and bond types
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import re

class FTIR_Calculator:
    def __init__(self, mol2_file):
        self.mol2_file = mol2_file
        self.atoms = []
        self.bonds = []
        self.bond_dict = defaultdict(list)
        
        # IR frequency database (wavenumber in cm^-1, relative intensity, bandwidth)
        # Format: (center_frequency, intensity, width)
        self.ir_database = {
            'C-H stretch': (2920, 1.0, 30),
            'C-H stretch (CH2)': (2850, 0.9, 25),
            'C-H stretch (CH3)': (2960, 0.85, 25),
            'C-H bend (CH2)': (1465, 0.6, 20),
            'C-H bend (CH3)': (1375, 0.5, 15),
            'C-C stretch': (1000, 0.3, 50),
            'C-S stretch': (650, 0.4, 30),
            'S=O stretch (asymmetric)': (1325, 1.0, 30),
            'S=O stretch (symmetric)': (1140, 0.95, 25),
            'S-O stretch': (1050, 0.4, 30),
            'C-O stretch': (1100, 0.5, 30),
        }
    
    def parse_mol2(self):
        """Parse MOL2 file to extract atoms and bonds"""
        with open(self.mol2_file, 'r') as f:
            lines = f.readlines()
        
        section = None
        for line in lines:
            line = line.strip()
            
            if line.startswith('@<TRIPOS>'):
                section = line.replace('@<TRIPOS>', '')
                continue
            
            if section == 'ATOM' and line and not line.startswith('@'):
                parts = line.split()
                if len(parts) >= 6:
                    atom_id = int(parts[0])
                    atom_type = parts[5]  # SYBYL atom type
                    self.atoms.append({
                        'id': atom_id,
                        'element': parts[1],
                        'type': atom_type,
                        'x': float(parts[2]),
                        'y': float(parts[3]),
                        'z': float(parts[4])
                    })
            
            elif section == 'BOND' and line and not line.startswith('@'):
                parts = line.split()
                if len(parts) >= 4:
                    bond_id = int(parts[0])
                    atom1 = int(parts[1])
                    atom2 = int(parts[2])
                    bond_order = parts[3]
                    self.bonds.append({
                        'id': bond_id,
                        'atom1': atom1,
                        'atom2': atom2,
                        'order': bond_order
                    })
                    self.bond_dict[atom1].append(atom2)
                    self.bond_dict[atom2].append(atom1)
    
    def identify_functional_groups(self):
        """Identify functional groups and bond types"""
        groups = []
        
        # Count atom types
        atom_types = defaultdict(int)
        for atom in self.atoms:
            element = atom['element']
            atom_type = atom['type']
            atom_types[element] += 1
            
            # Specific sulfone detection (S.O2)
            if atom_type == 'S.O2':
                groups.append('sulfone')
        
        # Analyze bonds
        for bond in self.bonds:
            atom1_elem = self.atoms[bond['atom1']-1]['element']
            atom2_elem = self.atoms[bond['atom2']-1]['element']
            atom1_type = self.atoms[bond['atom1']-1]['type']
            atom2_type = self.atoms[bond['atom2']-1]['type']
            bond_order = bond['order']
            
            # C-H bonds
            if (atom1_elem == 'C' and atom2_elem == 'H') or (atom1_elem == 'H' and atom2_elem == 'C'):
                # Count neighbors to determine CH2 vs CH3
                c_atom_id = bond['atom1'] if atom1_elem == 'C' else bond['atom2']
                num_h = sum(1 for b in self.bonds if 
                           (b['atom1'] == c_atom_id or b['atom2'] == c_atom_id) and
                           (self.atoms[b['atom1']-1]['element'] == 'H' or 
                            self.atoms[b['atom2']-1]['element'] == 'H'))
                
                if num_h == 2:
                    groups.append('CH2')
                elif num_h == 3:
                    groups.append('CH3')
                else:
                    groups.append('C-H')
            
            # C-C bonds
            elif atom1_elem == 'C' and atom2_elem == 'C':
                groups.append('C-C')
            
            # C-S bonds
            elif (atom1_elem == 'C' and atom2_elem == 'S') or (atom1_elem == 'S' and atom2_elem == 'C'):
                groups.append('C-S')
            
            # S=O bonds (detected from S.O2 type)
            elif bond_order == '2' and ((atom1_elem == 'S' and atom2_elem == 'O') or 
                                        (atom1_elem == 'O' and atom2_elem == 'S')):
                groups.append('S=O')
        
        return groups
    
    def calculate_spectrum(self, wavenumber_range=(400, 4000), resolution=1):
        """Calculate FTIR spectrum based on functional groups"""
        self.parse_mol2()
        groups = self.identify_functional_groups()
        
        # Count occurrences of each group
        group_counts = defaultdict(int)
        for g in groups:
            group_counts[g] += 1
        
        print(f"\nDetected functional groups:")
        for group, count in sorted(group_counts.items()):
            print(f"  {group}: {count}")
        
        # Create wavenumber array
        wavenumbers = np.arange(wavenumber_range[0], wavenumber_range[1], resolution)
        spectrum = np.zeros_like(wavenumbers, dtype=float)
        
        # Add peaks for each functional group
        peak_list = []
        
        # Sulfone groups (S=O stretching)
        if 'sulfone' in group_counts:
            count = group_counts['sulfone']
            # Asymmetric stretch
            freq, intensity, width = self.ir_database['S=O stretch (asymmetric)']
            spectrum += count * intensity * self.gaussian(wavenumbers, freq, width)
            peak_list.append(('S=O asym stretch', freq, count * intensity))
            
            # Symmetric stretch
            freq, intensity, width = self.ir_database['S=O stretch (symmetric)']
            spectrum += count * intensity * self.gaussian(wavenumbers, freq, width)
            peak_list.append(('S=O sym stretch', freq, count * intensity))
        
        # C-H stretching (CH2 and CH3)
        if 'CH2' in group_counts:
            count = group_counts['CH2']
            freq, intensity, width = self.ir_database['C-H stretch (CH2)']
            spectrum += count * intensity * self.gaussian(wavenumbers, freq, width)
            peak_list.append(('C-H stretch (CH2)', freq, count * intensity))
            
            # CH2 bending
            freq, intensity, width = self.ir_database['C-H bend (CH2)']
            spectrum += count * intensity * self.gaussian(wavenumbers, freq, width)
            peak_list.append(('C-H bend (CH2)', freq, count * intensity))
        
        if 'CH3' in group_counts:
            count = group_counts['CH3']
            freq, intensity, width = self.ir_database['C-H stretch (CH3)']
            spectrum += count * intensity * self.gaussian(wavenumbers, freq, width)
            peak_list.append(('C-H stretch (CH3)', freq, count * intensity))
            
            # CH3 bending
            freq, intensity, width = self.ir_database['C-H bend (CH3)']
            spectrum += count * intensity * self.gaussian(wavenumbers, freq, width)
            peak_list.append(('C-H bend (CH3)', freq, count * intensity))
        
        if 'C-H' in group_counts:
            count = group_counts['C-H']
            freq, intensity, width = self.ir_database['C-H stretch']
            spectrum += count * intensity * self.gaussian(wavenumbers, freq, width)
            peak_list.append(('C-H stretch', freq, count * intensity))
        
        # C-C stretching
        if 'C-C' in group_counts:
            count = group_counts['C-C']
            freq, intensity, width = self.ir_database['C-C stretch']
            spectrum += count * intensity * self.gaussian(wavenumbers, freq, width)
            peak_list.append(('C-C stretch', freq, count * intensity))
        
        # C-S stretching
        if 'C-S' in group_counts:
            count = group_counts['C-S']
            freq, intensity, width = self.ir_database['C-S stretch']
            spectrum += count * intensity * self.gaussian(wavenumbers, freq, width)
            peak_list.append(('C-S stretch', freq, count * intensity))
        
        # S=O bonds (additional to sulfone)
        if 'S=O' in group_counts:
            count = group_counts['S=O']
            freq, intensity, width = self.ir_database['S=O stretch (asymmetric)']
            spectrum += count * intensity * 0.5 * self.gaussian(wavenumbers, freq, width)
        
        # Normalize spectrum
        if spectrum.max() > 0:
            spectrum = spectrum / spectrum.max() * 100
        
        # Convert to transmittance (%)
        transmittance = 100 - spectrum
        
        return wavenumbers, transmittance, peak_list
    
    @staticmethod
    def gaussian(x, center, width):
        """Generate Gaussian peak"""
        return np.exp(-((x - center) / width) ** 2)
    
    def plot_spectrum(self, wavenumbers, transmittance, peak_list, output_file='ftir_spectrum.png'):
        """Plot FTIR spectrum"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Plot spectrum
        ax.plot(wavenumbers, transmittance, 'b-', linewidth=1.5)
        
        # Annotate major peaks
        print(f"\nMajor peaks in FTIR spectrum:")
        peak_list_sorted = sorted(peak_list, key=lambda x: x[2], reverse=True)[:10]
        for name, freq, intensity in peak_list_sorted:
            if intensity > 5:  # Only annotate significant peaks
                idx = np.argmin(np.abs(wavenumbers - freq))
                y_val = transmittance[idx]
                ax.annotate(f'{name}\n{freq:.0f} cm⁻¹', 
                           xy=(freq, y_val),
                           xytext=(freq, y_val - 10),
                           fontsize=8,
                           ha='center',
                           arrowprops=dict(arrowstyle='->', lw=0.5))
                print(f"  {name}: {freq:.0f} cm⁻¹ (intensity: {intensity:.1f})")
        
        # Formatting
        ax.set_xlabel('Wavenumber (cm⁻¹)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Transmittance (%)', fontsize=12, fontweight='bold')
        ax.set_title('Calculated FTIR Spectrum - Sulfone Molecule', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.set_xlim(wavenumbers[-1], wavenumbers[0])  # Reverse x-axis (standard for IR)
        ax.set_ylim(0, 105)
        
        # Add regions
        ax.axvspan(2800, 3000, alpha=0.1, color='red', label='C-H stretch')
        ax.axvspan(1300, 1500, alpha=0.1, color='green', label='C-H bend')
        ax.axvspan(1100, 1400, alpha=0.1, color='blue', label='S=O stretch')
        ax.axvspan(600, 800, alpha=0.1, color='orange', label='C-S stretch')
        
        ax.legend(loc='upper right', fontsize=9)
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"\nSpectrum saved to: {output_file}")
        
        return fig, ax


def main():
    # Initialize calculator
    calc = FTIR_Calculator('/workspace/sulfone_molecule.mol2')
    
    # Calculate spectrum
    wavenumbers, transmittance, peak_list = calc.calculate_spectrum(
        wavenumber_range=(400, 4000),
        resolution=1
    )
    
    # Plot spectrum
    calc.plot_spectrum(wavenumbers, transmittance, peak_list, 
                      output_file='/workspace/ftir_spectrum.png')
    
    # Also save data as CSV
    np.savetxt('/workspace/ftir_spectrum.csv', 
               np.column_stack([wavenumbers, transmittance]),
               delimiter=',',
               header='Wavenumber(cm-1),Transmittance(%)',
               comments='')
    print("\nSpectrum data saved to: ftir_spectrum.csv")


if __name__ == '__main__':
    main()
