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
        "screening_note": "ℹ️ **Note:** DRE is critical for **Staging** (cT2 vs cT3) but questionable for **Screening** (PROBASE).",

        # UI Labels
        "extent_label": "Disease Phase",
        "psa_label": "PSA Level (ng/ml)",
        "isup_label": "ISUP Grade",
        "tstage_label": "Clinical T-Stage",
        "n_stage_label": "N-Stage (Regional Nodes)",
        "meta_state_label": "Metastatic State",
        "psadt_label": "PSA Doubling Time (months)",
        "primary_tx_label": "Primary Therapy Received",
        
        # Options
        "extent_opts": ["Localized (cT1-2 N0 M0)", "Locally Advanced (cT3-4 or cN1)", "Biochemical Recurrence (BCR)", "Metastatic (M1)"],
        "n_stages": ["cN0 (Nodes Negative)", "cN1 (Regional Nodes Positive)"],
        "m_states": ["mHSPC (Hormone Sensitive)", "mCRPC (Castration Resistant)"],
        "prior_opts": ["ADT Only", "ADT + Docetaxel", "ADT + ARPI", "Triple Therapy"],
        "primary_tx_opts": ["Radical Prostatectomy (RP)", "Radiotherapy (EBRT)"],

        # --- CONTENT BLOCKS ---
        
        # 1. Localized
        "header_local": "Localized Disease (cT1-2 cN0)",
        "rec_as_extended": """
        **Active Surveillance (AS)**
        *S3 Guideline Variation:*
        - **Criteria:** PSA $\le$ 15 ng/ml (ISUP 1, cT1c/2a) is eligible in Germany (EAU strict <10).
        - **Protocol:** PSA q3-6mo, DRE q12mo, Re-biopsy/MRI at 12-18mo.
        """,
        "rec_curative": """
        **Standard Curative Therapy**
        - **Surgery:** Radical Prostatectomy (RP) + Lymph Node Dissection.
        - **Radiotherapy:** IMRT/VMAT ($74$-$80$ Gy) + Short-term ADT (4-6 mo) for Intermediate Risk.
        """,
        "rec_multi_high": """
        **High Risk Localized**
        - **Radiotherapy:** Dose-escalated + **Long-term ADT** (2-3 years).
        - **Surgery:** RP + Extended ePLND.
        """,

        # 2. Locally Advanced
        "header_la": "Locally Advanced (cT3-4 or cN1)",
        "rec_la_cn0": """
        **Locally Advanced (cT3-4 cN0)**
        *High Risk / Locally Advanced Protocol:*
        - **Standard:** EBRT (Prostate + SV) + **Long-term ADT** (2-3 years).
        - **Surgery:** RP only in multimodal setting (expect adjuvant RT).
        - 🇪🇺 **Approval:** ADT (GnRH agonists/antagonists) fully approved.
        """,
        "rec_la_cn1": """
        **Regional Nodal Disease (cN1)**
        *STAMPEDE Protocol (High Risk Non-Metastatic):*
        1. **ADT:** Continuous (3 years).
        2. **Radiotherapy:** Prostate + Whole Pelvis.
        3. **Abiraterone:** $1000$ mg OD + Prednisone $5$ mg.
           - *Duration:* 2 years.
        
        ⚠️ **Approval Note:**
        - 🇪🇺 **EMA:** Abiraterone approved for mHSPC. Use in cN1/M0 is based on Level 1 evidence (STAMPEDE) but label may vary.
        - 🇩🇪 **Germany:** Often considers cN1 usage **Off-Label**. Request reimbursement (Kostenübernahme).
        """,

        # 3. BCR
        "header_bcr": "Biochemical Recurrence",
        "rec_bcr_rp": """
        **Post-RP Recurrence (PSA > 0.2)**
        - **Diagnostic:** PSMA-PET/CT recommended.
        - **Therapy:** Salvage RT (Prostate Bed) +/- Pelvic Nodes.
        - **ADT:** Add Short-term ADT (6mo) if PSA >0.6 or ISUP >3 (GETUG-AFU 16).
        """,
        "rec_bcr_embark": """
        🔴 **High Risk BCR (EMBARK Trial)**
        *Criteria: PSADT < 9 months.*
        
        **Recommendation:**
        - **Enzalutamide** ($160$ mg OD) + ADT (Leuprolide).
        - *Outcome:* Superior Metastasis-Free Survival (MFS).
        
        ✅ **Approval:**
        - 🇪🇺 **EMA:** Enzalutamide approved for High-Risk BCR (2024).
        """,

        # 4. mHSPC
        "header_mhspc": "Metastatic Hormone-Sensitive (mHSPC)",
        "rec_mhspc_high": """
        🔴 **High Volume / High Risk**
        *Visceral Mets OR $\ge$4 Bone Mets*
        
        **Standard: Triple Therapy**
        1. **ADT** (Continuous).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (6 cycles).
        3. **ARPI:**
           - **Darolutamide:** $600$ mg BID.
           - *OR* **Abiraterone:** $1000$ mg OD + Prednisone.
        
        ✅ **Approvals:**
        - 🇪🇺 **Darolutamide:** Approved for mHSPC + Docetaxel (ARASENS).
        - 🇪🇺 **Abiraterone:** Approved for High Risk mHSPC (LATITUDE).
        """,
        "rec_mhspc_low": """
        🟢 **Low Volume**
        
        **Standard: Doublet + Local RT**
        1. **ADT** + **ARPI** (Enzalutamide / Apalutamide).
        2. **Prostate RT:** 55 Gy / 20 Fx (STAMPEDE H).
        
        ⛔ **Don't:** Do not use Docetaxel (toxicity > benefit).
        
        ✅ **Approvals:**
        - 🇪🇺 **Enzalutamide:** $160$ mg OD (ARCHES).
        - 🇪🇺 **Apalutamide:** $240$ mg OD (TITAN).
        """,

        # 5. mCRPC
        "header_mcrpc": "Metastatic Castration-Resistant (mCRPC)",
        "rec_mcrpc_chemo": """
        **Chemotherapy Options**
        
        **1. Docetaxel (Bi-weekly):**
        - **Dosis:** $50 \\text{ mg/m}^2$ every 2 weeks.
        - *Evidence:* **PROSTY Trial** (Kellokumpu-Lehtinen 2013) - comparable efficacy to 3-weekly, less toxicity.
        
        **2. Cabazitaxel:**
        - **Dosis:** $25 \\text{ mg/m}^2$ q3w.
        - *Setting:* 2nd line chemo or post-Docetaxel.
        """,
        "rec_mcrpc_parp": """
        **PARP Inhibitors (Precision Medicine)**
        *Requires BRCA1/2 Mutation*
        
        - **Olaparib:** $300$ mg BID (PROfound).
        - **Talazoparib:** $0.5$ mg OD (TALAPRO).
        
        ✅ **Approval:**
        - 🇪🇺 Approved for mCRPC post-ARPI (Olaparib) or 1st line mCRPC (Talazoparib+Enza).
        """,
        "rec_mcrpc_lutetium": """
        **Radioligand Therapy (Theranostics)**
        *Requires PSMA+ PET*
        
        - **Lu-177-PSMA-617:** $7.4$ GBq q6w (4-6 cycles).
        
        ✅ **Approval:**
        - 🇪🇺 Approved for pre-treated mCRPC (ARPI + Chemo) [VISION].
        """
    },

    "Deutsch": {
        "title": "Prostatakarzinom Algorithmus (S3-Leitlinie 2025 / EAU)",
        "sidebar_title": "Konfiguration",
        "screening_note": "ℹ️ **Hinweis:** DRU ist für das **Staging** (cT2 vs cT3) wichtig, für das **Screening** (PROBASE) jedoch umstritten.",

        "extent_label": "Krankheitsphase",
        "psa_label": "PSA-Wert (ng/ml)",
        "isup_label": "ISUP Grad",
        "tstage_label": "Klinisches T-Stadium",
        "n_stage_label": "N-Stadium (Regionär)",
        "meta_state_label": "Metastasen-Status",
        "psadt_label": "PSA-Verdopplungszeit (Monate)",
        "primary_tx_label": "Primärtherapie",

        "extent_opts": ["Lokalisiert (cT1-2 N0 M0)", "Lokal Fortgeschritten (cT3-4 oder cN1)", "Biochemisches Rezidiv (BCR)", "Metastasiert (M1)"],
        "n_stages": ["cN0 (Knoten Negativ)", "cN1 (Knoten Positiv)"],
        "m_states": ["mHSPC (Hormonsensitiv)", "mCRPC (Kastrationsresistent)"],
        "prior_opts": ["Nur ADT", "ADT + Docetaxel", "ADT + ARPI", "Tripel-Therapie"],
        "primary_tx_opts": ["Radikale Prostatektomie (RP)", "Strahlentherapie (EBRT)"],

        "header_local": "Lokalisiertes Stadium (cT1-2 cN0)",
        "rec_as_extended": """
        **Aktive Überwachung (AS)**
        *S3-Leitlinie Besonderheit:*
        - **Kriterium:** PSA $\le$ 15 ng/ml (ISUP 1, cT1c/2a) ist in DE möglich (EAU strikt <10).
        - **Protokoll:** PSA alle 3-6 Mon, DRU 1x/Jahr, Re-Biopsie/MRT nach 12-18 Mon.
        """,
        "rec_curative": """
        **Kurative Standardtherapie**
        - **OP:** Radikale Prostatektomie + LAE.
        - **RT:** IMRT/VMAT ($74$-$80$ Gy) + Kurzzeit-ADT (4-6 Mon) bei Intermediärem Risiko.
        """,
        "rec_multi_high": """
        **Hochrisiko Lokalisiert**
        - **RT:** Dosis-eskaliert + **Langzeit-ADT** (2-3 Jahre).
        - **OP:** RP + ausgedehnte LAE.
        """,

        "header_la": "Lokal Fortgeschritten (cT3-4 oder cN1)",
        "rec_la_cn0": """
        **Lokal Fortgeschritten (cT3-4 cN0)**
        *High Risk Protokoll:*
        - **Standard:** EBRT (Prostata + SB) + **Langzeit-ADT** (2-3 Jahre).
        - **OP:** RP nur im multimodalen Setting (hohe Wahrscheinlichkeit für adj. RT).
        - 🇪🇺 **Zulassung:** ADT voll zugelassen.
        """,
        "rec_la_cn1": """
        **Regionär Nodal Positiv (cN1)**
        *STAMPEDE Protokoll (High Risk M0):*
        1. **ADT:** Kontinuierlich (3 Jahre).
        2. **Strahlentherapie:** Prostata + gesamtes Becken.
        3. **Abirateron:** $1000$ mg + Prednison $5$ mg.
           - *Dauer:* 2 Jahre.
        
        ⚠️ **Zulassungshinweis:**
        - 🇪🇺 **EMA:** Abirateron für mHSPC zugelassen. cN1/M0 Status im Label nicht explizit genannt.
        - 🇩🇪 **Deutschland:** cN1-Einsatz oft **Off-Label**. Kostenübernahmeantrag (Verweis auf STAMPEDE/S3) erforderlich.
        """,

        "header_bcr": "Biochemisches Rezidiv (BCR)",
        "rec_bcr_rp": """
        **Rezidiv nach RP (PSA > 0,2)**
        - **Diagnostik:** PSMA-PET/CT.
        - **Therapie:** Salvage-RT (Loge) +/- Lymphabfluss.
        - **ADT:** Kurzzeit-ADT (6 Mon) addieren, wenn PSA >0,6 (GETUG-AFU 16).
        """,
        "rec_bcr_embark": """
        🔴 **High Risk BCR (EMBARK Studie)**
        *Kriterium: PSADT < 9 Monate.*
        
        **Empfehlung:**
        - **Enzalutamid** ($160$ mg) + ADT.
        - *Ergebnis:* Signifikant verlängertes MFS.
        
        ✅ **Zulassung:**
        - 🇪🇺 **EMA:** Enzalutamide seit 2024 für High-Risk BCR zugelassen.
        """,

        "header_mhspc": "Metastasiert Hormonsensitiv (mHSPC)",
        "rec_mhspc_high": """
        🔴 **Hohes Volumen / High Risk**
        *Viszerale Met. ODER $\ge$4 Knochenmet.*
        
        **Standard: Tripel-Therapie**
        1. **ADT** (Kontinuierlich).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (6 Zyklen).
        3. **ARPI:**
           - **Darolutamid:** $600$ mg 2x tgl.
           - *ODER* **Abirateron:** $1000$ mg + Prednison.
        
        ✅ **Zulassung:**
        - 🇪🇺 **Darolutamid:** Zugelassen für mHSPC + Docetaxel (ARASENS).
        - 🇪🇺 **Abirateron:** Zugelassen für High Risk mHSPC (LATITUDE).
        """,
        "rec_mhspc_low": """
        🟢 **Geringes Volumen**
        
        **Standard: Doublet + Lokaltherapie**
        1. **ADT** + **ARPI** (Enzalutamid / Apalutamid).
        2. **Prostata-RT:** 55 Gy / 20 Fx (STAMPEDE H).
        
        ⛔ **Cave:** Kein Docetaxel bei Low Volume (Toxizität > Nutzen).
        
        ✅ **Zulassung:**
        - 🇪🇺 **Enzalutamid:** $160$ mg (ARCHES).
        - 🇪🇺 **Apalutamide:** $240$ mg (TITAN).
        """,

        "header_mcrpc": "Metastasiert Kastrationsresistent (mCRPC)",
        "rec_mcrpc_chemo": """
        **Chemotherapie Optionen**
        
        **1. Docetaxel (2-Wochen-Schema):**
        - **Dosis:** $50 \\text{ mg/m}^2$ alle 2 Wochen.
        - *Evidenz:* **PROSTY-Studie** (Kellokumpu-Lehtinen 2013) - weniger Neutropenien bei gleicher Wirkung wie 3-Wochen-Schema.
        
        **2. Cabazitaxel:**
        - **Dosis:** $25 \\text{ mg/m}^2$ alle 3 Wochen.
        - *Indikation:* 2. Linie oder nach Docetaxel-Versagen.
        """,
        "rec_mcrpc_parp": """
        **PARP-Inhibitoren (Präzisionsmedizin)**
        *Nur bei BRCA1/2 Mutation*
        
        - **Olaparib:** $300$ mg 2x tgl (PROfound).
        - **Talazoparib:** $0,5$ mg 1x tgl (TALAPRO).
        
        ✅ **Zulassung:**
        - 🇪🇺 Zugelassen für mCRPC (Olaparib mono nach ARPI; Talazoparib+Enza 1. Linie).
        """,
        "rec_mcrpc_lutetium": """
        **Radioligandentherapie**
        *Nur bei PSMA+ PET*
        
        - **Lu-177-PSMA-617:** $7,4$ GBq alle 6 Wochen (4-6 Zyklen).
        
        ✅ **Zulassung:**
        - 🇪🇺 Zugelassen nach ARPI und Chemo (VISION).
        """
    },
    
    "Español": {
        "title": "Algoritmo Cáncer de Próstata (Guía S3 / EAU 2025)",
        "sidebar_title": "Configuración",
        "screening_note": "ℹ️ **Nota:** El tacto rectal es crítico para el **Estadiaje** (cT2 vs cT3) pero cuestionable para **Tamizaje** (PROBASE).",

        "extent_label": "Fase de la Enfermedad",
        "psa_label": "Nivel de PSA (ng/ml)",
        "isup_label": "Grado ISUP",
        "tstage_label": "Estadio T Clínico",
        "n_stage_label": "Estadio N (Regional)",
        "meta_state_label": "Estado Metastásico",
        "psadt_label": "Tiempo Duplicación PSA (meses)",
        "primary_tx_label": "Terapia Primaria Recibida",

        "extent_opts": ["Localizado (cT1-2 N0 M0)", "Localmente Avanzado (cT3-4 o cN1)", "Recurrencia Bioquímica (BCR)", "Metastásico (M1)"],
        "n_stages": ["cN0 (Ganglios Negativos)", "cN1 (Ganglios Positivos)"],
        "m_states": ["mHSPC (Hormonosensible)", "mCRPC (Resistente a Castración)"],
        "prior_opts": ["Solo ADT", "ADT + Docetaxel", "ADT + ARPI", "Terapia Triple"],
        "primary_tx_opts": ["Prostatectomía Radical (PR)", "Radioterapia (EBRT)"],

        "header_local": "Enfermedad Localizada (cT1-2 cN0)",
        "rec_as_extended": """
        **Vigilancia Activa (AS)**
        *Variación Guía S3:*
        - **Criterio:** PSA $\le$ 15 ng/ml (ISUP 1, cT1c/2a) es elegible en Alemania (EAU estricto <10).
        - **Protocolo:** PSA c/3-6m, Tacto c/12m, Re-biopsia/MRI a 12-18m.
        """,
        "rec_curative": """
        **Terapia Curativa Estándar**
        - **Cirugía:** Prostatectomía Radical (PR) + Linfadenectomía.
        - **Radioterapia:** IMRT/VMAT ($74$-$80$ Gy) + ADT corto (4-6 m) para Riesgo Intermedio.
        """,
        "rec_multi_high": """
        **Alto Riesgo Localizado**
        - **Radioterapia:** Dosis escalada + **ADT Largo** (2-3 años).
        - **Cirugía:** PR + Linfadenectomía Extendida.
        """,

        "header_la": "Localmente Avanzado (cT3-4 o cN1)",
        "rec_la_cn0": """
        **Localmente Avanzado (cT3-4 cN0)**
        *Protocolo Alto Riesgo:*
        - **Estándar:** EBRT (Próstata + VS) + **ADT Largo** (2-3 años).
        - **Cirugía:** PR solo en entorno multimodal.
        - 🇪🇺 **Aprobación:** ADT totalmente aprobado.
        """,
        "rec_la_cn1": """
        **Enfermedad Nodal Regional (cN1)**
        *Protocolo STAMPEDE (Alto Riesgo No Metastásico):*
        1. **ADT:** Continuo (3 años).
        2. **Radioterapia:** Próstata + Pelvis Completa.
        3. **Abiraterona:** $1000$ mg OD + Prednisona $5$ mg.
           - *Duración:* 2 años.
        
        ⚠️ **Nota Aprobación:**
        - 🇪🇺 **EMA:** Abiraterona aprobada mHSPC. Uso en cN1/M0 basado en Evidencia Nivel 1 (STAMPEDE).
        - 🇩🇪 **Alemania:** A menudo considera cN1 **Off-Label**. Solicitar reembolso.
        """,

        "header_bcr": "Recurrencia Bioquímica",
        "rec_bcr_rp": """
        **Recurrencia Post-PR (PSA > 0.2)**
        - **Diagnóstico:** PSMA-PET/CT recomendado.
        - **Terapia:** RT de Rescate (Lecho) +/- Ganglios.
        - **ADT:** Añadir ADT corto (6m) si PSA >0.6 o ISUP >3 (GETUG-AFU 16).
        """,
        "rec_bcr_embark": """
        🔴 **BCR Alto Riesgo (Estudio EMBARK)**
        *Criterio: PSADT < 9 meses.*
        
        **Recomendación:**
        - **Enzalutamida** ($160$ mg OD) + ADT.
        - *Resultado:* Sobrevida Libre de Metástasis superior.
        
        ✅ **Aprobación:**
        - 🇪🇺 **EMA:** Enzalutamida aprobada para BCR Alto Riesgo (2024).
        """,

        "header_mhspc": "Metastásico Hormonosensible (mHSPC)",
        "rec_mhspc_high": """
        🔴 **Alto Volumen / Alto Riesgo**
        *Mets Viscerales O $\ge$4 Mets Óseas*
        
        **Estándar: Terapia Triple**
        1. **ADT** (Continuo).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (6 ciclos).
        3. **ARPI:**
           - **Darolutamida:** $600$ mg BID.
           - *O* **Abiraterona:** $1000$ mg OD + Prednisona.
        
        ✅ **Aprobaciones:**
        - 🇪🇺 **Darolutamida:** Aprobada mHSPC + Docetaxel (ARASENS).
        - 🇪🇺 **Abiraterona:** Aprobada Alto Riesgo mHSPC (LATITUDE).
        """,
        "rec_mhspc_low": """
        🟢 **Bajo Volumen**
        
        **Estándar: Doble + RT Local**
        1. **ADT** + **ARPI** (Enzalutamida / Apalutamida).
        2. **RT Próstata:** 55 Gy / 20 Fx (STAMPEDE H).
        
        ⛔ **No:** Evitar Docetaxel (toxicidad > beneficio).
        
        ✅ **Aprobaciones:**
        - 🇪🇺 **Enzalutamida:** $160$ mg (ARCHES).
        - 🇪🇺 **Apalutamida:** $240$ mg (TITAN).
        """,

        "header_mcrpc": "Metastásico Resistente a Castración (mCRPC)",
        "rec_mcrpc_chemo": """
        **Opciones Quimioterapia**
        
        **1. Docetaxel (Esquema Bisemanal):**
        - **Dosis:** $50 \\text{ mg/m}^2$ cada 2 semanas.
        - *Evidencia:* **Estudio PROSTY** (Kellokumpu-Lehtinen 2013) - eficacia comparable al trisemanal, menos toxicidad.
        
        **2. Cabazitaxel:**
        - **Dosis:** $25 \\text{ mg/m}^2$ q3w.
        - *Escenario:* 2ª línea o tras Docetaxel.
        """,
        "rec_mcrpc_parp": """
        **Inhibidores PARP (Medicina Precisión)**
        *Requiere Mutación BRCA1/2*
        
        - **Olaparib:** $300$ mg BID (PROfound).
        - **Talazoparib:** $0.5$ mg OD (TALAPRO).
        
        ✅ **Aprobación:**
        - 🇪🇺 Aprobado para mCRPC post-ARPI (Olaparib) o 1ª línea (Talazoparib+Enza).
        """,
        "rec_mcrpc_lutetium": """
        **Terapia Radioligandos**
        *Requiere PSMA+ PET*
        
        - **Lu-177-PSMA-617:** $7.4$ GBq q6w (4-6 ciclos).
        
        ✅ **Aprobación:**
        - 🇪🇺 Aprobado post-ARPI y Quimio (VISION).
        """
    }
}

