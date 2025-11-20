# REVISION CHECKLIST FOR AUTHORS
## Manuscript: applnano-3955968-peer-review-v2
## "Initial Stage Flocculation of Positively Charged Colloidal Particles in the Presence of Ultrafine Bubbles"

---

## TIER 1: REQUIRED FOR ACCEPTANCE
**Timeline: 2-3 weeks**  
**These MUST be completed or paper will be rejected**

### [ ] 1. DLVO Calculations (3-5 days)

#### [ ] 1a. Calculate AL-AL interaction at bare conditions
- [ ] At 0.1 mM NaCl: Calculate V(h) where h = separation distance
- [ ] At 10 mM NaCl: Calculate V(h)
- [ ] Plot interaction energy vs. distance for both conditions
- [ ] Show that 0.1 mM has high barrier (slow aggregation expected)
- [ ] Show that 10 mM has low barrier (fast aggregation expected)
- [ ] Compare predictions to your Fig. 7 data

**Parameters you already have:**
- AL diameter: 1 µm
- Surface charge density: 15.6 µC/cm²
- Debye lengths: 30 nm (0.1 mM), 3 nm (10 mM)
- Hamaker constant: ~1 kT for polystyrene in water

**Output:** New figure showing DLVO potential curves

#### [ ] 1b. Calculate UFB-AL interaction
- [ ] Use measured UFB zeta potential: -15.3 mV
- [ ] Calculate attraction energy for UFB approaching AL
- [ ] Show that adsorption is energetically favorable (barrier < kT)
- [ ] Estimate binding energy per UFB

**Output:** Add to same figure or separate supplementary figure

#### [ ] 1c. Calculate modified AL-AL interaction after UFB adsorption
- [ ] Method 1: Reduce effective AL charge by factor (1-θ) where θ = coverage
- [ ] Method 2: Patch-charge model with discrete charges
- [ ] Show how barrier height changes with UFB adsorption
- [ ] Explain why β ≈ 2 (modest enhancement)

**Output:** Additional curves on DLVO figure

#### [ ] 1d. Add section to manuscript
- [ ] New subsection in Results: "3.X Theoretical Analysis of Interactions"
- [ ] Or new section: "4. Theoretical Interpretation"
- [ ] ~500-750 words
- [ ] 1-2 figures

---

### [ ] 2. System Parameters Table (1 day)

#### [ ] Create comprehensive table with all system parameters:

| Parameter | Symbol | Value | Units | Notes |
|-----------|--------|-------|-------|-------|
| **Particles** |
| AL diameter | d | 1.0 ± 0.044 | µm | DLS measurement |
| AL concentration | N_AL | 5×10⁷ | cm⁻³ | |
| Surface charge density | σ_AL | +15.6 | µC/cm² | Manufacturer |
| Charge per particle | Q_AL | ~+7700 | e | Calculated |
| Isoelectric point | IEP | ~10 | - | From literature |
| Volume fraction | φ | 2.6×10⁻⁵ | - | **CALCULATE** |
| **UFBs** |
| Size range | d_UFB | 100-300 | nm | NTA measurement |
| Mode size | d_mode | ~120-150 | nm | From Fig. 2 |
| Concentration | N_UFB | 1×10⁸ | cm⁻³ | |
| Zeta potential | ζ_UFB | -15.3 ± 2.25 | mV | EPM measurement |
| Charge per UFB | Q_UFB | ~-XX | e | **CALCULATE** |
| **Solution conditions** |
| Temperature | T | 20 | °C | |
| Ionic strength (low) | I | 0.1 | mM NaCl | |
| Ionic strength (high) | I | 10 | mM NaCl | |
| Debye length (low I) | κ⁻¹ | ~30 | nm | **State explicitly** |
| Debye length (high I) | κ⁻¹ | ~3 | nm | **State explicitly** |
| pH conditions | pH | 6.0, 9.0 | - | |
| **Dimensionless parameters** |
| EDL overlap (low I) | κa | ~167 | - | **CALCULATE** |
| EDL overlap (high I) | κa | ~1670 | - | **CALCULATE** |
| Interaction parameter | Γ/kT | ~XX | - | **CALCULATE** |
| UFB/AL ratio at CNP | R_CNP | 2.08-2.15 | - | From Fig. 3 |
| **Mixing conditions** |
| Rotation frequency | f | 1 | Hz | |
| Mixing time | t | 0-30 | min | |
| Shear rate | γ̇ | ~XX | s⁻¹ | **ESTIMATE** |

