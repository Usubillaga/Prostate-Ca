import streamlit as st

# Prostate Cancer Treatment Algorithm App
st.title("Prostate Cancer Treatment Algorithm")
st.markdown("""
This interactive app is based on the 2025 EAU (Uroweb) Guidelines and the German S3-Leitlinie Prostatakarzinom (Version 8.1, 2025). 
It guides from diagnosis to therapy, branching by localized vs. metastatic disease, and for metastatic, by androgen-sensitive (hormone-sensitive) vs. resistant (castration-resistant) status.
Therapies include notes on 'Zulassung' (approval status) where applicable, based on EMA/EU and German contexts. 
This is a simplified representation for educational purposes—consult full guidelines and a physician for clinical use.
""")

# Genetic Testing Section
st.subheader("Genetic Testing Recommendations")
st.write("""
- **Germline Testing (EAU/German S3)**: Recommended for all patients with metastatic prostate cancer (mPCa), high-risk localized (ISUP ≥3, T3/T4, N1), early-onset (<60 years), family history of PCa or related cancers (breast, ovarian, pancreatic), Ashkenazi Jewish or African ancestry.
- **Genes to Test**: Focus on HRR genes including BRCA1/2, ATM, CHEK2, HOXB13, PALB2; also MMR genes (MLH1, MSH2, MSH6, PMS2) for Lynch syndrome.
- **When to Perform**: At diagnosis for metastatic/high-risk; genetic counseling required prior to testing. Use NGS on blood/saliva.
- **Somatic Testing**: For metastatic (tissue/ctDNA) to identify HRR alterations; prompts germline if positive.
- **Impact**: Positive HRR (esp. BRCA2) indicates aggressive disease; eligibility for PARP inhibitors (e.g., olaparib, niraparib) in mCRPC/mHSPC; platinum chemo; influences active surveillance (cautious in BRCA+); family screening.
- **Prevalence**: 11-16% in metastatic; BRCA2 increases risk of high-grade/metastatic PCa.
""")

genetic_status = st.selectbox(
    "Genetic Testing Results:",
    ["Not Performed/Unknown", "Negative/No Pathogenic Variants", "BRCA1/2 Positive", "Other HRR Positive (e.g., ATM, CHEK2)", "MMR Deficient (MSI-H/dMMR)"]
)

# Step 1: Disease Extent
disease_extent = st.selectbox(
    "Select Disease Extent:",
    ["Localized (cT1-2, N0, M0)", "Locally Advanced (cT3-4 or N1, M0)", "Metastatic (M1)"]
)

if disease_extent == "Localized (cT1-2, N0, M0)":
    # Risk Stratification for Localized
    risk_group = st.selectbox(
        "Select Risk Group (based on PSA, ISUP Grade, T-stage):",
        ["Very Low/Low Risk (PSA <10, ISUP 1, cT1-2a)", 
         "Intermediate Risk - Favorable (PSA 10-20 or ISUP 2-3 or cT2b, with ≤1 intermediate factor)",
         "Intermediate Risk - Unfavorable (≥2 intermediate factors, ISUP 2-3, PSA 10-20)",
         "High Risk (PSA >20 or ISUP ≥4 or cT2c)"]
    )
    
    st.subheader("Recommended Pathways and Therapies")
    if "Very Low/Low Risk" in risk_group:
        st.write("""
        - **Primary Recommendation**: Active Surveillance (AS) – PSA every 6 months, mpMRI at 12-18 months, re-biopsy if progression indicators (e.g., PI-RADS ≥3, PSA doubling <3 years).
        - If AS declined: Radical Prostatectomy (RP) or External Beam Radiotherapy (EBRT, 74-80 Gy) or Brachytherapy (LDR monotherapy).
        - No ADT. No lymphadenectomy.
        - **Genetic Impact**: If BRCA2+, cautious AS with intensified monitoring; may favor curative therapy.
        - **Zulassung Notes**: All standard therapies approved in EU/Germany.
        """)
    elif "Favorable" in risk_group:
        st.write("""
        - **Options**: Active Surveillance (if no unfavorable features like cribriform pattern) or Curative Therapy.
        - Curative: RP (with possible lymphadenectomy if risk >5%) or EBRT (hypofractionated, e.g., 60 Gy/20 fx) + short-term ADT (4-6 months, LHRH agonists/antagonists).
        - Focal therapies (e.g., HIFU, Cryotherapy) in select cases, but not standard.
        - **Genetic Impact**: BRCA+ may exclude AS; intensify with ADT.
        - **Zulassung Notes**: ADT agents (e.g., GnRH analogs) approved; focal therapies may vary by center approval.
        """)
    elif "Unfavorable" in risk_group:
        st.write("""
        - **Curative Therapy Recommended**: RP with extended pelvic lymphadenectomy (ePLND) or EBRT + short-term ADT (4-6 months).
        - Brachytherapy boost possible.
        - **Genetic Impact**: HRR+ informs prognosis; consider intensification.
        - **Zulassung Notes**: Approved standards; ADT combinations standard.
        """)
    elif "High Risk" in risk_group:
        st.write("""
        - **Multimodal Therapy**: EBRT + long-term ADT (24-36 months) or RP + ePLND (adjuvant RT if pT3/R1).
        - Brachytherapy boost for select.
        - **Genetic Impact**: Recommend germline testing; if HRR+, worse prognosis, consider PARPi trials or intensification.
        - **Zulassung Notes**: ADT approved; abiraterone may be considered in some high-risk but not specifically approved for non-metastatic in Germany.
        """)