# --- 3. Sidebar UI & Logic ---
with st.sidebar:
    st.header("🌐 Language")
    lang_key = st.selectbox("Select", ["English", "Deutsch", "Español"])
    t = translations[lang_key]
    
    st.markdown("---")
    st.header(t["sidebar_title"])
    
    # 1. Extent Selection (Split Localized vs locally Advanced vs BCR)
    disease_extent = st.selectbox(t["extent_label"], t["extent_opts"])
    
    # Variables init
    risk_key = None
    is_cn1 = False
    psadt = 10
    m_state = None
    is_high_volume = False
    
    # --- A. LOCALIZED (cT1-2 N0) ---
    if disease_extent == t["extent_opts"][0]:
        st.subheader("Calculator")
        in_psa = st.number_input(t["psa_label"], value=6.0, step=0.5)
        in_isup = st.selectbox(t["isup_label"], ["ISUP 1", "ISUP 2", "ISUP 3", "ISUP 4", "ISUP 5"])
        in_tstage = st.selectbox(t["tstage_label"], ["cT1c", "cT2a", "cT2b", "cT2c"])
        
        # Risk Logic
        isup_val = int(in_isup.split(" ")[1])
        if in_psa > 20 or isup_val >= 4 or "cT2c" in in_tstage:
            risk_key = "high"
        elif in_psa >= 10 or isup_val >= 2 or "cT2b" in in_tstage:
            # German S3 Exception for AS
            if in_psa <= 15 and isup_val == 1: risk_key = "int_fav"
            else: risk_key = "int"
        else:
            risk_key = "low"
            
    # --- B. LOCALLY ADVANCED (cT3-4 or N1) ---
    elif disease_extent == t["extent_opts"][1]:
        st.subheader("Staging")
        n_stage = st.radio(t["n_stage_label"], t["n_stages"])
        is_cn1 = (n_stage == t["n_stages"][1])
        
    # --- C. BCR ---
    elif disease_extent == t["extent_opts"][2]:
        st.subheader("Details")
        primary_tx = st.radio(t["primary_tx_label"], t["primary_tx_opts"])
        psadt = st.number_input(t["psadt_label"], value=10.0, step=1.0)
        
    # --- D. METASTATIC ---
    elif disease_extent == t["extent_opts"][3]:
        st.subheader("Details")
        m_state = st.radio(t["meta_state_label"], t["m_states"])
        if m_state == t["m_states"][0]: # mHSPC
             visc = st.checkbox("Visceral Mets?")
             bone = st.number_input("Bone Mets", value=1)
             if visc or bone >= 4: is_high_volume = True

