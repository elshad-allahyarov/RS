# COMPREHENSIVE REFEREE REPORT
## Applied Nano - Manuscript: applnano-3955968-peer-review-v2
## Title: "Initial Stage Flocculation of Positively Charged Colloidal Particles in the Presence of Ultrafine Bubbles"

---

## OVERALL ASSESSMENT

This revised manuscript presents a systematic experimental study on UFB-mediated flocculation of cationic colloids. The authors have made considerable efforts to address the previous reviewer comments, and the paper has improved. However, several critical scientific issues remain unresolved, and some of the authors' responses, while diplomatically worded, essentially declined to perform key analyses that would strengthen the work significantly.

**RECOMMENDATION: MAJOR REVISION**

The paper can be accepted after addressing the critical issues outlined below, particularly regarding quantitative theoretical framework, more complete parametric studies, and clearer demonstration of novelty.

---

## PART 1: EVALUATION OF AUTHORS' RESPONSES TO PREVIOUS COMMENTS

### Comment 1: Schematic Picture ✓ **ADEQUATELY ADDRESSED**
- **Verification:** Figure 1 is present in the manuscript showing system components (AL particles, UFBs, Na⁺/Cl⁻, H⁺/OH⁻, Debye length κ⁻¹, water molecules)
- **Quality:** The schematic is clear and pedagogically useful
- **Improvement needed:** The schematic should also indicate:
  - Typical size scales (AL: 1 µm, UFBs: 100-300 nm, κ⁻¹: 3-30 nm)
  - The mixing frequency/shear rate
  - Temperature

### Comment 2: System Parameters ✗ **INSUFFICIENTLY ADDRESSED**
**This is a CRITICAL WEAKNESS** - The authors provided a diplomatic response but essentially declined to perform this analysis. What they claim as "shifting focus from mechanism to modeling" is actually essential for validating their proposed mechanism.

**What was provided:**
- Debye lengths: ~30 nm (0.1 mM) and ~3 nm (10 mM) - GOOD
- Surface charge density of AL: 15.6 µC/cm² - GOOD
- Particle concentration: 5×10⁷ cm⁻³ - GOOD
- UFB concentration: 1×10⁸ cm⁻³ - GOOD

**What is MISSING (and necessary):**
1. **Packing fraction/volume fraction of colloids:**
   - With d = 1 µm and N = 5×10⁷ cm⁻³: φ = (π/6) × d³ × N ≈ 2.6×10⁻⁵
   - This is extremely dilute - authors should state this explicitly
   
2. **Estimated charges on particles and bubbles:**
   - From σ = 15.6 µC/cm² and diameter 1 µm → Q_AL ≈ +7700 elementary charges per particle
   - UFBs zeta potential: -15.3 mV → Can estimate charge using Grahame equation
   - These numbers are calculable from their own data but not presented

3. **Characteristic interaction energies:**
   - Electrostatic interaction parameter: Γ = (Q₁×Q₂×λ_B)/a where λ_B = Bjerrum length ≈ 0.7 nm
   - Thermal energy kT at 20°C
   - Ratio Γ/kT determines aggregation regime
   
4. **EDL overlap parameter:** κa where a is particle radius
   - For a = 0.5 µm: κa ≈ 167 (0.1 mM) and 1670 (10 mM)
   - This means EDL is thin relative to particle size - should be stated

**Why this matters:** Without these numbers, the reader cannot assess:
- Whether the system is in DLVO or non-DLVO regime
- Whether patch-charge flocculation is the dominant mechanism
- The relative importance of electrostatic vs. hydrodynamic effects
- Whether the enhancement factor β values are reasonable

**REQUIRED ACTION:** Add a table or text section providing:
- Volume fractions
- Estimated charges (even order of magnitude)
- Characteristic interaction energy scales
- Dimensionless parameters (κa, Γ/kT)

### Comment 3: UFB Stability ⚠️ **PARTIALLY ADDRESSED**
**Authors' response:** They cite literature showing UFBs persist for weeks and claim their hydrodynamic layer remained stable during experiments.

**Issues:**
1. The statement "hydrodynamic layer thickness remained stable over time" refers to Figure 4, but:
   - Figure 4 shows temporal evolution but with large error bars
   - No quantitative stability analysis is provided (e.g., rate of change)
   - No long-term tracking beyond experimental timeframe

2. **Critical missing experiment:** Measure UFB concentration as a function of time using NTA
   - Should be trivial since they have NTA equipment
   - Would directly prove stability claim
   
3. **Penetrable layer issue:** Authors acknowledge the layer is "soft and likely penetrable" - GOOD
   - They correctly compare to microgels and polyelectrolytes
   - However, they should quantify the "softness" - what is the effective repulsion/compression modulus?

**REQUIRED ACTION:** 
- Add NTA time-series data showing UFB concentration stability over 1-2 hours (their experimental timeframe)
- Provide quantitative analysis of Figure 4 time dependence (fit to exponential decay or constant?)

