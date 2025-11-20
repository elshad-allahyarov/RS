#!/usr/bin/env python3
"""
Create FTIR plots in different styles - Absorbance mode
"""

import numpy as np
import matplotlib.pyplot as plt

# Load the calculated spectrum data
data = np.loadtxt('/workspace/ftir_spectrum.csv', delimiter=',', skiprows=1)
wavenumbers = data[:, 0]
transmittance = data[:, 1]

# Convert transmittance to absorbance
# A = -log10(T/100) = 2 - log10(T)
absorbance = 2 - np.log10(transmittance)
# Handle any inf or nan values
absorbance = np.nan_to_num(absorbance, nan=0.0, posinf=3.0, neginf=0.0)

# Peak information
peaks = [
    ('C-H stretch (CH₂)', 2850, 'C-H'),
    ('C-H stretch (CH₃)', 2960, 'C-H'),
    ('C-H bend (CH₂)', 1465, 'C-H bend'),
    ('C-H bend (CH₃)', 1375, 'C-H bend'),
    ('S=O asym stretch', 1325, 'S=O'),
    ('S=O sym stretch', 1140, 'S=O'),
    ('C-C stretch', 1000, 'C-C'),
    ('C-S stretch', 650, 'C-S'),
]

# Create figure with multiple subplots
fig = plt.figure(figsize=(16, 12))

# ==================== Plot 1: Absorbance (standard style) ====================
ax1 = plt.subplot(3, 2, 1)
ax1.plot(wavenumbers, absorbance, 'b-', linewidth=1.5)
ax1.set_xlabel('Wavenumber (cm⁻¹)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Absorbance (A.U.)', fontsize=11, fontweight='bold')
ax1.set_title('FTIR Spectrum - Absorbance Mode', fontsize=12, fontweight='bold')
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.set_xlim(wavenumbers[-1], wavenumbers[0])
ax1.invert_xaxis()

# Add shaded regions
ax1.axvspan(2800, 3000, alpha=0.1, color='red')
ax1.axvspan(1300, 1500, alpha=0.1, color='green')
ax1.axvspan(1100, 1400, alpha=0.1, color='blue')
ax1.axvspan(600, 800, alpha=0.1, color='orange')

# ==================== Plot 2: Transmittance (standard style) ====================
ax2 = plt.subplot(3, 2, 2)
ax2.plot(wavenumbers, transmittance, 'r-', linewidth=1.5)
ax2.set_xlabel('Wavenumber (cm⁻¹)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Transmittance (%)', fontsize=11, fontweight='bold')
ax2.set_title('FTIR Spectrum - Transmittance Mode', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.set_xlim(wavenumbers[-1], wavenumbers[0])
ax2.set_ylim(0, 105)
ax2.invert_xaxis()

# Add shaded regions
ax2.axvspan(2800, 3000, alpha=0.1, color='red')
ax2.axvspan(1300, 1500, alpha=0.1, color='green')
ax2.axvspan(1100, 1400, alpha=0.1, color='blue')
ax2.axvspan(600, 800, alpha=0.1, color='orange')

# ==================== Plot 3: Absorbance with peak annotations ====================
ax3 = plt.subplot(3, 2, 3)
ax3.plot(wavenumbers, absorbance, 'darkblue', linewidth=2)
ax3.fill_between(wavenumbers, 0, absorbance, alpha=0.3, color='lightblue')
ax3.set_xlabel('Wavenumber (cm⁻¹)', fontsize=11, fontweight='bold')
ax3.set_ylabel('Absorbance (A.U.)', fontsize=11, fontweight='bold')
ax3.set_title('Absorbance with Peak Annotations', fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3, linestyle='--')
ax3.set_xlim(wavenumbers[-1], wavenumbers[0])
ax3.invert_xaxis()

# Annotate peaks
for name, freq, category in peaks[:5]:  # Top 5 peaks
    idx = np.argmin(np.abs(wavenumbers - freq))
    y_val = absorbance[idx]
    if y_val > 0.1:  # Only annotate significant peaks
        ax3.plot(freq, y_val, 'ro', markersize=8)
        ax3.annotate(f'{name}\n{freq} cm⁻¹', 
                   xy=(freq, y_val),
                   xytext=(freq, y_val + 0.3),
                   fontsize=8,
                   ha='center',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.5),
                   arrowprops=dict(arrowstyle='->', lw=1))

