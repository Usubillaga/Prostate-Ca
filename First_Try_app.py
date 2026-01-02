import streamlit as st
import streamlit.components.v1 as components

# --- 1. Page Configuration & Translations ---
st.set_page_config(page_title="Prostate Cancer Algorithm 2025", layout="wide")

translations = {
    "English": {
        "title": "Prostate Cancer Treatment Algorithm (EAU/S3 2025)",
        "description": """
        **Interactive Clinical Decision Support Tool** based on **EAU Guidelines 2025** and **German S3-Leitlinie (v8.1)**.
        
        This tool navigates from screening/diagnosis to advanced metastatic management, incorporating:
        * **Risk Stratification** for localized disease.
        * **N-Status** impact on locally advanced therapy (STAMPEDE).
        * **Volume & Hormone Status** for metastatic care (CHAARTED/LATITUDE).
        * **Precision Medicine** (PARP inhibitors, Immunotherapy) based on genetic profile.
        """,
        "sidebar_title": "Patient Configuration",
        "language_label": "Select Language",
        "genetic_label": "Genetic Testing Results",
        "extent_label": "Disease Extent",
        "calc_title": "Risk Stratification Calculator",
        "psa_label": "PSA Level (ng/ml)",
        "isup_label": "ISUP Grade Group (Gleason)",
        "tstage_label": "Clinical T-Stage",
        "n_stage_label": "N-Stage (Regional Lymph Nodes)",
        "meta_state_label": "Metastatic State",
        "volume_label": "Disease Volume (CHAARTED Criteria)",
        "prior_label": "Prior Therapies (mCRPC)",
        
        # Options
        "isup_opts": ["ISUP 1 (Gleason 6)", "ISUP 2 (Gleason 3+4)", "ISUP 3 (Gleason 4+3)", "ISUP 4 (Gleason 8)", "ISUP 5 (Gleason 9-10)"],
        "t_opts": ["cT1", "cT2a", "cT2b", "cT2c", "cT3", "cT4"],
        "n_stages": ["cN0 (Nodes Negative)", "cN1 (Regional Nodes Positive)"],
        "m_states": ["mHSPC (Hormone Sensitive)", "mCRPC (Castration Resistant)"],
        "volumes": ["Low Volume", "High Volume (Visceral or ≥4 bone mets)"],
        "prior_opts": ["ADT Only", "Docetaxel", "Abiraterone/Enzalutamide"],

        # Outputs
        "calc_result": "Calculated Risk Group:",
        "risk_options": {
            "low": "Low Risk",
            "int_fav": "Intermediate Risk (Favorable)",
            "int_unfav": "Intermediate Risk (Unfavorable)",
            "high": "High Risk"
        },
        "rec_title": "Therapy Recommendations",
        "flow_title": "Visual Decision Pathway",
        
        # Text Blocks
        "text_low": """
        **Primary Recommendation: Active Surveillance (AS)**
        - **Protocol:** PSA every 6 months, DRE annually, mpMRI re-staging at 12-18 months.
        - **Trigger for Intervention:** Grade progression (ISUP >1), significant PSA-DT (<3 yrs), or radiological progression (PI-RADS ≥3).
        - **Alternative:** Radical Prostatectomy (RP) or Radiotherapy (EBRT/LDR-Brachy) if patient prefers curative treatment.
        """,
        "text_int": """
        **Intermediate Risk Management**
        - **Favorable (ISUP 2, <50% positive cores):** Active Surveillance is an option (exclude cribriform pattern/intraductal ca).
        - **Unfavorable:** Curative Therapy is standard.
        - **RP:** Radical Prostatectomy + ePLND (extended lymph node dissection) if risk >5%.
        - **EBRT:** Hypofractionated IMRT/VMAT (60Gy/20fx) + Short-term ADT (4-6 months).
        """,
        "text_high": """
        **High Risk Localized (cT3a or PSA >20 or ISUP 4-5)**
        - **Multimodal Therapy is Mandatory.**
        - **EBRT:** Dose-escalated IMRT + Long-term ADT (2-3 years).
        - **RP:** Radical Prostatectomy + ePLND (consider adjuvant RT if pT3/R1).
        - **Genetics:** Germline testing strongly recommended (BRCA2 status impacts prognosis).
        """,
        "text_n1": """
        **Locally Advanced / Regional Nodal Disease (cN1)**
        - **Standard:** EBRT to prostate & pelvic nodes + Long-term ADT (3 years).
        - **Intensification (STAMPEDE/Abiraterone):** Add **Abiraterone** (1000mg + Prednisone) for 2 years.
        - **Alternative:** RP + ePLND + Adjuvant therapy.
        - **Note:** In Germany, Abiraterone in the M0 setting may be off-label; check reimbursement.
        """,
        "text_mhspc_high": """
        **mHSPC - High Volume (CHAARTED)**
        - **Standard of Care:** Triple Therapy (ADT + Docetaxel 6 cycles + ARPI).
        - **Approved ARPIs:** Darolutamide (ARASENS), Abiraterone (PEACE-1).
        - **Alternative:** ADT + ARPI (Enzalutamide/Apalutamide) if unfit for chemo.
        """,
        "text_mhspc_low": """
        **mHSPC - Low Volume / Oligometastatic**
        - **Systemic:** ADT + ARPI (Doublet therapy).
        - **Local:** **Radiotherapy to the primary tumor** (prostate) improves Overall Survival (STAMPEDE Arm H).
        - **SBRT:** Consider metastasis-directed therapy (MDT) for oligometastases (requires PSMA-PET).
        """,
        "text_mcrpc": """
        **mCRPC (Castration Resistant)**
        - **Definition:** Testosterone <50ng/dl with PSA or radiological progression.
        - **Sequencing:** Switch mechanism of action.
          - Post-ADT: Enzalutamide/Abiraterone or Docetaxel.
          - Post-ARPI: Docetaxel.
          - Post-Docetaxel: Cabazitaxel, 2nd ARPI (weak evidence), or Theragnostics.
        - **Precision Medicine:**
          - **BRCA1/2+:** PARP Inhibitor (Olaparib, Niraparib, Talazoparib) +/- ARPI.
          - **PSMA+:** Lutetium-177-PSMA-617 (Vision Trial).
        """
    },
    
    "Deutsch": {
        "title": "Prostatakarzinom Behandlungsalgorithmus",
        "description": "**Interaktives Tool** basierend auf **EAU 2025** und **Deutscher S3-Leitlinie (v8.1)**.",
        "sidebar_title": "Patientenkonfiguration",
        "language_label": "Sprache auswählen",
        "genetic_label": "Genetische Testergebnisse",
        "extent_label": "Ausbreitung der Erkrankung",
        "calc_title": "Risiko-Kalkulator",
        "psa_label": "PSA-Wert (ng/ml)",
        "isup_label": "ISUP Graduierung (Gleason)",
        "tstage_label": "Klinisches T-Stadium",
        "n_stage_label": "N-Stadium (Regionäre Lymphknoten)",
        "meta_state_label": "Metastasierungsstatus",
        "volume_label": "Krankheitsvolumen (CHAARTED)",
        "prior_label": "Vortherapien (mCRPC)",
        
        "isup_opts": ["ISUP 1 (Gleason 6)", "ISUP 2 (Gleason 3+4)", "ISUP 3 (Gleason 4+3)", "ISUP 4 (Gleason 8)", "ISUP 5 (Gleason 9-10)"],
        "t_opts": ["cT1", "cT2a", "cT2b", "cT2c", "cT3", "cT4"],
        "n_stages": ["cN0 (Knoten negativ)", "cN1 (Regionäre Knoten positiv)"],
        "m_states": ["mHSPC (Hormonsensitiv)", "mCRPC (Kastrationsresistent)"],
        "volumes": ["Geringes Volumen", "Hohes Volumen (Viszeral od. ≥4 Knochenmet.)"],
        "prior_opts": ["Nur ADT", "Docetaxel", "Abirateron/Enzalutamid"],

        "calc_result": "Berechnete Risikogruppe:",
        "risk_options": {
            "low": "Niedriges Risiko",
            "int_fav": "Intermediäres Risiko (Günstig)",
            "int_unfav": "Intermediäres Risiko (Ungünstig)",
            "high": "Hohes Risiko"
        },
        "rec_title": "Therapieempfehlungen",
        "flow_title": "Visueller Entscheidungspfad",
        
        "text_low": """
        **Primäre Empfehlung: Aktive Überwachung (AS)**
        - **Protokoll:** PSA alle 6 Monate, mpMRT nach 12-18 Monaten.
        - **Abbruchkriterien:** Upgrade (ISUP >1), schneller PSA-Anstieg oder PI-RADS Progress.
        - **Alternative:** RP oder EBRT, wenn kurative Therapie gewünscht.
        """,
        "text_int": """
        **Intermediäres Risiko**
        - **Günstig:** AS möglich (Ausschluss kribriformes Muster).
        - **Ungünstig:** Kurative Therapie ist Standard.
        - **RP:** Prostatektomie + ePLND.
        - **EBRT:** Hypofraktionierte IMRT + kurzzeitige ADT (4-6 Monate).
        """,
        "text_high": """
        **Hohes Risiko (cT3a oder PSA >20)**
        - **Multimodale Therapie erforderlich.**
        - **EBRT:** IMRT + Langzeit-ADT (2-3 Jahre).
        - **RP:** Prostatektomie + ePLND (ggf. adjuvante RT).
        - **Genetik:** Keimbahntestung dringend empfohlen.
        """,
        "text_n1": """
        **Lokal Fortgeschritten / cN1**
        - **Standard:** EBRT (Prostata + Becken) + Langzeit-ADT (3 Jahre).
        - **Intensivierung:** Addition von **Abirateron** (2 Jahre) empfohlen (STAMPEDE).
        - **S3-Hinweis:** Abirateron ist im M0-Setting in DE oft Off-Label; Kostenübernahme vorab klären.
        """,
        "text_mhspc_high": """
        **mHSPC - Hohes Volumen**
        - **Standard:** Triple-Therapie (ADT + Docetaxel + ARPI).
        - **Zulassung:** Darolutamid (ARASENS) oder Abirateron (PEACE-1).
        - **Alternative:** ADT + ARPI wenn Chemo-unkritisch.
        """,
        "text_mhspc_low": """
        **mHSPC - Geringes Volumen**
        - **Systemisch:** ADT + ARPI (Zweifachkombination).
        - **Lokal:** **Strahlentherapie der Prostata** verbessert das Gesamtüberleben.
        """,
        "text_mcrpc": """
        **mCRPC (Kastrationsresistent)**
        - **Sequenz:** Wirkmechanismus wechseln.
        - **BRCA1/2+:** PARP-Inhibitor (Olaparib, Niraparib, Talazoparib) + ARPI.
        - **PSMA+:** Lutetium-177-PSMA (nach ARPI/Chemo).
        """
    }
}