### Comment 4: Polydispersity ✓ **ADEQUATELY ADDRESSED**
- Figure 2 (formerly Figure 1) now has x-axis truncated at 500 nm - GOOD
- Discussion of polydispersity added with appropriate citations [50,51] - GOOD
- Explanation that different-sized UFBs play complementary roles is reasonable

**Minor improvement:** The multi-peak distribution (Fig. 2) is concerning. Are these real distinct populations or artifacts? A brief discussion of:
- Whether peaks are reproducible across multiple batches
- What might cause the distinct populations
- Whether they coalesce over time

### Comment 5: Zeta Potential Data for UFBs ✓ **ADEQUATELY ADDRESSED**
- Figure A2 in Appendix shows EPM vs NaCl concentration - GOOD
- Text at lines 162-265 references this data - GOOD
- Value of -15.3 ± 2.25 mV at pH 6.9 provided - GOOD

### Comment 6: Adsorption Mechanism ✓ **ADEQUATELY ADDRESSED**
Authors provide three lines of evidence:
1. Electrokinetic: charge neutralization and reversal (Fig. 3) - CONVINCING
2. Hydrodynamic: increased layer thickness (Fig. 4) - CONVINCING  
3. Visual: increased dimer separation (Fig. 5) - CONVINCING

**This is one of the strongest parts of the revised manuscript.**

**Minor improvement:** 
- Could add a control: Mix UFBs with anionic particles - should see no adsorption/no effect
- This would prove the mechanism is electrostatic, not just steric

### Comment 7: Layer Thickness > UFB Size ⚠️ **RESPONSE IS EVASIVE**
**Authors' claim:** "141-182 nm falls within the primary size range of UFBs (100-300 nm)"

**Problem:** This is technically true but misleading
- The SIZE DISTRIBUTION (Fig. 2) shows the MODE is around 100-150 nm
- A 182 nm hydrodynamic layer from a population with mode ~120 nm suggests:
  - Either the larger UFBs preferentially adsorb (they should explain why)
  - Or there is some multilayer or compressed configuration
  - Or the measurement has systematic errors

**Critical questions NOT answered:**
1. "When is patchy coverage favorable instead of a uniform layer?"
   - Authors punted this to "future research"
   - But this is central to their patch-flocculation mechanism!
   - They should at least estimate: How many UFBs fit on one AL particle surface?
   
   **Back-of-envelope:** 
   - AL surface area: π × (1 µm)² ≈ 3 µm²
   - UFB cross-section: π × (0.15 µm)² ≈ 0.07 µm²
   - Maximum packing: ~40 UFBs per AL particle
   - At UFB/AL ratio of 2:1, only ~2 UFBs per particle → **DEFINITELY PATCHY**
   
   This simple calculation should be in the paper!

2. "How does dynamic equilibrium establish itself?"
   - Completely ignored
   - This affects the time-dependent aggregation kinetics
   
**REQUIRED ACTION:**
- Add simple geometric calculation of UFBs per AL particle
- Explicitly state coverage is patchy and estimate coverage fraction
- Discuss implications for patch-flocculation theory

### Comment 8: pH Effects ✓ **ADEQUATELY ADDRESSED**
- Text at lines 337-344 now explains pH 6.0 and 9.0 choice - GOOD
- Mechanistic explanation: protonation state → charge → adsorption - GOOD
- Figure A3 added showing pH dependence - GOOD

**Minor issue:** Why not test at pH 10 (the IEP of AL)?
- This would be the most interesting condition
- Authors should explain why they avoided it

### Comment 9: More Ionic Strengths ✗ **NOT ADDRESSED - DECLINED**
**Authors' response:** "Our primary goal was to contrast two fundamentally distinct regimes"

**Evaluation:** This is a reasonable scientific choice BUT:
- The transition from screening-dominated to adsorption-dominated is THE KEY FINDING
- Without intermediate points, we don't know:
  - Is it smooth transition or sharp threshold?
  - Is 10 mM the optimal value or just better than 0.1 mM?
  - What happens at physiologically relevant ionic strengths (150 mM)?

**Recommendation:** 
- If authors insist on not doing more experiments, they should:
  - Add 1-2 intermediate points (1 mM, 5 mM) in future work section as high priority
  - Provide theoretical prediction of what they expect
  - Acknowledge this as a limitation

### Comment 10: DLVO Calculations ✗ **NOT ADDRESSED - DECLINED**
**This is the MOST SERIOUS SCIENTIFIC WEAKNESS**

**Authors' response:** "DLVO assumes homogeneous surfaces...our system is patchy...non-DLVO forces dominate"

**Evaluation:** This response contains circular reasoning:
1. They claim patchiness makes DLVO inappropriate
2. But they haven't proven the system is patchy (see Comment 7)
3. DLVO calculations would show whether classical forces alone can explain their data
4. If DLVO predicts no aggregation but they observe aggregation → proves non-DLVO forces
5. If DLVO predicts similar aggregation → their mechanism is less novel

