import streamlit as st
import streamlit.components.v1 as components

# --- 1. Define Translations & Content ---
translations = {
    "English": {
        "title": "Prostate Cancer Treatment Algorithm",
        "description": "Interactive tool based on EAU 2025 and German S3 Guidelines (v8.1).",
        "sidebar_title": "Patient Configuration",
        "language_label": "Select Language",
        "genetic_label": "Genetic Testing Results",
        "extent_label": "Disease Extent",
        "calc_title": "Risk Stratification Calculator",
        "psa_label": "PSA Level (ng/ml)",
        "isup_label": "ISUP Grade Group (Gleason)",
        "tstage_label": "Clinical T-Stage",
        "calc_result": "Calculated Risk Group:",
        "risk_options": {
            "low": "Low Risk",
            "int_fav": "Intermediate Risk (Favorable)",
            "int_unfav": "Intermediate Risk (Unfavorable)",
            "high": "High Risk"
        },
        "rec_title": "Therapy Recommendations",
        "flow_title": "Visual Decision Pathway",
        "isup_opts": ["ISUP 1 (Gleason 6)", "ISUP 2 (Gleason 3+4)", "ISUP 3 (Gleason 4+3)", "ISUP 4 (Gleason 8)", "ISUP 5 (Gleason 9-10)"],
        "t_opts": ["cT1", "cT2a", "cT2b", "cT2c", "cT3", "cT4"],
        "text_map": {
            "low": """
**Primary Recommendation:** Active Surveillance (AS).
- **Protocol:** PSA every 6mo, mpMRI at 12-18mo.
- **Alternative:** RP or EBRT (if AS declined).
- **Zulassung:** All standard therapies approved.
            """,
            "int": """
**Options:** Active Surveillance (only if favorable) OR Curative Therapy.
- **Curative:** RP (radical prostatectomy) or EBRT + short-term ADT (4-6 mo).
- **Note:** Check for cribriform pattern (contraindication for AS).
            """,
            "high": """
**Multimodal Therapy Required:**
- **Option A:** EBRT + Long-term ADT (24-36 mo).
- **Option B:** RP + ePLND (extended lymph node dissection).
- **Genetics:** Germline testing recommended.
            """
        }
    },
    "Deutsch": {
        "title": "Prostatakarzinom Behandlungsalgorithmus",
        "description": "Interaktives Tool basierend auf EAU 2025 und Deutscher S3-Leitlinie (v8.1).",
        "sidebar_title": "Patientenkonfiguration",
        "language_label": "Sprache auswählen",
        "genetic_label": "Genetische Testergebnisse",
        "extent_label": "Ausbreitung der Erkrankung",
        "calc_title": "Risiko-Kalkulator",
        "psa_label": "PSA-Wert (ng/ml)",
        "isup_label": "ISUP Graduierung (Gleason)",
        "tstage_label": "Klinisches T-Stadium",
        "calc_result": "Berechnete Risikogruppe:",
        "risk_options": {
            "low": "Niedriges Risiko",
            "int_fav": "Intermediäres Risiko (Günstig)",
            "int_unfav": "Intermediäres Risiko (Ungünstig)",
            "high": "Hohes Risiko"
        },
        "rec_title": "Therapieempfehlungen",
        "flow_title": "Visueller Entscheidungspfad",
        "isup_opts": ["ISUP 1 (Gleason 6)", "ISUP 2 (Gleason 3+4)", "ISUP 3 (Gleason 4+3)", "ISUP 4 (Gleason 8)", "ISUP 5 (Gleason 9-10)"],
        "t_opts": ["cT1", "cT2a", "cT2b", "cT2c", "cT3", "cT4"],
        "text_map": {
            "low": """
**Primäre Empfehlung:** Aktive Überwachung (AS).
- **Protokoll:** PSA alle 6 Monate, mpMRI nach 12-18 Monaten.
- **Alternative:** RP oder EBRT (wenn AS abgelehnt).
            """,
            "int": """
**Optionen:** Aktive Überwachung (nur wenn günstig) ODER Kurative Therapie.
- **Kurativ:** RP (Radikale Prostatektomie) oder EBRT + kurzzeitig ADT (4-6 Mon).
            """,
            "high": """
**Multimodale Therapie erforderlich:**
- **Option A:** EBRT + Langzeit-ADT (24-36 Mon).
- **Option B:** RP + ePLND (Lymphadenektomie).
- **Genetik:** Keimbahntestung empfohlen.
            """
        }
    }
}

t_opts_map = ["Localized (cT1-2)", "Locally Advanced (cT3-4/N1)", "Metastatic (M1)"]
gen_opts = ["Not Performed", "Negative", "BRCA1/2 Positive", "ATM/CHECK2 Positive", "MMR Deficient"]

# --- 2. Risk Calculator Function ---
def calculate_risk_group(psa, isup_index, t_stage_index, lang_dict):
    isup = isup_index + 1
    # Check High Risk factors
    if psa > 20 or isup >= 4 or t_stage_index >= 3: # Index 3 is cT2c
        return "high", lang_dict["risk_options"]["high"]
    # Check Intermediate Risk factors
    elif (psa >= 10) or (isup == 2 or isup == 3) or (t_stage_index == 2): # Index 2 is cT2b
        return "int", lang_dict["risk_options"]["int_unfav"]
    # Default to Low
    else:
        return "low", lang_dict["risk_options"]["low"]

