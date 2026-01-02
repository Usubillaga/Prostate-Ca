import streamlit as st
import streamlit.components.v1 as components

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Prostate Cancer Algorithm 2025",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Translation & Content Dictionary ---
translations = {
    "English": {
        "title": "Prostate Cancer Algorithm (S3 Guidelines 2025 / EAU)",
        "sidebar_title": "Configuration",
        
        "screening_note": """
        ℹ️ **S3 Guidelines / EAU:** DRE is currently viewed critically for **Screening** due to low sensitivity (PROBASE).
        However, for **Staging** (cT2 vs cT3) after diagnosis, it remains a standard clinical tool.
        """,

        # Labels
        "extent_label": "Disease Extent",
        "psa_label": "PSA Level (ng/ml)",
        "isup_label": "ISUP Grade",
        "tstage_label": "Clinical T-Stage",
        "meta_state_label": "Metastatic State",
        "psadt_label": "PSA Doubling Time (PSADT)",
        "primary_tx_label": "Prior Primary Therapy",
        
        # Options
        "extent_opts": ["Localized (M0)", "Biochemical Recurrence (BCR)", "Metastatic (M1)"],
        "t_opts": ["cT1c", "cT2a", "cT2b", "cT2c", "cT3a", "cT3b", "cT4"],
        "primary_tx_opts": ["Radical Prostatectomy (RP)", "Radiotherapy (EBRT)"],
        "m_states": ["mHSPC", "mCRPC"],
        "prior_opts": ["ADT Only", "ADT + Docetaxel", "ADT + ARPI", "Triple Therapy"],

        # BCR Content
        "bcr_header": "Biochemical Recurrence Management",
        "rec_bcr_rp": """
        **Post-Prostatectomy Recurrence (PSA > 0.2 ng/ml)**
        - **Diagnostics:** **PSMA-PET/CT** recommended (detection rate correlates with PSA).
        - **Salvage RT:** Radiation to prostate bed +/- pelvic lymph nodes.
        - **ADT Addition:**
            - PSA < 0.6: Salvage RT alone often sufficient.
            - PSA > 0.6 or High Grade: Add Short-term ADT (6-24 mo).
        """,
        "rec_bcr_rt": """
        **Post-Radiotherapy Recurrence (Nadir + 2 ng/ml)**
        - **Diagnostics:** PSMA-PET/CT + Prostate Biopsy mandatory to confirm local vs. systemic recurrence.
        - **Therapy:** Local Salvage (RP/HIFU/Brachy) only for highly selected patients. Systemic ADT is standard.
        """,
        "rec_bcr_embark": """
        🔴 **High Risk BCR (EMBARK Definition)**
        *Criteria: PSA Doubling Time (PSADT) < 9 months.*
        
        **Standard:** **Enzalutamide** ($160$ mg) + ADT (Leuprolide).
        - *Evidence:* Improved Metastasis-Free Survival (MFS) vs ADT alone.
        """,

        # Other Content (Abbreviated for brevity but fully functional)
        "risk_header": "Risk Stratification",
        "rec_as_extended": "**Active Surveillance:** S3 allows up to PSA 15 ng/ml (ISUP 1, cT1c).",
        "rec_curative": "**Standard:** RP or EBRT+ADT.",
        "rec_multimodal": "**High Risk:** Multimodal Therapy mandatory.",
        "rec_mhspc_high": "**mHSPC High Vol:** Triple Therapy (ADT+Docetaxel+ARPI).",
        "rec_mhspc_low": "**mHSPC Low Vol:** ADT + ARPI + Prostate RT.",
        "rec_mcrpc_chemo": "**Taxane:** Docetaxel 50mg q2w (PROSTY) or 75mg q3w.",
    },

    "Deutsch": {
        "title": "Prostatakarzinom Algorithmus (S3-Leitlinie 2025 / EAU)",
        "sidebar_title": "Konfiguration",
        
        "screening_note": """
        ℹ️ **S3-Leitlinie:** DRU wird für das **Screening** kritisch gesehen (PROBASE).
        Für das **Staging** (cT2 vs cT3) nach Diagnose bleibt sie jedoch Standard.
        """,

        "extent_label": "Krankheitsstadium",
        "psa_label": "PSA-Wert (ng/ml)",
        "isup_label": "ISUP Grad",
        "tstage_label": "Klinisches T-Stadium",
        "meta_state_label": "Metastasen-Status",
        "psadt_label": "PSA-Verdopplungszeit (PSADT)",
        "primary_tx_label": "Primärtherapie",
        
        "extent_opts": ["Lokalisiert (M0)", "Biochemisches Rezidiv (BCR)", "Metastasiert (M1)"],
        "t_opts": ["cT1c", "cT2a", "cT2b", "cT2c", "cT3a", "cT3b", "cT4"],
        "primary_tx_opts": ["Radikale Prostatektomie (RP)", "Strahlentherapie (EBRT)"],
        "m_states": ["mHSPC", "mCRPC"],
        "prior_opts": ["Nur ADT", "ADT + Docetaxel", "ADT + ARPI", "Tripel-Therapie"],

        # BCR Content
        "bcr_header": "Management Biochemisches Rezidiv",
        "rec_bcr_rp": """
        **Rezidiv nach Prostatektomie (PSA > 0,2 ng/ml)**
        - **Diagnostik:** **PSMA-PET/CT** empfohlen (Detektion korreliert mit PSA-Höhe).
        - **Salvage-RT:** Bestrahlung der Prostataloge +/- pelvine Lymphwege.
        - **ADT-Addition:**
            - PSA < 0,6: Oft Salvage-RT alleine ausreichend.
            - PSA > 0,6 oder High Grade: Addition von ADT (6-24 Mon).
        """,
        "rec_bcr_rt": """
        **Rezidiv nach Strahlentherapie (Nadir + 2 ng/ml)**
        - **Diagnostik:** PSMA-PET/CT + Biopsie zwingend zur Unterscheidung lokal vs. systemisch.
        - **Therapie:** Lokale Salvage (RP/HIFU) nur für hochselektionierte Patienten. Standard ist systemische ADT.
        """,
        "rec_bcr_embark": """
        🔴 **Hochrisiko-BCR (EMBARK-Kriterien)**
        *Kriterium: PSA-Verdopplungszeit (PSADT) < 9 Monate.*
        
        **Standard:** **Enzalutamide** ($160$ mg) + ADT.
        - *Evidenz:* Verbessertes Metastasen-freies Überleben (MFS) vs ADT alleine.
        """,

        "risk_header": "Risikostratifizierung",
        "rec_as_extended": "**Aktive Überwachung:** S3 erlaubt PSA bis 15 ng/ml (ISUP 1).",
        "rec_curative": "**Standard:** RP oder EBRT+ADT.",
        "rec_multimodal": "**High Risk:** Multimodale Therapie obligat.",
        "rec_mhspc_high": "**mHSPC High Vol:** Tripel-Therapie (ADT+Docetaxel+ARPI).",
        "rec_mhspc_low": "**mHSPC Low Vol:** ADT + ARPI + Prostata-RT.",
        "rec_mcrpc_chemo": "**Taxan:** Docetaxel 50mg q2w (PROSTY) oder 75mg q3w.",
    },
    
    "Español": {
        "title": "Algoritmo Cáncer de Próstata (Guía S3 / EAU 2025)",
        "sidebar_title": "Configuración",
        
        "screening_note": """
        ℹ️ **Guía S3 / EAU:** El tacto rectal se desaconseja para el **tamizaje** (baja sensibilidad).
        Sin embargo, es estándar para el **estadiaje** (cT2 vs cT3) post-diagnóstico.
        """,

        "extent_label": "Estadio de la Enfermedad",
        "psa_label": "Nivel de PSA (ng/ml)",
        "isup_label": "Grado ISUP",
        "tstage_label": "Estadio T Clínico",
        "meta_state_label": "Estado Metastásico",
        "psadt_label": "Tiempo Duplicación PSA (PSADT)",
        "primary_tx_label": "Terapia Primaria Previa",
        
        "extent_opts": ["Localizado (M0)", "Recurrencia Bioquímica (BCR)", "Metastásico (M1)"],
        "t_opts": ["cT1c", "cT2a", "cT2b", "cT2c", "cT3a", "cT3b", "cT4"],
        "primary_tx_opts": ["Prostatectomía Radical (PR)", "Radioterapia (EBRT)"],
        "m_states": ["mHSPC", "mCRPC"],
        "prior_opts": ["Solo ADT", "ADT + Docetaxel", "ADT + ARPI", "Terapia Triple"],

        # BCR Content
        "bcr_header": "Manejo de Recurrencia Bioquímica",
        "rec_bcr_rp": """
        **Recurrencia post-Prostatectomía (PSA > 0.2 ng/ml)**
        - **Diagnóstico:** **PSMA-PET/CT** recomendado.
        - **RT de Rescate:** Radiación al lecho prostático +/- ganglios.
        - **Adición de ADT:**
            - PSA < 0.6: RT sola suele bastar.
            - PSA > 0.6 o Alto Grado: Añadir ADT (6-24 meses).
        """,
        "rec_bcr_rt": """
        **Recurrencia post-Radioterapia (Nadir + 2 ng/ml)**
        - **Diagnóstico:** PSMA-PET/CT + Biopsia obligatoria para confirmar.
        - **Terapia:** Rescate local (PR/HIFU) solo casos selectos. Estándar es ADT sistémica.
        """,
        "rec_bcr_embark": """
        🔴 **BCR de Alto Riesgo (Criterio EMBARK)**
        *Criterio: Tiempo de Duplicación (PSADT) < 9 meses.*
        
        **Estándar:** **Enzalutamida** ($160$ mg) + ADT.
        - *Evidencia:* Mejora Sobrevida Libre de Metástasis (MFS).
        """,

        "risk_header": "Estratificación de Riesgo",
        "rec_as_extended": "**Vigilancia Activa:** S3 permite PSA hasta 15 ng/ml (ISUP 1).",
        "rec_curative": "**Estándar:** PR o EBRT+ADT.",
        "rec_multimodal": "**Alto Riesgo:** Terapia Multimodal obligatoria.",
        "rec_mhspc_high": "**mHSPC High Vol:** Triple Terapia (ADT+Docetaxel+ARPI).",
        "rec_mhspc_low": "**mHSPC Low Vol:** ADT + ARPI + RT Próstata.",
        "rec_mcrpc_chemo": "**Taxano:** Docetaxel 50mg q2w (PROSTY) o 75mg q3w.",
    }
}

