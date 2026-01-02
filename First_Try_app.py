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
    "Deutsch": {
        "title": "Prostatakarzinom Algorithmus (S3-Leitlinie 2025 / EAU)",
        "sidebar_title": "Konfiguration",
        
        # Clinical Notes
        "screening_note_title": "Hinweis zur Digitalen Rektalen Untersuchung (DRU)",
        "screening_note": """
        ℹ️ **S3-Leitlinie (Version 8.1):** Die DRU wird für das **Screening** (Früherkennung) aufgrund geringer Sensitivität (PROBASE-Studie) kritisch gesehen.
        Für das **Staging** (Beurteilung der T-Kategorie: cT2 vs. cT3) nach gesicherter Diagnose bleibt sie jedoch ein wichtiges klinisches Werkzeug, ergänzend zur mpMRT.
        """,

        # Labels
        "extent_label": "Krankheitsstadium",
        "psa_label": "PSA-Wert (ng/ml)",
        "isup_label": "ISUP Grad (Gleason)",
        "tstage_label": "Klinisches T-Stadium",
        "meta_state_label": "Metastasen-Status",
        
        # Metastatic specific
        "visceral_label": "Viszerale Metastasen (Leber, Lunge)?",
        "bone_count_label": "Anzahl der Knochenmetastasen",
        "prior_tx_label": "Vortherapie in der hormonsensitiven Phase (mHSPC)?",
        
        # Options / Dropdowns
        "extent_opts": ["Lokalisiert/Lokal Fortgeschritten (M0)", "Metastasiert (M1)"],
        "t_opts": ["cT1c (Nicht tastbar)", "cT2a (<50% Seitenlappen)", "cT2b (>50%)", "cT2c (Beide Lappen)", "cT3a (Extrakapsulär)", "cT3b (Samenblasen)", "cT4 (Nachbarorgane)"],
        "prior_opts": ["Nur ADT (oder ADT + 1. Gen Antiandrogen)", "ADT + Docetaxel", "ADT + ARPI (Abirateron/Enza/Apa/Daro)", "Tripel-Therapie (ADT+Chemo+ARPI)"],
        "m_states": ["mHSPC (Hormonsensitiv)", "mCRPC (Kastrationsresistent)"],

        # Output Headers
        "risk_header": "Risikostratifizierung (S3)",
        "therapy_header": "Therapieempfehlung",
        "calc_result": "Ergebnis",

        # Recommendations Text
        "risk_low": "Niedriges Risiko",
        "risk_int_fav": "Intermediär (Günstig - AS Option)",
        "risk_int": "Intermediäres Risiko",
        "risk_high": "Hohes Risiko",

        "rec_as_extended": """
        **Aktive Überwachung (Active Surveillance - AS)**
        *Besonderheit der deutschen S3-Leitlinie:*
        Im Gegensatz zu strikteren EAU-Kriterien (<10 ng/ml) erlaubt die S3-Leitlinie AS auch bei **PSA bis 15 ng/ml** (in Einzelfällen bis 20), sofern:
        - ISUP 1 (Gleason 6).
        - cT1c/cT2a.
        - <50% positive Stanzen in der Biopsie.
        
        **Vorgehen:** PSA alle 3-6 Mon., Re-Biopsie/MRT nach 12-18 Mon.
        """,
        
        "rec_curative": """
        **Kurative Standardtherapie**
        - **Radikale Prostatektomie:** + pelvine Lymphadenektomie (LAE).
        - **Strahlentherapie (EBRT):** IMRT/VMAT + kurzzeitige ADT (4-6 Monate).
        """,

        "rec_multimodal": """
        **Multimodale Therapie (High Risk / cT3)**
        - **EBRT:** Dosis-eskaliert + **Langzeit-ADT** (2-3 Jahre).
        - **RP:** Radikale Prostatektomie + ausgedehnte LAE (oft multimodales Konzept nötig).
        """,

        "rec_mhspc_high": """
        🔴 **mHSPC - Hohes Volumen (High Volume)**
        *Definition (CHAARTED): Viszerale Met. ODER ≥4 Knochenmet. (davon ≥1 außerhalb Wirbelsäule/Becken)*
        
        **Standard: Tripel-Therapie**
        1. **ADT** (LHRH-Analogon kontinuierlich).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ alle 3 Wochen (6 Zyklen).
        3. **ARPI:** - **Darolutamid:** $600$ mg 2x tgl (ARASENS).
           - *ODER* **Abirateron:** $1000$ mg 1x tgl + Prednison (PEACE-1).
        """,
        
        "rec_mhspc_low": """
        🟢 **mHSPC - Geringes Volumen (Low Volume)**
        
        **Standard: Doublet-Therapie + Lokaltherapie**
        1. **ADT** + **ARPI** (Enzalutamid, Apalutamid oder Abirateron).
        2. **Strahlentherapie der Prostata:** (55 Gy in 20 Fx) - Überlebensvorteil (STAMPEDE Arm H).
        
        *Cave: Docetaxel hat bei Low Volume keinen Überlebensvorteil und sollte vermieden werden.*
        """,
        
        "rec_mcrpc_chemo": """
        **Option: Taxan-Chemotherapie**
        - *Wann?* Bei Progress unter ARPI oder hoher Symptomlast.
        - **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (1. Linie Chemo).
        - **Cabazitaxel:** $25 \\text{ mg/m}^2$ q3w (2. Linie Chemo oder direkt nach Docetaxel).
        """,
        
        "rec_mcrpc_lutetium": """
        **Option: PSMA-Radioligandentherapie**
        - *Wann?* PSMA-positiv im PET. Zugelassen nach ARPI und Chemo (VISION).
        - **Lutetium-177-PSMA-617:** $7,4$ GBq alle 6 Wochen (4-6 Zyklen).
        """,
        
        "rec_mcrpc_parp": """
        **Option: PARP-Inhibitoren**
        - *Wann?* Nachweis von **BRCA1/2**-Mutationen.
        - **Olaparib:** $300$ mg 2x tgl.
        - **Talazoparib:** $0,5$ mg 1x tgl.
        - *Kombination mit ARPI (z.B. Abirateron/Enzalutamid) in 1. Linie mCRPC möglich.*
        """,

        "advice_switch": "Patient hat auf ARPI versagt. Kein zweiter ARPI (Kreuzresistenz)! Wechsel auf Chemo oder Lu-177.",
        "advice_taxane": "Patient hatte bereits Chemo. Nächste Schritte: Cabazitaxel oder Lu-177 (wenn PSMA+).",
        "advice_naive": "Patient ist ARPI-naiv. Start mit Enzalutamid oder Abirateron möglich."
    },
    
    "Español": {
        "title": "Algoritmo Cáncer de Próstata (Guía S3 / EAU 2025)",
        "sidebar_title": "Configuración",

        # Clinical Notes
        "screening_note_title": "Nota sobre el Tacto Rectal (DRE)",
        "screening_note": """
        ℹ️ **Guía S3 (Alemania):** El tacto rectal se desaconseja actualmente para el **tamizaje** (detección temprana) debido a su baja sensibilidad (Estudio PROBASE).
        Sin embargo, para el **estadiaje** clínico (diferenciar cT2 vs cT3) una vez confirmado el cáncer, sigue siendo una herramienta necesaria junto a la mpMRI.
        """,

        # Labels
        "extent_label": "Estadio de la Enfermedad",
        "psa_label": "Nivel de PSA (ng/ml)",
        "isup_label": "Grado ISUP (Gleason)",
        "tstage_label": "Estadio Clínico T",
        "meta_state_label": "Estado Metastásico",
        
        # Metastatic specific
        "visceral_label": "¿Metástasis Viscerales (Hígado, Pulmón)?",
        "bone_count_label": "Número de Metástasis Óseas",
        "prior_tx_label": "¿Terapia previa en fase hormonosensible (mHSPC)?",

        # Options / Dropdowns
        "extent_opts": ["Localizado/Localmente Avanzado (M0)", "Metastásico (M1)"],
        "t_opts": ["cT1c (No palpable)", "cT2a (<50% lóbulo)", "cT2b (>50%)", "cT2c (Ambos lóbulos)", "cT3a (Extracapsular)", "cT3b (Vesículas)", "cT4 (Órganos adyacentes)"],
        "prior_opts": ["Solo ADT (o ADT + Bicalutamida)", "ADT + Docetaxel", "ADT + ARPI (Abiraterona/Enza/Apa/Daro)", "Terapia Triple (ADT+Quimio+ARPI)"],
        "m_states": ["mHSPC (Hormonosensible)", "mCRPC (Resistente a Castración)"],

        # Output Headers
        "risk_header": "Estratificación de Riesgo",
        "therapy_header": "Recomendación Terapéutica",
        "calc_result": "Resultado",

        # Recommendations Text
        "risk_low": "Bajo Riesgo",
        "risk_int_fav": "Intermedio (Favorable - Posible AS)",
        "risk_int": "Riesgo Intermedio",
        "risk_high": "Alto Riesgo",

        "rec_as_extended": """
        **Vigilancia Activa (Active Surveillance - AS)**
        *Criterio Extendido (Guía Alemana S3):*
        A diferencia de la EAU (PSA <10), la guía S3 permite AS con **PSA hasta 15 ng/ml** (casos selectos hasta 20) si:
        - ISUP 1 (Gleason 6).
        - Estadio cT1c/cT2a.
        - Baja carga tumoral en biopsia.
        
        **Protocolo:** PSA cada 3-6 meses, re-biopsia/MRI a los 12-18 meses.
        """,

        "rec_curative": """
        **Terapia Curativa Estándar**
        - **Prostatectomía Radical:** + linfadenectomía pélvica.
        - **Radioterapia (EBRT):** IMRT/VMAT + ADT a corto plazo (4-6 meses).
        """,

        "rec_multimodal": """
        **Terapia Multimodal (Alto Riesgo / cT3)**
        - **EBRT:** Dosis escalada + **ADT a largo plazo** (2-3 años).
        - **PR:** Prostatectomía Radical + linfadenectomía extendida (a menudo requiere adyuvancia).
        """,

        "rec_mhspc_high": """
        🔴 **mHSPC - Alto Volumen (High Volume)**
        *Definición (CHAARTED): Metástasis viscerales O ≥4 óseas (≥1 fuera de columna/pelvis)*
        
        **Estándar: Terapia Triple**
        1. **ADT** (Bloqueo androgénico continuo).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ cada 3 semanas (6 ciclos).
        3. **ARPI:** - **Darolutamida:** $600$ mg 2 veces al día (ARASENS).
           - *O* **Abiraterona:** $1000$ mg 1 vez al día + Prednisona (PEACE-1).
        """,
        
        "rec_mhspc_low": """
        🟢 **mHSPC - Bajo Volumen (Low Volume)**
        
        **Estándar: Terapia Doble + Terapia Local**
        1. **ADT** + **ARPI** (Enzalutamida, Apalutamida o Abiraterona).
        2. **Radioterapia a la Próstata:** (55 Gy en 20 fx) - Beneficio en Supervivencia Global (STAMPEDE H).
        
        *Precaución: Evitar Docetaxel en bajo volumen (toxicidad sin beneficio en OS).*
        """,
        
        "rec_mcrpc_chemo": """
        **Opción: Quimioterapia (Taxanos)**
        - *¿Cuándo?* Progresión tras ARPI o síntomas severos.
        - **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (1ª línea quimio).
        - **Cabazitaxel:** $25 \\text{ mg/m}^2$ q3w (2ª línea o tras Docetaxel).
        """,
        
        "rec_mcrpc_lutetium": """
        **Opción: Radioligandos (Teragnosis)**
        - *¿Cuándo?* PSMA-positivo en PET. Aprobado tras ARPI y Quimio (VISION).
        - **Lutetium-177-PSMA-617:** $7.4$ GBq cada 6 semanas (4-6 ciclos).
        """,
        
        "rec_mcrpc_parp": """
        **Opción: Inhibidores PARP**
        - *¿Cuándo?* Mutación **BRCA1/2** confirmada.
        - **Olaparib:** $300$ mg 2 veces al día.
        - **Talazoparib:** $0.5$ mg 1 vez al día.
        - *Combinación con ARPI posible en 1ª línea mCRPC.*
        """,

        "advice_switch": "Paciente progresó con ARPI. ¡No dar segundo ARPI (resistencia cruzada)! Cambiar a Quimio o Lutecio.",
        "advice_taxane": "Paciente ya recibió quimio. Pasos siguientes: Cabazitaxel o Lutecio (si PSMA+).",
        "advice_naive": "Paciente no ha recibido ARPI. Iniciar Enzalutamida o Abiraterona."
    }
}