# --- 3. Streamlit App Layout ---
with st.sidebar:
    st.header("⚙️ Configuration")
    lang = st.selectbox("Language / Sprache", ["English", "Deutsch"])
    t = translations[lang]
    st.markdown("---")
    st.subheader(t["sidebar_title"])
    genetic_status = st.selectbox(t["genetic_label"], gen_opts)
    disease_extent = st.selectbox(t["extent_label"], t_opts_map)
    
    calc_risk_key = None
    calc_risk_label = ""
    in_psa = 0
    in_isup = ""
    
    if disease_extent == t_opts_map[0]: # Localized
        st.markdown(f"### 🧮 {t['calc_title']}")
        st.info("Enter clinical data to calculate risk group automatically.")
        in_psa = st.number_input(t["psa_label"], min_value=0.0, value=5.0, step=0.1)
        in_isup = st.selectbox(t["isup_label"], t["isup_opts"])
        in_tstage = st.selectbox(t["tstage_label"], t["t_opts"])
        
        isup_idx = t["isup_opts"].index(in_isup)
        t_idx = t["t_opts"].index(in_tstage)
        calc_risk_key, calc_risk_label = calculate_risk_group(in_psa, isup_idx, t_idx, t)
        st.success(f"**{t['calc_result']}**\n\n{calc_risk_label}")

# Main Content
st.title(t["title"])
st.markdown(t["description"])
st.warning("⚠️ **Disclaimer:** For educational purposes only. Verify 'Zulassung' (approval status) locally.")

# Recommendations
st.header(t["rec_title"])

if disease_extent == t_opts_map[0]: # Localized
    # Contextual Image for Localized Staging
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Prostate_cancer_Gleason_score.jpg/640px-Prostate_cancer_Gleason_score.jpg", 
             caption="Gleason Score / ISUP Grading Patterns ", width=400)
    
    if calc_risk_key == "low":
        st.info(t["text_map"]["low"])
    elif "int" in calc_risk_key:
        st.warning(t["text_map"]["int"])
    elif calc_risk_key == "high":
        st.error(t["text_map"]["high"])
    if "BRCA" in genetic_status and calc_risk_key == "low":
        st.error("❗ **Genetic Alert:** BRCA2+ patients in Low Risk/AS have higher rates of upgrading.")

elif disease_extent == t_opts_map[1]: # Locally Advanced
    # Contextual Image for Advanced Staging
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/TNM_Staging_System_for_Prostate_Cancer.png/640px-TNM_Staging_System_for_Prostate_Cancer.png",
             caption="Prostate Cancer T-Stages (T1-T4) ", width=400)
    
    st.error(t["text_map"]["high"])
    st.write("- **N1 Disease:** Consider Abiraterone (2 yrs) + ADT + RT.")

else: # Metastatic
    st.info("Metastatic Management (mHSPC / mCRPC) - See full guidelines.")
    st.write("Determine Volume (CHAARTED) and start ADT + ARPI.")

# --- 4. Mermaid Visual Flow (Robust Fix) ---
st.markdown("---")
st.subheader(t["flow_title"])

# Helper function to sanitize text for Mermaid (wraps in quotes)
def q(text):
    return f'"{text}"'

# Start building graph
mermaid_code = "graph TD\n"
mermaid_code += f'Start["Diagnosis"] --> Gen{{"Genetics: {genetic_status}"}}\n'

if disease_extent == t_opts_map[0]: # Localized
    mermaid_code += f'Gen --> Calc{{"Risk Calc"}}\n'
    # Use generic label in edge to avoid paren syntax errors
    mermaid_code += f'Calc -->|PSA: {in_psa} / {in_isup.split(" ")[0]}...| RiskResult[{q(calc_risk_label)}]\n'
    
    if calc_risk_key == "low":
        mermaid_code += f'RiskResult --> AS["Active Surveillance"]\n'
    elif "int" in calc_risk_key:
        mermaid_code += f'RiskResult --> Opts["AS (fav) or RP/EBRT"]\n'
    else:
        mermaid_code += f'RiskResult --> Multi["Multimodal: RP+LND or EBRT+ADT"]\n'

elif disease_extent == t_opts_map[1]: # Locally Advanced
    mermaid_code += f'Gen --> Adv["Locally Advanced"]\n'
    mermaid_code += f'Adv --> Multi["Multimodal Therapy (High Risk Protocol)"]\n'
    mermaid_code += f'Multi --> N1["If N1: Consider Abiraterone"]\n'

elif disease_extent == t_opts_map[2]: # Metastatic
    mermaid_code += f'Gen --> Meta["Metastatic (M1)"]\n'
    mermaid_code += f'Meta --> HSPC["Hormone Sensitive (mHSPC)"]\n'
    mermaid_code += f'HSPC --> Backbone["ADT + ARPI +/- Docetaxel"]\n'

# Render Mermaid with simple wrapper
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