elif disease_extent == "Locally Advanced (cT3-4 or N1, M0)":
    st.subheader("Recommended Pathways and Therapies")
    st.write("""
    - **Risk Stratification**: High-risk features (ISUP 4-5, PSA >20, cT3-4).
    - **Diagnosis/Staging**: PSMA-PET/CT recommended over conventional imaging. Recommend germline testing if family history or high-risk.
    - **Therapies**: Multimodal – EBRT (IMRT/IGRT, dose-escalated) + long-term ADT (24-36 months, starting pre-RT).
    - If operable: RP + ePLND, possibly adjuvant RT.
    - For N1: Prostate + pelvic RT + ADT (3 years) + abiraterone (2 years) if ≥2 risk factors.
    - Brachytherapy boost (HDR/LDR) for cT3a.
    - **Genetic Impact**: If HRR+, consider PARPi in trials; informs prognosis.
    - **Zulassung Notes**: Abiraterone not approved in Germany for this indication despite evidence (off-label possible); GnRH analogs approved.
    """)

elif disease_extent == "Metastatic (M1)":
    # Androgen Sensitivity
    androgen_status = st.selectbox(
        "Select Androgen Status:",
        ["Hormone-Sensitive (mHSPC)", "Castration-Resistant (mCRPC)"]
    )
    
    if androgen_status == "Hormone-Sensitive (mHSPC)":
        volume = st.selectbox(
            "Select Disease Volume:",
            ["Low-Volume (≤3 bone mets, no visceral)", "High-Volume (≥4 bone mets or visceral)"]
        )
        
        st.subheader("Recommended Pathways and Therapies")
        st.write("""
        - **Diagnosis/Staging**: PSMA-PET/CT for confirmation; strongly recommend germline testing for all mHSPC (BRCA1/2, HRR genes); somatic if tissue available.
        - **Backbone**: Androgen Deprivation Therapy (ADT: GnRH agonist/antagonist or orchiectomy).
        - **Add-Ons**: Within 3 months, add ARPI (apalutamide 240mg/d, enzalutamide 160mg/d, darolutamide 600mg BID) or abiraterone (1000mg/d + prednisone 5mg).
        - If chemo-eligible: + Docetaxel (75mg/m² q3w, 6 cycles).
        - Triple Therapy (ADT + Docetaxel + ARPI, e.g., darolutamide) for high-volume.
        - Local Therapy: Prostate RT or SBRT for oligometastatic/low-volume.
        - Bone Agents: Denosumab or zoledronic acid for SRE prevention.
        """)
        if "Low-Volume" in volume:
            st.write("- Emphasize local RT to metastases for better OS.")
        else:
            st.write("- Triple therapy preferred.")
        
        genetic_impact = ""
        if "BRCA" in genetic_status or "HRR" in genetic_status:
            genetic_impact = "- **Genetic Impact**: HRR+ (e.g., BRCA): Consider PARP inhibitor combinations (e.g., abiraterone + olaparib/niraparib); improves rPFS/OS; platinum chemo if progression."
        elif "MMR" in genetic_status:
            genetic_impact = "- **Genetic Impact**: MMR deficient: Rare; consider immunotherapy (pembrolizumab) if MSI-H."
        
        st.write(genetic_impact)
        
        st.write("""
        - **Zulassung Notes**: 
          - Apalutamide (TITAN): Approved EMA for mHSPC + ADT.
          - Enzalutamide (ARCHES): Approved.
          - Darolutamide (ARANOTE/ARASENS): Approved, including triple.
          - Abiraterone (LATITUDE): Approved EMA but not in Germany for this indication (off-label).
          - Docetaxel: Approved in combination.
          - PARP inhibitors (e.g., olaparib for BRCA+): Approved for HRR mutations in mHSPC/mCRPC.
        """)
    
    else:  # mCRPC
        prior_therapy = st.multiselect(
            "Select Prior Therapies in mHSPC Phase:",
            ["None/ADT only", "ARPI (e.g., enzalutamide)", "Docetaxel", "Abiraterone"]
        )
        
        st.subheader("Recommended Pathways and Therapies")
        st.write("""
        - **Diagnosis**: Confirm CRPC (castrate T <50 ng/dl, PSA/radiologic progression); PSMA-PET/CT for imaging; strongly recommend germline/somatic testing for HRR/MMR.
        - **Therapies**: Continue ADT; sequence based on prior.
        - Asymptomatic: ARPI switch (e.g., if prior abiraterone → enzalutamide) or docetaxel.
        - Symptomatic: Docetaxel or radium-223 (for bone-predominant).
        - Post-docetaxel: Cabazitaxel, ARPI if not prior, PARP (if BRCA+).
        - PSMA-lutetium-177 for PSMA-positive after ARPI/docetaxel.
        - Bone agents for SRE.
        - **General Sequence**: ADT + ARPI/docetaxel → switch ARPI or chemo → PARP/Ra-223/Lu-PSMA.
        """)
        
        if "Docetaxel" in prior_therapy:
            st.write("- Post-docetaxel options: Cabazitaxel (25mg/m² q3w), olaparib (BRCA+), Lu-PSMA.")
        
        genetic_impact = ""
        if "BRCA" in genetic_status or "HRR" in genetic_status:
            genetic_impact = """
            - **Genetic Impact**: HRR+ (esp. BRCA1/2): Prioritize PARP inhibitors (olaparib 300mg BID, rucaparib, niraparib, talazoparib) post-ARPI; combinations (e.g., enzalutamide + talazoparib); platinum (carboplatin) if PARPi failure; improves OS/rPFS (e.g., PROfound trial).
            """
        elif "MMR" in genetic_status:
            genetic_impact = """
            - **Genetic Impact**: MMR deficient/MSI-H: Pembrolizumab (immunotherapy) approved if high TMB/MSI-H (rare in PCa).
            """
        
        st.write(genetic_impact)
        
        st.write("""
        - **Zulassung Notes**:
          - Enzalutamide (PREVAIL/AFFIRM): Approved post-ADT or post-chemo.
          - Abiraterone (COU-AA-302/301): Approved, but sequencing considerations.
          - Darolutamide (ARAMIS for nmCRPC, but extends to m): Approved.
          - Docetaxel/Cabazitaxel: Approved.
          - Radium-223 (ALSYMPCA): Approved for bone mets, no visceral.
          - Lu-PSMA-617 (VISION): Approved EMA for post-ARPI/chemo.
          - PARP (olaparib PROfound, niraparib, talazoparib): Approved for HRR mutations (BRCA1/2 etc.).
          - Note: Some combinations off-label in Germany if not EMA-aligned.
        """)

st.markdown("---")
st.info("References: EAU 2025 Guidelines[](https://uroweb.org/guidelines/prostate-cancer); German S3-Leitlinie Version 8.1 (2025). Always verify latest updates.")
