import streamlit as st
import streamlit.components.v1 as components

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Prostate Cancer Algorithm 2025/26",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Translation & Content Dictionary ---
translations = {
    "English": {
        "title": "Prostate Cancer Algorithm (EAU 2025 / Knowuro)",
        "sidebar_title": "Configuration",
        "screening_note": "ℹ️ **Source:** Logic based on EAU Guidelines 2024/25 & Knowuro Flowchart.",

        # UI Labels
        "extent_label": "Clinical Phase",
        "psa_label": "PSA Level (ng/ml)",
        "psad_label": "PSA Density (PSAD)",
        "pirads_label": "mpMRI PIRADS Score",
        "isup_label": "ISUP Grade",
        "tstage_label": "Clinical T-Stage",
        "n_stage_label": "N-Stage",
        "meta_state_label": "Metastatic State",
        "psadt_label": "PSA Doubling Time (months)",
        "recurrence_time_label": "Time to Recurrence (months)",
        "primary_tx_label": "Primary Therapy",
        
        # Options
        "extent_opts": ["Diagnosis (Biopsy Decision)", "Localized (Staging & Risk)", "Locally Advanced (cT3-4/cN1)", "Biochemical Recurrence (BCR)", "Metastatic (M1)"],
        "pirads_opts": ["PIRADS 1-2", "PIRADS 3", "PIRADS 4-5"],
        "n_stages": ["cN0", "cN1"],
        "m_states": ["mHSPC", "mCRPC"],
        "prior_opts": ["ADT Only", "ADT + Docetaxel", "ADT + ARPI", "Triple Therapy"],
        "primary_tx_opts": ["Radical Prostatectomy (RP)", "Radiotherapy (EBRT)"],

        # --- DIAGNOSIS CONTENT ---
        "header_diag": "Diagnosis: Biopsy Decision",
        "rec_diag_biopsy": "🔴 **Perform Biopsy** (Transperineal preferred).",
        "rec_diag_consider": "🟡 **Consider Biopsy** if High Risk in calc or PSAD > 0.10-0.20.",
        "rec_diag_obs": "🟢 **Observation** (No immediate biopsy unless clinical suspicion high).",

        # --- BCR CONTENT (Enhanced) ---
        "header_bcr": "Biochemical Recurrence (BCR)",
        "rec_bcr_low_risk": """
        🟢 **EAU Low-Risk BCR**
        *Criteria: PSADT > 1y AND ISUP < 4*
        - **Recommendation:** Offer **Salvage RT** or **Monitoring** (Observation).
        """,
        "rec_bcr_high_risk": """
        🔴 **EAU High-Risk BCR**
        *Criteria: PSADT < 1y OR ISUP $\ge$ 4*
        - **Recommendation:** **Early Salvage RT** + ADT.
        """,
        "rec_bcr_embark": """
        🔥 **Very High Risk (EMBARK/High-Risk)**
        *Criteria: PSADT < 9 months*
        - **Therapy:** **Enzalutamide** + ADT (Superior MFS).
        """,

        # --- mCRPC CONTENT (Enhanced) ---
        "header_mcrpc": "mCRPC Management",
        "rec_mcrpc_pembro": """
        🧬 **Immunotherapy Option**
        - **Pembrolizumab:** Approved if **MSI-High** or **dMMR** (Microsatellite Instability).
        """,
        "rec_mcrpc_ra223": """
        ☢️ **Radium-223**
        - *Indication:* Symptomatic bone mets, **no visceral mets**.
        """,
        
        # Standard texts (kept from previous)
        "rec_mhspc_high": "🔴 **High Volume:** Triple Therapy (ADT + Docetaxel + ARPI).",
        "rec_mhspc_low": "🟢 **Low Volume:** ADT + ARPI + Prostate RT.",
        "rec_la_cn1": "⚠️ **cN1:** STAMPEDE Protocol (ADT + RT + 2y Abiraterone).",
        "rec_mcrpc_chemo": "**Taxanes:** Docetaxel or Cabazitaxel.",
        "rec_mcrpc_parp": "**PARP:** Olaparib/Talazoparib (BRCA+).",
    },
    # (German/Spanish can be added similarly, keeping English for brevity in this update)
}