**CALCULATIONS TO ADD:**
1. Volume fraction: φ = (π/6) × d³ × N
2. Charges from surface areas and potentials
3. κa = particle radius / Debye length  
4. Γ = (Q₁×Q₂×λ_B)/a where λ_B = 0.7 nm (Bjerrum length)

**Where to add:** Section 2.1 Materials, or new Section 2.X System Characterization

---

### [ ] 3. Coverage Fraction Analysis (1 day)

#### [ ] Calculate UFBs per AL particle
- [ ] AL surface area: A_AL = π × d² = π × (1 µm)² ≈ 3.14 µm²
- [ ] UFB cross-section: A_UFB = π × (d_UFB/2)² ≈ 0.07 µm² (for d=150 nm)
- [ ] Maximum packing: N_max ≈ A_AL / A_UFB ≈ 45 UFBs per AL
- [ ] At CNP (R = 2): N_actual = 2 UFBs per AL
- [ ] Coverage fraction: θ = N_actual / N_max ≈ 0.044 or 4.4%

#### [ ] Implications
- [ ] State explicitly: **Coverage is patchy, not uniform**
- [ ] This supports patch-flocculation mechanism
- [ ] Explains why enhancement is modest (most surface remains bare)
- [ ] Compare to Gregory (1973) patch-flocculation theory

**Where to add:** 
- Section 3.2 (Hydrodynamic layer thickness)
- Add 1 paragraph with this calculation
- Reference to Fig. 6 (mechanism schematic)

---

### [ ] 4. Additional Ionic Strengths (1 week experiments)

#### [ ] Test at minimum 3 additional ionic strengths:
- [ ] 1 mM NaCl
- [ ] 3 mM NaCl  
- [ ] 5 mM NaCl
- [ ] (Optional: 50 mM NaCl to see high-I limit)

#### [ ] For each new ionic strength, measure:
- [ ] Electrophoretic mobility vs UFB/AL ratio (like Fig. 3)
- [ ] Flocculation kinetics at pH 6 (like Fig. 7a)
- [ ] Optional: Hydrodynamic layer thickness (like Fig. 4)

#### [ ] Analysis:
- [ ] Determine CNP at each ionic strength
- [ ] Calculate β at each ionic strength
- [ ] Plot β vs ionic strength to show transition
- [ ] Fit to model (e.g., exponential, power law)

**Output:**
- Update Fig. 3 with multiple ionic strengths (or make multi-panel)
- Update Fig. 7 with additional curves
- New analysis paragraph discussing transition regime

---

### [ ] 5. UFB Stability Time-Series (2-3 days)

#### [ ] NTA measurements of UFB suspension over time:
- [ ] t = 0 min (immediately after generation)
- [ ] t = 30 min
- [ ] t = 60 min  
- [ ] t = 120 min (covers your experimental timeframe)
- [ ] Measure: concentration and size distribution at each time

#### [ ] Analysis:
- [ ] Plot concentration vs time
- [ ] Fit to exponential decay or show it's constant
- [ ] Calculate half-life or stability time
- [ ] Show mean size doesn't change significantly

**Output:**
- New supplementary figure: "Fig. SX: UFB stability over time"
- Add 1 paragraph to Section 2.1 Materials
- Reference in Section 3.2 when discussing layer stability

---

### [ ] 6. Expanded Dimer Analysis (2-3 days)

#### [ ] Increase sample size:
- [ ] Analyze 30 dimers without UFBs (up from 10)
- [ ] Analyze 30 dimers with UFBs (up from 10)
- [ ] Record all measurements in supplementary table