# --- 3. Logic Functions ---

def calculate_risk(psa, isup_idx, t_idx):
    """
    Returns an internal key (low, int_fav, int, high) based on S3 German modifications.
    ISUP 0=Gleason6. T-Stage: 0=T1c, 1=T2a, 2=T2b, 3=T2c, 4=T3a...
    """
    isup = isup_idx + 1
    
    # High Risk
    if psa > 20 or isup >= 4 or t_idx >= 4:
        return "risk_high"
    
    # Intermediate Risk
    elif (psa >= 10) or (isup == 2 or isup == 3) or (t_idx >= 2):
        # S3 Exception: PSA up to 15 (sometimes 20) allowed for AS if favorable otherwise
        if psa <= 15 and isup == 1 and t_idx <= 1:
            return "risk_int_fav"
        return "risk_int"
    
    # Low Risk
    else:
        return "risk_low"

# --- 4. Sidebar UI ---
with st.sidebar:
    st.header("🌐 Language")
    lang_key = st.selectbox("Select", ["Deutsch", "Español"])
    t = translations[lang_key]
    
    st.markdown("---")
    st.header(t["sidebar_title"])
    
    # Main State Selection
    disease_extent = st.selectbox(t["extent_label"], t["extent_opts"])
    
    # --- INPUTS: LOCALIZED ---
    if disease_extent == t["extent_opts"][0]: # M0
        in_psa = st.number_input(t["psa_label"], value=6.0, step=0.5)
        in_isup_str = st.selectbox(t["isup_label"], ["ISUP 1 (Gleason 6)", "ISUP 2 (3+4)", "ISUP 3 (4+3)", "ISUP 4 (8)", "ISUP 5 (9-10)"])
        in_tstage_str = st.selectbox(t["tstage_label"], t["t_opts"])
        
        # Parse inputs for logic
        idx_isup = ["ISUP 1", "ISUP 2", "ISUP 3", "ISUP 4", "ISUP 5"].index(in_isup_str.split(" (")[0])
        idx_t = t["t_opts"].index(in_tstage_str)
        
        # Calculate Risk Key
        risk_key = calculate_risk(in_psa, idx_isup, idx_t)

    # --- INPUTS: METASTATIC ---
    else:
        st.subheader("Metastatic Config")
        m_state = st.radio(t["meta_state_label"], t["m_states"])
        
        # Volume Logic (CHAARTED)
        visceral = st.checkbox(t["visceral_label"])
        bone_mets = st.number_input(t["bone_count_label"], min_value=0, value=1)
        is_high_volume = False
        if visceral or bone_mets >= 4:
            is_high_volume = True 
            
        # Prior Therapy for mCRPC
        prior_therapy = None
        if m_state == t["m_states"][1]: # mCRPC
            prior_therapy = st.selectbox(t["prior_tx_label"], t["prior_opts"])

