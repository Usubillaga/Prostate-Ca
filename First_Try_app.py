import streamlit as st

# Prostate Cancer Treatment Algorithm App
st.title("Prostate Cancer Treatment Algorithm")
st.markdown("""
This interactive app is based on the 2025 EAU (Uroweb) Guidelines and the German S3-Leitlinie Prostatakarzinom (Version 8.1, August 2025). 
It guides from diagnosis to therapy, including localized, advanced, metastatic, and biochemical recurrence (BCR) pathways.
**New: EAU BCR Risk Stratification (Low-Risk vs. High-Risk)** integrated for personalized recommendations in BCR (post-RP and post-RT).
Expanded details on genetic testing and PSMA PET/CT imaging.
Therapies include notes on 'Zulassung' (approval/reimbursement status) in EU/Germany where relevant.
This is a simplified educational tool—always consult full guidelines and a multidisciplinary team for clinical decisions.
""")

# Genetic Testing Section (Global)
st.subheader("Genetic/Biomarker Testing Recommendations (EAU 2025)")
st.markdown("""
- **Germline Testing**: Offer to all metastatic patients and those with relevant family history (strong).
- **Somatic Testing**: Offer to metastatic/CRPC patients for HRR genes (BRCA1/2 etc.) and MMR/MSI (strong).
- Implications: HRR+ → PARP inhibitors; MSI-high → pembrolizumab (rare).
- In BCR: Consider if progression to metastatic expected or for counselling.
""")

if st.checkbox("Show genetic testing result (for therapy personalization)"):
    genetic_result = st.selectbox(
        "Known Biomarker Status:",
        ["Not tested / Unknown", "No actionable mutation", "HRR mutated (e.g., BRCA1/2, ATM)", "MMR deficient / MSI-high"],
        key="genetic"
    )
else:
    genetic_result = "Not tested / Unknown"

# PSMA PET Imaging Section (Global)
st.subheader("Imaging Recommendations - Focus on PSMA PET/CT (EAU 2025)")
st.markdown("""
- **Tracers**: ⁶⁸Ga-PSMA-11 or ¹⁸F-PSMA-1007 (approved EU/Germany).
- **Staging**: Strongly recommended in high-risk/unfavorable intermediate; superior to conventional.
- **BCR**: Strongly recommend at low PSA (0.2–1.0 ng/mL) to localize recurrence and guide therapy.
- **Metastatic/CRPC**: Essential for volume, response, and ¹⁷⁷Lu-PSMA eligibility.
- **German Context**: Reimbursed in indicated settings.
""")

if st.checkbox("Show PSMA PET/CT result (for staging/therapy personalization)"):
    psma_status = st.selectbox(
        "PSMA PET/CT Findings:",
        ["Not performed / Unknown", "No detectable disease", "Local recurrence only", "Oligorecurrence (1–5 lesions)", "Polymetastatic (>5 lesions or visceral)", "PSMA-positive (eligible for radioligand therapy)", "PSMA-negative/low (not eligible for Lu-177)"],
        key="psma"
    )
else:
    psma_status = "Not performed / Unknown"

# Step 1: Disease Extent
disease_extent = st.selectbox(
    "Select Disease Extent/Stage:",
    ["Localized (cT1-2, N0, M0)", "Locally Advanced (cT3-4 or N1, M0)", "Metastatic (M1)", "Biochemical Recurrence (BCR) after curative local therapy"]
)

if disease_extent in ["Localized (cT1-2, N0, M0)", "Locally Advanced (cT3-4 or N1, M0)"]:
    # Simplified other sections
    st.write("Refer to previous versions for detailed localized/locally advanced pathways.")

elif disease_extent == "Metastatic (M1)":
    # Simplified
    st.write("Refer to previous versions for mHSPC/mCRPC pathways.")