#### [ ] Improved analysis:
- [ ] Show histogram of separation distances (not just mean ± SD)
- [ ] Perform statistical test (t-test or Mann-Whitney)
- [ ] Report p-value to show significance
- [ ] Show more example images in SI (at least 5-6 per condition)

#### [ ] Quality control:
- [ ] State criteria for identifying dimers
- [ ] Show rejected examples (if any)
- [ ] Discuss measurement uncertainty

**Output:**
- Update Fig. 5 with histogram inset
- Add Fig. S1-S2 with more examples
- Update Table S1 with all measurements
- Report statistics in figure caption

---

## TIER 2: STRONGLY RECOMMENDED
**Timeline: 1-2 weeks**  
**These would significantly strengthen the paper**

### [ ] 7. UFB/AL Ratio Dependence in Kinetics (3-4 days)

#### [ ] Test flocculation kinetics at multiple UFB/AL ratios:
- [ ] Ratio = 1 (below CNP)
- [ ] Ratio = 2 (at CNP) ← already have this
- [ ] Ratio = 4 (above CNP)
- [ ] At pH 6, both 0.1 and 10 mM NaCl

#### [ ] Hypothesis to test:
- [ ] β should maximize at CNP (ratio ≈ 2)
- [ ] β should be lower at ratios 1 and 4
- [ ] This validates electrokinetic prediction

**Output:**
- New figure or add to Fig. 7
- Strengthens link between charge neutralization and flocculation

---

### [ ] 8. Control Experiment (1 week)

#### [ ] Option A: Anionic colloids + UFBs
- [ ] Use negatively charged particles (silica or carboxyl latex)
- [ ] Measure EPM vs UFB ratio
- [ ] Expect: No adsorption, no charge change
- [ ] Measure flocculation: expect no enhancement

#### [ ] Option B: Degassed water
- [ ] Prepare water with reduced dissolved gas
- [ ] Generate "UFBs" in degassed water
- [ ] Compare to normal UFBs
- [ ] Expect: Reduced stability and/or effect

**Output:**
- New supplementary figure
- Proves mechanism is electrostatic adsorption, not artifact

---

### [ ] 9. Kinetic Modeling (2-3 days analysis)

#### [ ] Fit flocculation data to Smoluchowski equation:
- [ ] dN/dt = -β × k_rapid × N²/2
- [ ] Extract β values with confidence intervals
- [ ] Compare to current method (slope of ln(N/N₀))

#### [ ] Relate β to hydrodynamic layer:
- [ ] β ∝ (R_eff / R_bare)² where R_eff includes layer
- [ ] Use measured layer thickness from Fig. 4
- [ ] Check consistency

**Output:**
- Updated Table 1 with confidence intervals
- New analysis paragraph in Section 3.3

---

### [ ] 10. Polydispersity Analysis (1 day analysis)

#### [ ] Analyze Fig. 2 size distribution quantitatively:
- [ ] Calculate mean, median, standard deviation
- [ ] Calculate D₁₀, D₅₀, D₉₀
- [ ] Report span: (D₉₀ - D₁₀) / D₅₀
- [ ] Discuss which size fraction likely dominates flocculation

#### [ ] If time permits:
- [ ] Fractionate UFBs by size (filtration or centrifugation)
- [ ] Test small vs large UFB fractions separately

**Output:**
- Add quantitative metrics to Section 2.1
- Discuss in Section 3.2

---

## TIER 3: NICE TO HAVE
**Timeline: Variable**  
**Would polish the paper but not essential**

### [ ] 11. Test at pH 10 (IEP of AL)
- Most interesting condition for charge effects
- May show maximum flocculation

### [ ] 12. Extend kinetics time window
- Measure for 1-2 hours instead of 30 min
- See if linear regime breaks down

### [ ] 13. Measure viscosity change
- Does UFB addition change solution viscosity?
- Relevant for hydrodynamic effects

