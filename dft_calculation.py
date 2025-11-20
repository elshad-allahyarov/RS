#!/usr/bin/env python3
"""
DFT-based FTIR Calculation using RDKit + Semi-empirical methods
"""

import numpy as np
import sys

print("\n" + "="*70)
print("PART 2: DFT/QUANTUM MECHANICAL FTIR CALCULATION")
print("="*70)

# Try to import required packages
print("\nChecking for quantum chemistry packages...")

packages_available = {}

try:
    from rdkit import Chem
    from rdkit.Chem import AllChem, Descriptors
    packages_available['rdkit'] = True
    print("✓ RDKit found")
except ImportError:
    packages_available['rdkit'] = False
    print("✗ RDKit not available")

try:
    import psi4
    packages_available['psi4'] = True
    print("✓ Psi4 found (full DFT capability!)")
except ImportError:
    packages_available['psi4'] = False
    print("✗ Psi4 not available")

try:
    from ase import Atoms
    from ase.calculators.emt import EMT
    packages_available['ase'] = True
    print("✓ ASE found")
except ImportError:
    packages_available['ase'] = False
    print("✗ ASE not available")

# ===================== Method 1: RDKit with UFF/MMFF Force Field =====================

if packages_available['rdkit']:
    print("\n" + "="*70)
    print("Method 1: RDKit Force Field Vibrational Analysis")
    print("="*70)
    
    try:
        # Read MOL2 file
        print("\nReading molecule from MOL2 file...")
        mol = Chem.MolFromMol2File('/workspace/sulfone_molecule.mol2', removeHs=False)
        
        if mol is None:
            print("✗ Failed to read MOL2 with RDKit, trying alternative...")
            # Try reading and adding hydrogens
            mol = Chem.MolFromMol2File('/workspace/sulfone_molecule.mol2', removeHs=True)
            if mol:
                mol = Chem.AddHs(mol)
        
        if mol:
            print(f"✓ Molecule loaded: {mol.GetNumAtoms()} atoms")
            
            # Optimize geometry with MMFF or UFF
            print("\nOptimizing geometry with force field...")
            try:
                # Try MMFF94 first (more accurate for organics)
                props = AllChem.MMFFGetMoleculeProperties(mol)
                ff = AllChem.MMFFGetMoleculeForceField(mol, props)
                ff.Initialize()
                converged = ff.Minimize(maxIts=500)
                print(f"✓ MMFF94 optimization: converged={converged==0}")
                ff_type = "MMFF94"
            except:
                # Fall back to UFF
                ff = AllChem.UFFGetMoleculeForceField(mol)
                converged = ff.Minimize(maxIts=500)
                print(f"✓ UFF optimization: converged={converged==0}")
                ff_type = "UFF"
            
            # Calculate vibrational frequencies (approximate from force field)
            print(f"\nCalculating vibrational frequencies with {ff_type}...")
            print("Note: Force field frequencies are approximate")
            print("      They scale ~0.9-0.95 vs experimental")
            
            # We can't directly get frequencies from RDKit force fields easily
            # But we can estimate from the Hessian if available
            print("\n⚠ RDKit force fields don't provide direct frequency calculation")
            print("   Falling back to enhanced empirical model")
            
            rdkit_available = False
            
        else:
            print("✗ Could not load molecule with RDKit")
            rdkit_available = False
            
    except Exception as e:
        print(f"✗ RDKit calculation failed: {e}")
        rdkit_available = False
else:
    rdkit_available = False
    print("\n⚠ RDKit not available - skipping force field method")

# ===================== Method 2: Psi4 DFT Calculation =====================