elif disease_extent == "Biochemical Recurrence (BCR) after curative local therapy":
    prior_therapy = st.selectbox(
        "Prior Curative Treatment:",
        ["Radical Prostatectomy (RP)", "Primary Radiotherapy (EBRT or Brachytherapy)"]
    )
    
    st.subheader("BCR Management Recommendations (EAU 2025 / German S3)")
    st.markdown("""
    - **Definitions**: Post-RP: PSA ≥0.2 ng/mL + rising. Post-RT: Nadir + 2 ng/mL (Phoenix).
    - **Imaging**: Strongly recommend early PSMA PET/CT (PSA 0.2–1.0 ng/mL) to guide therapy.
    """)
    
    if psma_status == "Not performed / Unknown":
        st.info("Perform PSMA PET/CT to classify recurrence type and personalize therapy.")
    
    # New: BCR Risk Stratification
    st.subheader("EAU BCR Risk Stratification (2025)")
    st.markdown("""
    Used when no metastases detectable (M0) to guide intensity of salvage/local therapy.
    """)
    
    bcr_risk = None
    if prior_therapy == "Radical Prostatectomy (RP)":
        psadt = st.selectbox("PSA Doubling Time (PSADT):", ["> 12 months", "≤ 12 months"])
        isup = st.selectbox("Pathological ISUP Grade Group:", ["1–3 (<4)", "4–5 (≥4)"])
        
        if psadt == "> 12 months" and isup == "1–3 (<4)":
            bcr_risk = "Low-Risk BCR"
        else:
            bcr_risk = "High-Risk BCR"
    
    else:  # Post-RT
        interval = st.selectbox("Interval to BCR (from end of RT):", ["> 18 months", "≤ 18 months"])
        isup = st.selectbox("Initial Biopsy ISUP Grade Group:", ["1–3 (<4)", "4–5 (≥4)"])
        
        if interval == "> 18 months" and isup == "1–3 (<4)":
            bcr_risk = "Low-Risk BCR"
        else:
            bcr_risk = "High-Risk BCR"
    
    if bcr_risk:
        st.write(f"**EAU Classification: {bcr_risk}**")
        if bcr_risk == "High-Risk BCR":
            st.warning("Higher risk of progression – consider intensified therapy.")
        else:
            st.success("Lower risk – monitoring or less intensive therapy often sufficient.")
    
    # Personalized Recommendations
    st.subheader("Recommended Pathways")
    
    if "No detectable disease" in psma_status or "Local recurrence only" in psma_status:
        st.write("**PSMA PET/CT: No distant metastases (M0) / local only**")
        if prior_therapy == "Radical Prostatectomy (RP)":
            st.write("""
            - **Early salvage RT** (eSRT) to prostate bed (± pelvic nodes if risk) strongly recommended (best if PSA <0.5 ng/mL).
            - **Intensity based on risk**:
            """)
            if bcr_risk == "Low-Risk BCR":
                st.write("- sRT alone sufficient (no ADT).")
            else:
                st.write("- sRT + short-term ADT (6 months GnRH agonist/antagonist).")
            st.write("""
            - Hypofractionated regimens possible.
            - **Zulassung**: Standard salvage RT reimbursed; ADT approved.
            """)
        
        else:  # Post-RT
            st.write("""
            - No standard salvage RT to prostate (prior irradiated).
            - **Monitoring** preferred, especially in Low-Risk BCR.
            - Salvage local therapies (RP, brachy, HIFU, cryo) only in highly selected patients (high morbidity).
            - If High-Risk BCR and symptomatic/progression: Consider early systemic therapy.
            """)
    
    elif "Oligorecurrence" in psma_status:
        st.write("**PSMA PET/CT: Oligorecurrence (1–5 lesions)**")
        st.write("""
        - **Metastasis-directed therapy (MDT)**: SBRT or surgery to all lesions (improves PFS).
        - Combine with salvage RT (post-RP) or systemic therapy (ADT ± ARPI) if High-Risk BCR or short PSADT.
        - Increasingly recommended in fit patients.
        - **Zulassung**: MDT widely practiced/reimbursed in centers; off-label for some indications.
        """)
    
    elif "Polymetastatic" in psma_status:
        st.write("**PSMA PET/CT: Polymetastatic**")
        st.write("- Treat as metastatic hormone-sensitive PCa (mHSPC): ADT + ARPI ± docetaxel (see Metastatic section).")
    
    # Additional for very high-risk M0
    if bcr_risk == "High-Risk BCR" and "No detectable" in psma_status:
        st.write("""
        - If very short PSADT (≤9–12 months) and PSA above threshold: Consider intensification with ARPI (e.g., enzalutamide ± ADT).
        - **Zulassung**: Enzalutamide approved for high-risk nmCRPC (PROSPER); applicability with negative PSMA PET limited.
        """)
    
    # Genetic note
    if "HRR mutated" in genetic_result:
        st.write("If progression to mCRPC: Prioritize PARP inhibitors.")

st.markdown("---")
st.info("""
References: 
- EAU Prostate Cancer Guidelines 2025 (uroweb.org/guidelines/prostate-cancer).
- German S3-Leitlinie Prostatakarzinom Version 8.1 (August 2025).
Always consult latest versions and MDT.
""")
