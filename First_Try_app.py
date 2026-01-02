import streamlit as st
import streamlit.components.v1 as components

# --- 1. Page Configuration & Translations ---
st.set_page_config(page_title="Prostate Cancer Algorithm 2025", layout="wide")

translations = {
    "English": {
        "title": "Prostate Cancer Treatment Algorithm (EAU/S3 2025)",
        "description": "Interactive tool based on **EAU Guidelines 2025** and **German S3-Leitlinie (v8.1)**.",
        "sidebar_title": "Patient Configuration",
        "rec_title": "Therapy Recommendations",
        "dos_donts_title": "Clinical Dos & Don'ts",
        "approval_title": "Zulassung (Approval Status)",
        
        # Labels
        "genetic_label": "Genetic Testing Results",
        "extent_label": "Disease Extent",
        "psa_label": "PSA Level (ng/ml)",
        "isup_label": "ISUP Grade (Gleason)",
        "tstage_label": "Clinical T-Stage",
        "n_stage_label": "N-Stage (Regional Nodes)",
        "meta_state_label": "Metastatic State",
        "volume_label": "Disease Volume (CHAARTED)",
        
        # Select Options
        "isup_opts": ["ISUP 1 (Gleason 6)", "ISUP 2 (Gleason 3+4)", "ISUP 3 (Gleason 4+3)", "ISUP 4 (Gleason 8)", "ISUP 5 (Gleason 9-10)"],
        "t_opts": ["cT1", "cT2a", "cT2b", "cT2c", "cT3", "cT4"],
        "n_stages": ["cN0 (Nodes Negative)", "cN1 (Regional Nodes Positive)"],
        "m_states": ["mHSPC (Hormone Sensitive)", "mCRPC (Castration Resistant)"],
        "volumes": ["Low Volume", "High Volume (Visceral or ≥4 bone mets)"],
        
        # Content - Localized
        "rec_low": """
        **Active Surveillance (AS)**
        - **Protocol:** PSA every 6mo, DRE annually, mpMRI re-staging at 12-18mo.
        - **Biopsy:** Confirmatory biopsy if MRI changes or PSA density >0.15.
        """,
        "dos_low": """
        ✅ **Do:** Adhere strictly to re-biopsy schedules.
        ⛔ **Don't:** Offer AS to patients with **BRCA2** mutations without discussing increased risk of upgrading (consider RP).
        """,
        
        # Content - Locally Advanced
        "rec_n1": """
        **Multimodal Therapy (STAMPEDE Protocol)**
        1. **ADT:** LHRH agonist/antagonist for 3 years.
        2. **Radiotherapy:** EBRT to prostate + whole pelvis (dose escalated).
        3. **Abiraterone:** $1000$ mg OD + Prednisone $5$ mg OD for 2 years.
        """,
        "dos_n1": """
        ✅ **Do:** Ensure bone density protection (Calcium/Vit D) during long-term ADT.
        ⛔ **Don't:** Use Abiraterone as monotherapy (must be combined with ADT).
        """,
        "approval_n1": """
        🇪🇺 **EMA:** Abiraterone approved for high-risk mHSPC, but **not explicitly** for M0/cN1 locally advanced disease in the label.
        🇩🇪 **Germany:** Use in M0/cN1 is based on STAMPEDE data (Level 1 Evidence) but is technically **Off-Label**. Requires individual funding request (Kostenübernahme) with insurance.
        """,
        
        # Content - mHSPC
        "rec_mhspc_high": """
        **Triple Therapy (Standard of Care)**
        - **ADT:** Continuous.
        - **Docetaxel:** $75$ $\\text{mg/m}^2$ q3w for 6 cycles.
        - **ARPI:** - **Darolutamide:** $600$ mg BID.
            - *OR* **Abiraterone:** $1000$ mg OD + Prednisone.
        """,
        "dos_mhspc": """
        ✅ **Do:** Offer Triple Therapy to all fit patients with High Volume disease (ARASENS/PEACE-1).
        ⛔ **Don't:** Use Docetaxel in Low Volume disease unless symptomatic (no OS benefit).
        """,
        "approval_mhspc": """
        🇪🇺/🇩🇪 **Zulassung:**
        - **Darolutamide:** Approved in combination with Docetaxel+ADT.
        - **Abiraterone:** Approved for high-risk mHSPC (LATITUDE criteria).
        - **Enzalutamide/Apalutamide:** Approved for mHSPC (usually doublet with ADT).
        """,
        
        # Content - mCRPC
        "rec_mcrpc": """
        **Sequence Therapy (Switch Mechanism)**
        - **If post-ADT only:** Enzalutamide ($160$ mg OD) or Abiraterone.
        - **If post-ARPI:** Docetaxel ($75$ $\\text{mg/m}^2$).
        - **If BRCA1/2+:** Olaparib ($300$ mg BID) or Talazoparib ($0.5$ mg OD).
        - **If PSMA+:** Lutetium-177 ($7.4$ GBq q6w x 6).
        """,
        "dos_mcrpc": """
        ✅ **Do:** Perform PSMA-PET/CT before deciding on Lutetium therapy.
        ⛔ **Don't:** Sequence ARPI after ARPI (e.g., Enzalutamide directly after Abiraterone) due to cross-resistance (CARD trial).
        ⛔ **Don't:** Use Radium-223 in patients with visceral metastases or bulky lymph nodes.
        """,
         "approval_mcrpc": """
        🇪🇺/🇩🇪 **Zulassung:**
        - **Olaparib:** Approved for BRCA1/2+ mCRPC (monotherapy or combo with Abi).
        - **Lutetium-177:** Approved for PSMA+ mCRPC after ARPI and Chemo (VISION).
        """
    },
    
    "Deutsch": {
        "title": "Prostatakarzinom Behandlungsalgorithmus",
        "description": "Interaktives Tool basierend auf **EAU 2025** und **S3-Leitlinie (v8.1)**.",
        "sidebar_title": "Konfiguration",
        "rec_title": "Therapieempfehlungen & Dosierung",
        "dos_donts_title": "Caveats (Do's & Don'ts)",
        "approval_title": "Zulassung & Erstattung",
        
        "genetic_label": "Genetische Testung",
        "extent_label": "Krankheitsstadium",
        "psa_label": "PSA-Wert (ng/ml)",
        "isup_label": "ISUP Grad",
        "tstage_label": "T-Stadium",
        "n_stage_label": "N-Stadium",
        "meta_state_label": "Status",
        "volume_label": "Volumen (CHAARTED)",
        
        "isup_opts": ["ISUP 1 (Gleason 6)", "ISUP 2 (Gleason 3+4)", "ISUP 3 (Gleason 4+3)", "ISUP 4 (Gleason 8)", "ISUP 5 (Gleason 9-10)"],
        "t_opts": ["cT1", "cT2a", "cT2b", "cT2c", "cT3", "cT4"],
        "n_stages": ["cN0 (Negativ)", "cN1 (Positiv)"],
        "m_states": ["mHSPC (Hormonsensitiv)", "mCRPC (Kastrationsresistent)"],
        "volumes": ["Geringes Volumen", "Hohes Volumen (Viszeral od. ≥4 Knochenmet.)"],

        "rec_low": """
        **Aktive Überwachung (AS)**
        - **Protokoll:** PSA alle 6 Mon, DRE jährlich, mpMRT Re-Staging nach 12-18 Mon.
        - **Biopsie:** Bestätigungsbiopsie bei MRT-Progress oder PSA-Dichte >0,15.
        """,
        "dos_low": """
        ✅ **Ja:** Strikte Einhaltung der Re-Biopsie-Intervalle.
        ⛔ **Nein:** AS bei **BRCA2**-Mutation ohne Aufklärung über hohes Progressionsrisiko (RP erwägen).
        """,

        "rec_n1": """
        **Multimodale Therapie (STAMPEDE-Arm)**
        1. **ADT:** LHRH-Analogon für 3 Jahre.
        2. **Strahlentherapie:** IMRT Prostata + pelvine Lymphabflusswege (dosis-eskaliert).
        3. **Abirateron:** $1000$ mg OD + Prednison $5$ mg OD für 2 Jahre.
        """,
        "dos_n1": """
        ✅ **Ja:** Osteoprotektion (Calcium/Vit D) während der Langzeit-ADT sicherstellen.
        ⛔ **Nein:** Abirateron als Monotherapie ohne ADT geben.
        """,
        "approval_n1": """
        🇪🇺 **EMA:** Abirateron ist für High-Risk mHSPC zugelassen, aber **nicht explizit** für M0/cN1 im Labelstext.
        🇩🇪 **Deutschland:** Einsatz bei M0/cN1 basiert auf Level-1-Evidenz (STAMPEDE), ist aber formal **Off-Label**. Kostengutsprache bei der Kasse empfohlen.
        """,

        "rec_mhspc_high": """
        **Triple-Therapie (Standard of Care)**
        - **ADT:** Kontinuierlich.
        - **Docetaxel:** $75$ $\\text{mg/m}^2$ q3w für 6 Zyklen.
        - **ARPI:** - **Darolutamid:** $600$ mg BID.
            - *ODER* **Abirateron:** $1000$ mg OD + Prednison.
        """,
        "dos_mhspc": """
        ✅ **Ja:** Triple-Therapie allen fitten Patienten mit hohem Volumen anbieten (ARASENS/PEACE-1).
        ⛔ **Nein:** Docetaxel bei geringem Volumen (Low Volume) einsetzen (kein OS-Vorteil, nur Toxizität).
        """,
        "approval_mhspc": """
        🇪🇺/🇩🇪 **Zulassung:**
        - **Darolutamid:** Zugelassen in Kombination mit Docetaxel+ADT.
        - **Abirateron:** Zugelassen für High-Risk mHSPC (LATITUDE).
        - **Enzalutamide/Apalutamide:** Zugelassen für mHSPC (meist als Doublet mit ADT).
        """,

        "rec_mcrpc": """
        **Sequenztherapie (Wirkmechanismus wechseln)**
        - **Post-ADT:** Enzalutamid ($160$ mg OD) oder Abirateron.
        - **Post-ARPI:** Docetaxel ($75$ $\\text{mg/m}^2$).
        - **Bei BRCA1/2+:** Olaparib ($300$ mg BID) oder Talazoparib ($0,5$ mg OD).
        - **Bei PSMA+:** Lutetium-177 ($7,4$ GBq q6w x 6).
        """,
        "dos_mcrpc": """
        ✅ **Ja:** PSMA-PET/CT vor Indikation zur Lutetium-Therapie durchführen.
        ⛔ **Nein:** ARPI nach ARPI (z.B. Enza direkt nach Abi) wegen Kreuzresistenz (CARD-Studie).
        ⛔ **Nein:** Radium-223 bei viszeralen Metastasen oder großen Lymphknotenpaketen (>3cm).
        """,
        "approval_mcrpc": """
        🇪🇺/🇩🇪 **Zulassung:**
        - **Olaparib:** Zugelassen für BRCA1/2+ mCRPC (Mono oder Kombi mit Abi).
        - **Lutetium-177:** Zugelassen für PSMA+ mCRPC nach ARPI und Chemo (VISION).
        """
    }
}

