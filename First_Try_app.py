import streamlit as st

# Prostate Cancer Treatment Algorithm App
st.title("Prostate Cancer Treatment Decision Pathway")
st.markdown("""
This interactive app is based on the 2025 EAU (Uroweb) Guidelines (limited update) and the German S3-Leitlinie Prostatakarzinom (Version 8.1, August 2025). 
It provides a **guided decision pathway** from diagnosis/staging to therapy recommendations, including localized, advanced, metastatic, and biochemical recurrence (BCR).
**New: Standard drug dosages** added to key therapies (aligned with EAU/German approvals and trial data).
Expanded details on genetic testing, PSMA PET/CT, BCR risk stratification, and PSA level.
Therapies include notes on 'Zulassung' (approval/reimbursement status) in EU/Germany.
This is a simplified educational tool—always consult full guidelines and a multidisciplinary team for clinical decisions.
""")

# Global Sections
st.subheader("Genetic/Biomarker Testing Recommendations (EAU 2025)")
st.markdown("""
- **Germline Testing**: Offer to all metastatic patients and those with relevant family history (strong).
- **Somatic Testing**: Offer to metastatic/CRPC patients for HRR genes (BRCA1/2 etc.) and MMR/MSI (strong).
- Implications: HRR+ → PARP inhibitors (e.g., olaparib 300 mg BID); MSI-high → pembrolizumab (rare).
""")

if st.checkbox("Show genetic testing result (for therapy personalization)"):
    genetic_result = st.selectbox(
        "Known Biomarker Status:",
        ["Not tested / Unknown", "No actionable mutation", "HRR mutated (e.g., BRCA1/2, ATM)", "MMR deficient / MSI-high"],
        key="genetic"
    )
else:
    genetic_result = "Not tested / Unknown"

st.subheader("Imaging Recommendations - Focus on PSMA PET/CT (EAU 2025)")
st.markdown("""
- **Tracers**: ⁶⁸Ga-PSMA-11 or ¹⁸F-PSMA-1007 (approved EU/Germany).
- **BCR**: Strongly recommend early (PSA ≥0.2–0.5 ng/mL post-RP).
- Detection rates: ~50% at PSA <0.5, ~80% at 0.5–1.0, >95% at >2.0 ng/mL.
""")

if st.checkbox("Show PSMA PET/CT result (for therapy personalization)"):
    psma_status = st.selectbox(
        "PSMA PET/CT Findings:",
        ["Not performed / Unknown", "No detectable disease", "Local recurrence only", "Oligorecurrence (1–5 lesions)", "Polymetastatic (>5 lesions or visceral)", "PSMA-positive (eligible for radioligand therapy)", "PSMA-negative/low (not eligible for Lu-177)"],
        key="psma"
    )
else:
    psma_status = "Not performed / Unknown"

# Guided Pathway Start
st.header("Step 1: Select Current Disease Stage")
disease_extent = st.selectbox(
    "Disease Extent/Stage:",
    ["Initial Diagnosis / Localized Disease", "Locally Advanced", "Metastatic (M1)", "Biochemical Recurrence (BCR) after curative local therapy"]
)

recommendations = []  # Collect for final pathway summary

if disease_extent == "Initial Diagnosis / Localized Disease":
    st.write("For detailed risk stratification and therapies (AS, RP, RT ± ADT), refer to EAU risk groups.")
    recommendations.append("Curative intent: Active Surveillance (low-risk) or RP/RT ± short ADT (higher risk).")

elif disease_extent == "Locally Advanced":
    recommendations.append("Multimodal: EBRT (76-78 Gy or hypofractionated) + long-term ADT (2-3 years).")

elif disease_extent == "Metastatic (M1)":
    androgen_status = st.selectbox("Androgen Status:", ["Hormone-Sensitive (mHSPC)", "Castration-Resistant (mCRPC)"])
    if androgen_status == "Hormone-Sensitive (mHSPC)":
        recommendations.append("""
        - Backbone: ADT (GnRH agonist e.g., leuprolide 22.5 mg/3 mo SC or antagonist e.g., degarelix 240 mg loading/80 mg monthly).
        - Intensification: + ARPI (apalutamide 240 mg PO daily; or enzalutamide 160 mg PO daily; or darolutamide 600 mg PO BID; or abiraterone 1000 mg PO daily + prednisone 5 mg daily) ± docetaxel 75 mg/m² IV q3w x6 cycles.
        """)
    else:
        recommendations.append("""
        - Continue ADT + sequence: ARPI switch (doses as above), cabazitaxel 20-25 mg/m² IV q3w, or ¹⁷⁷Lu-PSMA-617 7.4 GBq IV q6w x4-6 if PSMA+.
        """)