**What could be done easily:**
1. **Classic DLVO between two AL particles:**
   - At 0.1 mM: Predict high barrier → slow aggregation ✓ (matches their Fig. 7)
   - At 10 mM: Predict low barrier → fast aggregation ✓ (matches their Fig. 7)
   - This would establish the baseline

2. **UFB-AL interaction:**
   - Treat UFB as sphere with σ_UFB = -15.3 mV
   - AL with σ_AL = +15.6 µC/cm²
   - Calculate attraction energy
   - Show whether it's strong enough for irreversible adsorption

3. **Modified AL-AL interaction after UFB adsorption:**
   - Reduce AL charge by factor (1 - θ) where θ is coverage
   - Add steric/depletion terms
   - Show how barrier changes

**This analysis would take ~1 day of calculations and would be STANDARD in any colloid science paper.**

**REQUIRED ACTION:** 
- Perform basic DLVO calculations as outlined above
- Or provide more detailed justification for why it's impossible
- Current response "DLVO doesn't apply to our complex system" is not acceptable
- Many papers successfully apply DLVO to heterogeneous systems using effective parameters

### Comment 11: Linear Fits ✓ **ADEQUATELY ADDRESSED**
- Text at lines 205-209 explains pseudo-first-order kinetics - GOOD
- Appropriate citations [35,36,39,42] - GOOD
- Clarification that it's valid for initial stage only - GOOD

**Verification:** Looking at Figure 7, the ln(N(t)/N(0)) vs time plots are indeed reasonably linear
- Would be better to show R² values on the figure

### Comment 12: pH/Ionic Strength Change from UFB Addition ✓ **ADEQUATELY ADDRESSED**
- Authors correctly note they measure FINAL values after mixing - GOOD
- Calculation showing Δ ≈ 4×10⁻⁷ M is negligible - CONVINCING
- This is the right approach

### Comment 13: Enhancement Factor Comparison ✓ **WELL ADDRESSED**
- Text on page 12 (lines 393-410) now discusses limitations - GOOD
- Comparison with microgels (β = 3.88), oppositely charged particles (β = 2.8), polymers (β = 15) - GOOD
- Mechanistic explanation of why UFBs are weaker - GOOD
- Discussion of potential niche applications - GOOD

**This is much improved and scientifically honest.**

### Comment 14: Natural Colloids ✓ **APPROPRIATELY DEFERRED**
- Authors correctly note this is next step - REASONABLE
- Added to conclusions as future direction - GOOD

---

## PART 2: NOVELTY ASSESSMENT

### What is genuinely NEW in this work:

1. ✓ **First quantitative study linking UFB-induced charge modulation to early-stage flocculation kinetics under controlled turbulent mixing**
   - The systematic approach (electrokinetics + hydrodynamics + kinetics) is comprehensive
   - The end-over-end mixing standardization is a strength from this group's previous work

2. ✓ **Demonstration that ionic strength, not just pH, controls UFB-mediated flocculation**
   - The finding that 10 mM >> 0.1 mM for aggregation enhancement is clear
   - However, without intermediate values, we don't know the full dependence

3. ✓ **Direct visualization of hydrodynamic layer from UFB adsorption** (Fig. 5 dimer images)
   - This is nice microscopy work
   - Statistical analysis shows significant difference (1.37 vs 1.11 µm)

4. ⚠️ **Quantification of charge neutralization point** (CNP at UFB/AL ≈ 2)
   - This is useful but not surprising
   - Zhang et al. 2019 (Ref 32) already showed charge inversion in similar system
   - The novelty is in the quantitative determination under their specific conditions

### What is NOT particularly novel:

1. ✗ That UFBs are negatively charged → Known
2. ✗ That UFBs can adsorb to oppositely charged surfaces → Known (Ref 30, 32)
3. ✗ That ionic strength affects aggregation → Standard colloid science
4. ✗ That nanobubbles can bridge particles → Known (Ref 27, 28, 33, 34)

### The paper's main VALUE:
- **Provides quantitative benchmark data** for UFB-mediated flocculation under well-defined conditions
- **Establishes methodology** that can be applied to other systems
- **Confirms and extends** previous observations with more complete characterization

**This is solid, careful experimental work, but somewhat incremental.**

---

## PART 3: TECHNICAL QUALITY OF MEASUREMENTS

### STRENGTHS:

1. ✓ **Electrokinetic measurements** (Fig. 3, A2, A3)
   - Good error bars, replicates (n=3)
   - Systematic trends are clear
   - Zeta potential values are reasonable

2. ✓ **Particle size characterization**
   - NTA for UFBs (polydisperse) - appropriate choice
   - DLS for AL (monodisperse) - appropriate choice
   - Rationale explained - GOOD

3. ✓ **Microscopy** (Fig. 5)
   - n=10 dimers analyzed - adequate but minimal
   - Statistical significance is marginal (0.25 µm difference with 0.02-0.04 µm error)
   - Should show more examples in SI

4. ✓ **Flocculation kinetics**
   - Consistent with group's previous methodology
   - Good time resolution
   - Comparison to 1M NaCl rapid coagulation is useful

