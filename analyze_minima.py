#!/usr/bin/env python3
"""
Detailed analysis of transmittance minima in the 400-1000 cm⁻¹ region
Identify peaks and assign vibrational modes
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_prominences
from scipy.ndimage import gaussian_filter1d

print("="*80)
print("DETAILED MINIMA ANALYSIS: 400-1000 cm⁻¹ REGION")
print("="*80)

# Load all spectral data
print("\nLoading spectral data...")

# Experimental
exp_data = np.loadtxt('/workspace/experimental_ftir.csv', delimiter=',')
exp_wn = exp_data[:, 0]
exp_abs = exp_data[:, 1]
exp_trans = 10**(-exp_abs) * 100
exp_trans = np.clip(exp_trans, 0, 100)

# Enhanced
enh_data = np.loadtxt('/workspace/ftir_enhanced_calculated.csv', delimiter=',', skiprows=1)
enh_wn = enh_data[:, 0]
enh_trans = enh_data[:, 1]

# Ultra-Enhanced
ultra_data = np.loadtxt('/workspace/ftir_ultra_enhanced.csv', delimiter=',', skiprows=1)
ultra_wn = ultra_data[:, 0]
ultra_trans = ultra_data[:, 1]

print("✓ Data loaded successfully")

# Focus on 400-1000 cm⁻¹ region
print("\nFocusing on 400-1000 cm⁻¹ region...")

mask_exp = (exp_wn >= 400) & (exp_wn <= 1000)
mask_enh = (enh_wn >= 400) & (enh_wn <= 1000)
mask_ultra = (ultra_wn >= 400) & (ultra_wn <= 1000)

exp_wn_roi = exp_wn[mask_exp]
exp_trans_roi = exp_trans[mask_exp]

enh_wn_roi = enh_wn[mask_enh]
enh_trans_roi = enh_trans[mask_enh]

ultra_wn_roi = ultra_wn[mask_ultra]
ultra_trans_roi = ultra_trans[mask_ultra]

# Find minima (valleys in transmittance = absorption peaks)
print("\nDetecting minima (absorption peaks)...")

# For minima, we need to invert transmittance (find peaks in -transmittance)
exp_minima_idx, _ = find_peaks(-exp_trans_roi, height=-95, distance=15, prominence=2)
enh_minima_idx, _ = find_peaks(-enh_trans_roi, height=-98, distance=10, prominence=0.5)
ultra_minima_idx, _ = find_peaks(-ultra_trans_roi, height=-98, distance=5, prominence=0.5)

exp_minima_wn = exp_wn_roi[exp_minima_idx]
exp_minima_trans = exp_trans_roi[exp_minima_idx]

enh_minima_wn = enh_wn_roi[enh_minima_idx]
enh_minima_trans = enh_trans_roi[enh_minima_idx]

ultra_minima_wn = ultra_wn_roi[ultra_minima_idx]
ultra_minima_trans = ultra_trans_roi[ultra_minima_idx]

print(f"  Experimental minima found: {len(exp_minima_wn)}")
print(f"  Enhanced minima found: {len(enh_minima_wn)}")
print(f"  Ultra-Enhanced minima found: {len(ultra_minima_wn)}")

# ===================== Assign Vibrational Modes =====================

def assign_vibration(wavenumber):
    """
    Assign vibrational mode based on wavenumber
    Returns: (short_name, full_description, category)
    """
    wn = wavenumber
    
    if 950 <= wn <= 1000:
        return ("C-C skeletal", "C-C stretching (skeletal backbone)", "C-C")
    elif 900 <= wn < 950:
        return ("CH₂ rock", "CH₂ rocking vibration", "C-H")
    elif 860 <= wn < 900:
        return ("Ring breathing", "Ring breathing mode (weak)", "Ring")
    elif 800 <= wn < 860:
        return ("CH₂ rock", "CH₂ rocking (chain)", "C-H")
    elif 750 <= wn < 800:
        return ("CH₂ rock/C-S", "CH₂ rocking + C-S stretch", "C-H+C-S")
    elif 700 <= wn < 750:
        return ("C-S stretch", "C-S stretching (strong)", "C-S")
    elif 650 <= wn < 700:
        return ("C-S stretch", "C-S stretching (medium)", "C-S")
    elif 600 <= wn < 650:
        return ("C-S stretch", "C-S stretching (weak)", "C-S")
    elif 550 <= wn < 600:
        return ("SO₂ bend", "SO₂ scissoring/deformation", "S=O")
    elif 500 <= wn < 550:
        return ("Ring def", "Ring deformation", "Ring")
    elif 450 <= wn < 500:
        return ("SO₂ rock/Ring", "SO₂ rocking + Ring puckering", "S=O+Ring")
    elif 400 <= wn < 450:
        return ("C-C-C bend", "C-C-C bending (skeletal)", "C-C")
    else:
        return ("Mixed mode", "Complex coupled vibration", "Mixed")

# Analyze experimental minima in detail
print("\n" + "="*80)
print("EXPERIMENTAL MINIMA (RED LINE) - DETAILED ANALYSIS")
print("="*80)
print(f"\n{'Position':<12} {'Trans %':<10} {'Short Name':<20} {'Full Description':<40} {'Type':<10}")
print("-"*110)

exp_assignments = []
for wn, trans in zip(exp_minima_wn, exp_minima_trans):
    short, full, category = assign_vibration(wn)
    exp_assignments.append((wn, trans, short, full, category))
    print(f"{wn:8.1f} cm⁻¹  {trans:6.1f}%    {short:<20} {full:<40} {category:<10}")

# Match enhanced and ultra-enhanced with experimental
print("\n" + "="*80)
print("MATCHING CALCULATED MINIMA WITH EXPERIMENTAL")
print("="*80)

def find_closest_match(exp_wn, calc_wn_list, calc_trans_list, tolerance=30):
    """Find closest calculated peak to experimental peak"""
    matches = []
    for calc_wn, calc_trans in zip(calc_wn_list, calc_trans_list):
        if abs(calc_wn - exp_wn) <= tolerance:
            matches.append((calc_wn, calc_trans, abs(calc_wn - exp_wn)))
    
    if matches:
        # Return closest match
        matches.sort(key=lambda x: x[2])
        return matches[0][0], matches[0][1]  # wavenumber, transmittance
    else:
        return None, None

print(f"\n{'Exp Position':<12} {'Enhanced':<15} {'Δ(cm⁻¹)':<10} {'Ultra-Enh':<15} {'Δ(cm⁻¹)':<10} {'Assignment':<30}")
print("-"*110)

matched_data = []
for exp_wn, exp_trans, short, full, category in exp_assignments:
    # Find enhanced match
    enh_wn_match, enh_trans_match = find_closest_match(exp_wn, enh_minima_wn, enh_minima_trans, tolerance=30)
    
    # Find ultra-enhanced match
    ultra_wn_match, ultra_trans_match = find_closest_match(exp_wn, ultra_minima_wn, ultra_minima_trans, tolerance=30)
    
    enh_str = f"{enh_wn_match:.1f} cm⁻¹" if enh_wn_match else "Not found"
    enh_delta = f"{abs(enh_wn_match - exp_wn):.1f}" if enh_wn_match else "---"
    
    ultra_str = f"{ultra_wn_match:.1f} cm⁻¹" if ultra_wn_match else "Not found"
    ultra_delta = f"{abs(ultra_wn_match - exp_wn):.1f}" if ultra_wn_match else "---"
    
    matched_data.append({
        'exp_wn': exp_wn,
        'exp_trans': exp_trans,
        'enh_wn': enh_wn_match,
        'enh_trans': enh_trans_match,
        'ultra_wn': ultra_wn_match,
        'ultra_trans': ultra_trans_match,
        'short': short,
        'full': full,
        'category': category
    })
    
    print(f"{exp_wn:8.1f} cm⁻¹  {enh_str:<15} {enh_delta:<10} {ultra_str:<15} {ultra_delta:<10} {short:<30}")

# ===================== Create Detailed Annotated Figure =====================

print("\n" + "="*80)
print("Creating detailed annotated figure...")
print("="*80)

fig, axes = plt.subplots(2, 2, figsize=(20, 14))

# ========== Plot 1: Overview with all minima marked ==========
ax1 = axes[0, 0]

ax1.plot(ultra_wn_roi, ultra_trans_roi, 'b-', linewidth=2.5, label='Ultra-Enhanced', alpha=0.8, zorder=3)
ax1.plot(enh_wn_roi, enh_trans_roi, 'g-', linewidth=2, label='Enhanced', alpha=0.7, zorder=2)
ax1.plot(exp_wn_roi, exp_trans_roi, 'r-', linewidth=2, label='Experimental', alpha=0.7, zorder=1)

# Mark all minima
ax1.plot(exp_minima_wn, exp_minima_trans, 'ro', markersize=8, label='Exp minima', zorder=5)
ax1.plot(enh_minima_wn, enh_minima_trans, 'go', markersize=6, alpha=0.7, zorder=4)
ax1.plot(ultra_minima_wn, ultra_minima_trans, 'bo', markersize=6, alpha=0.7, zorder=4)

ax1.set_xlabel('Wavenumber (cm⁻¹)', fontsize=13, fontweight='bold')
ax1.set_ylabel('Transmittance (%)', fontsize=13, fontweight='bold')
ax1.set_title('400-1000 cm⁻¹ Region: All Minima Identified', fontsize=14, fontweight='bold')
ax1.set_xlim(1000, 400)
ax1.set_ylim(0, 105)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.legend(loc='lower left', fontsize=11)

# Add count
ax1.text(0.98, 0.97, f'Minima detected:\nExp: {len(exp_minima_wn)}\nEnhanced: {len(enh_minima_wn)}\nUltra: {len(ultra_minima_wn)}',
        transform=ax1.transAxes, ha='right', va='top',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7),
        fontsize=10, family='monospace')

# ========== Plot 2: Experimental with detailed annotations ==========
ax2 = axes[0, 1]

ax2.plot(exp_wn_roi, exp_trans_roi, 'r-', linewidth=2.5, label='Experimental', alpha=0.8)
ax2.plot(exp_minima_wn, exp_minima_trans, 'ro', markersize=10, zorder=5, markeredgecolor='darkred', markeredgewidth=2)

# Annotate each experimental minimum
for i, (wn, trans, short, full, category) in enumerate(exp_assignments):
    # Alternate annotation positions
    offset = 8 if i % 2 == 0 else -15
    
    # Color code by category
    colors = {
        'C-S': 'purple',
        'C-H': 'red',
        'C-H+C-S': 'orange',
        'Ring': 'blue',
        'S=O': 'darkblue',
        'S=O+Ring': 'darkviolet',
        'C-C': 'green',
        'Mixed': 'gray'
    }
    color = colors.get(category, 'black')
    
    ax2.annotate(f'{short}\n{wn:.0f} cm⁻¹',
                xy=(wn, trans),
                xytext=(wn, trans + offset),
                fontsize=8,
                ha='center',
                color=color,
                weight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                         edgecolor=color, alpha=0.8, linewidth=1.5),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

ax2.set_xlabel('Wavenumber (cm⁻¹)', fontsize=13, fontweight='bold')
ax2.set_ylabel('Transmittance (%)', fontsize=13, fontweight='bold')
ax2.set_title('Experimental Minima - Detailed Annotations', fontsize=14, fontweight='bold')
ax2.set_xlim(1000, 400)
ax2.set_ylim(0, 105)
ax2.grid(True, alpha=0.3, linestyle='--')

# ========== Plot 3: Comparison table ==========
ax3 = axes[1, 0]
ax3.axis('off')

# Create detailed comparison table
table_text = "EXPERIMENTAL MINIMA vs CALCULATED MATCHES\n"
table_text += "="*80 + "\n\n"
table_text += f"{'Exp (cm⁻¹)':<12} {'Enhanced':<12} {'Δ':<6} {'Ultra':<12} {'Δ':<6} {'Assignment':<30}\n"
table_text += "-"*80 + "\n"

for data in matched_data[:15]:  # Show first 15
    exp_wn = data['exp_wn']
    enh_wn = data['enh_wn']
    ultra_wn = data['ultra_wn']
    short = data['short']
    
    enh_str = f"{enh_wn:.0f}" if enh_wn else "---"
    enh_delta = f"{abs(enh_wn - exp_wn):.0f}" if enh_wn else "---"
    
    ultra_str = f"{ultra_wn:.0f}" if ultra_wn else "---"
    ultra_delta = f"{abs(ultra_wn - exp_wn):.0f}" if ultra_wn else "---"
    
    table_text += f"{exp_wn:8.0f}     {enh_str:<12} {enh_delta:<6} {ultra_str:<12} {ultra_delta:<6} {short:<30}\n"

ax3.text(0.05, 0.95, table_text,
        ha='left', va='top', fontsize=9, family='monospace',
        transform=ax3.transAxes)

# ========== Plot 4: Statistics and Summary ==========
ax4 = axes[1, 1]
ax4.axis('off')

# Calculate matching statistics
enh_matched = sum(1 for d in matched_data if d['enh_wn'] is not None)
ultra_matched = sum(1 for d in matched_data if d['ultra_wn'] is not None)

# Count by category
category_counts = {}
for data in matched_data:
    cat = data['category']
    category_counts[cat] = category_counts.get(cat, 0) + 1

stats_text = "VIBRATIONAL MODE STATISTICS\n"
stats_text += "="*60 + "\n\n"
stats_text += f"Total experimental minima: {len(exp_minima_wn)}\n"
stats_text += f"Enhanced matched: {enh_matched} ({enh_matched/len(exp_minima_wn)*100:.0f}%)\n"
stats_text += f"Ultra-Enhanced matched: {ultra_matched} ({ultra_matched/len(exp_minima_wn)*100:.0f}%)\n"
stats_text += "\n" + "-"*60 + "\n"
stats_text += "VIBRATIONAL MODE BREAKDOWN:\n"
stats_text += "-"*60 + "\n"

for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
    bar = "█" * count
    stats_text += f"{cat:<15} {count:2d}  {bar}\n"

stats_text += "\n" + "="*60 + "\n"
stats_text += "KEY VIBRATIONAL MODES IN THIS REGION:\n"
stats_text += "="*60 + "\n\n"

mode_descriptions = [
    ("950-1000 cm⁻¹", "C-C skeletal stretching", "Backbone vibrations"),
    ("850-950 cm⁻¹", "CH₂ rocking, Ring breathing", "Chain + ring modes"),
    ("700-850 cm⁻¹", "CH₂ rocking + C-S stretch", "Combined modes"),
    ("600-750 cm⁻¹", "C-S stretching (multiple)", "Sulfur-carbon bonds"),
    ("500-600 cm⁻¹", "SO₂ bending + Ring modes", "Sulfone deformation"),
    ("400-500 cm⁻¹", "Ring deformation, C-C-C bend", "Low frequency skeletal"),
]

for region, primary, description in mode_descriptions:
    stats_text += f"{region:<18} {primary:<30}\n"
    stats_text += f"                   → {description}\n\n"

ax4.text(0.05, 0.95, stats_text,
        ha='left', va='top', fontsize=10, family='monospace',
        transform=ax4.transAxes,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8, pad=0.8))

fig.suptitle('Detailed Minima Analysis: 400-1000 cm⁻¹ Region\nTransmittance Valleys = Absorption Peaks', 
            fontsize=16, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('/workspace/minima_detailed_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Detailed figure saved!")

# ===================== Export detailed table =====================

print("\nExporting detailed assignment table...")

with open('/workspace/minima_assignments.txt', 'w') as f:
    f.write("="*100 + "\n")
    f.write("DETAILED MINIMA ANALYSIS: 400-1000 cm⁻¹ REGION\n")
    f.write("="*100 + "\n\n")
    
    f.write("EXPERIMENTAL MINIMA (RED LINE) WITH VIBRATIONAL ASSIGNMENTS\n")
    f.write("-"*100 + "\n")
    f.write(f"{'Position':<12} {'Trans %':<10} {'Enhanced':<15} {'Ultra-Enh':<15} {'Assignment':<30} {'Description':<40}\n")
    f.write("-"*100 + "\n")
    
    for data in matched_data:
        exp_wn = data['exp_wn']
        exp_trans = data['exp_trans']
        enh_wn = data['enh_wn']
        ultra_wn = data['ultra_wn']
        short = data['short']
        full = data['full']
        
        enh_str = f"{enh_wn:.1f}" if enh_wn else "---"
        ultra_str = f"{ultra_wn:.1f}" if ultra_wn else "---"
        
        f.write(f"{exp_wn:8.1f} cm⁻¹  {exp_trans:6.1f}%    {enh_str:<15} {ultra_str:<15} {short:<30} {full}\n")
    
    f.write("\n" + "="*100 + "\n")
    f.write("SUMMARY STATISTICS\n")
    f.write("="*100 + "\n")
    f.write(f"Total experimental minima: {len(exp_minima_wn)}\n")
    f.write(f"Enhanced matched: {enh_matched} ({enh_matched/len(exp_minima_wn)*100:.1f}%)\n")
    f.write(f"Ultra-Enhanced matched: {ultra_matched} ({ultra_matched/len(exp_minima_wn)*100:.1f}%)\n")
    f.write("\n")
    f.write("Vibrational mode distribution:\n")
    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        f.write(f"  {cat:<15}: {count:2d} peaks\n")

print("✓ Assignment table exported!")

print("\n" + "="*80)
print("✓ ANALYSIS COMPLETE!")
print("="*80)
print("\nGenerated files:")
print("  1. minima_detailed_analysis.png - Comprehensive annotated figure")
print("  2. minima_assignments.txt - Detailed assignment table")
print(f"\nKey findings:")
print(f"  • {len(exp_minima_wn)} experimental minima identified in 400-1000 cm⁻¹")
print(f"  • Ultra-Enhanced matched {ultra_matched}/{len(exp_minima_wn)} ({ultra_matched/len(exp_minima_wn)*100:.0f}%)")
print(f"  • Main modes: C-S stretch, CH₂ rock, SO₂ bend, Ring modes, C-C skeletal")