t_opts_map = ["Localized (cT1-2)", "Locally Advanced (cT3-4 / cN1)", "Metastatic (M1)"]
gen_opts = ["Not Performed/Negative", "BRCA1/2 Positive", "HRR Other Positive", "MMR Deficient"]

# --- 2. Helper Functions ---
def calculate_risk_group(psa, isup_index, t_stage_index, lang_dict):
    """Calculates risk based on EAU/S3 criteria."""
    isup = isup_index + 1
    # High Risk: PSA >20 OR ISUP 4-5 OR cT2c/T3
    if psa > 20 or isup >= 4 or t_stage_index >= 3: # Index 3 is cT2c
        return "high", lang_dict["risk_options"]["high"]
    # Intermediate: PSA 10-20 OR ISUP 2-3 OR cT2b
    elif (psa >= 10) or (isup == 2 or isup == 3) or (t_stage_index == 2):
        # Simplified split logic for demo
        if isup == 2 and psa < 10 and t_stage_index < 2:
             return "int_fav", lang_dict["risk_options"]["int_fav"]
        return "int_unfav", lang_dict["risk_options"]["int_unfav"]
    # Low
    else:
        return "low", lang_dict["risk_options"]["low"]

def q(text):
    """Sanitize text for Mermaid"""
    return f'"{text}"'

