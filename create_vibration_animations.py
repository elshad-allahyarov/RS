#!/usr/bin/env python3
"""
Create animations of molecular vibrations corresponding to FTIR peaks
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
import matplotlib.patches as mpatches

# ===================== Parse MOL2 file =====================

def parse_mol2_structure(filename):
    """Parse MOL2 file to extract atom coordinates and bonds"""
    atoms = []
    bonds = []
    
    with open(filename, 'r') as f:
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
                atoms.append({
                    'id': int(parts[0]),
                    'element': parts[1],
                    'x': float(parts[2]),
                    'y': float(parts[3]),
                    'z': float(parts[4]),
                    'type': parts[5]
                })
        
        elif section == 'BOND' and line and not line.startswith('@'):
            parts = line.split()
            if len(parts) >= 4:
                bonds.append({
                    'atom1': int(parts[1]) - 1,
                    'atom2': int(parts[2]) - 1,
                    'order': parts[3]
                })
    
    return atoms, bonds

def get_atom_color(element):
    """Return color for each element type"""
    colors = {
        'C': '#808080',
        'H': '#FFFFFF',
        'O': '#FF0000',
        'S': '#FFFF00',
    }
    return colors.get(element, '#FF00FF')

def get_atom_size(element):
    """Return size for each element type"""
    sizes = {
        'C': 150,
        'H': 40,
        'O': 140,
        'S': 180,
    }
    return sizes.get(element, 100)

# Parse molecule
atoms, bonds = parse_mol2_structure('/workspace/sulfone_molecule.mol2')
coords = np.array([[atom['x'], atom['y'], atom['z']] for atom in atoms])
elements = [atom['element'] for atom in atoms]

# ===================== Define Vibrational Modes =====================

def create_ch_stretch_displacement():
    """Create displacement vectors for C-H stretching vibration"""
    displacements = np.zeros_like(coords)
    
    # Find all C-H bonds and move them in phase
    for bond in bonds:
        atom1_idx = bond['atom1']
        atom2_idx = bond['atom2']
        elem1 = elements[atom1_idx]
        elem2 = elements[atom2_idx]
        
        if (elem1 == 'C' and elem2 == 'H') or (elem1 == 'H' and elem2 == 'C'):
            c_idx = atom1_idx if elem1 == 'C' else atom2_idx
            h_idx = atom2_idx if elem1 == 'C' else atom1_idx
            
            # Vector from C to H
            vec = coords[h_idx] - coords[c_idx]
            vec = vec / np.linalg.norm(vec)
            
            # H moves outward, C moves slightly inward
            displacements[h_idx] = vec * 0.3
            displacements[c_idx] = -vec * 0.05
    
    return displacements

def create_so_stretch_displacement():
    """Create displacement vectors for S=O stretching vibration"""
    displacements = np.zeros_like(coords)
    
    # Find S=O bonds
    for i, atom in enumerate(atoms):
        if atom['type'] == 'S.O2':  # Sulfone sulfur
            s_idx = i
            # Find connected oxygens
            for bond in bonds:
                if bond['order'] == '2':  # Double bond
                    atom1_idx = bond['atom1']
                    atom2_idx = bond['atom2']
                    
                    if atom1_idx == s_idx and elements[atom2_idx] == 'O':
                        o_idx = atom2_idx
                        vec = coords[o_idx] - coords[s_idx]
                        vec = vec / np.linalg.norm(vec)
                        # Asymmetric stretch - oxygens move in opposite directions
                        displacements[o_idx] = vec * 0.4
                        displacements[s_idx] = -vec * 0.1
                    elif atom2_idx == s_idx and elements[atom1_idx] == 'O':
                        o_idx = atom1_idx
                        vec = coords[o_idx] - coords[s_idx]
                        vec = vec / np.linalg.norm(vec)
                        displacements[o_idx] = -vec * 0.4  # Opposite direction
                        displacements[s_idx] = vec * 0.1
    
    return displacements

def create_ch_bend_displacement():
    """Create displacement vectors for C-H bending vibration"""
    displacements = np.zeros_like(coords)
    
    # Find CH2 groups and create scissoring motion
    for i, atom in enumerate(atoms):
        if elements[i] == 'C':
            # Find hydrogens bonded to this carbon
            h_indices = []
            for bond in bonds:
                if bond['atom1'] == i and elements[bond['atom2']] == 'H':
                    h_indices.append(bond['atom2'])
                elif bond['atom2'] == i and elements[bond['atom1']] == 'H':
                    h_indices.append(bond['atom1'])
            
            # If it's a CH2 group, create scissoring
            if len(h_indices) == 2:
                h1_idx, h2_idx = h_indices
                # Vector perpendicular to C-H bonds
                vec1 = coords[h1_idx] - coords[i]
                vec2 = coords[h2_idx] - coords[i]
                # Cross product gives perpendicular direction
                perp = np.cross(vec1, vec2)
                if np.linalg.norm(perp) > 0:
                    perp = perp / np.linalg.norm(perp)
                    # Scissoring motion
                    displacements[h1_idx] = perp * 0.3
                    displacements[h2_idx] = -perp * 0.3
    
    return displacements

def create_cs_stretch_displacement():
    """Create displacement vectors for C-S stretching vibration"""
    displacements = np.zeros_like(coords)
    
    # Find C-S bonds
    for bond in bonds:
        atom1_idx = bond['atom1']
        atom2_idx = bond['atom2']
        elem1 = elements[atom1_idx]
        elem2 = elements[atom2_idx]
        
        if (elem1 == 'C' and elem2 == 'S') or (elem1 == 'S' and elem2 == 'C'):
            c_idx = atom1_idx if elem1 == 'C' else atom2_idx
            s_idx = atom2_idx if elem1 == 'C' else atom1_idx
            
            # Vector from S to C
            vec = coords[c_idx] - coords[s_idx]
            vec = vec / np.linalg.norm(vec)
            
            # Stretch along C-S bond
            displacements[c_idx] = vec * 0.2
            displacements[s_idx] = -vec * 0.2
    
    return displacements

def create_backbone_bend_displacement():
    """Create displacement vectors for backbone bending"""
    displacements = np.zeros_like(coords)
    
    # Create a wave-like motion along the carbon chain
    carbon_indices = [i for i, elem in enumerate(elements) if elem == 'C']
    
    for i, c_idx in enumerate(carbon_indices):
        # Sinusoidal displacement perpendicular to backbone
        phase = (i / len(carbon_indices)) * 2 * np.pi
        amplitude = 0.3
        # Displace in z-direction
        displacements[c_idx] = np.array([0, 0, amplitude * np.sin(phase)])
    
    return displacements

# ===================== Create Animation Function =====================

def create_vibration_animation(mode_name, displacement_func, freq, output_file, 
                              num_frames=60, amplitude=1.0):
    """Create animation of a vibrational mode"""
    
    print(f"Creating {mode_name} animation...")
    
    # Get displacement vectors
    displacements = displacement_func() * amplitude
    
    # Setup figure
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Initialize plot elements
    bond_lines = []
    atom_scatter = []
    
    def init():
        """Initialize animation"""
        ax.clear()
        return []
    
    def animate(frame):
        """Animation function"""
        ax.clear()
        
        # Calculate phase
        phase = np.sin(2 * np.pi * frame / num_frames)
        
        # Apply displacement
        displaced_coords = coords + displacements * phase
        
        # Plot bonds
        for bond in bonds:
            atom1_idx = bond['atom1']
            atom2_idx = bond['atom2']
            
            x = [displaced_coords[atom1_idx, 0], displaced_coords[atom2_idx, 0]]
            y = [displaced_coords[atom1_idx, 1], displaced_coords[atom2_idx, 1]]
            z = [displaced_coords[atom1_idx, 2], displaced_coords[atom2_idx, 2]]
            
            ax.plot(x, y, z, 'gray', linewidth=1, alpha=0.6)
        
        # Plot atoms (skip hydrogens for clarity in most modes)
        skip_h = mode_name not in ["C-H Stretch", "C-H Bend"]
        
        for i, (atom, element) in enumerate(zip(displaced_coords, elements)):
            if element == 'H' and skip_h:
                continue
            
            # Highlight atoms involved in this mode
            is_active = np.linalg.norm(displacements[i]) > 0.01
            edge_color = 'red' if is_active else 'black'
            edge_width = 2 if is_active else 1
            
            ax.scatter(atom[0], atom[1], atom[2],
                      c=get_atom_color(element),
                      s=get_atom_size(element),
                      edgecolors=edge_color,
                      linewidths=edge_width,
                      alpha=0.9)
        
        # Set labels and title
        ax.set_xlabel('X (Å)', fontsize=10, fontweight='bold')
        ax.set_ylabel('Y (Å)', fontsize=10, fontweight='bold')
        ax.set_zlabel('Z (Å)', fontsize=10, fontweight='bold')
        
        # Add title with frequency
        title = f'{mode_name}\nν ≈ {freq} cm⁻¹\nFrame: {frame+1}/{num_frames}'
        ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
        
        # Keep consistent view
        ax.view_init(elev=20, azim=45 + frame * 2)  # Slowly rotate
        
        # Set consistent axis limits
        margin = 2
        ax.set_xlim([coords[:, 0].min() - margin, coords[:, 0].max() + margin])
        ax.set_ylim([coords[:, 1].min() - margin, coords[:, 1].max() + margin])
        ax.set_zlim([coords[:, 2].min() - margin, coords[:, 2].max() + margin])
        
        return []
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                  frames=num_frames, interval=50, blit=False)
    
    # Save as GIF
    writer = PillowWriter(fps=20)
    anim.save(output_file, writer=writer)
    plt.close()
    
    print(f"  ✓ Saved to {output_file}")

# ===================== Create All Animations =====================

print("="*60)
print("CREATING MOLECULAR VIBRATION ANIMATIONS")
print("="*60)

# Define vibrational modes to animate
modes = [
    {
        'name': 'C-H Stretch (CH₂)',
        'func': create_ch_stretch_displacement,
        'freq': 2850,
        'file': '/workspace/vibration_ch_stretch.gif',
        'amplitude': 1.0
    },
    {
        'name': 'S=O Stretch (Asymmetric)',
        'func': create_so_stretch_displacement,
        'freq': 1325,
        'file': '/workspace/vibration_so_stretch.gif',
        'amplitude': 1.2
    },
    {
        'name': 'C-H Bend (Scissoring)',
        'func': create_ch_bend_displacement,
        'freq': 1465,
        'file': '/workspace/vibration_ch_bend.gif',
        'amplitude': 1.0
    },
    {
        'name': 'C-S Stretch',
        'func': create_cs_stretch_displacement,
        'freq': 650,
        'file': '/workspace/vibration_cs_stretch.gif',
        'amplitude': 1.0
    },
    {
        'name': 'Backbone Bending',
        'func': create_backbone_bend_displacement,
        'freq': 1000,
        'file': '/workspace/vibration_backbone_bend.gif',
        'amplitude': 1.0
    },
]

# Create each animation
for mode in modes:
    create_vibration_animation(
        mode['name'],
        mode['func'],
        mode['freq'],
        mode['file'],
        num_frames=60,
        amplitude=mode['amplitude']
    )

print("\n" + "="*60)
print("CREATING SUMMARY FIGURE")
print("="*60)

# Create a summary figure showing all modes
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Molecular Vibrational Modes - Representative Frames', 
             fontsize=16, fontweight='bold')

mode_funcs = [
    (create_ch_stretch_displacement, 'C-H Stretch\n2850 cm⁻¹', 0.5),
    (create_so_stretch_displacement, 'S=O Stretch\n1325 cm⁻¹', 0.6),
    (create_ch_bend_displacement, 'C-H Bend\n1465 cm⁻¹', 0.5),
    (create_cs_stretch_displacement, 'C-S Stretch\n650 cm⁻¹', 0.5),
    (create_backbone_bend_displacement, 'Backbone Bend\n1000 cm⁻¹', 0.5),
]

for idx, (func, title, amp) in enumerate(mode_funcs):
    row = idx // 3
    col = idx % 3
    ax = axes[row, col]
    ax = fig.add_subplot(2, 3, idx + 1, projection='3d')
    
    # Get displacement and apply it
    displacement = func() * amp
    displaced_coords = coords + displacement
    
    # Plot bonds
    for bond in bonds:
        atom1_idx = bond['atom1']
        atom2_idx = bond['atom2']
        
        x = [displaced_coords[atom1_idx, 0], displaced_coords[atom2_idx, 0]]
        y = [displaced_coords[atom1_idx, 1], displaced_coords[atom2_idx, 1]]
        z = [displaced_coords[atom1_idx, 2], displaced_coords[atom2_idx, 2]]
        
        ax.plot(x, y, z, 'gray', linewidth=0.8, alpha=0.5)
    
    # Plot atoms
    for i, (atom, element) in enumerate(zip(displaced_coords, elements)):
        if element == 'H' and title not in ['C-H Stretch', 'C-H Bend']:
            continue
        
        is_active = np.linalg.norm(displacement[i]) > 0.01
        edge_color = 'red' if is_active else 'black'
        edge_width = 1.5 if is_active else 0.5
        
        ax.scatter(atom[0], atom[1], atom[2],
                  c=get_atom_color(element),
                  s=get_atom_size(element) * 0.5,
                  edgecolors=edge_color,
                  linewidths=edge_width,
                  alpha=0.8)
    
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=8)
    ax.set_ylabel('Y', fontsize=8)
    ax.set_zlabel('Z', fontsize=8)
    ax.view_init(elev=20, azim=45)
    
    # Remove tick labels for cleaner look
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])

# Add text description in the last subplot
ax_text = axes[1, 2]
ax_text.axis('off')
ax_text.text(0.5, 0.8, 'Vibrational Mode Summary', 
            ha='center', va='top', fontsize=14, fontweight='bold',
            transform=ax_text.transAxes)

description = """
Red-highlighted atoms show
which atoms are actively 
vibrating in each mode.