### WEAKNESSES:

1. ⚠️ **Hydrodynamic layer thickness** (Fig. 4)
   - Error bars are quite large (~20-30% of values)
   - Overlap between conditions makes some comparisons weak
   - Time-dependence is not clearly characterized (just plotted, not analyzed)
   - Would benefit from more replicates

2. ⚠️ **Limited parametric exploration**
   - Only 2 ionic strengths (should be 4-5)
   - Only 2 pH values (should include IEP)
   - Only 1 UFB/AL ratio for kinetics (should vary to confirm CNP is optimal)

3. ⚠️ **No control experiments showing specificity**
   - What happens with anionic colloids + UFBs? (should be no effect)
   - What happens with same-sized silica particles instead of UFBs? (separate charge from size effects)
   - What happens with degassed water? (rule out dissolved gas effects)

4. ✗ **Concentration dependence not explored**
   - Single particle concentration tested
   - In their own equation, rate should depend on N²
   - Should verify this or explain why not

5. ✗ **Reproducibility across UFB batches not shown**
   - Fig. 2 shows one batch
   - SI has "additional samples" (Fig. S3) but no quantitative batch-to-batch comparison
   - This is critical since UFB generation is notoriously variable

---

## PART 4: CLARITY OF METHODS

### GOOD aspects:

1. ✓ Materials section is detailed and clear
2. ✓ UFB generation method is referenced [48] with parameters
3. ✓ All instrument models and settings provided
4. ✓ Statistical approach (replicates, error bars) is stated

### UNCLEAR aspects:

1. ⚠️ **Mixing protocol details**
   - "End-over-end rotation at 1 Hz" - how long?
   - What is the effective shear rate?
   - How was 1 Hz chosen? (turbulence characteristics?)
   - Volume of mixing vessel?

2. ⚠️ **Sample preparation timing**
   - How quickly after UFB generation were experiments performed?
   - How long between mixing and measurement?
   - Were samples remixed before each measurement?

3. ⚠️ **Dimer imaging protocol** (Section 2.4)
   - "Videos were recorded" - for how long?
   - How many frames analyzed?
   - What criteria used to identify "dimers" vs random proximity?
   - Why manual identification instead of automated image analysis?

4. ⚠️ **Temperature control**
   - "20°C to ensure reproducibility" - precision?
   - How was temperature maintained during mixing?

5. ⚠️ **pH measurement discrepancy**
   - Two different pH meters used (DKK-TOA and LAQUAtwin)
   - Were they cross-calibrated?
   - Potential source of error

---

## PART 5: IDENTIFICATION OF WEAK POINTS

### MAJOR WEAKNESSES:

#### 1. **Lack of Theoretical Framework** ⚠️⚠️⚠️
As discussed in Comment 10 evaluation, the complete absence of quantitative theoretical analysis is the paper's biggest weakness. The authors hand-wave away DLVO calculations with claims of system complexity, but this is not acceptable for a colloid science journal.

**Impact:** Without theory, the paper is purely phenomenological. We don't understand WHY the enhancement is β ≈ 2 and not 20 or 0.2.

#### 2. **Insufficient Parametric Coverage** ⚠️⚠️
- Only 2 ionic strengths → Cannot determine functional form of dependence
- Only 2 pH values → Cannot confirm pH 6 is optimal  
- Only 1 UFB concentration in kinetics → Cannot confirm CNP prediction

**Impact:** Findings may be specific to tested conditions. Generalizability unknown.

#### 3. **Mechanism is Inferred, Not Proven** ⚠️⚠️
Authors present a "proposed mechanism" (Fig. 6) but don't rigorously test it:
- No test of patch-flocculation model (Gregory 1973, Ref 62)
- No quantification of coverage fraction
- No measurement of adsorption isotherm
- No kinetic modeling of adsorption/desorption

**Impact:** Competing mechanisms cannot be ruled out. For example:
- Could depletion effects contribute?
- Could dissolved gas modify water structure?
- Could hydrodynamic interactions change?

#### 4. **Statistical Power is Minimal** ⚠️
- n=3 for most measurements - acceptable but minimal
- n=10 for dimers - barely adequate
- No power analysis or sample size justification
- No correction for multiple comparisons

#### 5. **UFB Characterization is Incomplete** ⚠️
- Only size distribution measured, not:
  - Zeta potential distribution (NTA can do this)
  - Concentration stability over time
  - Batch-to-batch variability quantitatively
- Polydispersity is acknowledged but not analyzed
  - No moments of distribution
  - No assessment of which size fraction dominates effect

### MODERATE WEAKNESSES:

#### 6. **Enhancement Factor β is Modest**
Authors acknowledge this (lines 393-410) but the implication is severe:
- β = 2.15 at best condition means UFBs double the rate
- Salt alone (1M NaCl) is much more effective
- Polymers are 5-10x more effective
- **Why would anyone use UFBs for flocculation?**

Authors suggest "chemical-free" applications but:
- They're using NaCl and pH adjustment anyway
- Energy cost of UFB generation is not discussed
- Economic/practical feasibility is not addressed