# --- 3. Logic Functions ---
def calculate_risk(psa, isup_idx, t_idx):
    isup = isup_idx + 1
    if psa > 20 or isup >= 4 or t_idx >= 4: return "risk_high" # T3a is idx 4
    elif (psa >= 10) or (isup == 2 or isup == 3) or (t_idx >= 2):
        if psa <= 15 and isup == 1 and t_idx <= 1: return "risk_int_fav"
        return "risk_int"
    else: return "risk_low"

# --- 4. Sidebar UI ---
with st.sidebar:
    st.header("🌐 Language")
    lang_key = st.selectbox("Select", ["English", "Deutsch", "Español"])
    t = translations[lang_key]
    
    st.markdown("---")
    st.header(t["sidebar_title"])
    
    # MAIN EXTENT SELECTOR (Restored BCR)
    disease_extent = st.selectbox(t["extent_label"], t["extent_opts"])
    
    # --- A. INPUTS: LOCALIZED ---
    if disease_extent == t["extent_opts"][0]: 
        in_psa = st.number_input(t["psa_label"], value=6.0, step=0.5)
        in_isup_str = st.selectbox(t["isup_label"], ["ISUP 1", "ISUP 2", "ISUP 3", "ISUP 4", "ISUP 5"])
        in_tstage_str = st.selectbox(t["tstage_label"], t["t_opts"])
        
        idx_isup = ["ISUP 1", "ISUP 2", "ISUP 3", "ISUP 4", "ISUP 5"].index(in_isup_str)
        idx_t = t["t_opts"].index(in_tstage_str)
        risk_key = calculate_risk(in_psa, idx_isup, idx_t)

    # --- B. INPUTS: BCR (RESTORED) ---
    elif disease_extent == t["extent_opts"][1]:
        st.subheader("Recurrence Details")
        primary_tx = st.radio(t["primary_tx_label"], t["primary_tx_opts"])
        psadt = st.number_input(t["psadt_label"] + " (months)", value=10.0, step=1.0)

    # --- C. INPUTS: METASTATIC ---
    else:
        st.subheader("Metastatic Config")
        m_state = st.radio(t["meta_state_label"], t["m_states"])
        
        is_high_volume = False
        if m_state == t["m_states"][0]: # mHSPC only
            visceral = st.checkbox("Visceral Mets?")
            bone_mets = st.number_input("Bone Mets Count", min_value=0, value=1)
            if visceral or bone_mets >= 4: is_high_volume = True 
            
        prior_therapy = None
        if m_state == t["m_states"][1]: # mCRPC
            prior_therapy = st.selectbox("Prior Therapy", t["prior_opts"])