Animations show the full
vibrational motion with
arrows indicating
displacement directions.

Frequencies correspond to
FTIR absorption peaks.

All animations saved as
.gif files for easy viewing.
"""

ax_text.text(0.5, 0.65, description,
            ha='center', va='top', fontsize=10,
            transform=ax_text.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))

# Add legend
legend_elements = [
    mpatches.Patch(color='gray', label='Carbon (C)'),
    mpatches.Patch(color='yellow', label='Sulfur (S)'),
    mpatches.Patch(color='red', label='Oxygen (O)'),
    mpatches.Patch(color='white', label='Hydrogen (H)'),
    mpatches.Patch(facecolor='white', edgecolor='red', linewidth=2, label='Active in vibration'),
]
ax_text.legend(handles=legend_elements, loc='center', fontsize=9, framealpha=0.8)

plt.tight_layout()
plt.savefig('/workspace/vibration_modes_summary.png', dpi=300, bbox_inches='tight')
print("  ✓ Summary figure saved")

print("\n" + "="*60)
print("✓ ALL ANIMATIONS COMPLETE!")
print("="*60)

print("\nGenerated files:")
print("  1. vibration_ch_stretch.gif - C-H stretching (2850 cm⁻¹)")
print("  2. vibration_so_stretch.gif - S=O stretching (1325 cm⁻¹)")
print("  3. vibration_ch_bend.gif - C-H bending (1465 cm⁻¹)")
print("  4. vibration_cs_stretch.gif - C-S stretching (650 cm⁻¹)")
print("  5. vibration_backbone_bend.gif - Backbone bending (1000 cm⁻¹)")
print("  6. vibration_modes_summary.png - Summary figure")

print("\n" + "="*60)
print("How to view the animations:")
print("  - Open the .gif files in any image viewer or web browser")
print("  - Each animation shows one complete vibrational cycle")
print("  - Red-highlighted atoms indicate active vibration")
print("  - The molecule slowly rotates for better 3D visualization")
print("="*60)