### [ ] 14. Energy/cost analysis
- Energy required for UFB generation
- Compare to mechanical mixing
- Discuss practical viability

### [ ] 15. Batch-to-batch UFB reproducibility
- Generate UFBs on 3 different days
- Show size/concentration consistency
- Report coefficient of variation

---

## WRITING IMPROVEMENTS

### [ ] Abstract
- [ ] Add quantitative result: "enhancement factor β = 2.15 at optimal conditions"
- [ ] State mechanistic conclusion more clearly
- [ ] Reduce length if over word limit

### [ ] Introduction  
- [ ] Lines 92-97: Clarify DLVO vs non-DLVO discussion
- [ ] Either commit to calculating DLVO or don't mention it
- [ ] Add 1-2 sentences on why this study is needed

### [ ] Section 3.1 (Electrokinetics)
- [ ] Lines 250-255: Explain how CNP was interpolated (method?)
- [ ] Add confidence intervals on CNP values
- [ ] Discuss why CNP is independent of ionic strength (physical reason?)

### [ ] Section 3.2 (Hydrodynamic layer)
- [ ] Add quantitative analysis of Fig. 4 time-dependence
- [ ] State uncertainty more clearly
- [ ] Compare layer thickness to UFB size distribution more carefully

### [ ] Section 3.3 (Flocculation kinetics)
- [ ] Add R² values for linear fits in Fig. 7
- [ ] Discuss what limits β to ~2 (mechanistic explanation)
- [ ] Connect more explicitly to Sections 3.1 and 3.2

### [ ] Conclusions
- [ ] Shorten (currently too verbose)
- [ ] Lead with quantitative findings
- [ ] State key mechanistic insight clearly
- [ ] Prioritize future directions (most important first)

### [ ] Figures
- [ ] Fig. 2: Add mean/median/span to caption
- [ ] Fig. 3: Consider multi-panel if adding ionic strengths
- [ ] Fig. 4: Add legend explaining error bars (SD? SE? range?)
- [ ] Fig. 5: Higher resolution images if possible
- [ ] Fig. 7: Add R² values on plots or in caption

### [ ] Supplementary Material
- [ ] Organize clearly with section numbers
- [ ] Reference all SI figures/tables in main text
- [ ] Ensure all SI figures have proper captions
- [ ] Include raw data for reproducibility

---

## CHECKLIST FOR RESPONSE LETTER

### [ ] Address each reviewer comment explicitly:
- [ ] Comment 2: System parameters - **completed in new Table X**
- [ ] Comment 3: UFB stability - **added time-series in Fig. SX**
- [ ] Comment 7: Patchiness - **added coverage calculation in Section 3.2**
- [ ] Comment 9: More ionic strengths - **tested 1, 3, 5 mM NaCl**
- [ ] Comment 10: DLVO - **calculated and shown in new Fig. X**

### [ ] For each change:
- [ ] State what was done
- [ ] Reference figure/table/section where it appears
- [ ] Explain why this strengthens the paper

### [ ] Format:
- [ ] Clear heading for each comment
- [ ] Original comment quoted
- [ ] Your response
- [ ] Changes in manuscript (with line numbers)

---

## QUALITY CONTROL BEFORE RESUBMISSION

### [ ] Data checks:
- [ ] All numbers consistent across text, figures, tables
- [ ] All error bars explained (SD, SE, range, CI?)
- [ ] All statistics reported with appropriate tests
- [ ] Sample sizes stated for all measurements

### [ ] Figure checks:
- [ ] High resolution (300 dpi minimum)
- [ ] All axes labeled with units
- [ ] All symbols defined in caption or legend
- [ ] Color-blind friendly palette if using colors
- [ ] Consistent font sizes across all figures

### [ ] Reference checks:
- [ ] All citations in text are in reference list
- [ ] All references in list are cited in text
- [ ] Format consistent with journal style
- [ ] DOIs provided where available

### [ ] Supplementary material checks:
- [ ] All supplementary figures/tables referenced in main text
- [ ] Numbering is clear (Fig. S1, Table S1, etc.)
- [ ] All have complete captions
- [ ] File naming is clear