# --- 3. Sidebar Logic ---
with st.sidebar:
    st.title("⚙️ " + translations["English"]["sidebar_title"])
    lang_choice = st.selectbox("Language / Sprache", ["English", "Deutsch"])
    t = translations[lang_choice]
    
    st.markdown("---")
    
    # 1. Genetics
    genetic_status = st.selectbox(t["genetic_label"], gen_opts)
    
    # 2. Extent
    disease_extent = st.selectbox(t["extent_label"], t_opts_map)
    
    # 3. Dynamic Inputs based on extent
    calc_risk_key = None
    calc_risk_label = ""
    in_psa = 0
    in_isup = ""
    n_stage = None
    m_state = None
    volume = None
    
    if disease_extent == t_opts_map[0]: # Localized
        st.subheader(f"🧮 {t['calc_title']}")
        in_psa = st.number_input(t["psa_label"], value=5.0, step=0.1)
        in_isup = st.selectbox(t["isup_label"], t["isup_opts"])
        in_tstage = st.selectbox(t["tstage_label"], t["t_opts"])
        
        # Auto-Calculate
        isup_idx = t["isup_opts"].index(in_isup)
        t_idx = t["t_opts"].index(in_tstage)
        calc_risk_key, calc_risk_label = calculate_risk_group(in_psa, isup_idx, t_idx, t)
        
        st.success(f"**{t['calc_result']}**\n\n{calc_risk_label}")
        
    elif disease_extent == t_opts_map[1]: # Locally Advanced
        st.subheader("Staging Details")
        n_stage = st.radio(t["n_stage_label"], t["n_stages"])
        
    elif disease_extent == t_opts_map[2]: # Metastatic
        st.subheader("Metastatic Details")
        m_state = st.radio(t["meta_state_label"], t["m_states"])
        if m_state == t["m_states"][0]: # mHSPC
            volume = st.radio(t["volume_label"], t["volumes"])
        else: # mCRPC
            prior = st.multiselect(t["prior_label"], t["prior_opts"])