# --- 5. Main Content ---
st.title(t["title"])
st.info(t["screening_note"])

# --- OUTPUT A: LOCALIZED ---
if disease_extent == t["extent_opts"][0]:
    st.header(t["risk_header"])
    col1, col2 = st.columns(2)
    with col1:
        
        st.write(f"**PSA:** {in_psa} | **ISUP:** {in_isup_str}")
        if risk_key == "risk_low" or risk_key == "risk_int_fav":
            st.success(t["rec_as_extended"])
        elif risk_key == "risk_int":
            st.warning(t["rec_curative"])
        else:
            st.error(t["rec_multimodal"])

# --- OUTPUT B: BCR (RESTORED) ---
elif disease_extent == t["extent_opts"][1]:
    st.header(t["bcr_header"])
    col1, col2 = st.columns(2)
    
    with col1:
        
        st.write(f"**Primary:** {primary_tx}")
        st.write(f"**PSADT:** {psadt} months")
        
    with col2:
        # High Risk EMBARK Check
        if psadt < 9.0:
            st.error(t["rec_bcr_embark"])
        
        # Standard Recurrence Logic
        st.markdown("---")
        if primary_tx == t["primary_tx_opts"][0]: # RP
            st.info(t["rec_bcr_rp"])
        else: # RT
            st.warning(t["rec_bcr_rt"])

