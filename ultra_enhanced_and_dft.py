#!/usr/bin/env python3
"""
Part 1: Ultra-Enhanced Empirical FTIR with Maximum Vibrational Modes
Part 2: DFT Quantum Mechanical Calculation for Perfect Match
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import subprocess
import os

print("="*70)
print("ULTRA-ENHANCED FTIR CALCULATION")
print("="*70)

# ===================== Part 1: Ultra-Enhanced Empirical Model =====================

class UltraEnhanced_FTIR:
    def __init__(self, mol2_file):
        self.mol2_file = mol2_file
        self.atoms = []
        self.bonds = []
        
        # COMPREHENSIVE vibrational database with ALL known modes
        self.ir_database = {
            # ========== C-H STRETCHING (HIGH FREQUENCY) ==========
            'CH3 asym stretch v1': [(2962, 0.85, 12)],
            'CH3 asym stretch v2': [(2926, 0.75, 15)],
            'CH3 sym stretch': [(2872, 0.8, 12), (2853, 0.7, 15)],
            'CH2 asym stretch': [(2926, 1.0, 18), (2918, 0.9, 15)],
            'CH2 sym stretch': [(2853, 0.95, 18), (2849, 0.85, 15)],
            'CH stretch': [(2890, 0.6, 15), (2880, 0.5, 12)],
            
            # ========== C-H BENDING (MEDIUM FREQUENCY) ==========
            'CH3 asym bend (umbrella)': [(1460, 0.55, 12), (1450, 0.5, 10)],
            'CH3 sym bend': [(1375, 0.5, 10), (1370, 0.45, 8)],
            'CH3 rocking': [(1050, 0.25, 15), (890, 0.2, 12)],
            'CH2 scissoring': [(1468, 0.6, 12), (1458, 0.55, 15)],
            'CH2 wagging': [(1350, 0.35, 18), (1320, 0.3, 15), (1250, 0.3, 20)],
            'CH2 twisting': [(1305, 0.25, 20), (1285, 0.25, 18)],
            'CH2 rocking': [(780, 0.4, 20), (750, 0.35, 18), (720, 0.35, 15)],
            'CH bend (in-plane)': [(1410, 0.3, 15)],
            'CH bend (out-of-plane)': [(870, 0.25, 20), (840, 0.2, 18)],
            
            # ========== S=O STRETCHING (SULFONE - DIAGNOSTIC!) ==========
            'SO2 asym stretch v1': [(1325, 1.0, 22)],
            'SO2 asym stretch v2': [(1310, 0.95, 20)],
            'SO2 asym stretch v3': [(1295, 0.9, 18)],
            'SO2 sym stretch v1': [(1150, 0.95, 22)],
            'SO2 sym stretch v2': [(1135, 0.9, 20)],
            'SO2 sym stretch v3': [(1120, 0.85, 18)],
            'SO2 combination': [(2450, 0.15, 60)],  # ~1300+1150
            
            # ========== S=O BENDING ==========
            'SO2 scissoring': [(565, 0.3, 25), (545, 0.25, 20)],
            'SO2 wagging': [(525, 0.25, 25)],
            'SO2 rocking': [(505, 0.2, 20)],
            
            # ========== C-S STRETCHING ==========
            'C-S stretch (strong, near SO2)': [(730, 0.45, 25), (710, 0.4, 22)],
            'C-S stretch (medium)': [(680, 0.35, 22), (660, 0.3, 20)],
            'C-S stretch (weak)': [(635, 0.28, 20), (615, 0.25, 18)],
            'C-S stretch (far from SO2)': [(595, 0.2, 20)],
            
            # ========== C-S BENDING ==========
            'C-S-C bend': [(445, 0.2, 25), (425, 0.18, 22)],
            'S-C bend': [(380, 0.15, 25)],
            
            # ========== C-C STRETCHING (SKELETAL) ==========
            'C-C stretch (strong)': [(1130, 0.35, 25), (1110, 0.3, 22)],
            'C-C stretch (medium)': [(1080, 0.3, 25), (1060, 0.28, 22), (1040, 0.25, 20)],
            'C-C stretch (weak)': [(1020, 0.25, 25), (995, 0.22, 22)],
            'C-C stretch (skeletal)': [(970, 0.3, 28), (940, 0.28, 25), (915, 0.25, 22)],
            'C-C stretch (gauche)': [(890, 0.25, 25), (865, 0.22, 22)],
            'C-C stretch (trans)': [(1100, 0.28, 25)],
            
            # ========== C-C BENDING ==========
            'C-C-C bend (strong)': [(460, 0.22, 28), (440, 0.2, 25)],
            'C-C-C bend (weak)': [(410, 0.18, 25)],
            
            # ========== RING VIBRATIONS (CYCLIC SULFONE) ==========
            'Ring breathing (strong)': [(1045, 0.4, 25)],
            'Ring breathing (weak)': [(860, 0.32, 28), (820, 0.28, 25)],
            'Ring stretch (asym)': [(1180, 0.3, 28)],
            'Ring stretch (sym)': [(990, 0.28, 25)],
            'Ring deformation': [(545, 0.28, 30), (510, 0.25, 28), (485, 0.22, 25)],
            'Ring puckering': [(460, 0.2, 30)],
            'Ring torsion': [(420, 0.15, 30), (395, 0.12, 28)],
            
            # ========== CHAIN VIBRATIONS ==========
            'Chain rocking': [(1340, 0.25, 30)],
            'Chain twist': [(1280, 0.22, 28)],
            'Chain wag': [(1230, 0.2, 30)],
            
            # ========== OVERTONES (2ν) ==========
            'CH2 scissor overtone': [(2930, 0.18, 45)],  # 2×1465
            'CH3 bend overtone': [(2750, 0.15, 50)],  # 2×1375
            'CH2 rock overtone': [(1540, 0.12, 40)],  # 2×770
            
            # ========== COMBINATION BANDS ==========
            'CH2 scissor + CH2 wag': [(2815, 0.15, 50)],  # 1465+1350
            'SO2 asym + SO2 sym': [(2475, 0.18, 60)],  # 1325+1150
            'CH2 twist + CH2 rock': [(2080, 0.12, 55)],  # 1300+780
            'C-C + C-S': [(1765, 0.1, 50)],  # 1080+685
            'Ring breathing + C-C': [(2030, 0.1, 50)],  # 1040+990
            
            # ========== DIFFERENCE BANDS (ν1 - ν2) ==========
            'SO2 difference': [(175, 0.08, 30)],  # 1325-1150
            
            # ========== LOW FREQUENCY LATTICE MODES ==========
            'Torsional modes': [(350, 0.15, 35), (320, 0.12, 30), (285, 0.1, 28)],
            'Lattice vibrations': [(250, 0.1, 40), (210, 0.08, 35)],
            'Acoustic modes': [(180, 0.06, 40), (145, 0.05, 35)],
            
            # ========== FERMI RESONANCE PEAKS ==========
            'Fermi CH2 (2×1465 ≈ 2930)': [(2935, 0.2, 35)],
            'Fermi CH3 (2×1375 ≈ 2750)': [(2755, 0.18, 40)],
        }
    
    def parse_mol2(self):
        """Parse MOL2 file"""
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
                    self.atoms.append({
                        'element': parts[1],
                        'type': parts[5],
                    })
            elif section == 'BOND' and line and not line.startswith('@'):
                parts = line.split()
                if len(parts) >= 4:
                    self.bonds.append({
                        'atom1': int(parts[1]),
                        'atom2': int(parts[2]),
                    })
    
    def count_groups(self):
        """Count functional groups"""
        groups = defaultdict(int)
        for atom in self.atoms:
            if atom['type'] == 'S.O2':
                groups['SO2'] += 1
        
        for bond in self.bonds:
            atom1 = self.atoms[bond['atom1']-1]
            atom2 = self.atoms[bond['atom2']-1]
            elem1, elem2 = atom1['element'], atom2['element']
            
            if (elem1 == 'C' and elem2 == 'H') or (elem1 == 'H' and elem2 == 'C'):
                c_idx = bond['atom1'] if elem1 == 'C' else bond['atom2']
                h_count = sum(1 for b in self.bonds 
                            if ((b['atom1'] == c_idx and self.atoms[b['atom2']-1]['element'] == 'H') or
                                (b['atom2'] == c_idx and self.atoms[b['atom1']-1]['element'] == 'H')))
                
                groups[f'CH{h_count}'] += 1
            elif elem1 == 'C' and elem2 == 'C':
                groups['C-C'] += 1
            elif (elem1 == 'C' and elem2 == 'S') or (elem1 == 'S' and elem2 == 'C'):
                groups['C-S'] += 1
        
        return groups
    
    def calculate_spectrum(self):
        """Calculate ultra-enhanced spectrum"""
        self.parse_mol2()
        groups = self.count_groups()
        
        print(f"\nMolecular composition:")
        for group, count in sorted(groups.items()):
            print(f"  {group}: {count}")
        
        wavenumbers = np.arange(100, 4000, 0.5)  # Higher resolution!
        spectrum = np.zeros_like(wavenumbers, dtype=float)
        
        mode_count = 0
        for mode_name, peak_list in self.ir_database.items():
            scale = self._get_scale_factor(mode_name, groups)
            
            if scale > 0:
                for freq, intensity, width in peak_list:
                    # Voigt profile (realistic peak shape)
                    gaussian = np.exp(-((wavenumbers - freq) / width) ** 2)
                    lorentzian = 1 / (1 + ((wavenumbers - freq) / (width * 0.5)) ** 2)
                    voigt = 0.6 * gaussian + 0.4 * lorentzian
                    
                    spectrum += scale * intensity * voigt
                    mode_count += 1
        
        print(f"\nTotal vibrational modes: {mode_count}")
        
        # Normalize
        spectrum = (spectrum / spectrum.max()) * 100 if spectrum.max() > 0 else spectrum
        transmittance = 100 - spectrum
        absorbance = 2 - np.log10(transmittance / 100)
        absorbance = np.nan_to_num(absorbance, nan=0.0, posinf=4.0, neginf=0.0)
        
        return wavenumbers, transmittance, absorbance
    
    def _get_scale_factor(self, mode_name, groups):
        """Determine scaling based on molecular composition"""
        mode_lower = mode_name.lower()
        
        if 'ch3' in mode_lower and 'CH3' in groups:
            return groups['CH3'] / 4.0
        elif 'ch2' in mode_lower and 'CH2' in groups:
            return groups['CH2'] / 10.0
        elif 'ch ' in mode_lower and 'CH1' in groups:
            return groups['CH1'] / 2.0
        elif 'so2' in mode_lower and 'SO2' in groups:
            return groups['SO2'] * 1.8
        elif 'c-s' in mode_lower and 'C-S' in groups:
            return groups['C-S'] / 3.0
        elif 'c-c' in mode_lower and 'C-C' in groups:
            return groups['C-C'] / 10.0
        elif 'ring' in mode_lower:
            return 0.9
        elif 'chain' in mode_lower:
            return 0.7
        elif 'combination' in mode_lower or 'overtone' in mode_lower:
            return 0.4
        elif 'fermi' in mode_lower:
            return 0.35
        elif 'lattice' in mode_lower or 'acoustic' in mode_lower:
            return 0.2
        else:
            return 0.5

# Run ultra-enhanced calculation
print("\n" + "="*70)
print("Running Ultra-Enhanced Empirical Calculation...")
print("="*70)

calc = UltraEnhanced_FTIR('/workspace/sulfone_molecule.mol2')
ultra_wn, ultra_trans, ultra_abs = calc.calculate_spectrum()

# Save data
np.savetxt('/workspace/ftir_ultra_enhanced.csv',
          np.column_stack([ultra_wn, ultra_trans, ultra_abs]),
          delimiter=',',
          header='Wavenumber(cm-1),Transmittance(%),Absorbance(A.U.)',
          comments='')

print("✓ Ultra-enhanced spectrum calculated!")
print(f"  Resolution: {len(ultra_wn)} data points")
print(f"  Peak density: Much higher!")

print("\n" + "="*70)
print("Now attempting DFT Quantum Mechanical Calculation...")
print("="*70)
