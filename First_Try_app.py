import streamlit as st
import streamlit.components.v1 as components

# --- 1. Configuración de la Página ---
st.set_page_config(
    page_title="Prostate Cancer Algorithm 2026",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Traducciones y Contenido ---
translations = {
    "English": {
        "title": "Prostate Cancer Treatment Algorithm (EAU/S3 2026)",
        "description": "Clinical Decision Support based on **EAU Guidelines 2025** and **German S3-Leitlinie (v8.1)**.",
        "sidebar_title": "Patient Configuration",
        "rec_title": "Therapy Recommendations",
        "dos_donts_title": "✅ Dos & ⛔ Don'ts",
        "approval_title": "Zulassung (Approval & Reimbursement)",
        
        # Etiquetas
        "genetic_label": "Genetic Testing Results",
        "extent_label": "Disease Extent",
        "psa_label": "PSA Level (ng/ml)",
        "isup_label": "ISUP Grade (Gleason)",
        "tstage_label": "Clinical T-Stage",
        "n_stage_label": "N-Stage (Regional Nodes)",
        "meta_state_label": "Metastatic State",
        "volume_label": "Disease Volume (CHAARTED)",
        "psadt_label": "PSA Doubling Time (PSADT)",
        "primary_tx_label": "Prior Primary Therapy",
        
        # Opciones
        "isup_opts": ["ISUP 1 (Gleason 6)", "ISUP 2 (Gleason 3+4)", "ISUP 3 (Gleason 4+3)", "ISUP 4 (Gleason 8)", "ISUP 5 (Gleason 9-10)"],
        "t_opts": ["cT1", "cT2a", "cT2b", "cT2c", "cT3", "cT4"],
        "n_stages": ["cN0 (Nodes Negative)", "cN1 (Regional Nodes Positive)"],
        "m_states": ["mHSPC (Hormone Sensitive)", "mCRPC (Castration Resistant)"],
        "volumes": ["Low Volume", "High Volume (Visceral or ≥4 bone mets)"],
        "primary_tx_opts": ["Radical Prostatectomy (RP)", "Radiotherapy (EBRT)"],
        
        # Contenido - Localizado
        "rec_low": """
        **Active Surveillance (AS)**
        - **Protocol:** PSA every 6mo, DRE annually, mpMRI re-staging at 12-18mo.
        - **Biopsy:** Confirmatory biopsy if MRI changes or PSA density >0.15.
        """,
        "dos_low": """
        ✅ **Do:** Adhere strictly to re-biopsy schedules.
        ⛔ **Don't:** Offer AS to patients with **BRCA2** mutations without discussing increased risk of upgrading (consider RP).
        """,
        
        # Contenido - Localmente Avanzado
        "rec_la_cn0": """
        **Locally Advanced cT3-4 cN0 (High Risk)**
        *Multimodal therapy is mandatory.*
        
        **Option A: Radiotherapy (Preferred for older/comorbid)**
        - **EBRT:** IMRT/VMAT dose-escalated ($74$-$80$ Gy) to prostate/seminal vesicles.
        - **ADT:** Long-term ADT (LHRH agonist/antagonist) for **2-3 years**.
        
        **Option B: Surgery (Selected Patients)**
        - **RP:** Radical Prostatectomy + ePLND (extended lymph node dissection).
        - **Adjuvant:** Likely need for adjuvant/salvage RT +/- ADT based on pathology (pT3, R1, pN+).
        """,
        "rec_la_cn1": """
        **Locally Advanced cN1 (Regional Nodal Disease)**
        *STAMPEDE / High-Risk Protocol*
        
        1. **ADT:** Continuous LHRH agonist/antagonist for **3 years**.
        2. **Radiotherapy:** EBRT to Prostate + Whole Pelvis ($46$-$50$ Gy pelvic, boost prostate to $74$+ Gy).
        3. **Abiraterone:** $1000$ mg OD + Prednisone $5$ mg OD for **2 years**.
        """,
        "dos_la": """
        ✅ **Do:** Discuss Abiraterone addition for cN1 (Level 1 Evidence: STAMPEDE).
        ✅ **Do:** Perform staging with **PSMA-PET/CT** if available (superior sensitivity for M1).
        ⛔ **Don't:** Perform monotherapy (Surgery only or RT only) for cT3-4 disease.
        """,
        "approval_la": """
        🇪🇺 **EMA:** Abiraterone approved for mHSPC, but label varies for M0/cN1.
        🇩🇪 **Germany:** Use of Abiraterone in M0/cN1 is based on STAMPEDE but is **Off-Label**. Apply for reimbursement (Kostenübernahme).
        """,
        
        # BCR
        "rec_bcr_rp": """
        **Post-RP Recurrence (PSA >0.2 ng/ml)**
        - **Diagnostics:** Perform **PSMA-PET/CT** (PSA >0.2 is threshold for detection).
        - **Salvage RT:** Radiation to prostate bed +/- pelvic nodes.
        - **ADT Addition:**
            - PSA <0.7: sRT alone often sufficient.
            - PSA >0.7 or High Grade: Add Short-term ADT (6 mo).
        """,
        "rec_bcr_rt": """
        **Post-RT Recurrence (Nadir + 2 ng/ml)**
        - **Diagnostics:** PSMA-PET/CT + Prostate Biopsy mandatory to confirm local recurrence vs distant.
        - **Therapy:** Local Salvage (RP, HIFU, Cryo, Brachy) only for highly selected patients. Systemic ADT is standard.
        """,
        "rec_bcr_high_risk": """
        **High Risk BCR (EMBARK Definition)**
        - *Criteria:* PSADT < 9 months.
        - **Therapy:** **Enzalutamide** ($160$ mg) + ADT (Leuprolide) showed superior MFS vs ADT alone.
        - **Zulassung:** Enzalutamide approved (FDA/EMA) for High-Risk BCR.
        """,
        
        # mHSPC
        "rec_mhspc_high": """
        **High Volume mHSPC (Triple Therapy)**
        - **Standard:** ADT + **Docetaxel** ($75$ $\\text{mg/m}^2$ x6) + **Abiraterone** OR **Darolutamide**.
        - **Approvals:** - Darolutamide (ARASENS).
          - Abiraterone (PEACE-1).
        """,
        "rec_mhspc_low": """
        **Low Volume mHSPC (Doublet Therapy)**
        - **Systemic:** ADT + ARPI.
        - **Local:** **Radiotherapy to Prostate** (55Gy/20fx) improves Survival (STAMPEDE Arm H).
        - **Options:**
          - **Apalutamide:** $240$ mg OD (TITAN).
          - **Enzalutamide:** $160$ mg OD (ARCHES/ENZAMET).
          - **Abiraterone:** $1000$ mg + Pred (LATITUDE - High Risk).
        """,
        "approval_mhspc": """
        ✅ **Apalutamide (TITAN):** Approved for mHSPC (regardless of volume).
        ✅ **Enzalutamide (ARCHES):** Approved for mHSPC.
        ✅ **Darolutamide:** Approved for mHSPC in combo with Docetaxel.
        ⚠️ **Abiraterone:** Approved for *High Risk* mHSPC (LATITUDE). Low volume use may be off-label in DE.
        """,
        
        # mCRPC
        "rec_mcrpc": """
        **mCRPC Sequence**
        - **Target:** Change mechanism of action (e.g., ADT+Chemo $\\rightarrow$ ARPI).
        - **Precision:** - **BRCA1/2:** Olaparib ($300$mg BID) or Talazoparib.
          - **PSMA+:** Lu-177-PSMA-617 ($7.4$ GBq).
        """,
        "dos_mcrpc": """
        ⛔ **Don't:** Give Enzalutamide after Abiraterone (cross-resistance). Switch to Taxane or Lutetium.
        """
    },
    
    "Deutsch": {
        "title": "Prostatakarzinom Behandlungsalgorithmus",
        "description": "Klinische Entscheidungshilfe basierend auf **EAU 2025** und **Deutscher S3-Leitlinie (v8.1)**.",
        "sidebar_title": "Konfiguration",
        "rec_title": "Therapieempfehlungen",
        "dos_donts_title": "Dos & Don'ts",
        "approval_title": "Zulassung & Erstattung",
        
        "genetic_label": "Genetik",
        "extent_label": "Stadium / Situation",
        "psadt_label": "PSA-Verdopplungszeit (PSADT)",
        "primary_tx_label": "Primärtherapie",
        
        "isup_opts": ["ISUP 1 (Gleason 6)", "ISUP 2 (Gleason 3+4)", "ISUP 3 (Gleason 4+3)", "ISUP 4 (Gleason 8)", "ISUP 5 (Gleason 9-10)"],
        "t_opts": ["cT1", "cT2a", "cT2b", "cT2c", "cT3", "cT4"],
        "n_stages": ["cN0 (Knoten negativ)", "cN1 (Regionäre Knoten positiv)"],
        "m_states": ["mHSPC (Hormonsensitiv)", "mCRPC (Kastrationsresistent)"],
        "volumes": ["Geringes Volumen", "Hohes Volumen (Viszeral od. ≥4 Knochenmet.)"],
        "primary_tx_opts": ["Radikale Prostatektomie (RP)", "Strahlentherapie (EBRT)"],

        "rec_low": """
        **Aktive Überwachung (AS)**
        - **Protokoll:** PSA alle 6 Mon, DRE jährlich, mpMRT alle 12-18 Mon.
        - **Biopsie:** Bei PSA-Dichte >0,15 oder MRT-Progress.
        """,
        "dos_low": """
        ✅ **Ja:** Konsequente Re-Biopsien.
        ⛔ **Nein:** AS bei **BRCA2** ohne Aufklärung über hohes Risiko (RP bevorzugen).
        """,

        "rec_la_cn0": """
        **Lokal Fortgeschritten cT3-4 cN0 (High Risk)**
        *Multimodale Therapie obligatorisch.*
        
        **Option A: Strahlentherapie (Präferenz Ältere)**
        - **EBRT:** IMRT/VMAT Prostata/Samenblasen ($74$-$80$ Gy).
        - **ADT:** Langzeit-ADT für **2-3 Jahre**.
        
        **Option B: OP (Selektioniert)**
        - **RP:** Prostatektomie + ePLND.
        - **Adjuvant:** Oft adjuvante/Salvage RT nötig.
        """,
        "rec_la_cn1": """
        **Lokal Fortgeschritten cN1 (Regionäre Knoten)**
        *STAMPEDE Protokoll*
        
        1. **ADT:** 3 Jahre.
        2. **RT:** Prostata + Beckenlymphabfluss ($50$ Gy Becken, Boost Prostata).
        3. **Abirateron:** $1000$ mg + Prednison für **2 Jahre**.
        """,
        "dos_la": """
        ✅ **Ja:** Abirateron bei cN1 evaluieren (Level 1 Evidenz).
        ✅ **Ja:** **PSMA-PET/CT** zum Staging (Ausschluss M1).
        ⛔ **Nein:** Monotherapie (nur OP oder nur RT) bei cT3/4.
        """,
        "approval_la": """
        🇪🇺 **EMA:** Abirateron Label deckt nicht explizit M0/cN1 ab.
        🇩🇪 **Deutschland:** Einsatz bei cN1 ist **Off-Label**. Kostenübernahmeantrag empfohlen.
        """,

        "rec_bcr_rp": """
        **Rezidiv nach RP (PSA >0,2 ng/ml)**
        - **Diagnostik:** **PSMA-PET/CT** (empfohlen ab PSA >0,2).
        - **Salvage-RT:** Bestrahlung Loge +/- Becken.
        - **ADT:** Hinzufügen (6 Mon) wenn PSA >0,7 oder ISUP >3.
        """,
        "rec_bcr_rt": """
        **Rezidiv nach RT (Nadir + 2)**
        - **Diagnostik:** PSMA-PET + Biopsie zwingend zur Sicherung.
        - **Therapie:** Lokale Salvage (RP/HIFU) nur in Expertenzentren. Sonst ADT.
        """,
        "rec_bcr_high_risk": """
        **Hochrisiko-BCR (EMBARK)**
        - *Kriterium:* PSADT < 9 Monate.
        - **Therapie:** **Enzalutamid** + ADT zeigte überlegenes MFS.
        - **Zulassung:** Enzalutamid ist für Hochrisiko-BCR zugelassen.
        """,

        "rec_mhspc_high": """
        **Hohes Volumen mHSPC (Triple)**
        - **Standard:** ADT + **Docetaxel** + **Abirateron** ODER **Darolutamide**.
        - **Zulassung:** Darolutamid (ARASENS), Abirateron (PEACE-1).
        """,
        "rec_mhspc_low": """
        **Geringes Volumen mHSPC (Doublet)**
        - **Systemisch:** ADT + ARPI.
        - **Lokal:** **RT der Prostata** verbessert Überleben (STAMPEDE H).
        - **Optionen:**
          - **Apalutamid:** $240$ mg (TITAN).
          - **Enzalutamid:** $160$ mg (ARCHES).
          - **Abirateron:** $1000$ mg (LATITUDE - High Risk).
        """,
        "approval_mhspc": """
        ✅ **Apalutamide:** Zugelassen für mHSPC (unabhängig vom Volumen).
        ✅ **Enzalutamide:** Zugelassen für mHSPC.
        ✅ **Darolutamide:** Zugelassen für mHSPC (+Docetaxel).
        ⚠️ **Abirateron:** Zugelassen für *High Risk* mHSPC. Einsatz bei Low Volume/Low Risk formal Off-Label.
        """,

        "rec_mcrpc": """
        **mCRPC Sequenz**
        - **Prinzip:** Wirkmechanismus ändern.
        - **Präzision:** - **BRCA1/2:** Olaparib/Talazoparib.
          - **PSMA+:** Lu-177-PSMA-617.
        """,
        "dos_mcrpc": """
        ⛔ **Nein:** Enzalutamid nach Abirateron (Kreuzresistenz). Wechsel auf Taxan oder Lutetium.
        """
    },
    
    "Español": {
        "title": "Algoritmo de Tratamiento Cáncer de Próstata (2026)",
        "description": "Herramienta de decisión clínica basada en **Guías EAU 2025** y **S3-Leitlinie (v8.1)**.",
        "sidebar_title": "Configuración del Paciente",
        "rec_title": "Recomendaciones Terapéuticas",
        "dos_donts_title": "✅ Recomendaciones y ⛔ Precauciones",
        "approval_title": "Zulassung (Aprobación y Reembolso)",
        
        "genetic_label": "Resultados Genéticos",
        "extent_label": "Estadio de la Enfermedad",
        "psa_label": "Nivel de PSA (ng/ml)",
        "isup_label": "Grado ISUP (Gleason)",
        "tstage_label": "Estadio Clínico T",
        "n_stage_label": "Estadio N (Ganglios Regionales)",
        "meta_state_label": "Estado Metastásico",
        "volume_label": "Volumen de Enfermedad (CHAARTED)",
        "psadt_label": "Tiempo de Duplicación PSA (PSADT)",
        "primary_tx_label": "Terapia Primaria Previa",
        
        "isup_opts": ["ISUP 1 (Gleason 6)", "ISUP 2 (Gleason 3+4)", "ISUP 3 (Gleason 4+3)", "ISUP 4 (Gleason 8)", "ISUP 5 (Gleason 9-10)"],
        "t_opts": ["cT1", "cT2a", "cT2b", "cT2c", "cT3", "cT4"],
        "n_stages": ["cN0 (Ganglios Negativos)", "cN1 (Ganglios Regionales Positivos)"],
        "m_states": ["mHSPC (Hormonosensible)", "mCRPC (Resistente a Castración)"],
        "volumes": ["Bajo Volumen", "Alto Volumen (Visceral o ≥4 met. óseas)"],
        "primary_tx_opts": ["Prostatectomía Radical (PR)", "Radioterapia (EBRT)"],

        "rec_low": """
        **Vigilancia Activa (AS)**
        - **Protocolo:** PSA cada 6 meses, tacto rectal anual, mpMRI a los 12-18 meses.
        - **Biopsia:** Confirmatoria si hay cambios en MRI o densidad de PSA >0.15.
        """,
        "dos_low": """
        ✅ **Hacer:** Adherirse estrictamente a los programas de re-biopsia.
        ⛔ **No Hacer:** Ofrecer AS a pacientes con mutaciones **BRCA2** sin discutir el alto riesgo de progresión (considerar PR).
        """,

        "rec_la_cn0": """
        **Localmente Avanzado cT3-4 cN0 (Alto Riesgo)**
        *La terapia multimodal es obligatoria.*
        
        **Opción A: Radioterapia (Preferida en mayores/comorbilidades)**
        - **EBRT:** IMRT/VMAT con escalada de dosis ($74$-$80$ Gy) a próstata/vesículas seminales.
        - **ADT:** Terapia de privación androgénica a largo plazo por **2-3 años**.
        
        **Opción B: Cirugía (Pacientes Seleccionados)**
        - **PR:** Prostatectomía Radical + ePLND (linfadenectomía extendida).
        - **Adyuvancia:** Probable necesidad de RT adyuvante/rescate +/- ADT según patología.
        """,
        "rec_la_cn1": """
        **Localmente Avanzado cN1 (Enfermedad Nodal Regional)**
        *Protocolo STAMPEDE / Alto Riesgo*
        
        1. **ADT:** Agonista/antagonista LHRH continuo por **3 años**.
        2. **Radioterapia:** EBRT a Próstata + Pelvis completa ($46$-$50$ Gy pelvis, boost a próstata $74$+ Gy).
        3. **Abiraterona:** $1000$ mg OD + Prednisona $5$ mg OD por **2 años**.
        """,
        "dos_la": """
        ✅ **Hacer:** Discutir la adición de Abiraterona para cN1 (Evidencia Nivel 1: STAMPEDE).
        ✅ **Hacer:** Realizar estadificación con **PSMA-PET/CT** si está disponible (sensibilidad superior para M1).
        ⛔ **No Hacer:** Monoterapia (solo cirugía o solo RT) para enfermedad cT3-4.
        """,
        "approval_la": """
        🇪🇺 **EMA:** Abiraterona aprobada para mHSPC, pero la etiqueta varía para M0/cN1.
        🇩🇪 **Alemania:** El uso en M0/cN1 se basa en STAMPEDE pero es técnicamente **Off-Label**. Solicitar reembolso.
        """,

        "rec_bcr_rp": """
        **Recurrencia post-PR (PSA >0.2 ng/ml)**
        - **Diagnóstico:** Realizar **PSMA-PET/CT** (PSA >0.2 es el umbral de detección).
        - **RT de Rescate:** Radiación al lecho prostático +/- ganglios pélvicos.
        - **Adición de ADT:**
            - PSA <0.7: RT de rescate sola suele ser suficiente.
            - PSA >0.7 o Alto Grado: Añadir ADT a corto plazo (6 meses).
        """,
        "rec_bcr_rt": """
        **Recurrencia post-RT (Nadir + 2 ng/ml)**
        - **Diagnóstico:** PSMA-PET/CT + Biopsia de próstata obligatoria para confirmar recurrencia local vs distante.
        - **Terapia:** Rescate Local (PR, HIFU, Crio, Braqui) solo para pacientes muy seleccionados. ADT sistémica es el estándar.
        """,
        "rec_bcr_high_risk": """
        **BCR de Alto Riesgo (Definición EMBARK)**
        - *Criterio:* PSADT < 9 meses.
        - **Terapia:** **Enzalutamida** ($160$ mg) + ADT mostró MFS superior vs ADT sola.
        - **Aprobación:** Enzalutamida aprobada (FDA/EMA) para BCR de Alto Riesgo.
        """,

        "rec_mhspc_high": """
        **mHSPC de Alto Volumen (Terapia Triple)**
        - **Estándar:** ADT + **Docetaxel** ($75$ $\\text{mg/m}^2$ x6) + **Abiraterona** O **Darolutamida**.
        - **Aprobaciones:** - Darolutamida (ARASENS).
          - Abiraterona (PEACE-1).
        """,
        "rec_mhspc_low": """
        **mHSPC de Bajo Volumen (Terapia Doble)**
        - **Sistémico:** ADT + ARPI.
        - **Local:** **Radioterapia a la Próstata** (55Gy/20fx) mejora la Supervivencia (STAMPEDE Arm H).
        - **Opciones:**
          - **Apalutamida:** $240$ mg OD (TITAN).
          - **Enzalutamida:** $160$ mg OD (ARCHES).
          - **Abiraterona:** $1000$ mg + Pred (LATITUDE - Alto Riesgo).
        """,
        "approval_mhspc": """
        ✅ **Apalutamida (TITAN):** Aprobada para mHSPC (independientemente del volumen).
        ✅ **Enzalutamida (ARCHES):** Aprobada para mHSPC.
        ✅ **Darolutamida:** Aprobada para mHSPC en combinación con Docetaxel.
        ⚠️ **Abiraterona:** Aprobada para mHSPC de *Alto Riesgo*. El uso en bajo volumen puede ser off-label en DE.
        """,

        "rec_mcrpc": """
        **Secuencia mCRPC**
        - **Objetivo:** Cambiar mecanismo de acción (ej. ADT+Quimio $\\rightarrow$ ARPI).
        - **Precisión:** - **BRCA1/2:** Olaparib ($300$mg BID) o Talazoparib.
          - **PSMA+:** Lu-177-PSMA-617 ($7.4$ GBq).
        """,
        "dos_mcrpc": """
        ⛔ **No Hacer:** Dar Enzalutamida después de Abiraterona (resistencia cruzada). Cambiar a Taxano o Lutecio.
        """
    }
}

t_opts_map = ["Localized (cT1-2)", "Locally Advanced (cT3-4 / cN1)", "Biochemical Recurrence (BCR)", "Metastatic (M1)"]
gen_opts = ["Not Performed/Negative", "BRCA1/2 Positive", "HRR Other Positive", "MMR Deficient"]

# --- 3. Funciones Auxiliares ---
def calculate_risk_group(psa, isup_index, t_stage_index):
    isup = isup_index + 1
    if psa > 20 or isup >= 4 or t_stage_index >= 3: return "high"
    elif (psa >= 10) or (isup == 2 or isup == 3) or (t_stage_index == 2): return "int"
    else: return "low"

def q(text):
    return f'"{text}"'

# --- 4. Lógica de la Barra Lateral ---
with st.sidebar:
    st.header("⚙️ Configuration")
    lang_choice = st.selectbox("Language / Sprache / Idioma", ["English", "Deutsch", "Español"])
    t = translations[lang_choice]
    st.markdown("---")
    
    genetic_status = st.selectbox(t["genetic_label"], gen_opts)
    disease_extent = st.selectbox(t["extent_label"], t_opts_map)
    
    # Inputs Condicionales
    calc_risk_key = None
    n_stage = None
    m_state = None
    volume = None
    psadt = None
    primary_tx = None
    
    if disease_extent == t_opts_map[0]: # Localizado
        st.subheader("Calculator")
        in_psa = st.number_input(t["psa_label"], value=5.0, step=0.1)
        in_isup = st.selectbox(t["isup_label"], t["isup_opts"])
        in_tstage = st.selectbox(t["tstage_label"], t["t_opts"])
        isup_idx = t["isup_opts"].index(in_isup)
        t_idx = t["t_opts"].index(in_tstage)
        calc_risk_key = calculate_risk_group(in_psa, isup_idx, t_idx)
        
    elif disease_extent == t_opts_map[1]: # Localmente Avanzado
        st.subheader("Staging")
        n_stage = st.radio(t["n_stage_label"], t["n_stages"])
        
    elif disease_extent == t_opts_map[2]: # BCR
        st.subheader("Recurrence Details")
        primary_tx = st.radio(t["primary_tx_label"], t["primary_tx_opts"])
        psadt = st.number_input(t["psadt_label"] + " (months)", value=10.0, step=1.0)

    elif disease_extent == t_opts_map[3]: # Metastásico
        st.subheader("Metastatic Details")
        m_state = st.radio(t["meta_state_label"], t["m_states"])
        if m_state == t["m_states"][0]:
            volume = st.radio(t["volume_label"], t["volumes"])

# --- 5. Contenido Principal ---
st.title(t["title"])
st.markdown(t["description"])

# --- A. LOCALIZADO ---
if disease_extent == t_opts_map[0]:
    st.subheader(t["rec_title"])
    if calc_risk_key == "low":
        st.info(t["rec_low"])
        st.success(t["dos_low"])
    else:
        st.warning("**Intermediate/High Risk:** Radical Prostatectomy (RP) or EBRT+ADT.")

# --- B. LOCALMENTE AVANZADO ---
elif disease_extent == t_opts_map[1]:
    st.header(t_opts_map[1])
    st.subheader(t["rec_title"])
    
    # Lógica Split: cN0 vs cN1
    if n_stage == t["n_stages"][1]: # cN1
        st.error(t["rec_la_cn1"])
        st.markdown(f"#### {t['dos_donts_title']}")
        st.success(t["dos_la"])
        st.markdown("---")
        st.warning(f"⚖️ {t['approval_la']}")
    else: # cN0 High Risk
        st.warning(t["rec_la_cn0"])
        st.info("✅ **Tip:** PSMA-PET is highly recommended for T3/T4.")

# --- C. BIOCHEMICAL RECURRENCE (BCR) ---
elif disease_extent == t_opts_map[2]:
    st.header(t_opts_map[2])
    
    # High Risk BCR (EMBARK) Check
    if psadt < 9.0:
        st.error(t["rec_bcr_high_risk"])
    
    # Post-RP vs Post-RT
    if primary_tx == t["primary_tx_opts"][0]: # RP
        st.info(t["rec_bcr_rp"])
    else: # RT
        st.warning(t["rec_bcr_rt"])
        
    st.success("✅ **Zulassung:** Enzalutamide is approved for High Risk BCR (PSADT <9 mo) with or without ADT.")

# --- D. METASTÁSICO ---
elif disease_extent == t_opts_map[3]:
    if m_state == t["m_states"][0]: # mHSPC
        st.header("mHSPC Management")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.info(t["approval_mhspc"])
        with col2:
            if volume == t["volumes"][1]: # High
                st.error(t["rec_mhspc_high"])
            else: # Low
                st.success(t["rec_mhspc_low"])
    else: # mCRPC
        st.header("mCRPC Management")
        st.info(t["rec_mcrpc"])
        st.warning(t["dos_mcrpc"])

# --- 6. Flujo Visual Mermaid ---
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
        mermaid_code += f'NStage -->|cN0| Multi["Multimodal: EBRT+LongADT or RP"]\n'

elif disease_extent == t_opts_map[2]: # BCR
    mermaid_code += f'Gen --> BCR{{"Primary Tx?"}}\n'
    if primary_tx == t["primary_tx_opts"][0]:
        mermaid_code += f'BCR -->|Post-RP| sRT["Salvage RT +/- ADT"]\n'
    else:
        mermaid_code += f'BCR -->|Post-RT| Eval["Local Salvage (Selected) or ADT"]\n'
    
    if psadt < 9.0:
        mermaid_code += f'Eval -.->|High Risk PSADT<9| Embark["Enzalutamide + ADT"]\n'
        mermaid_code += f'sRT -.->|High Risk| Embark["Enzalutamide + ADT"]\n'

elif disease_extent == t_opts_map[3]:
    if m_state == t["m_states"][0]:
        mermaid_code += f'Gen --> Vol{{"Volume?"}}\n'
        if volume == t["volumes"][1]:
            mermaid_code += f'Vol -->|High| Triple["Triple: ADT + Chemo + ARPI"]\n'
        else:
            mermaid_code += f'Vol -->|Low| Double["Doublet: ADT + ARPI + RT"]\n'
            mermaid_code += f'Double --> Apa["Option: Apalutamide/Enza"]\n'

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
    height=500,
    scrolling=True
)