# --- OUTPUT C: METASTATIC ---
else:
    st.header(f"Therapy - {m_state}")
    
    if m_state == t["m_states"][0]: # mHSPC
        vol_text = "High Volume" if is_high_volume else "Low Volume"
        st.subheader(vol_text)
        if is_high_volume:
            st.error(t["rec_mhspc_high"])
        else:
            st.success(t["rec_mhspc_low"])
            
    else: # mCRPC
        st.markdown(f"**Prior:** {prior_therapy}")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Chemo / Switch")
            st.write(t["rec_mcrpc_chemo"]) # Updated with Docetaxel 50mg q2w
        with col2:
             st.markdown("### Precision")
             st.write("**PSMA-Lu177 / PARP-i**")

# --- 6. Mermaid Visual ---
st.markdown("---")
st.subheader("Visual Pathway")
mermaid_code = "graph TD\n"

if disease_extent == t["extent_opts"][0]:
    mermaid_code += f'Start --> Risk{{{risk_key}}}\n'
    if risk_key in ["risk_low", "risk_int_fav"]: mermaid_code += f'Risk --> AS["Active Surveillance"]\n'
    else: mermaid_code += f'Risk --> Tx["Curative Tx"]\n'

elif disease_extent == t["extent_opts"][1]: # BCR Flow
    mermaid_code += f'Start[Recurrence] --> Prim{{"{primary_tx}"}}\n'
    if primary_tx == t["primary_tx_opts"][0]: mermaid_code += f'Prim --> sRT["Salvage RT"]\n'
    else: mermaid_code += f'Prim --> Eval["Local Salvage?"]\n'
    if psadt < 9.0: mermaid_code += f'Start -.->|PSADT <9mo| Embark["Enzalutamide"]\n'

else: # Metastatic
    if m_state == t["m_states"][0]:
        vol_str = "High" if is_high_volume else "Low"
        mermaid_code += f'Start[mHSPC] --> Vol{{{vol_str}}}\n'
        mermaid_code += f'Vol -->|High| Triple["Triple Tx"]\n'
        mermaid_code += f'Vol -->|Low| Double["Doublet + RT"]\n'
    else:
        mermaid_code += f'Start[mCRPC] --> Prev{{"Prev Tx?"}}\n'
        mermaid_code += f'Prev --> Switch["Switch Mech / Chemo"]\n'

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