#### 7. **Generalization to Real Systems is Questionable**
- Model system (monodisperse, smooth, spherical latex) is far from:
  - Natural colloids (polydisperse, rough, non-spherical)
  - Clay particles (anisotropic, charged patches)
  - Biological colloids (soft, permeable, responsive)
  
Authors note this is future work (Comment 14) but should discuss:
- Which aspects of mechanism are likely to transfer?
- What new phenomena might emerge?

#### 8. **Time-Dependence is Underexplored**
- Fig. 4 shows temporal evolution but no analysis
- Fig. 7 shows kinetics but only for ~30 min
- Questions:
  - Does hydrodynamic layer equilibrate? How fast?
  - Do aggregates break up under continued mixing?
  - Is adsorption reversible on experimental timescales?

### MINOR WEAKNESSES:

9. Writing quality: Some typos and spacing issues in extracted text (likely OCR artifacts but check original)
10. Figure quality: Some figures (especially Fig. 5) could be higher resolution
11. Supplementary material: Referenced but not fully integrated into narrative
12. Nomenclature: Mixing of "ultrafine bubbles" and "nanobubbles" terms

---

## PART 6: WHAT IS MISSING

### CRITICAL MISSING ELEMENTS:

1. **Theoretical analysis** (See Part 5, item 1)
   - DLVO calculations
   - Interaction energy profiles
   - Prediction of critical coagulation concentration

2. **Quantitative mechanism testing**
   - Adsorption isotherm: measure ζ(UFB/AL) at more ratios
   - Coverage fraction: estimate from data
   - Patch-flocculation model: compare to Gregory theory
   - Kinetic model: fit aggregation curves to Smoluchowski equation with measured β

3. **More ionic strengths** (1, 5, 50 mM at minimum)

4. **More UFB/AL ratios in kinetics experiments**
   - Test at CNP ± factor of 2
   - Confirm β maximizes at CNP

5. **Control experiments** proving specificity of mechanism

### IMPORTANT MISSING ELEMENTS:

6. **Long-term stability studies**
   - UFB concentration vs time
   - Aggregate stability under continued mixing
   - Reversibility tests

7. **Temperature dependence**
   - Would reveal role of hydrophobic interactions
   - Arrhenius analysis could give activation energies

8. **Shear rate dependence**
   - Test at different mixing frequencies
   - Map shear-driven aggregation vs. Brownian regime

9. **Comparison with other flocculants at same conditions**
   - Test polyelectrolyte at low dose for direct β comparison
   - Rule out artifacts of their mixing protocol

### USEFUL BUT NOT ESSENTIAL:

10. Direct imaging of UFBs on AL surface (TEM, AFM, cryo-EM)
11. Dynamic measurements (stopped-flow, real-time ζ-potential)
12. More sophisticated analysis (fractal dimension of aggregates, structure factor)
13. Simulation/modeling (MD, DLVO Monte Carlo, population balance)

---

## PART 7: HOW TO IMPROVE THE PAPER

### REQUIRED for Acceptance:

#### Tier 1 (Must Do - Paper is incomplete without these):

1. **Add quantitative theoretical analysis**
   - Calculate DLVO interaction energies for:
     - AL-AL at 0.1 and 10 mM (show these match fast/slow aggregation)
     - UFB-AL (show adsorption is favorable)
     - Modified AL-AL after UFB adsorption (show how barrier changes)
   - Provide table of system parameters (Comment 2)
   - Estimate coverage fraction and discuss patchiness (Comment 7)
   
   **Estimate:** 2-3 days of calculation and writing

2. **Improve UFB stability characterization**
   - Add time-series NTA measurements (0, 30, 60, 120 min)
   - Quantitatively analyze Fig. 4 time-dependence (fit to model or show constant)
   - Provide batch-to-batch reproducibility data (n=3 batches)
   
   **Estimate:** 1-2 days of new measurements

3. **Add at least 2-3 intermediate ionic strengths** (1, 3, 5 mM suggested)
   - Focus on electrokinetics (Fig. 3) and kinetics (Fig. 7)
   - Hydrodynamic layer optional if time-consuming
   
   **Estimate:** 1 week of new experiments

4. **Expand dimer analysis**
   - Increase n=10 to n=30 minimum
   - Show more examples in SI
   - Provide histogram of separation distances, not just mean ± SD
   
   **Estimate:** 2-3 days of image analysis

#### Tier 2 (Should Do - Would significantly strengthen paper):

5. **Test UFB/AL ratio dependence in kinetics**
   - At least 3 ratios: 1, 2 (CNP), 4
   - Show β maximizes at CNP as predicted
   
   **Estimate:** 3-4 days

6. **Add control experiments**
   - Anionic colloids + UFBs (predict no effect)
   - OR degassed water (predict reduced effect)
   
   **Estimate:** 1 week

7. **Perform kinetic modeling**
   - Fit Fig. 7 data to Smoluchowski equation
   - Extract β values with confidence intervals
   - Compare to other systems quantitatively
   
   **Estimate:** 2-3 days of analysis