# --- 4. Main Content Area ---
st.title(t["title"])
st.markdown(t["description"])

# Global Disclaimer
st.warning("⚠️ **Disclaimer:** This tool is for educational purposes only. Treatment decisions must be individualized. Verify 'Zulassung' (approval status) in your specific region.")

# --- LOGIC & RENDERING ---
st.header(t["rec_title"])
mermaid_code = "graph TD\n"
mermaid_code += f'Start["Diagnosis"] --> Gen{{"Genetics: {genetic_status}"}}\n'

# --- A. Localized Disease ---
if disease_extent == t_opts_map[0]:
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Prostate_cancer_Gleason_score.jpg/640px-Prostate_cancer_Gleason_score.jpg", 
             caption="Gleason Score / ISUP Grading Patterns ", use_column_width=True)
    with col2:
        if calc_risk_key == "low":
            st.info(t["text_low"])
            if "BRCA" in genetic_status:
                st.error("❗ **BRCA+ Warning:** Active Surveillance is risky. Upgrading is common. Consider confirmatory biopsy or radical therapy.")
        elif "int" in calc_risk_key:
            st.warning(t["text_int"])
        else:
            st.error(t["text_high"])
            
    # Mermaid
    mermaid_code += f'Gen --> Loc["Localized Disease"]\n'
    mermaid_code += f'Loc --> Risk{{"Risk Stratification"}}\n'
    mermaid_code += f'Risk -->|PSA {in_psa}| {calc_risk_key.upper()}[{q(calc_risk_label)}]\n'
    if calc_risk_key == "low":
        mermaid_code += f'{calc_risk_key.upper()} --> AS["Active Surveillance"]\n'
    elif "int" in calc_risk_key:
        mermaid_code += f'{calc_risk_key.upper()} --> IntOpts["AS (fav) or RP/EBRT"]\n'
    else:
        mermaid_code += f'{calc_risk_key.upper()} --> Multi["Multimodal: RP+LND or EBRT+ADT"]\n'