# --- 4. Main Content ---
st.title(t["title"])
st.info(t["screening_note"])

# --- OUTPUT A: LOCALIZED ---
if disease_extent == t["extent_opts"][0]:
    st.header(t["header_local"])
    col1, col2 = st.columns([1,2])
    with col1:
        
    with col2:
        if risk_key == "low" or risk_key == "int_fav":
            st.success(t["rec_as_extended"])
        elif risk_key == "int":
            st.warning(t["rec_curative"])
        else:
            st.error(t["rec_multi_high"])

# --- OUTPUT B: LOCALLY ADVANCED ---
elif disease_extent == t["extent_opts"][1]:
    st.header(t["header_la"])
    col1, col2 = st.columns([1,2])
    with col1:
        
    with col2:
        if is_cn1:
            st.error(t["rec_la_cn1"]) # STAMPEDE
        else:
            st.warning(t["rec_la_cn0"]) # High Risk Protocol

# --- OUTPUT C: BCR ---
elif disease_extent == t["extent_opts"][2]:
    st.header(t["header_bcr"])
    
    # EMBARK CHECK
    if psadt < 9.0:
        st.error(t["rec_bcr_embark"])
    
    st.markdown("---")
    if primary_tx == t["primary_tx_opts"][0]:
        st.info(t["rec_bcr_rp"])
    else:
        st.warning("**Post-RT:** PSMA-PET mandatory. Systemic ADT is standard.")