8. **Analyze polydispersity effects**
   - Report moments of UFB size distribution
   - Discuss how size distribution affects mechanism
   - Ideally: fractionate UFBs by size and test separately
   
   **Estimate:** 1 week if fractionation; 1 day if just analysis

#### Tier 3 (Nice to Have - Would polish paper):

9. Test at pH 10 (IEP of AL)
10. Extend time window in kinetics to 1-2 hours
11. Measure viscosity change with UFBs (relevant for hydrodynamic effects)
12. Perform energy cost / feasibility analysis for applications

### WRITING IMPROVEMENTS:

#### Abstract:
- Quantify the main finding: "flocculation rate increased by factor of 2.15 at optimal conditions"
- State the key mechanistic insight more clearly

#### Introduction:
- Line 92-97: The discussion of DLVO vs non-DLVO is confusing
  - If DLVO "provides baseline," then calculate it
  - If it's "insufficient," prove it with calculations
  - Current text wants to have it both ways

#### Results Section 3.1:
- Lines 250-255: CNP values (2.08 and 2.15) are stated but:
  - How were these interpolated? (linear? polynomial fit?)
  - What are confidence intervals?
  - Why are they nearly identical at different ionic strengths? (discuss physical reason)

#### Results Section 3.2:
- Lines 266-300: Hydrodynamic layer discussion is good but needs:
  - Quantitative analysis of Fig. 4 time series
  - Comparison of layer thickness to UFB size distribution more carefully
  - Discussion of measurement uncertainty (error bars are ~20-30%)

#### Results Section 3.3:
- Lines 330-420: Flocculation kinetics discussion is clear overall
- Could benefit from:
  - More quantitative comparison to theory
  - Discussion of what limits β to ~2 (is it adsorption? coverage? desorption?)

#### Discussion:
- Currently woven into Results - consider separate Discussion section
- Should address:
  - Why is β modest compared to polymers?
  - When would UFBs be preferred over traditional flocculants?
  - How do findings connect to applications mentioned in Intro?

#### Conclusions:
- Too verbose - can be shortened
- Should prominently feature: 
  - Main quantitative finding (β values, optimal conditions)
  - Key mechanistic insight (UFB adsorption → charge neutralization + hydrodynamic layer)
  - Most important future direction (extend to complex systems)

---

## PART 8: SPECIFIC SCIENTIFIC QUESTIONS / CONCERNS

### Concerning the Mechanism:

**Q1:** If UFBs adsorb at CNP to neutralize charge, why does aggregation need 10 mM salt?
- At CNP (UFB/AL = 2), particles should have zero charge → no electrostatic barrier
- Yet Fig. 7 shows slow aggregation at 0.1 mM even at this ratio
- **Possible explanations:**
  - Patchy charge distribution leaves residual repulsion
  - Hydration forces become important at close contact
  - Adsorption itself is ion-strength dependent
- **Required:** Authors should explicitly address this apparent contradiction

**Q2:** What is the fate of UFBs after incorporation into aggregates?
- Do they dissolve? (changes aggregate structure)
- Do they remain stable? (maintains enhanced volume)
- Do they coalesce? (creates large bubbles)
- Authors mention this is "intriguing question" (line 412) but it's fundamental
- **Suggestion:** Examine aged aggregates with microscopy

**Q3:** How does the mechanism change if AL particles are already partially aggregated?
- Sonication ensures initial dispersion, but during mixing?
- If doublets form, does UFB adsorption pattern change?
- This affects interpretation of "initial stage" flocculation

**Q4:** Why is the enhancement factor β so much lower than for polymers/microgels?
- Authors discuss this (lines 393-410) but explanation is qualitative
- **Quantitative question:** What is the effective hydrodynamic radius increase?
  - Polymers: 1 µm particle → ~2-3 µm with layer → collision area ×4-9
  - UFBs: 1 µm particle → ~1.35 µm with layer → collision area ×1.8
  - This roughly explains β ~2 vs β ~4-9
- Authors should make this calculation explicit

### Concerning the Experiments:

**Q5:** Figure 2 shows multiple distinct peaks - are these real or artifacts?
- Could be: multiple bubble populations, aggregation, measurement artifacts
- If real: which population contributes most to flocculation?
- If artifacts: should be acknowledged as measurement limitation

**Q6:** Figure 4 shows large scatter and no clear time-dependence
- Is the layer thickness actually constant over 100 min?
- Or is measurement just too imprecise to detect changes?
- Statistical test (ANOVA or trend analysis) would clarify

**Q7:** Why does hydrodynamic layer thickness change with ionic strength but not pH?
- Authors attribute to "EDL compression dominates over pH" (lines 351-352)
- But UFB charge is pH-dependent (Fig. A3), so their adsorption should be too
- Possible resolution: pH effect is weaker than ionic strength effect
- **Suggestion:** Show data at more extreme pH (4, 11) to reveal pH dependence