# ==================== Plot 4: Inverted Transmittance (looks like absorbance) ====================
ax4 = plt.subplot(3, 2, 4)
inverted_trans = 100 - transmittance
ax4.plot(wavenumbers, inverted_trans, 'darkgreen', linewidth=2)
ax4.fill_between(wavenumbers, 0, inverted_trans, alpha=0.3, color='lightgreen')
ax4.set_xlabel('Wavenumber (cm⁻¹)', fontsize=11, fontweight='bold')
ax4.set_ylabel('Absorption (%)', fontsize=11, fontweight='bold')
ax4.set_title('FTIR Spectrum - Inverted Transmittance', fontsize=12, fontweight='bold')
ax4.grid(True, alpha=0.3, linestyle='--')
ax4.set_xlim(wavenumbers[-1], wavenumbers[0])
ax4.invert_xaxis()

# ==================== Plot 5: Absorbance - Zoomed to fingerprint region ====================
ax5 = plt.subplot(3, 2, 5)
# Filter data for fingerprint region (600-1800 cm-1)
mask = (wavenumbers >= 600) & (wavenumbers <= 1800)
ax5.plot(wavenumbers[mask], absorbance[mask], 'purple', linewidth=2)
ax5.fill_between(wavenumbers[mask], 0, absorbance[mask], alpha=0.3, color='lavender')
ax5.set_xlabel('Wavenumber (cm⁻¹)', fontsize=11, fontweight='bold')
ax5.set_ylabel('Absorbance (A.U.)', fontsize=11, fontweight='bold')
ax5.set_title('Fingerprint Region (600-1800 cm⁻¹)', fontsize=12, fontweight='bold')
ax5.grid(True, alpha=0.3, linestyle='--')
ax5.set_xlim(1800, 600)

# Annotate key peaks in fingerprint region
fingerprint_peaks = [
    ('S=O asym', 1325),
    ('S=O sym', 1140),
    ('C-C', 1000),
    ('C-S', 650),
]
for name, freq in fingerprint_peaks:
    idx = np.argmin(np.abs(wavenumbers - freq))
    y_val = absorbance[idx]
    if y_val > 0.1:
        ax5.plot(freq, y_val, 'ro', markersize=6)
        ax5.text(freq, y_val + 0.15, f'{name}\n{freq}', 
                fontsize=8, ha='center', va='bottom',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7))

# ==================== Plot 6: Comparison overlay ====================
ax6 = plt.subplot(3, 2, 6)
# Normalize absorbance to 0-100 scale for comparison
abs_normalized = (absorbance / absorbance.max()) * 100
ax6.plot(wavenumbers, abs_normalized, 'b-', linewidth=2, label='Absorbance (normalized)', alpha=0.7)
ax6.plot(wavenumbers, 100-transmittance, 'r--', linewidth=2, label='100 - Transmittance', alpha=0.7)
ax6.set_xlabel('Wavenumber (cm⁻¹)', fontsize=11, fontweight='bold')
ax6.set_ylabel('Intensity (A.U.)', fontsize=11, fontweight='bold')
ax6.set_title('Absorbance vs. Inverted Transmittance Comparison', fontsize=12, fontweight='bold')
ax6.grid(True, alpha=0.3, linestyle='--')
ax6.set_xlim(wavenumbers[-1], wavenumbers[0])
ax6.legend(loc='upper right', fontsize=9)
ax6.invert_xaxis()