# --- B. Locally Advanced ---
elif disease_extent == t_opts_map[1]:
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/TNM_Staging_System_for_Prostate_Cancer.png/640px-TNM_Staging_System_for_Prostate_Cancer.png",
             caption="TNM Staging: Note Regional Nodes ", use_column_width=True)
    with col2:
        if n_stage == t["n_stages"][1]: # cN1
            st.error(t["text_n1"])
        else:
            st.warning(t["text_high"])
            st.write("**Note:** Even for cN0, if high-risk features exist, long-term ADT is indicated.")

    # Mermaid
    mermaid_code += f'Gen --> Adv["Locally Advanced"]\n'
    mermaid_code += f'Adv --> Node{{"N-Status?"}}\n'
    if n_stage == t["n_stages"][1]:
        mermaid_code += f'Node -->|cN1| N1Tx["EBRT + ADT (3y) + Abiraterone (2y)"]\n'
    else:
        mermaid_code += f'Node -->|cN0| N0Tx["EBRT + ADT (2-3y) OR RP + ePLND"]\n'

# --- C. Metastatic ---
elif disease_extent == t_opts_map[2]:
    # 1. mHSPC
    if m_state == t["m_states"][0]:
        st.subheader("mHSPC Management")
        col1, col2 = st.columns([1, 1])
        with col1:
             st.image("https://upload.wikimedia.org/wikipedia/commons/6/6d/Bone_scan_Prostate_Cancer.jpg", caption="Bone Scan vs PSMA-PET for Volume ", use_column_width=True)
        with col2:
            if volume == t["volumes"][1]: # High
                st.error(t["text_mhspc_high"])
            else:
                st.success(t["text_mhspc_low"])
        
        # Mermaid
        mermaid_code += f'Gen --> mHSPC["mHSPC"]\n'
        mermaid_code += f'mHSPC --> Vol{{"Volume?"}}\n'
        if volume == t["volumes"][1]:
            mermaid_code += f'Vol -->|High| Triple["Triple: ADT+Chemo+ARPI"]\n'
        else:
            mermaid_code += f'Vol -->|Low| Double["Doublet: ADT+ARPI"]\n'
            mermaid_code += f'Double --> RT["+ RT to Prostate"]\n'
            
    # 2. mCRPC
    else:
        st.subheader("mCRPC Management")
        st.write(t["text_mcrpc"])
        
        # PARP Logic
        with st.expander("🧬 PARP Inhibitors Details"):
            st.write("**Mechanism:** Synthetic Lethality in HRR-deficient cells.")
            
            st.write("- **Olaparib:** BRCA1/2, ATM (PROfound trial).")
            st.write("- **Niraparib/Talazoparib:** Combined with ARPI (MAGNITUDE/TALAPRO-2).")
        
        # Mermaid
        mermaid_code += f'Gen --> mCRPC["mCRPC"]\n'
        mermaid_code += f'mCRPC --> Switch["Switch Mechanism"]\n'
        if "BRCA" in genetic_status:
            mermaid_code += f'Switch -->|BRCA+| PARP["PARP Inhibitor Combo"]\n'
        else:
            mermaid_code += f'Switch -->|BRCA-| Chemo["Taxane / PSMA-Lu"]\n'

# --- 5. Visual Flow Component ---
st.markdown("---")
st.subheader(t["flow_title"])

# Robust Mermaid Rendering
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
    height=450,
    scrolling=True
)
