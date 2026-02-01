# REFEREE REPORT
## Manuscript BSPC-D-26-00735
### "CANINE GUARD: A SMART WEARABLE VEST FOR CONTINUOUS VITAL SIGN AND LOCATION MONITORING IN DOGS"

---

## RECOMMENDATION: **MAJOR REVISION REQUIRED**

---

## SUMMARY

This manuscript presents a multi-sensor wearable vest for monitoring heart rate, respiratory rate, footsteps, and location in dogs. The system integrates an Ecoflex-embedded electret microphone (MAX9814 amplifier) for acoustic cardiac sensing, a conductive stretch sensor for respiration, an ADXL335 accelerometer for activity tracking, and a GPS module, all processed by an ESP32 microcontroller. While the system integration approach shows practical merit, the manuscript suffers from significant deficiencies in experimental validation, statistical rigor, and scientific novelty that preclude publication in its current form.

---

## MAJOR CONCERNS

### 1. **Lack of Rigorous Experimental Validation**

The most critical weakness is the **complete absence of quantitative validation data**. The Results section (Section IV, p. 7-9) contains only qualitative descriptions and example waveforms without any:

- **Sample size specification**: How many dogs were tested? What breeds, ages, weights, and coat types?
- **Gold standard comparison**: No comparison with veterinary-grade ECG, respiratory monitors, or manual counting by trained personnel
- **Statistical analysis**: No means, standard deviations, confidence intervals, or significance tests
- **Validation protocol**: The experimental procedure is vaguely described as "multiple phases" without detailed methodology

**Specific issues**:
- Lines 615-616 state "heart rate measurement error remained within 3–5 BPM during resting states" - but no data table, statistical test, or Bland-Altman analysis is provided
- Line 640 mentions "measurement error remained within 2–3 breaths per minute" - again, no quantitative evidence
- Line 741 claims "accuracy rates above 92%" for step detection - no confusion matrix, precision/recall metrics, or validation details provided
- The statement "average measurement error during mild motion increased to 8–10 BPM" (lines 628-629) lacks context about acceptable clinical thresholds

**Required improvements**: A proper validation study must include: (1) minimum n=20-30 dogs across multiple breeds, (2) simultaneous recording with gold standard equipment, (3) Bland-Altman agreement analysis, (4) intra-class correlation coefficients, (5) sensitivity/specificity analysis for abnormality detection.

### 2. **Missing Methodological Details**

**Signal Processing Algorithms** (Section III.B, p. 5-6): The software design section is largely descriptive without technical specifics:
- No mathematical description of filtering operations (filter type, cutoff frequencies, order)
- Peak detection algorithms mentioned (lines 525, 541, 551) but not defined
- "Adaptive thresholding" (line 526) and "adaptive noise cancellation" (line 776) referenced without algorithmic details
- No pseudocode or flowcharts for key processing steps

**Hardware Configuration** (Section III.A, p. 4-5):
- Circuit diagrams (Figs. 2-4) show basic connectivity but lack component values (e.g., what is the 10kΩ resistor tolerance? ADC sampling rate? Supply voltage regulation specifications?)
- MAX9814 AGC settings not specified
- Battery capacity, runtime, and power consumption not quantified despite claims of "low power consumption" (line 509)

### 3. **Limited Scientific Novelty**

The paper is **predominantly an engineering integration project** rather than a fundamental scientific contribution:

**Known components**:
- Acoustic phonocardiography in animals: extensively studied (Okuno 2018, Murata 2022 - cited by authors)
- Stretch sensors for respiration: well-established (Arakawa 2020, Nuttelman 2021 - cited)
- Accelerometer-based step counting: commercial implementations exist (Whistle, FitBark, PetPace - mentioned line 347)
- ESP32 for biosignal processing: widely documented in IoT literature

**Claimed novelty** (Ecoflex-embedded acoustic sensing for canine heart rate) is **incremental**: The use of soft silicone interfaces for acoustic coupling is described in human wearables literature and has been adapted here for dogs. While practical, this does not constitute a significant methodological advance.

**Missing comparison**: No head-to-head comparison with existing commercial canine wearables (e.g., PetPace, which monitors heart rate, respiration, temperature, and activity). The authors briefly mention these devices (line 347) but never evaluate their system against them.

### 4. **Trustworthiness of Data**

Several factors raise concerns about data reliability:

- **No mention of ethical approval**: Animal testing requires Institutional Animal Care and Use Committee (IACUC) approval, which is not mentioned
- **No blinding or independent validation**: Were measurements compared by independent observers unaware of device readings?
- **Cherry-picked waveforms**: Figures 5-7 show single example traces without indication of representativeness. Were these best-case examples?
- **Panting artifacts acknowledged but not quantified** (lines 642-649): The authors admit respiratory monitoring fails during panting (a common canine behavior) but provide no quantitative assessment of failure rates or conditions
- **Motion artifact limitations** (lines 620-629): Heart rate accuracy degrades significantly during activity, yet no systematic characterization of this limitation is provided

### 5. **Incomplete Related Work Analysis**

The Literature Survey (Section II, p. 2-4) is **selective and insufficiently critical**:

- **Missing recent work**: No citation of Angelucci et al. (2024) "Validation of a Wearable System for Respiratory Rate Monitoring in Dogs" (IEEE Access) - which appears in their own reference list [8] but is never discussed
- **Commercial systems under-reviewed**: Only brief mention of Whistle, FitBark, PetPace without detailed comparison of capabilities, validation status, or limitations
- **Human wearable literature**: Extensive discussion of human sensors but insufficient adaptation justification for canine-specific challenges beyond fur interference
- **No systematic review methodology**: The survey appears narrative rather than systematic, with unclear inclusion/exclusion criteria

---

## MODERATE CONCERNS

### 6. **Overclaimed Contributions**

The Abstract and Conclusion contain **unsupported claims**:

- "The proposed system demonstrates a cost-effective, scalable, and non-invasive solution" (lines 24-25, 82-83) - No cost analysis provided, scalability not demonstrated, non-invasiveness not validated through stress/comfort assessment
- "This thoughtful design allows the vest to serve as a continuous health monitoring companion suitable for all breeds and sizes" (lines 223-226) - Only tested on unspecified number of dogs, breed diversity not documented
- "The Smart Canine Vest developed in this project represents a major advancement in the domain" (lines 1049-1051) - Overstated given the incremental nature and lack of validation

### 7. **Inadequate Discussion of Limitations**

Section IV.B mentions some limitations (lines 818-826) but these are treated superficially:
- Motion artifacts during intense activity: How intense? At what activity level does the system become unreliable?
- Panting detection failure: What percentage of monitoring time is affected? Is this clinically acceptable?
- Step detection during running: Quantification of underestimation needed
- Environmental testing: "highlights the need for improved waterproofing" (line 826) suggests the device is not currently waterproof - a critical limitation for practical use not adequately emphasized

### 8. **Figures and Data Presentation**

- **Figure 1**: System architecture diagram is generic and could apply to any multi-sensor wearable
- **Figures 2-4**: Circuit diagrams lack sufficient detail for reproducibility (missing component values, tolerances, PCB layout considerations)
- **Figures 5-7**: Waveform examples without statistical overlays, error bars, or representative sampling indication
- **No tables**: Quantitative results should be presented in tabular form with statistical measures
- **No Bland-Altman plots**: Essential for agreement studies in biomedical instrumentation

### 9. **Writing Quality Issues**

- **Inconsistent sensor naming**: "MAX9814 sensor" (lines 16, 71) when MAX9814 is an amplifier, not a sensor
- **Repetitive content**: Introduction and Conclusion overlap substantially
- **Vague technical language**: "high precision" (line 185), "excellent durability" (line 330), "stable" (line 609) without quantification
- **Missing GPS evaluation**: GPS module mentioned in title, abstract, and design but never evaluated in results

---

## MINOR CONCERNS

### 10. **Future Work Section Inappropriately Extensive**

Section IV.B (lines 973-1047) on "Future Scope" is **excessively long** (2 pages) and reads like a research proposal rather than a discussion of future extensions. Much of this content (AI/ML integration, additional sensors, cloud platforms, energy harvesting) is speculative and dilutes the focus on what was actually accomplished.

### 11. **Missing Practical Considerations**

- **Washability**: How is the vest cleaned? Are electronics removable?
- **Durability**: Long-term wear testing results not provided
- **User acceptance**: No survey of veterinarians or dog owners on perceived utility
- **Data security**: No discussion of privacy implications for location and health data
- **Regulatory status**: Medical device considerations not addressed

---

## SPECIFIC TECHNICAL QUESTIONS

1. **Line 71, 124**: "MAX9814 sensor" - This is a microphone amplifier, not a sensor. Please correct throughout.