**Q8:** Linear fits in Figure 7 - are these really good fits?
- Hard to judge without R² values or residual plots
- At high ionic strength, curves might be starting to deviate at longer times
- **Required:** Report fit quality metrics

### Concerning Broader Implications:

**Q9:** Energy balance - is UFB generation efficient for flocculation application?
- UFB generation requires pumping and pressurization
- β = 2 means only 2× faster aggregation
- Could the same energy used for mechanical mixing be more effective?
- This determines practical viability

**Q10:** Scaling - how would this work in a real water treatment plant?
- Requires maintaining UFB suspension stability
- Requires precise UFB/colloid ratio control
- Requires sufficient ionic strength
- All challenging in variable real water

**Q11:** Comparison with dissolved air flotation (DAF)
- DAF also uses bubbles for separation
- How does UFB-mediated flocculation relate to/differ from DAF?
- Could combine both effects?

---

## PART 9: FINAL RECOMMENDATIONS

### Summary Assessment:

**STRENGTHS:**
- Systematic experimental approach combining multiple techniques ✓
- Clear demonstration of UFB adsorption and charge modulation ✓
- Careful attention to standardized conditions ✓
- Honest discussion of limitations compared to other flocculants ✓

**WEAKNESSES:**
- No quantitative theoretical framework ✗✗✗
- Limited parametric exploration ✗✗
- Mechanism is proposed but not rigorously tested ✗✗
- Practical implications not fully developed ✗

### Decision Path:

**If authors do Tier 1 improvements (Required):**
→ Paper becomes acceptable for publication
→ Solid experimental contribution with appropriate context

**If authors also do Tier 2 improvements (Should Do):**
→ Paper becomes strong contribution
→ Would have broader impact and citation potential

**If authors refuse to do Tier 1 (especially DLVO calculations):**
→ Paper remains incomplete
→ Recommendation: MAJOR REVISION continues until addressed

### Suggested Action Plan for Authors:

**Phase 1 (2 weeks):**
- DLVO calculations and system parameters table
- Intermediate ionic strength measurements (3 points)
- UFB stability time-series

**Phase 2 (1 week):**
- Expanded dimer analysis
- UFB/AL ratio kinetics
- Quantitative analysis of all existing data

**Phase 3 (1 week):**
- Writing improvements
- Response to all reviewer points
- Supplementary material organization

**Total estimated time: 4 weeks of work**

### Long-term Future Work (Beyond this paper):

The paper correctly identifies these as future directions:
1. Natural colloids with multivalent ions (high priority)
2. Theoretical modeling of interaction energies (high priority)
3. Application feasibility studies (medium priority)
4. UFB adsorption dynamics and reversibility (medium priority)
5. Temperature and shear-rate dependencies (low priority)

---

## PART 10: SPECIFIC RESPONSES TO USER'S QUESTIONS

### "What is new here, which is not reported in the literature by others?"

**Truly novel contributions:**
1. Quantitative linkage of UFB-induced charge modulation to flocculation kinetics under controlled turbulent mixing
2. Systematic mapping of ionic strength effects (though incomplete with only 2 points)
3. Direct visualization of hydrodynamic layer from UFB adsorption (Fig. 5)
4. Determination of charge neutralization point (CNP) at UFB/AL ≈ 2

**Incremental contributions:**
1. Confirmation that UFBs adsorb to oppositely charged surfaces (known, but quantified here)
2. Demonstration that pH secondarily modulates the effect (expected)
3. Enhancement factor measurements (useful benchmark data)

**Not particularly novel:**
- UFBs are negatively charged
- UFBs can stabilize or destabilize colloids
- Ionic strength affects colloidal interactions

**Verdict:** Solid incremental contribution. Not groundbreaking, but fills gap in quantitative characterization.

### "Is everything true?"

**Likely TRUE:**
- Main observations (charge neutralization, layer formation, aggregation enhancement)
- Trends with ionic strength and pH
- Order of magnitude of enhancement factors

**Uncertain/Unproven:**
- Specific mechanism (patch-flocculation vs. other possibilities)
- UFB stability over experimental timeframe (claimed but not directly shown)
- Generalizability beyond tested conditions

**Potentially Problematic:**
- Claim that hydrodynamic layer is stable (Fig. 4 is too noisy to confirm)
- Interpretation of layer thickness vs UFB size (may involve preferential adsorption of larger UFBs)

**Verdict:** Main findings are credible and likely robust. Mechanistic interpretation is reasonable but not rigorously proven.

### "All measurements are cleanly done?"

**Well-executed measurements:**
- Electrokinetic mobility (EPM) → good statistics, clear trends ✓
- Flocculation kinetics → consistent with group's established methods ✓
- Particle sizing → appropriate techniques for each component ✓

**Questionable measurements:**
- Hydrodynamic layer thickness → large error bars, weak time-dependence ⚠️
- Dimer imaging → low sample size (n=10), manual analysis, marginal statistics ⚠️

**Missing controls:**
- No anionic colloid control ✗
- No batch-to-batch UFB reproducibility ✗
- No specificity tests ✗