# --- 3. Logic Functions ---

def get_diagnosis_rec(pirads, psad):
    """Logic based on Knowuro/EAU Flowchart"""
    if pirads == "PIRADS 4-5":
        return "rec_diag_biopsy"
    elif pirads == "PIRADS 3":
        if psad >= 0.20: return "rec_diag_biopsy"
        elif psad >= 0.10: return "rec_diag_consider"
        else: return "rec_diag_obs"
    else: # 1-2
        if psad >= 0.20: return "rec_diag_biopsy" # Clinical suspicion override
        return "rec_diag_obs"

def get_bcr_risk(primary, psadt, isup_idx, interval):
    """
    EAU Low vs High Risk BCR
    ISUP 0-2 (<4) vs 3-4 (>=4)
    """
    is_high_grade = (isup_idx >= 3) # ISUP 4 or 5
    
    if primary == "Radical Prostatectomy (RP)":
        # Post-RP: Low Risk if PSADT > 1y AND ISUP < 4
        if psadt > 12 and not is_high_grade: return "rec_bcr_low_risk"
        else: return "rec_bcr_high_risk"
    else:
        # Post-RT: Low Risk if Interval > 18m AND ISUP < 4
        if interval > 18 and not is_high_grade: return "rec_bcr_low_risk"
        else: return "rec_bcr_high_risk"

# --- 4. UI ---
with st.sidebar:
    st.header("⚙️ Configuration")
    t = translations["English"] # Defaulting to English for this enhanced demo
    
    # Phase Selection
    disease_extent = st.selectbox(t["extent_label"], t["extent_opts"])
    
    # --- A. DIAGNOSIS ---
    if disease_extent == t["extent_opts"][0]:
        st.subheader("Diagnostics")
        in_pirads = st.selectbox(t["pirads_label"], t["pirads_opts"])
        in_psad = st.number_input(t["psad_label"], value=0.15, step=0.01, format="%.2f")
    
    # --- B. LOCALIZED ---
    elif disease_extent == t["extent_opts"][1]:
        st.subheader("Risk Calc")
        in_psa = st.number_input(t["psa_label"], value=6.0)
        in_isup = st.selectbox(t["isup_label"], ["ISUP 1", "ISUP 2", "ISUP 3", "ISUP 4", "ISUP 5"])
        in_tstage = st.selectbox(t["tstage_label"], ["cT1c", "cT2a", "cT2b", "cT2c"])
    
    # --- C. LOCALLY ADVANCED ---
    elif disease_extent == t["extent_opts"][2]:
        n_stage = st.radio(t["n_stage_label"], t["n_stages"])
        
    # --- D. BCR ---
    elif disease_extent == t["extent_opts"][3]:
        st.subheader("Recurrence Details")
        primary_tx = st.radio(t["primary_tx_label"], t["primary_tx_opts"])
        in_isup = st.selectbox(t["isup_label"], ["ISUP 1", "ISUP 2", "ISUP 3", "ISUP 4", "ISUP 5"])
        psadt = st.number_input(t["psadt_label"], value=10.0)
        recurrence_time = 0
        if primary_tx == "Radiotherapy (EBRT)":
            recurrence_time = st.number_input(t["recurrence_time_label"], value=12)
            
    # --- E. METASTATIC ---
    elif disease_extent == t["extent_opts"][4]:
        m_state = st.radio(t["meta_state_label"], t["m_states"])
        is_high_vol = False
        msi_high = False
        if m_state == "mHSPC":
            if st.checkbox("High Volume (Visceral/4+ Bone)?"): is_high_vol = True
        else: # mCRPC
            prior = st.selectbox("Prior Therapy", t["prior_opts"])
            msi_high = st.checkbox("MSI-High / dMMR?")

# --- 5. Main Content ---
st.title(t["title"])
st.info(t["screening_note"])

# === LOGIC & DISPLAY ===