### [ ] Language checks:
- [ ] Spell-check (American or British English consistently)
- [ ] Grammar check
- [ ] Avoid passive voice where possible
- [ ] Define all acronyms at first use
- [ ] Check for spacing issues (seen in extracted text)

---

## ESTIMATED TIMELINE

### Week 1:
- Days 1-3: DLVO calculations and figures
- Days 4-5: System parameters table and coverage analysis

### Week 2:
- Days 1-5: New ionic strength experiments (preparation, measurement, analysis)

### Week 3:  
- Days 1-2: UFB stability measurements
- Days 3-4: Expanded dimer analysis
- Day 5: Compile results, start writing

### Week 4:
- Days 1-2: Integrate new data into manuscript
- Days 3-4: Revise text, update figures
- Day 5: Response letter, final checks

### Optional Week 5 (if doing Tier 2):
- Days 1-3: UFB/AL ratio experiments or control experiment
- Days 4-5: Kinetic modeling and polydispersity analysis

**Total: 4 weeks (minimum) to 5 weeks (recommended)**

---

## DAILY PROGRESS TRACKING

Use this to track your progress:

| Task | Status | Date Started | Date Completed | Notes |
|------|--------|--------------|----------------|-------|
| DLVO calculation (AL-AL) | ⬜ | | | |
| DLVO calculation (UFB-AL) | ⬜ | | | |
| DLVO calculation (modified) | ⬜ | | | |
| DLVO figures | ⬜ | | | |
| System parameters table | ⬜ | | | |
| Coverage fraction calculation | ⬜ | | | |
| Ionic strength: 1 mM | ⬜ | | | |
| Ionic strength: 3 mM | ⬜ | | | |
| Ionic strength: 5 mM | ⬜ | | | |
| UFB stability time-series | ⬜ | | | |
| Dimer analysis (n=30) | ⬜ | | | |
| UFB/AL ratio experiments | ⬜ | | | |
| Control experiment | ⬜ | | | |
| Kinetic modeling | ⬜ | | | |
| Polydispersity analysis | ⬜ | | | |
| Manuscript revision | ⬜ | | | |
| Figure updates | ⬜ | | | |
| Response letter | ⬜ | | | |
| Final checks | ⬜ | | | |

---

## RESOURCES YOU'LL NEED

### Software:
- [ ] MATLAB/Mathematica for DLVO calculations
  - Or use existing codes from your group's previous papers
- [ ] Origin/GraphPad for figure making
- [ ] ImageJ for dimer analysis (you already have)
- [ ] NTA software for stability measurements (you already have)

### Materials:
- [ ] NaCl solutions at 1, 3, 5 mM (easy to prepare)
- [ ] Same AL and UFB batches if possible (consistency)
- [ ] Calibration standards for all instruments

### Literature:
- [ ] Gregory (1973) - patch flocculation theory
- [ ] Israelachvili book - DLVO calculations
- [ ] Your group's previous papers - methods and format
- [ ] Reviewer's suggested references

---

## FINAL CHECKLIST BEFORE SUBMISSION

### [ ] All Tier 1 items completed
### [ ] Manuscript compiled with new data
### [ ] All figures updated and high quality
### [ ] Supplementary material organized
### [ ] Response letter drafted
### [ ] All authors have approved
### [ ] Checked against journal formatting requirements
### [ ] Cover letter prepared (if required)
### [ ] All files renamed per journal requirements

---

## CONTACT FOR HELP

If you get stuck on:
- **DLVO calculations:** See Israelachvili book Chapter 11, or your group's Refs 37-42
- **Statistical analysis:** Consult university statistics center
- **Figure formatting:** Check journal's author guidelines
- **Kinetic modeling:** See Refs 35, 36 from your own group

---

**Good luck! The paper is close - these revisions will get it across the finish line.**

**Remember: The goal is not perfection, but completion with scientific rigor.**

---

*Checklist Version 1.0*  
*Date: 2025-11-20*