plt.tight_layout()
plt.savefig('/workspace/ftir_absorbance_multi.png', dpi=300, bbox_inches='tight')
print("Multi-panel plot saved to: ftir_absorbance_multi.png")

# ==================== Create a single large absorbance plot ====================
fig2, ax = plt.subplots(figsize=(14, 7))

# Plot with gradient fill
ax.plot(wavenumbers, absorbance, 'darkblue', linewidth=2.5, label='Absorbance')
ax.fill_between(wavenumbers, 0, absorbance, alpha=0.4, color='steelblue')

# Major peak annotations with better styling
for i, (name, freq, category) in enumerate(peaks):
    idx = np.argmin(np.abs(wavenumbers - freq))
    y_val = absorbance[idx]
    
    if y_val > 0.15:  # Only annotate significant peaks
        # Color code by category
        colors = {'C-H': 'red', 'C-H bend': 'green', 'S=O': 'blue', 'C-C': 'orange', 'C-S': 'purple'}
        color = colors.get(category, 'black')
        
        ax.plot(freq, y_val, 'o', color=color, markersize=10, markeredgecolor='black', markeredgewidth=1)
        
        # Alternate annotation positions to avoid overlap
        offset = 0.4 if i % 2 == 0 else 0.6
        ax.annotate(f'{name}\n{freq} cm⁻¹', 
                   xy=(freq, y_val),
                   xytext=(freq, y_val + offset),
                   fontsize=10,
                   ha='center',
                   weight='bold',
                   bbox=dict(boxstyle='round,pad=0.4', facecolor=color, alpha=0.3, edgecolor=color),
                   arrowprops=dict(arrowstyle='->', lw=1.5, color=color))

# Formatting
ax.set_xlabel('Wavenumber (cm⁻¹)', fontsize=14, fontweight='bold')
ax.set_ylabel('Absorbance (A.U.)', fontsize=14, fontweight='bold')
ax.set_title('FTIR Spectrum - Sulfone Molecule (Absorbance Mode)', fontsize=16, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_xlim(4000, 400)

# Add colored region labels
ax.axvspan(2800, 3000, alpha=0.15, color='red', label='C-H stretch region')
ax.axvspan(1300, 1500, alpha=0.15, color='green', label='C-H bend region')
ax.axvspan(1100, 1400, alpha=0.15, color='blue', label='S=O stretch region')
ax.axvspan(600, 800, alpha=0.15, color='orange', label='C-S stretch region')

# Add text labels for regions
ax.text(2900, absorbance.max() * 0.95, 'C-H stretch', fontsize=10, ha='center', weight='bold', color='darkred')
ax.text(1400, absorbance.max() * 0.95, 'C-H bend', fontsize=10, ha='center', weight='bold', color='darkgreen')
ax.text(1250, absorbance.max() * 0.95, 'S=O', fontsize=10, ha='center', weight='bold', color='darkblue')
ax.text(700, absorbance.max() * 0.95, 'C-S', fontsize=10, ha='center', weight='bold', color='darkorange')

ax.legend(loc='upper left', fontsize=10, framealpha=0.9)

plt.tight_layout()
plt.savefig('/workspace/ftir_absorbance_main.png', dpi=300, bbox_inches='tight')
print("Main absorbance plot saved to: ftir_absorbance_main.png")

# Save absorbance data
np.savetxt('/workspace/ftir_absorbance.csv', 
           np.column_stack([wavenumbers, absorbance]),
           delimiter=',',
           header='Wavenumber(cm-1),Absorbance(A.U.)',
           comments='')
print("Absorbance data saved to: ftir_absorbance.csv")

print("\n✓ All plots generated successfully!")
print("\nGenerated files:")
print("  1. ftir_absorbance_main.png - Large single absorbance plot with annotations")
print("  2. ftir_absorbance_multi.png - 6-panel comparison plot")
print("  3. ftir_absorbance.csv - Absorbance data in CSV format")