t_opts_map = ["Localized (cT1-2)", "Locally Advanced (cT3-4 / cN1)", "Metastatic (M1)"]
gen_opts = ["Not Performed/Negative", "BRCA1/2 Positive", "HRR Other Positive", "MMR Deficient"]

# --- 2. Helper Functions ---
def calculate_risk_group(psa, isup_index, t_stage_index):
    isup = isup_index + 1
    # High: PSA >20 OR ISUP 4-5 OR cT2c/T3
    if psa > 20 or isup >= 4 or t_stage_index >= 3: 
        return "high"
    # Intermediate: PSA 10-20 OR ISUP 2-3 OR cT2b
    elif (psa >= 10) or (isup == 2 or isup == 3) or (t_stage_index == 2):
        return "int"
    # Low
    else:
        return "low"

def q(text):
    return f'"{text}"'

# --- 3. Sidebar Logic ---
with st.sidebar:
    st.header("⚙️ Configuration")
    lang_choice = st.selectbox("Language / Sprache", ["English", "Deutsch"])
    t = translations[lang_choice]
    st.markdown("---")
    
    # Global Inputs
    genetic_status = st.selectbox(t["genetic_label"], gen_opts)
    disease_extent = st.selectbox(t["extent_label"], t_opts_map)
    
    # Conditional Inputs
    calc_risk_key = None
    n_stage = None
    m_state = None
    volume = None
    
    if disease_extent == t_opts_map[0]: # Localized
        st.subheader("Calculator")
        in_psa = st.number_input(t["psa_label"], value=5.0, step=0.1)
        in_isup = st.selectbox(t["isup_label"], t["isup_opts"])
        in_tstage = st.selectbox(t["tstage_label"], t["t_opts"])
        
        isup_idx = t["isup_opts"].index(in_isup)
        t_idx = t["t_opts"].index(in_tstage)
        calc_risk_key = calculate_risk_group(in_psa, isup_idx, t_idx)
        
    elif disease_extent == t_opts_map[1]: # Locally Advanced
        st.subheader("Staging")
        n_stage = st.radio(t["n_stage_label"], t["n_stages"])
        
    elif disease_extent == t_opts_map[2]: # Metastatic
        st.subheader("Metastatic Details")
        m_state = st.radio(t["meta_state_label"], t["m_states"])
        if m_state == t["m_states"][0]:
            volume = st.radio(t["volume_label"], t["volumes"])