# --- 5. Main Content ---
st.title(t["title"])

# DRE Warning
st.info(t["screening_note"])

# --- RESULT: LOCALIZED ---
if disease_extent == t["extent_opts"][0]:
    st.header(t["risk_header"])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### {t['calc_result']}")
        st.write(f"**PSA:** {in_psa} | **Gleason:** {in_isup_str} | **T:** {in_tstage_str.split(' ')[0]}")
        
        display_risk = t[risk_key] # Map key to translated string
        
        if risk_key == "risk_low":
            st.success(f"✅ **{display_risk}**")
            st.info(t["rec_as_extended"])
        elif risk_key == "risk_int_fav":
            st.success(f"✅ **{display_risk}**")
            st.info(t["rec_as_extended"])
        elif risk_key == "risk_int":
            st.warning(f"⚠️ **{display_risk}**")
            st.write(t["rec_curative"])
        else: # High
            st.error(f"🔴 **{display_risk}**")
            st.write(t["rec_multimodal"])
            

# --- RESULT: METASTATIC ---
else:
    st.header(f"{t['therapy_header']} - {m_state}")
    
    # mHSPC
    if m_state == t["m_states"][0]:
        vol_text = "High Volume" if is_high_volume else "Low Volume"
        st.subheader(f"{vol_text}")
        
        if is_high_volume:
            st.error(t["rec_mhspc_high"])
            
        else:
            st.success(t["rec_mhspc_low"])
            
    # mCRPC
    else:
        st.markdown(f"**{t['prior_tx_label']}** {prior_therapy}")
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 1. Chemo / Switch")
            # Logic for advice
            if "ARPI" in prior_therapy:
                st.warning(t["advice_switch"])
                st.write(t["rec_mcrpc_chemo"])
            elif "Docetaxel" in prior_therapy:
                st.warning(t["advice_taxane"])
                st.write("**Cabazitaxel**")
            else:
                st.success(t["advice_naive"])
                st.write("Enzalutamid / Abirateron")
                
        with col2:
            st.markdown("### 2. Teragnosis (PSMA)")
            st.write(t["rec_mcrpc_lutetium"])
            

        with col3:
            st.markdown("### 3. Precision (BRCA)")
            st.write(t["rec_mcrpc_parp"])