2. **Line 164**: "The stretch sensor is a resistive, conductive rubber cord" - What is the baseline resistance? Resistance change per unit strain? Hysteresis characteristics?

3. **Lines 204-205**: "digital signal processing routines including bandpass filtering" - What filter type (Butterworth, Chebyshev, FIR)? What order? Cutoff frequencies?

4. **Line 441**: "based on a fruit stretch sensor" - Should this be "Adafruit stretch sensor"? Typographical error?

5. **Line 609**: "signal to noise ratio (SNR) was high" - Quantify with dB values.

6. **Lines 750-751**: "multi-threaded operation allowed one core to handle sampling and the other to manage filtering" - What was the latency? Provide timing analysis.

7. **Section III.A**: What is the total weight of the system? Critical specification missing.

8. **Section IV**: Where are the GPS tracking results? The title emphasizes location monitoring but it's never evaluated.

---

## RECOMMENDATIONS FOR REVISION

### Essential Changes (Must be addressed):

1. **Conduct proper validation study**: Test on ≥20 dogs of varied breeds with simultaneous gold standard measurements. Provide complete statistical analysis including Bland-Altman plots, ICC, sensitivity/specificity.

2. **Provide complete methodological details**: Include filter specifications, algorithm pseudocode, sampling rates, ADC resolution, and all parameters necessary for reproduction.

3. **Add comparative analysis**: Benchmark against existing commercial systems (PetPace) or published research prototypes with similar functionality.

4. **Include data tables**: Present all quantitative results in tables with means, SDs, ranges, and statistical comparisons.

5. **Address ethical approval**: State IACUC approval number and compliance with animal research guidelines.

6. **Quantify limitations**: Provide systematic characterization of failure modes (during panting, intense activity, etc.) with quantitative metrics.

### Strongly Recommended:

7. **Revise novelty claims**: Clearly distinguish between engineering integration (main contribution) and fundamental scientific advances (limited).

8. **Reduce Future Scope section**: Condense to <1 page, focusing on immediate next steps rather than speculative long-term vision.

9. **Add GPS validation**: Either evaluate GPS tracking with results or remove from title/claims.

10. **Include clinical relevance**: Consult with veterinary medicine experts to establish clinical significance thresholds and validate against veterinary diagnostic criteria.

11. **Improve figures**: Add error bars, statistical annotations, and multiple representative examples rather than single traces.

---

## VERDICT ON KEY REVIEW CRITERIA

| Criterion | Assessment |
|-----------|------------|
| **Scientific Novelty** | **Low** - Primarily integration of existing technologies |
| **Experimental Rigor** | **Insufficient** - No quantitative validation or statistical analysis |
| **Reproducibility** | **Poor** - Missing critical methodological details |
| **Clinical Relevance** | **Unclear** - No veterinary validation or clinical utility assessment |
| **Writing Quality** | **Acceptable** - Generally clear but with repetition and overclaiming |
| **Publishability (current form)** | **Not acceptable** - Major revisions required |

---

## CONCLUSION

This manuscript describes a practical engineering implementation of a multi-sensor canine monitoring vest, but **falls short of the standards required for publication in a biomedical signal processing journal**. The primary deficiencies are: (1) absence of rigorous experimental validation with quantitative metrics, (2) limited scientific novelty beyond system integration, (3) insufficient methodological detail for reproducibility, and (4) lack of clinical validation.

The work represents **an incremental engineering project** rather than a significant scientific contribution. While the practical utility of such a device is evident, the current manuscript does not demonstrate that this particular implementation offers validated advantages over existing commercial solutions, nor does it advance the fundamental understanding of canine physiological monitoring.

**I recommend MAJOR REVISION** with emphasis on comprehensive validation experiments, statistical analysis, and honest assessment of the incremental nature of the contribution. If the authors can provide rigorous validation data demonstrating clinical utility superior to existing devices, the manuscript may become suitable for publication, possibly in a more engineering-focused venue.

---

**Reviewer Recommendation**: Request major revisions with re-review after substantial additional experimental work.

**Estimated revision timeline**: 6-12 months (requires new validation experiments)

**Alternate journal suggestions if revisions insufficient**: 
- IEEE Sensors Journal (more engineering-focused)
- Journal of Veterinary Behavior (if clinical validation added)
- Sensors (MDPI) - less stringent validation requirements

---