# --- 4. Main Content ---
st.title(t["title"])
st.markdown(t["description"])

# --- LOGIC BRANCHING ---

# A. LOCALIZED DISEASE
if disease_extent == t_opts_map[0]:
    col1, col2 = st.columns([1, 1])
    with col1:
        # Valid Wikimedia Commons URL for Gleason
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Prostate_cancer_Gleason_score.jpg/640px-Prostate_cancer_Gleason_score.jpg", 
                 caption="Gleason/ISUP Grading System", use_column_width=True)
    with col2:
        st.subheader(t["rec_title"])
        if calc_risk_key == "low":
            st.info(t["rec_low"])
            st.success(t["dos_low"])
        else:
            st.warning("**Intermediate/High Risk:** Radical Prostatectomy (RP) or EBRT+ADT.")
            st.error("⛔ **Don't:** Watchful Waiting in healthy patients with high-risk disease.")

# B. LOCALLY ADVANCED (N1 Focus)
elif disease_extent == t_opts_map[1]:
    st.header(f"{t_opts_map[1]}")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        # Valid Wikimedia Commons URL for Staging/Nodes
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/TNM_Staging_System_for_Prostate_Cancer.png/640px-TNM_Staging_System_for_Prostate_Cancer.png",
                 caption="TNM Staging: Regional Nodes (N1)", use_column_width=True)
    with col2:
        if n_stage == t["n_stages"][1]: # cN1
            st.info(t["rec_n1"])
        else:
            st.write("For cN0 cT3-4: Standard EBRT + ADT (2-3 years) or RP.")
            
    # Dos and Donts Section
    st.subheader(t["dos_donts_title"])
    if n_stage == t["n_stages"][1]:
        st.success(t["dos_n1"])
    
    # Zulassung Section
    st.markdown("---")
    st.subheader(f"⚖️ {t['approval_title']}")
    if n_stage == t["n_stages"][1]:
        st.warning(t["approval_n1"])
    else:
        st.success("Standard therapies (ADT, EBRT) are fully approved.")