# --- 6. Mermaid Visual ---
st.markdown("---")
st.subheader("Visual Pathway")

# Build dynamic Mermaid string based on current state
mermaid_code = "graph TD\n"

if disease_extent == t["extent_opts"][0]:
    # Localized Flow
    mermaid_code += f'Start[Diagnose] --> Risk{{{risk_key}}}\n'
    if risk_key in ["risk_low", "risk_int_fav"]:
        mermaid_code += f'Risk --> AS["Active Surveillance (S3: PSA<15)"]\n'
    else:
        mermaid_code += f'Risk --> Tx["Curative (RP/EBRT)"]\n'
else:
    if m_state == t["m_states"][0]:
        # mHSPC Flow
        vol_str = "HighVolume" if is_high_volume else "LowVolume"
        mermaid_code += f'Start[mHSPC] --> Vol{{{vol_str}}}\n'
        mermaid_code += f'Vol -->|High| Triple["Triple Tx (ADT+Chemo+ARPI)"]\n'
        mermaid_code += f'Vol -->|Low| Double["Doublet (ADT+ARPI) + Prostate RT"]\n'
    else:
        # mCRPC Flow
        mermaid_code += f'Start[mCRPC] --> Prev{{"Prev Tx?"}}\n'
        if "ARPI" in prior_therapy:
            mermaid_code += f'Prev --> Chemo["Docetaxel"]\n'
        elif "Docetaxel" in prior_therapy:
            mermaid_code += f'Prev --> Cab["Cabazitaxel"]\n'
        else:
            mermaid_code += f'Prev --> ARPI["Enza/Abi"]\n'
        mermaid_code += f'Prev -.->|PSMA+| Lu["Lu-177"]\n'

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