elif disease_extent == "Biochemical Recurrence (BCR) after curative local therapy":
    prior_therapy = st.selectbox(
        "Prior Curative Treatment:",
        ["Radical Prostatectomy (RP)", "Primary Radiotherapy (EBRT or Brachytherapy)"]
    )
    
    current_psa = st.number_input(
        "Current PSA (ng/mL)",
        min_value=0.0,
        max_value=1000.0,
        value=0.5,
        step=0.01,
        format="%.2f"
    )
    
    if psma_status == "Not performed / Unknown" and current_psa >= 0.2:
        st.info("Strongly recommend PSMA PET/CT now for localization and guidance.")
    
    # BCR Risk Stratification
    st.subheader("EAU BCR Risk Stratification")
    bcr_risk = None
    if prior_therapy == "Radical Prostatectomy (RP)":
        psadt = st.selectbox("PSA Doubling Time (PSADT):", ["> 12 months", "≤ 12 months"])
        isup = st.selectbox("Pathological ISUP Grade Group:", ["1–3", "4–5"])
        if psadt == "> 12 months" and isup == "1–3":
            bcr_risk = "Low-Risk BCR"
        else:
            bcr_risk = "High-Risk BCR"
    else:
        interval = st.selectbox("Interval to BCR (months from RT end):", ["> 18", "≤ 18"])
        isup = st.selectbox("Initial Biopsy ISUP Grade Group:", ["1–3", "4–5"])
        if interval == "> 18" and isup == "1–3":
            bcr_risk = "Low-Risk BCR"
        else:
            bcr_risk = "High-Risk BCR"
    
    if bcr_risk:
        recommendations.append(f"**BCR Risk: {bcr_risk}**")
    
    # Pathway Recommendations with Doses
    st.subheader("Recommended Therapy Pathway")
    
    if "No detectable" in psma_status or "Local" in psma_status:
        if current_psa <= 0.5:
            recommendations.append("Optimal timing (PSA ≤0.5): Highest cure chance with salvage therapy.")
        elif current_psa > 1.0:
            recommendations.append(f"PSA {current_psa} >1.0: Consider adding systemic therapy due to risk of occult disease.")
        
        if prior_therapy == "Radical Prostatectomy (RP)":
            recommendations.append("""
            - Early salvage RT (66-72 Gy to prostate bed ± pelvic nodes; hypofractionated options e.g., 62.5 Gy/25 fx).
            - If High-Risk BCR: + ADT (GnRH agonist/antagonist, 6 months; e.g., leuprolide 22.5 mg/3 mo).
            """)
        else:
            recommendations.append("Monitoring preferred (esp. Low-Risk); salvage local (RP/HIFU) selected cases only.")
    
    elif "Oligorecurrence" in psma_status:
        recommendations.append("""
        - Metastasis-directed therapy (MDT): SBRT (e.g., 30-50 Gy in 3-5 fx per lesion).
        - If High-Risk: + systemic ADT ± ARPI (apalutamide 240 mg daily; enzalutamide 160 mg daily; darolutamide 600 mg BID).
        """)
    
    elif "Polymetastatic" in psma_status:
        recommendations.append("""
        - Treat as mHSPC: ADT + ARPI (doses as above) ± docetaxel 75 mg/m² q3w x6.
        """)
    
    if bcr_risk == "High-Risk BCR" and "No detectable" in psma_status and current_psa > 0.5:
        recommendations.append("""
        - Consider ARPI for high-risk nmCRPC (apalutamide 240 mg daily; darolutamide 600 mg BID; enzalutamide 160 mg daily) if PSADT ≤10 months.
        - Zulassung: Approved EMA/Germany for nmCRPC.
        """)

# Final Personalized Decision Pathway Summary
st.header("Your Personalized Decision Pathway Summary")
if recommendations:
    for rec in recommendations:
        st.markdown(f"- {rec}")
    st.success("Discuss with MDT; dosages are standard—adjust per patient factors (e.g., renal/hepatic).")
else:
    st.info("Select stage and inputs to generate pathway.")

st.markdown("---")
st.info("""
References: EAU Prostate Cancer Guidelines 2025; German S3-Leitlinie Version 8.1 (Aug 2025).
""")