if packages_available['psi4']:
    print("\n" + "="*70)
    print("Method 2: Psi4 DFT Calculation (B3LYP/6-31G*)")
    print("="*70)
    print("⚠ WARNING: DFT calculation may take 30-60 minutes for 72 atoms!")
    print("   This will calculate ALL 210 normal modes accurately")
    
    try:
        import psi4
        
        # Convert MOL2 to Psi4 geometry
        print("\nConverting MOL2 to Psi4 format...")
        
        # Read MOL2
        atoms = []
        with open('/workspace/sulfone_molecule.mol2', 'r') as f:
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
                    elem = parts[1]
                    x, y, z = float(parts[2]), float(parts[3]), float(parts[4])
                    atoms.append((elem, x, y, z))
        
        # Create Psi4 geometry string
        geom_str = "0 1\n"  # charge 0, multiplicity 1
        for elem, x, y, z in atoms:
            geom_str += f"{elem} {x:.6f} {y:.6f} {z:.6f}\n"
        
        print(f"✓ Geometry prepared: {len(atoms)} atoms")
        
        # Set up Psi4
        psi4.set_memory('2 GB')
        psi4.set_num_threads(4)
        
        mol_psi4 = psi4.geometry(geom_str)
        
        print("\n Starting DFT optimization...")
        print("   Basis set: 6-31G*")
        print("   Functional: B3LYP")
        print("   This may take 30-60 minutes...")
        
        # Optimize geometry
        psi4.set_options({'basis': '6-31G*'})
        energy, wfn = psi4.optimize('b3lyp', molecule=mol_psi4, return_wfn=True)
        
        print(f"✓ Optimization complete! Energy = {energy:.6f} Hartree")
        
        # Calculate frequencies (Hessian)
        print("\n📊 Calculating vibrational frequencies (Hessian)...")
        print("   This step computes all 210 normal modes...")
        
        freq_data = psi4.frequency('b3lyp/6-31G*', molecule=mol_psi4, return_wfn=False)
        
        # Extract frequencies
        frequencies = wfn.frequencies().to_array()
        intensities = wfn.get_array('IR_INTENSITY')
        
        print(f"✓ Frequency calculation complete!")
        print(f"   Found {len(frequencies)} vibrational modes")
        
        # Save DFT frequencies
        dft_data = np.column_stack([frequencies, intensities])
        np.savetxt('/workspace/dft_frequencies.csv', dft_data,
                  delimiter=',',
                  header='Frequency(cm-1),Intensity(km/mol)',
                  comments='')
        
        print("✓ DFT frequencies saved to dft_frequencies.csv")
        
        psi4_success = True
        
    except Exception as e:
        print(f"\n✗ Psi4 DFT calculation failed: {e}")
        print("   This is common - DFT requires significant computational resources")
        psi4_success = False
else:
    psi4_success = False
    print("\n⚠ Psi4 not available")
    print("   Installing Psi4: conda install -c psi4 psi4")
    print("   Or: pip install psi4")

# ===================== Method 3: Semi-Empirical (GFN-xTB or MOPAC) =====================

print("\n" + "="*70)
print("Method 3: Checking for semi-empirical methods...")
print("="*70)

# Check for xtb (GFN-xTB)
try:
    result = subprocess.run(['xtb', '--version'], capture_output=True, text=True)
    if result.returncode == 0:
        print("✓ GFN-xTB found!")
        print("   Running xTB frequency calculation...")
        
        # Convert MOL2 to XYZ for xTB
        with open('/workspace/molecule.xyz', 'w') as f:
            # Count atoms
            atoms_data = []
            with open('/workspace/sulfone_molecule.mol2', 'r') as mol2:
                lines = mol2.readlines()
            
            section = None
            for line in lines:
                line = line.strip()
                if line.startswith('@<TRIPOS>'):
                    section = line.replace('@<TRIPOS>', '')
                    continue
                
                if section == 'ATOM' and line and not line.startswith('@'):
                    parts = line.split()
                    if len(parts) >= 6:
                        elem = parts[1]
                        x, y, z = parts[2], parts[3], parts[4]
                        atoms_data.append(f"{elem} {x} {y} {z}")
            
            f.write(f"{len(atoms_data)}\n")
            f.write("Sulfone molecule\n")
            for atom_line in atoms_data:
                f.write(atom_line + "\n")
        
        # Run xTB
        print("   Running: xtb molecule.xyz --hess --gfn 2")
        result = subprocess.run(
            ['xtb', 'molecule.xyz', '--hess', '--gfn', '2'],
            cwd='/workspace',
            capture_output=True,
            text=True,
            timeout=600  # 10 minute timeout
        )
        
        if 'normal termination' in result.stdout.lower() or result.returncode == 0:
            print("✓ xTB calculation completed!")
            
            # Parse frequency output
            # xTB creates hessian file, would need to parse it
            print("   Frequency data in: hessian file")
            xtb_success = True
        else:
            print(f"✗ xTB calculation had issues")
            xtb_success = False
            
    else:
        print("✗ xTB not working properly")
        xtb_success = False
        
except (FileNotFoundError, subprocess.TimeoutExpired) as e:
    print("✗ GFN-xTB (xtb) not available")
    print("   Install: conda install -c conda-forge xtb")
    xtb_success = False

print("\n" + "="*70)
print("QUANTUM CALCULATION SUMMARY")
print("="*70)
print(f"RDKit force field: {'✓ Available' if rdkit_available else '✗ Not available'}")
print(f"Psi4 DFT: {'✓ Completed!' if psi4_success else '✗ Not available/failed'}")
print(f"xTB semi-empirical: {'✓ Completed!' if xtb_success else '✗ Not available'}")

if not (psi4_success or xtb_success):
    print("\n⚠ No quantum methods succeeded")
    print("   Using ultra-enhanced empirical model instead")
    print("\n💡 To enable DFT:")
    print("   pip install psi4  (or conda install -c psi4 psi4)")
    print("   conda install -c conda-forge xtb")

print("\n" + "="*70)