# --- OUTPUT D: METASTATIC ---
elif disease_extent == t["extent_opts"][3]:
    if m_state == t["m_states"][0]: # mHSPC
        st.header(t["header_mhspc"])
        col1, col2 = st.columns([1,1])
        with col1:
             
        with col2:
            if is_high_volume:
                st.error(t["rec_mhspc_high"])
            else:
                st.success(t["rec_mhspc_low"])
    else: # mCRPC
        st.header(t["header_mcrpc"])
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("### 1. Chemo")
            st.info(t["rec_mcrpc_chemo"]) # Docetaxel 50mg q2w
        with col2:
            st.markdown("### 2. PARP")
            st.warning(t["rec_mcrpc_parp"])
        with col3:
            st.markdown("### 3. PSMA-Lu")
            st.success(t["rec_mcrpc_lutetium"])

# --- 5. Mermaid Visual ---
st.markdown("---")
st.subheader("Visual Pathway")
mermaid_code = "graph TD\n"

if disease_extent == t["extent_opts"][0]:
    mermaid_code += f'Start --> Risk{{{risk_key}}}\n'
    if risk_key in ["low", "int_fav"]: mermaid_code += f'Risk --> AS["Active Surveillance"]\n'
    else: mermaid_code += f'Risk --> Curative["Surgery or EBRT"]\n'

elif disease_extent == t["extent_opts"][1]:
    mermaid_code += f'Start --> Node{{"cN1?"}}\n'
    mermaid_code += f'Node -->|Yes| Stampede["EBRT + ADT + Abiraterone"]\n'
    mermaid_code += f'Node -->|No| Multi["EBRT + Long ADT"]\n'

elif disease_extent == t["extent_opts"][2]:
    mermaid_code += f'Start --> PSADT{{"PSADT < 9mo?"}}\n'
    mermaid_code += f'PSADT -->|Yes| Embark["Enzalutamide + ADT"]\n'
    mermaid_code += f'PSADT -->|No| Std["Salvage RT or ADT"]\n'

elif disease_extent == t["extent_opts"][3]:
    if m_state == t["m_states"][0]:
         vol_str = "High" if is_high_volume else "Low"
         mermaid_code += f'Start[mHSPC] --> Vol{{{vol_str}}}\n'
         mermaid_code += f'Vol -->|High| Triple["Triple (ADT+Docetaxel+ARPI)"]\n'
         mermaid_code += f'Vol -->|Low| Double["Doublet + Prostate RT"]\n'
    else:
         mermaid_code += f'Start[mCRPC] --> Opts["Switch / Chemo / PSMA-Lu"]\n'

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