# C. METASTATIC
elif disease_extent == t_opts_map[2]:
    
    # 1. mHSPC Logic
    if m_state == t["m_states"][0]:
        st.header("mHSPC Management")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            # Valid Wikimedia Commons URL for Bone Scan
            st.image("https://upload.wikimedia.org/wikipedia/commons/6/6d/Bone_scan_Prostate_Cancer.jpg", 
                     caption="Disease Volume Assessment", use_column_width=True)
        with col2:
            if volume == t["volumes"][1]: # High Volume
                st.error(t["rec_mhspc_high"]) # Triple Therapy
            else:
                st.info("**Low Volume:** ADT + ARPI (e.g., Enzalutamide $160$ mg). Add **Radiotherapy to Prostate**.")
        
        st.subheader(t["dos_donts_title"])
        st.success(t["dos_mhspc"])
        
        st.markdown("---")
        st.subheader(f"⚖️ {t['approval_title']}")
        st.write(t["approval_mhspc"])

    # 2. mCRPC Logic
    else:
        st.header("mCRPC Management")
        st.info(t["rec_mcrpc"])
        
        st.subheader(t["dos_donts_title"])
        st.success(t["dos_mcrpc"])
        
        if "BRCA" in genetic_status:
            st.error("🧬 **Genetic Note:** Patient is BRCA+. Prioritize PARP Inhibitors (Olaparib/Talazoparib) over Taxanes if fit.")
        
        st.markdown("---")
        st.subheader(f"⚖️ {t['approval_title']}")
        st.write(t["approval_mcrpc"])

# --- 5. Visual Flow (Mermaid) ---
st.markdown("---")
st.subheader("Visual Decision Pathway")

mermaid_code = "graph TD\n"
mermaid_code += f'Start["Diagnosis"] --> Gen{{"Genetics: {genetic_status}"}}\n'

if disease_extent == t_opts_map[0]:
    mermaid_code += f'Gen --> Risk{{"Risk Stratification"}}\n'
    if calc_risk_key == "low":
        mermaid_code += f'Risk -->|Low| AS["Active Surveillance"]\n'
    else:
        mermaid_code += f'Risk -->|Int/High| Curative["RP or EBRT+ADT"]\n'

elif disease_extent == t_opts_map[1]:
    mermaid_code += f'Gen --> NStage{{"N-Stage?"}}\n'
    if n_stage == t["n_stages"][1]:
        mermaid_code += f'NStage -->|cN1| Stampede["EBRT + ADT + Abiraterone"]\n'
    else:
        mermaid_code += f'NStage -->|cN0| Std["EBRT + ADT or RP"]\n'

elif disease_extent == t_opts_map[2]:
    if m_state == t["m_states"][0]:
        mermaid_code += f'Gen --> Vol{{"Volume?"}}\n'
        if volume == t["volumes"][1]:
            mermaid_code += f'Vol -->|High| Triple["Triple: ADT + Docetaxel + ARPI"]\n'
        else:
            mermaid_code += f'Vol -->|Low| Double["Doublet: ADT + ARPI + RT"]\n'
    else:
        mermaid_code += f'Gen --> Seq["Sequence Therapy"]\n'
        mermaid_code += f'Seq -->|BRCA+| PARP["PARP Inhibitor"]\n'
        mermaid_code += f'Seq -->|PSMA+| Lu["Lutetium-177"]\n'

components.html(
    f"""
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    <div class="mermaid">
        {mermaid_code}
    </div>
    """,
    height=400,
    scrolling=True
)