# 1. DIAGNOSIS
if disease_extent == t["extent_opts"][0]:
    st.header(t["header_diag"])
    res_key = get_diagnosis_rec(in_pirads, in_psad)
    
    if res_key == "rec_diag_biopsy":
        st.error(t[res_key])
    elif res_key == "rec_diag_consider":
        st.warning(t[res_key])
    else:
        st.success(t[res_key])
        
    # Mermaid for Diagnosis
    mermaid_code = f"""
    graph TD
    Start[Suspicion] --> MRI{{{in_pirads}}}
    MRI -->|PIRADS 4-5| Bx[Biopsy]
    MRI -->|PIRADS 3| PSAD{{PSAD {in_psad}}}
    PSAD -->|>=0.10| Bx
    PSAD -->|<0.10| Obs[Observation]
    MRI -->|PIRADS 1-2| Obs
    """

# 2. LOCALIZED
elif disease_extent == t["extent_opts"][1]:
    st.header("Localized Disease")
    # (Simplified logic for brevity, reusing previous robust logic in production)
    if in_psa > 20 or "ISUP 4" in in_isup or "ISUP 5" in in_isup:
        st.error("🔴 **High Risk:** Multimodal Therapy (RP/EBRT + Long ADT).")
        mermaid_code = "graph TD\nStart --> High[High Risk] --> Multi[EBRT+ADT or RP]"
    else:
        st.success("🟢 **Low/Intermediate:** Active Surveillance or Single Modality.")
        mermaid_code = "graph TD\nStart --> LowInt --> AS_RP_RT[AS / RP / RT]"

# 3. LOCALLY ADVANCED
elif disease_extent == t["extent_opts"][2]:
    st.header("Locally Advanced")
    if n_stage == "cN1":
        st.error(t["rec_la_cn1"])
        mermaid_code = "graph TD\nStart --> cN1 --> STAMPEDE[ADT + RT + Abiraterone]"
    else:
        st.warning("High Risk Protocol: EBRT + Long Term ADT.")
        mermaid_code = "graph TD\nStart --> cN0 --> HR[EBRT + 2-3y ADT]"

# 4. BCR (ENHANCED)
elif disease_extent == t["extent_opts"][3]:
    st.header(t["header_bcr"])
    
    isup_idx = ["ISUP 1", "ISUP 2", "ISUP 3", "ISUP 4", "ISUP 5"].index(in_isup)
    
    # 1. EMBARK Check (Overriding)
    if psadt < 9:
        st.error(t["rec_bcr_embark"])
    
    # 2. EAU Risk Stratification
    st.markdown("---")
    risk_key = get_bcr_risk(primary_tx, psadt, isup_idx, recurrence_time)
    
    if risk_key == "rec_bcr_high_risk":
        st.warning(t[risk_key])
    else:
        st.success(t[risk_key])
        
    mermaid_code = f"""
    graph TD
    Start[BCR] --> Risk{{EAU Risk}}
    Risk -->|High| Salvage[Early Salvage]
    Risk -->|Low| Obs[Monitoring / Salvage]
    Start -.->|PSADT <9m| Enza[Enzalutamide]
    """

# 5. METASTATIC (ENHANCED)
elif disease_extent == t["extent_opts"][4]:
    if m_state == "mHSPC":
        st.header("mHSPC")
        if is_high_vol:
            st.error(t["rec_mhspc_high"])
        else:
            st.success(t["rec_mhspc_low"])
        mermaid_code = "graph TD\nmHSPC --> Vol{Volume}\nVol -->|High| Triple\nVol -->|Low| Double"
    else:
        st.header(t["header_mcrpc"])
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### Standard")
            st.info(t["rec_mcrpc_chemo"])
        with c2:
            st.markdown("### Precision")
            st.write(t["rec_mcrpc_parp"])
            if msi_high:
                st.error(t["rec_mcrpc_pembro"])
            st.write(t["rec_mcrpc_ra223"])
            
        mermaid_code = f"""
        graph TD
        mCRPC --> Options
        Options --> Chemo
        Options --> PARP
        Options --> Lu177
        Options --> Pembro{{{msi_high}}}
        Pembro -->|Yes| Immunotherapy
        """

# Render Mermaid
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
