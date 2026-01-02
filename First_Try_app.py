import streamlit as st
import streamlit.components.v1 as components

# --- 1. Configuración de la Página ---
st.set_page_config(
    page_title="Prostate Cancer Algorithm 2025 (S3/EAU)",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Textos, Traducciones y Lógica Clínica ---
translations = {
    "Deutsch": {
        "title": "Prostatakarzinom Algorithmus (S3-Leitlinie 2025 / EAU)",
        "config_title": "Patientenkonfiguration",
        
        # Screening Note
        "screening_warning": """
        ℹ️ **Hinweis zum Screening (S3-Leitlinie/Prof. Grimm):** Der Nutzen der digitalen rektalen Untersuchung (DRU) im **Screening** (Früherkennung) wird kritisch gesehen (PROBASE-Studie: geringe Sensitivität). 
        Für das **Staging** (cT-Kategorie) nach Diagnose behält sie jedoch ihren Stellenwert, wobei die mpMRT überlegen ist.
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
        
        # Options
        "t_opts": ["cT1c (Nicht tastbar)", "cT2a (<50% Seitenlappen)", "cT2b (>50%)", "cT2c (Beide Lappen)", "cT3a (ECE)", "cT3b (Samenblasen)", "cT4 (Nachbarorgane)"],
        "prior_opts": ["Nur ADT (oder ADT + 1. Gen Antiandrogen)", "ADT + Docetaxel", "ADT + ARPI (Abirateron/Enza/Apa/Daro)", "Triple Therapie (ADT+Chemo+ARPI)"],

        # Recommendations
        "rec_as_extended": """
        **Aktive Überwachung (Active Surveillance - AS)**
        *S3-Leitlinie Deutschland Besonderheit:*
        - Während EAU oft PSA <10 fordert, erlaubt die S3-Leitlinie AS auch bei **PSA bis 15 ng/ml** (und in Einzelfällen bis 20), sofern:
          - ISUP 1 (Gleason 6).
          - cT1c/cT2a.
          - <50% positive Stanzen.
        - **Vorgehen:** PSA alle 3-6 Mon., Re-Biopsie/MRT nach 12-18 Mon.
        """,
        "rec_mhspc_high": """
        🔴 **mHSPC - Hohes Volumen (High Volume)**
        *Kriterien (CHAARTED): Viszerale Met. ODER ≥4 Knochenmet. (davon ≥1 außerhalb Wirbelsäule/Becken)*
        
        **Empfehlung: Triple-Therapie**
        1. **ADT** (LHRH-Analogon kontinuierlich).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ alle 3 Wochen (6 Zyklen).
        3. **ARPI:** - **Darolutamid:** $600$ mg 2x tgl (ARASENS).
           - *ODER* **Abirateron:** $1000$ mg 1x tgl + Prednison (PEACE-1).
        """,
        "rec_mhspc_low": """
        🟢 **mHSPC - Geringes Volumen (Low Volume)**
        
        **Empfehlung: Doublet-Therapie + Lokaltherapie**
        1. **ADT** + **ARPI** (Enzalutamid, Apalutamid oder Abirateron).
        2. **Strahlentherapie der Prostata:** (55 Gy in 20 Fx) - signifikanter OS-Vorteil (STAMPEDE H).
        *Keine Chemotherapie bei Low Volume (kein Nutzen).*
        """,
        "rec_mcrpc_header": "mCRPC Therapie-Algorithmus",
        "rec_mcrpc_chemo": """
        **Option: Taxan-Chemotherapie**
        - Indikation: Nach Versagen von ARPI oder symptomatisch.
        - **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (1. Linie Chemo).
        - **Cabazitaxel:** $25 \\text{ mg/m}^2$ q3w (2. Linie Chemo, CARD-Studie).
        """,
        "rec_mcrpc_lutetium": """
        **Option: PSMA-Radioligandentherapie**
        - Indikation: PSMA-positiv im PET, nach ARPI und Chemo (VISION-Trial) oder vor Chemo (PSMAfore - Zulassung prüfen).
        - **Lutetium-177-PSMA-617:** $7,4$ GBq alle 6 Wochen (bis zu 6 Zyklen).
        """,
        "rec_mcrpc_parp": """
        **Option: PARP-Inhibitoren (nur bei BRCA1/2 Mutation)**
        - **Olaparib:** $300$ mg 2x tgl.
        - **Talazoparib:** $0,5$ mg 1x tgl.
        - *Kombination mit ARPI möglich in der 1. Linie mCRPC.*
        """
    },
    
    "Español": {
        "title": "Algoritmo Cáncer de Próstata (S3 Alemania / EAU 2026)",
        "config_title": "Configuración del Paciente",

        # Screening Note
        "screening_warning": """
        ℹ️ **Nota sobre Tamizaje (S3 / Prof. Grimm):** El tacto rectal (DRE) para el **tamizaje/screening** primario está desaconsejado actualmente (Estudio PROBASE: baja sensibilidad). 
        Sin embargo, para el **estadiaje** (definir cT2 vs cT3) una vez diagnosticado el cáncer, sigue teniendo utilidad clínica.
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

        # Options
        "t_opts": ["cT1c (No palpable)", "cT2a (<50% lóbulo)", "cT2b (>50%)", "cT2c (Ambos lóbulos)", "cT3a (Extensión extracapsular)", "cT3b (Vesículas seminales)", "cT4 (Invasión órganos)"],
        "prior_opts": ["Solo ADT (o ADT + Bicalutamida)", "ADT + Docetaxel", "ADT + ARPI (Abiraterona/Enza/Apa/Daro)", "Triple Terapia (ADT+Quimio+ARPI)"],

        # Recommendations
        "rec_as_extended": """
        **Vigilancia Activa (Active Surveillance - AS)**
        *Criterio Extendido (Alemania S3):*
        - Mientras la EAU sugiere PSA <10, la guía alemana considera aceptable AS con **PSA hasta 15 ng/ml** si:
          - ISUP 1 (Gleason 6).
          - Estadio cT1c/cT2a.
          - Baja carga tumoral en biopsia.
        - **Protocolo:** PSA cada 3-6 meses, re-biopsia/MRI a los 12-18 meses.
        """,
        "rec_mhspc_high": """
        🔴 **mHSPC - Alto Volumen (High Volume)**
        *Criterios (CHAARTED): Metástasis viscerales O ≥4 óseas (≥1 fuera de columna/pelvis)*
        
        **Recomendación: Triple Terapia**
        1. **ADT** (Bloqueo androgénico continuo).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ cada 3 semanas (6 ciclos).
        3. **ARPI:** - **Darolutamida:** $600$ mg 2 veces al día (ARASENS).
           - *O* **Abiraterona:** $1000$ mg 1 vez al día + Prednisona (PEACE-1).
        """,
        "rec_mhspc_low": """
        🟢 **mHSPC - Bajo Volumen (Low Volume)**
        
        **Recomendación: Terapia Doble + Terapia Local**
        1. **ADT** + **ARPI** (Enzalutamida, Apalutamida o Abiraterona).
        2. **Radioterapia a la Próstata:** (55 Gy en 20 fx) - Beneficio en Supervivencia Global (STAMPEDE H).
        *Evitar Docetaxel en bajo volumen (toxicidad sin beneficio en OS).*
        """,
        "rec_mcrpc_header": "Algoritmo Terapéutico mCRPC",
        "rec_mcrpc_chemo": """
        **Opción: Quimioterapia (Taxanos)**
        - Indicación: Progresión tras ARPI o enfermedad sintomática rápida.
        - **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (1ª línea quimio).
        - **Cabazitaxel:** $25 \\text{ mg/m}^2$ q3w (2ª línea quimio o tras Docetaxel, estudio CARD).
        """,
        "rec_mcrpc_lutetium": """
        **Opción: Radioligandos (Teragnosis)**
        - Indicación: PSMA-positivo en PET, tras fallo de ARPI y Quimio (VISION).
        - **Lutetium-177-PSMA-617:** $7.4$ GBq cada 6 semanas (hasta 6 ciclos).
        """,
        "rec_mcrpc_parp": """
        **Opción: Inhibidores PARP (Solo si mutación BRCA1/2)**
        - **Olaparib:** $300$ mg 2 veces al día.
        - **Talazoparib:** $0.5$ mg 1 vez al día.
        - *Priorizar ante quimioterapia si el paciente es apto.*
        """
    }
}

# --- 3. Lógica de Riesgo (Ajustada para Alemania/PSA 15) ---
def calculate_risk_german_context(psa, isup_idx, t_idx):
    # Índices: ISUP 0=Gleason6, ISUP 1=3+4...
    # T-Stage: 0=T1c, 1=T2a, 2=T2b, 3=T2c, 4=T3a...
    
    isup = isup_idx + 1
    
    # Alto Riesgo
    if psa > 20 or isup >= 4 or t_idx >= 4: # T3a es index 4 en mi lista nueva
        return "High"
    
    # Riesgo Intermedio (con matiz para AS en Alemania)
    # PSA 10-20 o ISUP 2-3 o T2b
    elif (psa >= 10) or (isup == 2 or isup == 3) or (t_idx >= 2):
        # Lógica especial S3: PSA 10-15 con ISUP 1 y T1c/T2a puede ser "AS-eligible"
        if psa <= 15 and isup == 1 and t_idx <= 1:
            return "Intermediate-Favorable (AS Possible)"
        return "Intermediate"
    
    # Bajo Riesgo
    else:
        return "Low"

# --- 4. Interfaz de Usuario ---
with st.sidebar:
    st.header("⚙️ Settings")
    lang_key = st.selectbox("Idioma / Sprache", ["Deutsch", "Español"])
    t = translations[lang_key]
    
    st.markdown("---")
    
    # Estado General
    disease_extent = st.selectbox(t["extent_label"], 
                                  ["Localized/Locally Advanced (M0)", "Metastatic (M1)"])
    
    # --- INPUTS M0 ---
    if disease_extent == "Localized/Locally Advanced (M0)":
        st.subheader(t["config_title"])
        in_psa = st.number_input(t["psa_label"], value=6.0, step=0.5)
        in_isup = st.selectbox(t["isup_label"], ["ISUP 1 (Gleason 6)", "ISUP 2 (3+4)", "ISUP 3 (4+3)", "ISUP 4 (8)", "ISUP 5 (9-10)"])
        in_tstage = st.selectbox(t["tstage_label"], t["t_opts"])
        
        # Calcular índices
        idx_isup = ["ISUP 1", "ISUP 2", "ISUP 3", "ISUP 4", "ISUP 5"].index(in_isup.split(" (")[0])
        idx_t = t["t_opts"].index(in_tstage)
        
        risk_result = calculate_risk_german_context(in_psa, idx_isup, idx_t)

    # --- INPUTS M1 ---
    else:
        st.subheader("Configuración Metástasis")
        m_state = st.radio(t["meta_state_label"], ["mHSPC", "mCRPC"])
        
        # Lógica de Volumen (CHAARTED)
        visceral = st.checkbox(t["visceral_label"])
        bone_mets = st.number_input(t["bone_count_label"], min_value=0, value=1)
        
        # Determinar Volumen automáticamente
        is_high_volume = False
        if visceral or bone_mets >= 4:
            is_high_volume = True # Simplificación, CHAARTED requiere 1 fuera de esqueleto axial, asumimos para demo
            
        # Historial Terapéutico (Para mCRPC)
        if m_state == "mCRPC":
            prior_therapy = st.selectbox(t["prior_tx_label"], t["prior_opts"])

# --- 5. Contenido Principal ---
st.title(t["title"])

# Nota sobre DRE/Tamizaje
st.info(t["screening_warning"])

# --- RESULTADOS M0 ---
if disease_extent == "Localized/Locally Advanced (M0)":
    st.header(f"Estadio M0 - Riesgo: {risk_result}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📊 Calculadora S3")
        st.write(f"**PSA:** {in_psa} | **Gleason:** {in_isup} | **T:** {in_tstage.split(' ')[0]}")
        
        if risk_result == "Low":
            st.success("✅ **Bajo Riesgo:** Active Surveillance es el estándar.")
        elif risk_result == "Intermediate-Favorable (AS Possible)":
            st.success("✅ **Intermedio Favorable (Criterio S3):**")
            st.write(t["rec_as_extended"])
        elif risk_result == "Intermediate":
            st.warning("⚠️ **Riesgo Intermedio:** Radioterapia o Prostatectomía.")
        else:
            st.error("🔴 **Alto Riesgo:** Terapia Multimodal (RP+LND o EBRT+ADT).")
            

# --- RESULTADOS M1 (METASTÁSICO) ---
else:
    st.header(f"Estadio M1 - {m_state}")
    
    # mHSPC LOGIC
    if m_state == "mHSPC":
        vol_text = "Alto Volumen (High Volume)" if is_high_volume else "Bajo Volumen (Low Volume)"
        st.subheader(f"Clasificación: {vol_text}")
        
        col1, col2 = st.columns(2)
        with col1:
            if is_high_volume:
                st.error(t["rec_mhspc_high"])
                
            else:
                st.success(t["rec_mhspc_low"])
                st.info("💡 **Nota:** La RT al primario es crucial en bajo volumen.")
        
    # mCRPC LOGIC
    else:
        st.subheader(t["rec_mcrpc_header"])
        st.write(f"**Terapia Previa:** {prior_therapy}")
        
        st.markdown("---")
        
        # Algoritmo de Decisión mCRPC
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 1. Cambio de Mecanismo")
            if "Docetaxel" in prior_therapy:
                st.info("Paciente ya recibió Taxano en mHSPC.")
                st.write("➡️ **Opción:** Cabazitaxel ($25 mg/m^2$) o Lu-177.")
            elif "ARPI" in prior_therapy:
                st.info("Paciente progresó a ARPI (Enza/Abi).")
                st.write("➡️ **Estándar:** Docetaxel ($75 mg/m^2$).")
                st.error("⛔ No dar otro ARPI (resistencia cruzada).")
            else:
                st.success("➡️ **Opción:** Enzalutamida o Abiraterona (si no usados antes).")
        
        with col2:
            st.markdown("### 2. Teragnosis (PSMA)")
            st.write(t["rec_mcrpc_lutetium"])
            
        
        with col3:
            st.markdown("### 3. Medicina de Precisión")
            st.write(t["rec_mcrpc_parp"])
            st.warning("🧬 Requiere test genético germinal/somático.")

# --- 6. Visualización Mermaid (Dinámica) ---
st.markdown("---")
st.subheader("Visual Pathway")

mermaid_code = "graph TD\n"

if disease_extent == "Localized/Locally Advanced (M0)":
    mermaid_code += f'Start[Diagnose] --> Risk{{{risk_result}}}\n'
    if "AS Possible" in risk_result or risk_result == "Low":
        mermaid_code += f'Risk --> AS["Active Surveillance (S3: PSA<15/Gl6)"]\n'
    else:
        mermaid_code += f'Risk --> Tx["Curative Therapy (RP/EBRT)"]\n'
else:
    if m_state == "mHSPC":
        vol_str = "HighVolume" if is_high_volume else "LowVolume"
        mermaid_code += f'Start[mHSPC] --> Vol{{{vol_str}}}\n'
        mermaid_code += f'Vol -->|High| Triple["Triple Tx (ADT+Chemo+ARPI)"]\n'
        mermaid_code += f'Vol -->|Low| Double["Doublet (ADT+ARPI) + Prostate RT"]\n'
    else: # mCRPC
        mermaid_code += f'Start[mCRPC] --> Prev{{"Prev: {prior_therapy}"}}\n'
        if "ARPI" in prior_therapy:
            mermaid_code += f'Prev --> Chemo["Docetaxel 75mg"]\n'
        elif "Docetaxel" in prior_therapy:
            mermaid_code += f'Prev --> Cab["Cabazitaxel 25mg"]\n'
        else:
            mermaid_code += f'Prev --> ARPI["Enza/Abi"]\n'
            
        mermaid_code += f'Prev -.->|PSMA+| Lu["Lu-177 (6x)"]\n'
        mermaid_code += f'Prev -.->|BRCA+| PARP["Olaparib"]\n'

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