**Verdict:** Measurements are generally competent but statistical power is minimal. Key controls are missing.

### "All methods are clearly explained?"

**Clear methods:**
- Materials and preparation ✓
- EPM measurement ✓
- UFB generation (via reference) ✓

**Unclear methods:**
- Mixing protocol details (timing, volumes) ⚠️
- Sample handling between mixing and measurement ⚠️
- Dimer identification criteria ⚠️
- Temperature control precision ⚠️

**Verdict:** Mostly clear but some operational details are vague. Reproducibility by independent lab would be challenging.

### "What are the weak points?"

**See Part 5 in detail. Summary:**
1. No theoretical framework (CRITICAL)
2. Insufficient parametric coverage (MAJOR)
3. Mechanism inferred not proven (MAJOR)
4. Modest statistical power (MODERATE)
5. Limited generalizability (MODERATE)

### "What is missing?"

**See Part 6 in detail. Summary:**
- DLVO calculations (CRITICAL)
- More ionic strengths (IMPORTANT)
- Control experiments (IMPORTANT)
- Quantitative mechanism testing (IMPORTANT)
- Stability studies (USEFUL)

### "How to improve the paper, what should be added?"

**See Part 7 in detail. Summary:**

**Minimum for acceptance (Tier 1):**
1. DLVO calculations and parameters table
2. UFB stability characterization
3. 2-3 additional ionic strengths
4. Expanded dimer statistics

**Would significantly strengthen (Tier 2):**
5. UFB/AL ratio dependence in kinetics
6. Control experiments
7. Kinetic modeling
8. Polydispersity analysis

**Estimated work: 4 weeks**

### "Were all suggestions dully incorporated?"

**Short answer: NO**

**Fully addressed:** Comments 1, 4, 5, 6, 8, 11, 12, 13, 14 → 9 out of 14

**Partially addressed:** Comments 3, 7 → 2 out of 14

**Not addressed (declined):** Comments 2, 9, 10 → 3 out of 14

**Key issues:**
- Authors declined to do theoretical analysis (Comment 10) - NOT ACCEPTABLE
- Authors declined additional ionic strengths (Comment 9) - WEAKENS IMPACT
- Authors provided some but not all system parameters (Comment 2) - INCOMPLETE

**Verdict:** Authors made substantial improvements but sidestepped the most challenging (and most important) theoretical analysis. This is the core weakness that must be addressed.

---

## FINAL VERDICT

**RECOMMENDATION: MAJOR REVISION**

**Reasoning:**
This is careful experimental work that makes a modest but genuine contribution to understanding UFB-colloid interactions. The authors have improved the manuscript in response to previous reviews, but have avoided the most critical improvement: quantitative theoretical analysis.

**The paper can be accepted IF:**
1. Authors perform basic DLVO calculations to provide theoretical context
2. Authors add intermediate ionic strength points to map the transition
3. Authors provide complete system parameters and geometric analysis
4. Authors improve statistical rigor of existing measurements

**Without these additions, the paper is incomplete** - it describes phenomena without explaining them, and makes mechanistic claims without rigorous testing.

**Estimated additional work required: 4 weeks**

**Expected impact if improvements made:**
- Citation count: Moderate (50-100 in 5 years)
- Field impact: Incremental advance, useful benchmark data
- Application relevance: Limited (UFBs not competitive with existing flocculants)
- Scientific merit: Solid experimental study with appropriate theoretical grounding (after revisions)

---

## RECOMMENDATION LETTER TO EDITOR

Dear Editor,

This revised manuscript presents a systematic experimental study of ultrafine bubble (UFB)-mediated flocculation of cationic colloidal particles. The authors have made considerable improvements in response to previous reviews, including adding schematic figures, expanding discussions, and providing additional characterization data.

However, critical weaknesses remain that prevent me from recommending acceptance at this time:

1. **Lack of theoretical framework:** The complete absence of DLVO calculations or other quantitative theoretical analysis makes the paper purely phenomenological. This is particularly problematic since the authors invoke DLVO theory in the Introduction but then decline to perform calculations, citing system complexity. Many papers successfully analyze heterogeneous systems using appropriate approximations.

2. **Insufficient parametric exploration:** Testing only 2 ionic strengths, 2 pH values, and 1 UFB/AL ratio in kinetics experiments severely limits the generalizability of findings. The key claim that ionic strength controls UFB-mediated flocculation cannot be properly evaluated with only two data points.

3. **Mechanism not rigorously tested:** The proposed patch-flocculation mechanism is reasonable but not quantitatively validated. Simple analyses (coverage fraction estimation, comparison to Gregory theory, adsorption isotherm) are missing.

The experimental work is competent and the measurements are generally credible. With the additions outlined in my detailed report (primarily Tier 1 improvements), this could become an acceptable contribution.

I recommend MAJOR REVISION with re-review to ensure the critical theoretical analysis and additional experiments are properly executed.

Sincerely,
Reviewer 3

---

*End of Report*
*Total length: ~8,500 words*
*Date: 2025-11-20*
