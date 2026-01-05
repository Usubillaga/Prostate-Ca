import streamlit as st
import streamlit.components.v1 as components

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Prostate Cancer Algorithm 2025",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Translations & Content Dictionary ---
translations = {
    "English": {
        "title": "Prostate Cancer Algorithm (EAU / S3 Guidelines 2025)",
        "sidebar_title": "Configuration",
        "screening_note": "ℹ️ **Note:** DRE is critical for **Staging** (cT2 vs cT3) but questionable for **Screening** (PROBASE study).",

        # Labels
        "extent_label": "Clinical Phase",
        "psa_label": "PSA Level (ng/ml)",
        "psad_label": "PSA Density (ng/ml/cc)",
        "pirads_label": "mpMRI PIRADS Score",
        "isup_label": "ISUP Grade (Gleason)",
        "tstage_label": "Clinical T-Stage",
        "n_stage_label": "N-Stage (Regional Nodes)",
        "meta_state_label": "Metastatic State",
        "psadt_label": "PSA Doubling Time (months)",
        "primary_tx_label": "Primary Therapy Received",
        "recurrence_time_label": "Time to Recurrence (months)",
        
        # Options
        "extent_opts": ["Diagnosis (Biopsy Decision)", "Localized (cT1-2 N0)", "Locally Advanced (cT3-4 or cN1)", "Biochemical Recurrence (BCR)", "Metastatic (M1)"],
        "pirads_opts": ["PIRADS 1-2", "PIRADS 3", "PIRADS 4-5"],
        "n_stages": ["cN0 (Nodes Negative)", "cN1 (Regional Nodes Positive)"],
        "m_states": ["mHSPC (Hormone Sensitive)", "mCRPC (Castration Resistant)"],
        "prior_opts": ["ADT Only", "ADT + Docetaxel", "ADT + ARPI", "Triple Therapy"],
        "primary_tx_opts": ["Radical Prostatectomy (RP)", "Radiotherapy (EBRT)"],

        # --- DIAGNOSIS (New from Flowchart) ---
        "header_diag": "Diagnosis: Biopsy Decision",
        "rec_diag_biopsy": """
        🔴 **Perform Biopsy**
        *Reason:* PIRADS 4-5 OR PIRADS 3 with High Risk factors.
        - **Method:** Transperineal biopsy (1st choice) or Transrectal.
        """,
        "rec_diag_consider": """
        🟡 **Consider Biopsy**
        *Reason:* PIRADS 3 with PSAD 0.10-0.20.
        - **Action:** Discuss risk/benefit. Perform if PSAD $\ge$ 0.20 or high clinical suspicion.
        """,
        "rec_diag_obs": """
        🟢 **Observation / Follow-up**
        *Reason:* PIRADS 1-2 or PIRADS 3 with low PSAD (<0.10).
        - **Action:** PSA monitoring. No immediate biopsy.
        """,

        # --- LOCALIZED ---
        "header_local": "Localized Disease (cT1-2 cN0)",
        "rec_as_extended": """
        **Active Surveillance (AS)**
        *Guideline Variation:*
        - **EAU:** Strict PSA < 10 ng/ml.
        - **S3 Germany:** PSA $\le$ 15 ng/ml (ISUP 1, cT1c/2a, <50% cores) is eligible.
        - **Protocol:** PSA q3-6mo, DRE q12mo, Re-biopsy/MRI at 12-18mo.
        """,
        "rec_curative": """
        **Standard Curative Therapy**
        - **Surgery:** Radical Prostatectomy (RP) + ePLND.
        - **Radiotherapy:** IMRT/VMAT ($74$-$80$ Gy) + Short-term ADT (4-6 mo).
        """,
        "rec_multi_high": """
        **High Risk Localized**
        - **Radiotherapy:** Dose-escalated + **Long-term ADT** (2-3 years).
        - **Surgery:** RP + Extended ePLND (Multimodal).
        """,

        # --- LOCALLY ADVANCED ---
        "header_la": "Locally Advanced (cT3-4 or cN1)",
        "rec_la_cn0": """
        **Locally Advanced (cT3-4 cN0)**
        *High Risk Protocol:*
        - **Standard:** EBRT (Prostate + SV) + **Long-term ADT** (2-3 years).
        - **Surgery:** RP only in multimodal setting.
        """,
        "rec_la_cn1": """
        **Regional Nodal Disease (cN1)**
        *STAMPEDE Protocol (High Risk M0):*
        1. **ADT:** Continuous (3 years).
        2. **Radiotherapy:** Prostate + Whole Pelvis.
        3. **Abiraterone:** $1000$ mg OD + Prednisone $5$ mg.
           - *Duration:* 2 years.
        
        ⚠️ **Approval Note:**
        - 🇪🇺 **EMA:** Abiraterone approved for mHSPC. Use in cN1/M0 is Level 1 evidence (STAMPEDE) but label may vary.
        - 🇩🇪 **Germany:** Often **Off-Label** for M0. Request reimbursement (Kostenübernahme).
        """,

        # --- BCR ---
        "header_bcr": "Biochemical Recurrence (BCR)",
        "rec_bcr_rp": """
        **Post-RP Recurrence (PSA > 0.2)**
        - **Diagnostic:** PSMA-PET/CT recommended.
        - **Therapy:** Salvage RT (Prostate Bed) +/- Pelvic Nodes.
        - **ADT:** Add Short-term ADT (6mo) if PSA >0.6 (GETUG-AFU 16).
        """,
        "rec_bcr_embark": """
        🔴 **High Risk BCR (EMBARK / EAU High Risk)**
        *Criteria: PSADT < 9 months (EMBARK) or PSADT < 1y (EAU).*
        
        **Therapy:**
        - **Enzalutamide** ($160$ mg OD) + ADT (Leuprolide).
        
        ✅ **Approval:**
        - 🇪🇺 **EMA:** Enzalutamide approved for High-Risk BCR (2024).
        """,
        "rec_bcr_low": """
        🟢 **Low Risk BCR (EAU)**
        *Criteria: PSADT > 1 year AND ISUP < 4.*
        - **Action:** Observation (Monitoring) or Salvage RT.
        """,

        # --- mHSPC ---
        "header_mhspc": "Metastatic Hormone-Sensitive (mHSPC)",
        "rec_mhspc_high": """
        🔴 **High Volume / High Risk**
        *Visceral Mets OR $\ge$4 Bone Mets*
        
        **Standard: Triple Therapy**
        1. **ADT** (Continuous).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (6 cycles).
        3. **ARPI:**
           - **Darolutamide:** $600$ mg BID[cite: 95].
           - *OR* **Abiraterone:** $1000$ mg OD + Prednisone[cite: 105].
        
        ✅ **Approvals:**
        - 🇪🇺 **Darolutamide:** Approved mHSPC + Docetaxel (ARASENS).
        - 🇪🇺 **Abiraterone:** Approved High Risk mHSPC (LATITUDE).
        """,
        "rec_mhspc_low": """
        🟢 **Low Volume**
        
        **Standard: Doublet + Local RT**
        1. **ADT** + **ARPI** (Enzalutamide / Apalutamide).
        2. **Prostate RT:** 55 Gy / 20 Fx (STAMPEDE H)[cite: 28].
        
        ⛔ **Don't:** No Docetaxel for Low Volume (toxicity > benefit).
        
        ✅ **Approvals:**
        - 🇪🇺 **Enzalutamide:** $160$ mg OD (ARCHES)[cite: 67].
        - 🇪🇺 **Apalutamide:** $240$ mg OD (TITAN)[cite: 50].
        """,

        # --- mCRPC ---
        "header_mcrpc": "Metastatic Castration-Resistant (mCRPC)",
        "rec_mcrpc_chemo": """
        **Chemotherapy Options**
        - **Docetaxel:** $75 \\text{ mg/m}^2$ q3w OR $50 \\text{ mg/m}^2$ q2w (PROSTY Trial - less toxicity)[cite: 106].
        - **Cabazitaxel:** $25 \\text{ mg/m}^2$ q3w (2nd line or post-Doc)[cite: 55].
        """,
        "rec_mcrpc_parp": """
        **PARP Inhibitors (BRCA1/2 Mutation)** [cite: 52, 108]
        - **Olaparib:** $300$ mg BID.
        - **Talazoparib:** $0.5$ mg OD.
        ✅ 🇪🇺 Approved.
        """,
        "rec_mcrpc_lutetium": """
        **Radioligand Therapy (PSMA+)** [cite: 110]
        - **Lu-177-PSMA-617:** $7.4$ GBq q6w (6 cycles).
        ✅ 🇪🇺 Approved post-ARPI & Chemo (VISION).
        """,
        "rec_mcrpc_pembro": """
        **Immunotherapy (MSI-High / dMMR)** 
        - **Pembrolizumab:** $200$ mg q3w.
        ✅ 🇪🇺 Approved for MSI-H solid tumors.
        """,
        "rec_mcrpc_ra223": """
        **Radium-223 (Bone Only)** 
        - **Dosis:** $55$ kBq/kg q4w (6 injections).
        - *Contraindication:* Visceral metastases.
        """
    },

    "Deutsch": {
        "title": "Prostatakarzinom Algorithmus (EAU / S3-Leitlinie 2025)",
        "sidebar_title": "Konfiguration",
        "screening_note": "ℹ️ **Hinweis:** DRU ist für das **Staging** (cT2 vs cT3) wichtig, für das **Screening** (PROBASE) jedoch umstritten.",

        "extent_label": "Krankheitsphase",
        "psa_label": "PSA-Wert (ng/ml)",
        "psad_label": "PSA-Dichte (ng/ml/cc)",
        "pirads_label": "mpMRT PIRADS",
        "isup_label": "ISUP Grad",
        "tstage_label": "Klinisches T-Stadium",
        "n_stage_label": "N-Stadium (Regionär)",
        "meta_state_label": "Metastasen-Status",
        "psadt_label": "PSA-Verdopplungszeit (Monate)",
        "primary_tx_label": "Primärtherapie",
        "recurrence_time_label": "Zeit bis Rezidiv (Monate)",

        "extent_opts": ["Diagnose (Biopsie-Entscheidung)", "Lokalisiert (cT1-2 N0)", "Lokal Fortgeschritten (cT3-4 oder cN1)", "Biochemisches Rezidiv (BCR)", "Metastasiert (M1)"],
        "pirads_opts": ["PIRADS 1-2", "PIRADS 3", "PIRADS 4-5"],
        "n_stages": ["cN0 (Knoten Negativ)", "cN1 (Knoten Positiv)"],
        "m_states": ["mHSPC (Hormonsensitiv)", "mCRPC (Kastrationsresistent)"],
        "prior_opts": ["Nur ADT", "ADT + Docetaxel", "ADT + ARPI", "Tripel-Therapie"],
        "primary_tx_opts": ["Radikale Prostatektomie (RP)", "Strahlentherapie (EBRT)"],

        "header_diag": "Diagnose: Biopsie-Indikation",
        "rec_diag_biopsy": """
        🔴 **Biopsie durchführen**
        *Grund:* PIRADS 4-5 ODER PIRADS 3 mit Risikofaktoren.
        - **Methode:** Transperineal (1. Wahl) oder Transrektal[cite: 31].
        """,
        "rec_diag_consider": """
        🟡 **Biopsie erwägen**
        *Grund:* PIRADS 3 mit PSAD 0,10-0,20.
        - **Vorgehen:** Abwägung. Bei PSAD $\ge$ 0,20 dringliche Biopsie[cite: 27].
        """,
        "rec_diag_obs": """
        🟢 **Beobachtung**
        *Grund:* PIRADS 1-2 oder PIRADS 3 mit PSAD <0,10.
        - **Vorgehen:** PSA-Kontrolle. Keine sofortige Biopsie[cite: 12].
        """,

        "header_local": "Lokalisiertes Stadium (cT1-2 cN0)",
        "rec_as_extended": """
        **Aktive Überwachung (AS)**
        *S3-Leitlinie Besonderheit:*
        - **Kriterium:** PSA $\le$ 15 ng/ml (ISUP 1, cT1c/2a) in DE möglich (EAU <10).
        - **Protokoll:** PSA alle 3-6 Mon, DRU 1x/Jahr, Re-Biopsie/MRT nach 12-18 Mon.
        """,
        "rec_curative": """
        **Kurative Standardtherapie**
        - **OP:** Radikale Prostatektomie + LAE.
        - **RT:** IMRT/VMAT ($74$-$80$ Gy) + Kurzzeit-ADT (4-6 Mon).
        """,
        "rec_multi_high": """
        **Hochrisiko Lokalisiert**
        - **RT:** Dosis-eskaliert + **Langzeit-ADT** (2-3 Jahre).
        - **OP:** RP + ausgedehnte LAE (Multimodal).
        """,

        "header_la": "Lokal Fortgeschritten (cT3-4 oder cN1)",
        "rec_la_cn0": """
        **Lokal Fortgeschritten (cT3-4 cN0)**
        *High Risk Protokoll:*
        - **Standard:** EBRT (Prostata + SB) + **Langzeit-ADT** (2-3 Jahre).
        - **OP:** RP nur im multimodalen Setting.
        """,
        "rec_la_cn1": """
        **Regionär Nodal Positiv (cN1)**
        *STAMPEDE Protokoll (High Risk M0):*
        1. **ADT:** Kontinuierlich (3 Jahre).
        2. **Strahlentherapie:** Prostata + gesamtes Becken.
        3. **Abirateron:** $1000$ mg + Prednison $5$ mg.
           - *Dauer:* 2 Jahre.
        
        ⚠️ **Zulassungshinweis:**
        - 🇪🇺 **EMA:** Abirateron für mHSPC zugelassen.
        - 🇩🇪 **Deutschland:** cN1-Einsatz oft **Off-Label**. Kostenübernahmeantrag (Verweis auf STAMPEDE/S3) erforderlich.
        """,

        "header_bcr": "Biochemisches Rezidiv (BCR)",
        "rec_bcr_rp": """
        **Rezidiv nach RP (PSA > 0,2)**
        - **Diagnostik:** PSMA-PET/CT.
        - **Therapie:** Salvage-RT (Loge) +/- Lymphabfluss.
        - **ADT:** Kurzzeit-ADT (6 Mon) addieren, wenn PSA >0,6.
        """,
        "rec_bcr_embark": """
        🔴 **High Risk BCR (EMBARK / EAU High Risk)**
        *Kriterium: PSADT < 9 Monate (EMBARK) oder PSADT < 1 Jahr (EAU).*
        
        **Therapie:**
        - **Enzalutamid** ($160$ mg) + ADT[cite: 182].
        
        ✅ **Zulassung:**
        - 🇪🇺 **EMA:** Enzalutamide seit 2024 für High-Risk BCR zugelassen.
        """,
        "rec_bcr_low": """
        🟢 **Low Risk BCR (EAU)**
        *Kriterium: PSADT > 1 Jahr UND ISUP < 4.*
        - **Vorgehen:** Beobachtung (Monitoring) oder Salvage-RT[cite: 144].
        """,

        "header_mhspc": "Metastasiert Hormonsensitiv (mHSPC)",
        "rec_mhspc_high": """
        🔴 **Hohes Volumen / High Risk**
        *Viszerale Met. ODER $\ge$4 Knochenmet.*
        
        **Standard: Tripel-Therapie**
        1. **ADT** (Kontinuierlich).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (6 Zyklen).
        3. **ARPI:**
           - **Darolutamid:** $600$ mg 2x tgl[cite: 95].
           - *ODER* **Abirateron:** $1000$ mg + Prednison[cite: 105].
        
        ✅ **Zulassung:**
        - 🇪🇺 **Darolutamid:** Zugelassen für mHSPC + Docetaxel (ARASENS).
        - 🇪🇺 **Abirateron:** Zugelassen für High Risk mHSPC (LATITUDE).
        """,
        "rec_mhspc_low": """
        🟢 **Geringes Volumen**
        
        **Standard: Doublet + Lokaltherapie**
        1. **ADT** + **ARPI** (Enzalutamid / Apalutamida).
        2. **Prostata-RT:** 55 Gy / 20 Fx (STAMPEDE H)[cite: 28].
        
        ⛔ **Cave:** Kein Docetaxel bei Low Volume (Toxizität > Nutzen).
        
        ✅ **Zulassung:**
        - 🇪🇺 **Enzalutamid:** $160$ mg (ARCHES)[cite: 67].
        - 🇪🇺 **Apalutamida:** $240$ mg (TITAN)[cite: 50].
        """,

        "header_mcrpc": "Metastasiert Kastrationsresistent (mCRPC)",
        "rec_mcrpc_chemo": """
        **Chemotherapie Optionen**
        - **Docetaxel:** $75 \\text{ mg/m}^2$ q3w ODER $50 \\text{ mg/m}^2$ q2w (PROSTY-Studie)[cite: 106].
        - **Cabazitaxel:** $25 \\text{ mg/m}^2$ q3w (2. Linie)[cite: 55].
        """,
        "rec_mcrpc_parp": """
        **PARP-Inhibitoren (BRCA1/2 Mutation)** [cite: 52, 108]
        - **Olaparib:** $300$ mg 2x tgl.
        - **Talazoparib:** $0,5$ mg 1x tgl.
        ✅ 🇪🇺 Zugelassen.
        """,
        "rec_mcrpc_lutetium": """
        **Radioligandentherapie (PSMA+)** [cite: 110]
        - **Lu-177-PSMA-617:** $7,4$ GBq alle 6 Wochen.
        ✅ 🇪🇺 Zugelassen (VISION).
        """,
        "rec_mcrpc_pembro": """
        **Immuntherapie (MSI-High / dMMR)** 
        - **Pembrolizumab:** $200$ mg q3w.
        ✅ 🇪🇺 Zugelassen bei MSI-H.
        """,
        "rec_mcrpc_ra223": """
        **Radium-223 (Nur Knochen)** 
        - **Dosis:** $55$ kBq/kg alle 4 Wochen.
        - *Kontraindikation:* Viszerale Metastasen.
        """
    },
    
    "Español": {
        "title": "Algoritmo Cáncer de Próstata (Guía S3 / EAU 2025)",
        "sidebar_title": "Configuración",
        "screening_note": "ℹ️ **Nota:** El tacto rectal es crítico para el **Estadiaje** (cT2 vs cT3) pero cuestionable para **Tamizaje** (PROBASE).",

        "extent_label": "Fase de la Enfermedad",
        "psa_label": "Nivel de PSA (ng/ml)",
        "psad_label": "Densidad de PSA (ng/ml/cc)",
        "pirads_label": "Puntuación mpMRI PIRADS",
        "isup_label": "Grado ISUP",
        "tstage_label": "Estadio T Clínico",
        "n_stage_label": "Estadio N (Regional)",
        "meta_state_label": "Estado Metastásico",
        "psadt_label": "Tiempo Duplicación PSA (meses)",
        "primary_tx_label": "Terapia Primaria Recibida",
        "recurrence_time_label": "Tiempo hasta Recurrencia (meses)",

        "extent_opts": ["Diagnóstico (Decisión Biopsia)", "Localizado (cT1-2 N0)", "Localmente Avanzado (cT3-4 o cN1)", "Recurrencia Bioquímica (BCR)", "Metastásico (M1)"],
        "pirads_opts": ["PIRADS 1-2", "PIRADS 3", "PIRADS 4-5"],
        "n_stages": ["cN0 (Ganglios Negativos)", "cN1 (Ganglios Positivos)"],
        "m_states": ["mHSPC (Hormonosensible)", "mCRPC (Resistente a Castración)"],
        "prior_opts": ["Solo ADT", "ADT + Docetaxel", "ADT + ARPI", "Terapia Triple"],
        "primary_tx_opts": ["Prostatectomía Radical (PR)", "Radioterapia (EBRT)"],

        "header_diag": "Diagnóstico: Decisión de Biopsia",
        "rec_diag_biopsy": """
        🔴 **Realizar Biopsia**
        *Razón:* PIRADS 4-5 O PIRADS 3 con factores de riesgo.
        - **Método:** Transperineal (1ª elección) o Transrectal[cite: 31].
        """,
        "rec_diag_consider": """
        🟡 **Considerar Biopsia**
        *Razón:* PIRADS 3 con PSAD 0.10-0.20.
        - **Acción:** Discutir riesgo/beneficio. Biopsia si PSAD $\ge$ 0.20[cite: 27].
        """,
        "rec_diag_obs": """
        🟢 **Observación**
        *Razón:* PIRADS 1-2 o PIRADS 3 con PSAD <0.10.
        - **Acción:** Monitorización PSA. No biopsia inmediata[cite: 12].
        """,

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
        - **Radioterapia:** IMRT/VMAT ($74$-$80$ Gy) + ADT corto (4-6 m).
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
        - **ADT:** Añadir ADT corto (6m) si PSA >0.6.
        """,
        "rec_bcr_embark": """
        🔴 **BCR Alto Riesgo (EMBARK / EAU High Risk)**
        *Criterio: PSADT < 9 meses (EMBARK) o < 1 año (EAU).*
        
        **Terapia:**
        - **Enzalutamida** ($160$ mg OD) + ADT[cite: 182].
        
        ✅ **Aprobación:**
        - 🇪🇺 **EMA:** Enzalutamida aprobada para BCR Alto Riesgo (2024).
        """,
        "rec_bcr_low": """
        🟢 **BCR Bajo Riesgo (EAU)**
        *Criterio: PSADT > 1 año Y ISUP < 4.*
        - **Acción:** Observación o RT de Rescate[cite: 144].
        """,

        "header_mhspc": "Metastásico Hormonosensible (mHSPC)",
        "rec_mhspc_high": """
        🔴 **Alto Volumen / Alto Riesgo**
        *Mets Viscerales O $\ge$4 Mets Óseas*
        
        **Estándar: Terapia Triple**
        1. **ADT** (Continuo).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (6 ciclos).
        3. **ARPI:**
           - **Darolutamida:** $600$ mg BID[cite: 95].
           - *O* **Abiraterona:** $1000$ mg OD + Prednisona[cite: 105].
        
        ✅ **Aprobaciones:**
        - 🇪🇺 **Darolutamida:** Aprobada mHSPC + Docetaxel (ARASENS).
        - 🇪🇺 **Abiraterona:** Aprobada Alto Riesgo mHSPC (LATITUDE).
        """,
        "rec_mhspc_low": """
        🟢 **Bajo Volumen**
        
        **Estándar: Doble + RT Local**
        1. **ADT** + **ARPI** (Enzalutamida / Apalutamida).
        2. **RT Próstata:** 55 Gy / 20 Fx (STAMPEDE H)[cite: 28].
        
        ⛔ **No:** Evitar Docetaxel (toxicidad > beneficio).
        
        ✅ **Aprobaciones:**
        - 🇪🇺 **Enzalutamida:** $160$ mg (ARCHES)[cite: 67].
        - 🇪🇺 **Apalutamida:** $240$ mg (TITAN)[cite: 50].
        """,

        "header_mcrpc": "Metastásico Resistente a Castración (mCRPC)",
        "rec_mcrpc_chemo": """
        **Opciones Quimioterapia**
        - **Docetaxel:** $75 \\text{ mg/m}^2$ q3w O $50 \\text{ mg/m}^2$ q2w (PROSTY - menos toxicidad)[cite: 106].
        - **Cabazitaxel:** $25 \\text{ mg/m}^2$ q3w (2ª línea)[cite: 55].
        """,
        "rec_mcrpc_parp": """
        **Inhibidores PARP (Mutación BRCA1/2)** [cite: 52, 108]
        - **Olaparib:** $300$ mg BID.
        - **Talazoparib:** $0.5$ mg OD.
        ✅ 🇪🇺 Aprobado.
        """,
        "rec_mcrpc_lutetium": """
        **Terapia Radioligandos (PSMA+)** [cite: 110]
        - **Lu-177-PSMA-617:** $7.4$ GBq q6w (6 ciclos).
        ✅ 🇪🇺 Aprobado post-ARPI & Quimio (VISION).
        """,
        "rec_mcrpc_pembro": """
        **Inmunoterapia (MSI-High / dMMR)** 
        - **Pembrolizumab:** $200$ mg q3w.
        ✅ 🇪🇺 Aprobado MSI-H.
        """,
        "rec_mcrpc_ra223": """
        **Radium-223 (Solo Hueso)** 
        - **Dosis:** $55$ kBq/kg c/4sem.
        - *Contraindicación:* Metástasis viscerales.
        """
    }
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
    Logic: High Risk vs Low Risk BCR
    """
    is_high_grade = (isup_idx >= 3) # ISUP 4 or 5
    
    if primary == "Radical Prostatectomy (RP)":
        # Post-RP: Low Risk if PSADT > 1y AND ISUP < 4
        if psadt > 12 and not is_high_grade: return "rec_bcr_low"
        else: return "rec_bcr_embark"
    else:
        # Post-RT: Low Risk if Interval > 18m AND ISUP < 4
        if interval > 18 and not is_high_grade: return "rec_bcr_low"
        else: return "rec_bcr_embark"

def calculate_risk_local(psa, isup_idx, t_idx):
    # ISUP 0=Gleason6. T-Stage: 0=T1c, 1=T2a, 2=T2b, 3=T2c, 4=T3a...
    isup = isup_idx + 1
    
    # High Risk
    if psa > 20 or isup >= 4 or t_idx >= 4: return "rec_multi_high"
    # Intermediate
    elif (psa >= 10) or (isup == 2 or isup == 3) or (t_idx >= 2):
        if psa <= 15 and isup == 1 and t_idx <= 1: return "rec_as_extended" # S3 AS
        return "rec_curative"
    # Low
    else: return "rec_as_extended"

# --- 4. UI ---
with st.sidebar:
    st.header("🌐 Language")
    lang_key = st.selectbox("Select", ["English", "Deutsch", "Español"])
    t = translations[lang_key]
    
    st.markdown("---")
    st.header(t["sidebar_title"])
    
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
        if "Radiotherapy" in primary_tx:
            recurrence_time = st.number_input(t["recurrence_time_label"], value=12)
            
    # --- E. METASTATIC ---
    elif disease_extent == t["extent_opts"][4]:
        st.subheader("Metastatic Details")
        m_state = st.radio(t["meta_state_label"], t["m_states"])
        is_high_vol = False
        msi_high = False
        if m_state == t["m_states"][0]: # mHSPC
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
    
    if res_key == "rec_diag_biopsy": st.error(t[res_key])
    elif res_key == "rec_diag_consider": st.warning(t[res_key])
    else: st.success(t[res_key])
        
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
    # Calc Logic
    idx_isup = ["ISUP 1", "ISUP 2", "ISUP 3", "ISUP 4", "ISUP 5"].index(in_isup)
    idx_t = ["cT1c", "cT2a", "cT2b", "cT2c"].index(in_tstage)
    res_key = calculate_risk_local(in_psa, idx_isup, idx_t)
    
    if res_key == "rec_multi_high": st.error(t[res_key])
    elif res_key == "rec_curative": st.warning(t[res_key])
    else: st.success(t[res_key])
    
    mermaid_code = "graph TD\nStart --> Risk{Risk Calc} --> " + ("Multi[Multimodal]" if res_key=="rec_multi_high" else "Single[AS or Curative]")

# 3. LOCALLY ADVANCED
elif disease_extent == t["extent_opts"][2]:
    st.header("Locally Advanced")
    if n_stage == t["n_stages"][1]: # cN1
        st.error(t["rec_la_cn1"])
        mermaid_code = "graph TD\nStart --> cN1 --> STAMPEDE[ADT + RT + Abiraterone]"
    else:
        st.warning(t["rec_la_cn0"])
        mermaid_code = "graph TD\nStart --> cN0 --> HR[EBRT + 2-3y ADT]"

# 4. BCR
elif disease_extent == t["extent_opts"][3]:
    st.header(t["header_bcr"])
    
    isup_idx = ["ISUP 1", "ISUP 2", "ISUP 3", "ISUP 4", "ISUP 5"].index(in_isup)
    
    # 1. EMBARK Check (Overriding)
    if psadt < 9:
        st.error(t["rec_bcr_embark"])
        mermaid_code = "graph TD\nStart --> Embark[Enzalutamide + ADT]"
    else:
        # 2. EAU Risk
        risk_key = get_bcr_risk(primary_tx, psadt, isup_idx, recurrence_time)
        if risk_key == "rec_bcr_embark": 
            st.warning(t["rec_bcr_embark"])
            mermaid_code = "graph TD\nStart --> HighRisk --> EarlySalvage"
        else:
            st.success(t[risk_key])
            mermaid_code = "graph TD\nStart --> LowRisk --> Obs[Observation/Salvage]"

# 5. METASTATIC
elif disease_extent == t["extent_opts"][4]:
    if m_state == t["m_states"][0]: # mHSPC
        st.header("mHSPC")
        if is_high_vol:
            st.error(t["rec_mhspc_high"])
            mermaid_code = "graph TD\nmHSPC --> Vol{High Volume}\nVol --> Triple[Triple Therapy]"
        else:
            st.success(t["rec_mhspc_low"])
            mermaid_code = "graph TD\nmHSPC --> Vol{Low Volume}\nVol --> Double[Doublet + RT]"
    else: # mCRPC
        st.header(t["header_mcrpc"])
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### Standard")
            st.info(t["rec_mcrpc_chemo"])
        with c2:
            st.markdown("### Precision")
            st.write(t["rec_mcrpc_parp"])
            st.write(t["rec_mcrpc_lutetium"])
            if msi_high: st.error(t["rec_mcrpc_pembro"])
            st.write(t["rec_mcrpc_ra223"])
            
        mermaid_code = f"""
        graph TD
        mCRPC --> Options
        Options --> Chemo[Docetaxel/Cabazitaxel]
        Options --> PARP[Olaparib/Talazoparib]
        Options --> Lu177[PSMA-Lu]
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
