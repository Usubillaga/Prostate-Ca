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
        "title": "Prostate Cancer Algorithm (EAU / S3 Guidelines 2025)",
        "sidebar_title": "Configuration",
        [span_2](start_span)"screening_note": "ℹ️ **Note:** DRE is critical for **Staging** (cT2 vs cT3) but questionable for **Screening** (PROBASE study)[span_2](end_span).",

        # Labels
        "extent_label": "Clinical Phase",
        "genetic_label": "Genetic Testing Results",
        "psa_label": "PSA Level (ng/ml)",
        "vol_label": "Prostate Volume (cc)",
        "psad_label": "PSA Density (ng/ml/cc)",
        "pirads_label": "mpMRI PIRADS Score",
        "isup_label": "ISUP Grade (Gleason)",
        "tstage_label": "Clinical T-Stage",
        "n_stage_label": "N-Stage (Regional Nodes)",
        "meta_state_label": "Metastatic State",
        "psadt_label": "PSA Doubling Time (months)",
        "primary_tx_label": "Primary Therapy Received",
        "recurrence_time_label": "Time to Recurrence (months)",
        
        # Rotterdam Specific
        "rotterdam_header": "Rotterdam Risk Calculator Inputs",
        "age_label": "Age (years)",
        "dre_label": "DRE Findings (Digital Rectal Exam)",
        "fam_hist_label": "Family History of PCa?",
        "prev_bx_label": "Previous Negative Biopsy?",
        "dre_opts": ["Normal", "Abnormal (Suspicious)"],
        
        # Options
        "extent_opts": ["Diagnosis (Biopsy Decision)", "Localized (cT1-2 N0)", "Locally Advanced (cT3-4 or cN1)", "Biochemical Recurrence (BCR)", "nmCRPC (M0 CRPC)", "Metastatic (M1)"],
        "genetic_opts": ["Not Performed/Unknown", "Negative", "BRCA1/2 Positive", "Other HRR Positive", "MSI-High / dMMR"],
        "pirads_opts": ["PIRADS 1-2", "PIRADS 3", "PIRADS 4-5"],
        "n_stages": ["cN0 (Nodes Negative)", "cN1 (Regional Nodes Positive)"],
        "m_states": ["mHSPC (Hormone Sensitive)", "mCRPC (Castration Resistant)"],
        "prior_opts": ["ADT Only", "ADT + Docetaxel", "ADT + ARPI", "Triple Therapy"],
        "primary_tx_opts": ["Radical Prostatectomy (RP)", "Radiotherapy (EBRT)"],

        # --- DIAGNOSIS ---
        "header_diag": "Diagnosis: Risk Stratification & Biopsy",
        "rotterdam_high": """
        🔴 **High Risk Profile (Rotterdam Criteria)**
        *Risk Factors:* Abnormal DRE, High PSA Density (>0.15), or Family History.
        - **Recommendation:** **mpMRI** is mandatory. [span_3](start_span)If PIRADS $\ge$ 3, perform **Biopsy**[span_3](end_span).
        """,
        "rotterdam_low": """
        🟢 **Low Risk Profile**
        *Normal DRE, Low PSA Density.*
        - **Recommendation:** Discuss MRI. If PIRADS 1-2, biopsy can likely be omitted (Safety Net: PSA monitoring).
        """,
        "rec_diag_biopsy": """
        🔴 **Perform Biopsy**
        - **[span_4](start_span)Method:** Transperineal (1st choice) or Transrectal[span_4](end_span).
        - **[span_5](start_span)Target:** Systematic + Targeted (fusion) for PIRADS $\ge$ 3[span_5](end_span).
        """,
        "rec_diag_consider": """
        🟡 **Consider Biopsy**
        - **Context:** PIRADS 3 with borderline risk.
        - **[span_6](start_span)Decision:** Driven by PSA Density ($\ge$ 0.10) and patient preference[span_6](end_span).
        """,
        "rec_diag_obs": """
        🟢 **Observation / Follow-up**
        - **Context:** Low probability of csPCa.
        - **Action:** PSA monitoring. [span_7](start_span)Avoid immediate biopsy to reduce overdiagnosis[span_7](end_span).
        """,

        # --- LOCALIZED ---
        "header_local": "Localized Disease (cT1-2 cN0)",
        "rec_as_extended": """
        **Active Surveillance (AS)**
        *Guideline Variation:*
        - **[span_8](start_span)EAU:** Strict PSA < 10 ng/ml[span_8](end_span).
        - **S3 Germany:** PSA $\le$ 15 ng/ml (ISUP 1, cT1c/2a, <50% cores) is eligible.
        - **Protocol:** PSA q3-6mo, DRE q12mo, Re-biopsy/MRI at 12-18mo.
        """,
        "rec_curative": """
        **Standard Curative Therapy**
        - **[span_9](start_span)Surgery:** Radical Prostatectomy (RP) + ePLND[span_9](end_span).
        - **Radiotherapy:** IMRT/VMAT ($74$-$80$ Gy) + Short-term ADT (4-6 mo).
        """,
        "rec_multi_high": """
        **High Risk Localized**
        - **[span_10](start_span)Radiotherapy:** Dose-escalated + **Long-term ADT** (2-3 years)[span_10](end_span).
        - **Surgery:** RP + Extended ePLND (Multimodal).
        """,

        # --- LOCALLY ADVANCED ---
        "header_la": "Locally Advanced (cT3-4 or cN1)",
        "rec_la_cn0": """
        **Locally Advanced (cT3-4 cN0)**
        *High Risk Protocol:*
        - **[span_11](start_span)Standard:** EBRT (Prostate + SV) + **Long-term ADT** (2-3 years)[span_11](end_span).
        - **Surgery:** RP only in multimodal setting.
        """,
        "rec_la_cn1": """
        **Regional Nodal Disease (cN1)**
        *STAMPEDE Protocol (High Risk M0):*
        1. **ADT:** Continuous (3 years).
        2. **Radiotherapy:** Prostate + Whole Pelvis.
        3. **[span_12](start_span)Abiraterone:** $1000$ mg OD + Prednisone $5$ mg[span_12](end_span).
           - *Duration:* 2 years.
        
        ⚠️ **Approval Note:**
        - 🇪🇺 **EMA:** Abiraterone approved for mHSPC. Use in cN1/M0 is Level 1 evidence (STAMPEDE) but label may vary.
        - 🇩🇪 **Germany:** Often **Off-Label** for M0. Request reimbursement (Kostenübernahme).
        """,

        # --- BCR ---
        "header_bcr": "Biochemical Recurrence (BCR)",
        "rec_bcr_rp": """
        **Post-RP Recurrence (PSA > 0.2)**
        - **[span_13](start_span)Diagnostic:** PSMA-PET/CT recommended[span_13](end_span).
        - **[span_14](start_span)Therapy:** Salvage RT (Prostate Bed) +/- Pelvic Nodes[span_14](end_span).
        - **[span_15](start_span)ADT:** Add Short-term ADT (6mo) if PSA >0.6 (GETUG-AFU 16)[span_15](end_span).
        """,
        "rec_bcr_embark": """
        🔴 **High Risk BCR (EMBARK / EAU High Risk)**
        *Criteria: PSADT < 9 months (EMBARK) or PSADT < 1y (EAU).*
        
        **Therapy:**
        - **[span_16](start_span)Enzalutamide** ($160$ mg OD) + ADT (Leuprolide)[span_16](end_span).
        
        ✅ **Approval:**
        - 🇪🇺 **EMA:** Enzalutamide approved for High-Risk BCR (2024).
        """,
        "rec_bcr_low": """
        🟢 **Low Risk BCR (EAU)**
        *Criteria: PSADT > 1 year AND ISUP < 4.*
        - **[span_17](start_span)Action:** Observation (Monitoring) or Salvage RT[span_17](end_span).
        """,

        # --- nmCRPC ---
        "header_nmcrpc": "Non-Metastatic CRPC (M0)",
        "crpc_criteria": """
        **[span_18](start_span)CRPC Definition (EAU)[span_18](end_span):**
        1. **Castrate Testosterone:** < 50 ng/dL (< 1.7 nmol/L).
        2. **Biochemical Progression:** 3 consecutive PSA rises, 1 week apart, PSA > 2.0 ng/mL.
        3. **No Distant Metastases:** Confirmed by conventional imaging (CT/Bone Scan).
        """,
        "rec_nmcrpc_high": """
        🔴 **High Risk nmCRPC (PSADT < 10 months)**
        *Standard of Care (Level 1 Evidence):*
        
        - **[span_19](start_span)Apalutamide:** $240$ mg OD (SPARTAN)[span_19](end_span).
        - **[span_20](start_span)Enzalutamide:** $160$ mg OD (PROSPER)[span_20](end_span).
        - **[span_21](start_span)Darolutamide:** $600$ mg BID (ARAMIS)[span_21](end_span).
        
        ✅ **Approval:** All three are fully approved (EMA/FDA) for high-risk nmCRPC.
        """,
        "rec_nmcrpc_low": """
        🟢 **Low Risk nmCRPC (PSADT > 10 months)**
        - **Recommendation:** Continue ADT. [span_22](start_span)Observation[span_22](end_span).
        - *Reason:* Benefit of ARPIs not clearly established in slow-growing disease.
        """,

        # --- BONE PROTECTION ---
        "bone_prot_mhspc": """
        🦴 **Bone Health (mHSPC)**
        *Goal: Prevent Osteoporosis/Fractures from ADT.*
        - **[span_23](start_span)Denosumab:** $60$ mg s.c. every 6 months[span_23](end_span).
        - **Zoledronic Acid:** $4$ mg i.v. annually (or q3-6mo).
        - *Note:* High-dose (120mg) is **NOT** standard for mHSPC unless specific high-risk/CRPC features exist.
        """,
        "bone_prot_mcrpc": """
        🦴 **SRE Prevention (mCRPC)**
        *Goal: Prevent Skeletal Related Events (Pathological fractures, cord compression).*
        - **[span_24](start_span)Denosumab (Xgeva):** $120$ mg s.c. every 4 weeks[span_24](end_span).
        - **[span_25](start_span)Zoledronic Acid:** $4$ mg i.v. every 3-4 weeks[span_25](end_span).
        - *Supplement:* Calcium + Vit D. Dental check mandatory.
        """,

        # --- mHSPC ---
        "header_mhspc": "Metastatic Hormone-Sensitive (mHSPC)",
        "rec_mhspc_high": """
        🔴 **High Volume / High Risk**
        *Visceral Mets OR $\ge$4 Bone Mets*
        
        **1st Line Standard: Triple Therapy**
        1. **[span_26](start_span)ADT** (Continuous)[span_26](end_span).
        2. **[span_27](start_span)Docetaxel:** $75 \\text{ mg/m}^2$ q3w (6 cycles) OR $50 \\text{ mg/m}^2$ q2w (PROSTY)[span_27](end_span).
        3. **ARPI:**
           - **[span_28](start_span)Darolutamide:** $600$ mg BID (ARASENS)[span_28](end_span).
           - *[span_29](start_span)OR* **Abiraterone:** $1000$ mg OD + Prednisone (PEACE-1)[span_29](end_span).
        
        ✅ **Approvals:**
        - 🇪🇺 **Darolutamide/Abiraterone:** Approved for mHSPC.
        """,
        "rec_mhspc_low": """
        🟢 **Low Volume**
        
        **1st Line Standard: Doublet + Local RT**
        1. **[span_30](start_span)ADT** + **ARPI** (Enzalutamide / Apalutamide)[span_30](end_span).
        2. **[span_31](start_span)Prostate RT:** 55 Gy / 20 Fx (STAMPEDE H)[span_31](end_span).
        
        ⛔ **Don't:** No Docetaxel for Low Volume (toxicity > benefit).
        
        ✅ **Approvals:**
        - 🇪🇺 **Enzalutamide/Apalutamide:** Approved.
        """,

        # --- mCRPC ---
        "header_mcrpc": "Metastatic Castration-Resistant (mCRPC)",
        
        "line1_naive": """
        **1st Line (ARPI-Naïve)**
        - **[span_32](start_span)Enzalutamide** or **Abiraterone**[span_32](end_span).
        - *Alternative:* Docetaxel if symptomatic/visceral crisis.
        """,
        
        "line1_post_arpi": """
        **1st/2nd Line (Post-ARPI Progression)**
        *Switch Mechanism! Do not use 2nd ARPI.*
        - **[span_33](start_span)Docetaxel:** $75 \\text{ mg/m}^2$ q3w OR $50 \\text{ mg/m}^2$ q2w (PROSTY)[span_33](end_span).
        """,
        
        "line2_post_doc": """
        **2nd/3rd Line (Post-Docetaxel)**
        - **[span_34](start_span)Cabazitaxel:** $25 \\text{ mg/m}^2$ q3w (CARD Trial)[span_34](end_span).
        - **[span_35](start_span)Lu-177-PSMA:** $7.4$ GBq q6w (if PSMA+)[span_35](end_span).
        - **[span_36](start_span)Olaparib:** $300$ mg BID (if BRCA+)[span_36](end_span).
        """,
        
        "rec_mcrpc_pembro": """
        **Immunotherapy (Any Line)**
        - **[span_37](start_span)Pembrolizumab:** $200$ mg q3w[span_37](end_span).
        - *Indication:* MSI-High / dMMR only.
        """,
        
        "rec_mcrpc_ra223": """
        **Bone-Targeted (3rd Line/Symptomatic)**
        - **[span_38](start_span)Radium-223:** $55$ kBq/kg q4w[span_38](end_span).
        - *Indication:* Symptomatic bone mets, NO visceral mets.
        """
    },

    "Deutsch": {
        "title": "Prostatakarzinom Algorithmus (EAU / S3-Leitlinie 2025)",
        "sidebar_title": "Konfiguration",
        "screening_note": "ℹ️ **Hinweis:** DRU ist für das **Staging** (cT2 vs cT3) wichtig, für das **Screening** (PROBASE) jedoch umstritten.",

        "extent_label": "Krankheitsphase",
        "genetic_label": "Genetische Testung (Keimbahn/Somatisch)",
        "psa_label": "PSA-Wert (ng/ml)",
        "vol_label": "Prostatavolumen (ml/cc)",
        "pirads_label": "mpMRT PIRADS",
        "isup_label": "ISUP Grad",
        "tstage_label": "Klinisches T-Stadium",
        "n_stage_label": "N-Stadium (Regionär)",
        "meta_state_label": "Metastasen-Status",
        "psadt_label": "PSA-Verdopplungszeit (Monate)",
        "primary_tx_label": "Primärtherapie",
        "recurrence_time_label": "Zeit bis Rezidiv (Monate)",
        
        "rotterdam_header": "Rotterdam Risiko-Kalkulator Inputs",
        "age_label": "Alter (Jahre)",
        "dre_label": "DRU Befund",
        "fam_hist_label": "Familienanamnese PCa?",
        "prev_bx_label": "Vorherige negative Biopsie?",
        "dre_opts": ["Normal", "Abnormal (Suspekt)"],

        "extent_opts": ["Diagnose (Rotterdam & Biopsie)", "Lokalisiert (cT1-2 N0)", "Lokal Fortgeschritten (cT3-4 oder cN1)", "Biochemisches Rezidiv (BCR)", "nmCRPC (M0 CRPC)", "Metastasiert (M1)"],
        "genetic_opts": ["Nicht durchgeführt/Unbekannt", "Negativ", "BRCA1/2 Positiv", "Andere HRR Positiv", "MSI-High / dMMR"],
        "pirads_opts": ["PIRADS 1-2", "PIRADS 3", "PIRADS 4-5"],
        "n_stages": ["cN0 (Knoten Negativ)", "cN1 (Knoten Positiv)"],
        "m_states": ["mHSPC (Hormonsensitiv)", "mCRPC (Kastrationsresistent)"],
        "prior_opts": ["Nur ADT (Naiv)", "ADT + Docetaxel", "ADT + ARPI", "Tripel-Therapie"],
        "primary_tx_opts": ["Radikale Prostatektomie (RP)", "Strahlentherapie (EBRT)"],

        "header_diag": "Diagnose: Risiko & Biopsie",
        "rotterdam_high": """
        🔴 **Hochrisiko-Profil (Rotterdam Kriterien)**
        *Risikofaktoren:* Suspekte DRU, Hohe PSA-Dichte (>0,15) oder Familienanamnese.
        - **Empfehlung:** **mpMRT** obligatorisch. Bei PIRADS $\ge$ 3 **Biopsie**.
        """,
        "rotterdam_low": """
        🟢 **Niedrigrisiko-Profil**
        *Normale DRU, Geringe PSA-Dichte.*
        - **Empfehlung:** MRT erwägen. Bei PIRADS 1-2 kann Biopsie ggf. unterbleiben (PSA-Monitoring).
        """,
        "rec_diag_biopsy": """
        🔴 **Biopsie durchführen**
        - **Methode:** Transperineal (1. Wahl) oder Transrektal.
        - **Ziel:** Systematisch + Gezielt (Fusion) bei PIRADS $\ge$ 3.
        """,
        "rec_diag_consider": """
        🟡 **Biopsie erwägen**
        - **Kontext:** PIRADS 3 mit Grenzbefunden.
        - **Entscheidung:** Abhängig von PSA-Dichte ($\ge$ 0,10) und Patientenwunsch.
        """,
        "rec_diag_obs": """
        🟢 **Beobachtung**
        - **Kontext:** Unwahrscheinliches Karzinom.
        - **Vorgehen:** PSA-Kontrolle. Keine sofortige Biopsie zur Vermeidung von Überdiagnose.
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
        - **Enzalutamid** ($160$ mg) + ADT.
        
        ✅ **Zulassung:**
        - 🇪🇺 **EMA:** Enzalutamide seit 2024 für High-Risk BCR zugelassen.
        """,
        "rec_bcr_low": """
        🟢 **Low Risk BCR (EAU)**
        *Kriterium: PSADT > 1 Jahr UND ISUP < 4.*
        - **Vorgehen:** Beobachtung (Monitoring) oder Salvage-RT.
        """,

        "header_nmcrpc": "Nicht-Metastasiertes CRPC (nmCRPC / M0)",
        "crpc_criteria": """
        **CRPC Definition (EAU):**
        1. **Kastrationsniveau:** Testosteron < 50 ng/dL (< 1,7 nmol/L).
        2. **Biochemischer Progress:** 3 konsekutive PSA-Anstiege, 1 Woche Abstand, PSA > 2,0 ng/mL.
        3. **Keine Metastasen:** Konventionelles Imaging (CT/Szinti) negativ.
        """,
        "rec_nmcrpc_high": """
        🔴 **Hochrisiko nmCRPC (PSADT < 10 Monate)**
        *1. Linie Standard:*
        
        - **Apalutamid:** $240$ mg (SPARTAN).
        - **Enzalutamid:** $160$ mg (PROSPER).
        - **Darolutamid:** $600$ mg 2x tgl (ARAMIS).
        
        ✅ **Zulassung:** Alle drei Substanzen sind für Hochrisiko-nmCRPC voll zugelassen.
        """,
        "rec_nmcrpc_low": """
        🟢 **Niedrigrisiko nmCRPC (PSADT > 10 Monate)**
        - **Empfehlung:** Fortführung ADT. Beobachtung.
        - *Grund:* Vorteil der ARPIs bei langsamem Verlauf nicht eindeutig belegt.
        """,

        "bone_prot_mhspc": """
        🦴 **Osteoprotektion (mHSPC)**
        *Ziel: Prävention ADT-induzierter Osteoporose.*
        - **Denosumab:** $60$ mg s.c. alle 6 Monate.
        - **Zoledronsäure:** $4$ mg i.v. jährlich.
        - *Cave:* Hochdosis (120mg) in mHSPC nicht Standard (außer bei CRPC-Übergang).
        """,
        "bone_prot_mcrpc": """
        🦴 **SRE-Prävention (mCRPC)**
        *Ziel: Vermeidung pathologischer Frakturen.*
        - **Denosumab (Xgeva):** $120$ mg s.c. alle 4 Wochen.
        - **Zoledronsäure:** $4$ mg i.v. alle 3-4 Wochen.
        - *Support:* Calcium + Vit D obligat.
        """,

        "header_mhspc": "Metastasiert Hormonsensitiv (mHSPC)",
        "rec_mhspc_high": """
        🔴 **Hohes Volumen / High Risk**
        *Viszerale Met. ODER $\ge$4 Knochenmet.*
        
        **1. Linie Standard: Tripel-Therapie**
        1. **ADT** (Kontinuierlich).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (6 Zyklen) ODER $50 \\text{ mg/m}^2$ q2w (PROSTY).
        3. **ARPI:**
           - **Darolutamid:** $600$ mg 2x tgl.
           - *ODER* **Abirateron:** $1000$ mg + Prednison.
        
        ✅ **Zulassung:**
        - 🇪🇺 **Darolutamid/Abirateron:** Voll zugelassen.
        """,
        "rec_mhspc_low": """
        🟢 **Geringes Volumen**
        
        **1. Linie Standard: Doublet + Lokaltherapie**
        1. **ADT** + **ARPI** (Enzalutamid / Apalutamida).
        2. **Prostata-RT:** 55 Gy / 20 Fx (STAMPEDE H).
        
        ⛔ **Cave:** Kein Docetaxel bei Low Volume (Toxizität > Nutzen).
        
        ✅ **Zulassung:**
        - 🇪🇺 **Enzalutamid:** $160$ mg (ARCHES).
        - 🇪🇺 **Apalutamida:** $240$ mg (TITAN).
        """,

        "header_mcrpc": "Metastasiert Kastrationsresistent (mCRPC)",
        
        "line1_naive": """
        **1. Linie (ARPI-Naiv)**
        - **Enzalutamid** oder **Abirateron**.
        - *Alternativ:* Docetaxel bei hoher Symptomlast.
        """,
        
        "line1_post_arpi": """
        **1./2. Linie (Nach ARPI-Progress)**
        *Mechanismus wechseln!*
        - **Docetaxel:** $75 \\text{ mg/m}^2$ q3w ODER $50 \\text{ mg/m}^2$ q2w (PROSTY).
        """,
        
        "line2_post_doc": """
        **2./3. Linie (Nach Docetaxel)**
        - **Cabazitaxel:** $25 \\text{ mg/m}^2$ q3w.
        - **Lu-177-PSMA:** $7,4$ GBq q6w (wenn PSMA+).
        - **Olaparib:** $300$ mg 2x tgl (wenn BRCA+).
        """,
        
        "rec_mcrpc_pembro": """
        **Immuntherapie (Jede Linie)**
        - **Pembrolizumab:** $200$ mg q3w.
        - *Indikation:* Nur bei MSI-High / dMMR.
        """,
        
        "rec_mcrpc_ra223": """
        **Knochen-Zielgerichtet (3. Linie/Symptome)**
        - **Radium-223:** $55$ kBq/kg q4w.
        - *Indikation:* Nur Knochenmetastasen (keine viszeralen).
        """
    },
    
    "Español": {
        "title": "Algoritmo Cáncer de Próstata (Guía S3 / EAU 2025)",
        "sidebar_title": "Configuración",
        "screening_note": "ℹ️ **Nota:** El tacto rectal es crítico para el **Estadiaje** (cT2 vs cT3) pero cuestionable para **Tamizaje** (PROBASE).",

        "extent_label": "Fase de la Enfermedad",
        "genetic_label": "Pruebas Genéticas",
        "psa_label": "Nivel de PSA (ng/ml)",
        "vol_label": "Volumen Prostático (cc)",
        "psad_label": "Densidad de PSA",
        "pirads_label": "Puntuación mpMRI PIRADS",
        "isup_label": "Grado ISUP",
        "tstage_label": "Estadio T Clínico",
        "n_stage_label": "Estadio N (Regional)",
        "meta_state_label": "Estado Metastásico",
        "psadt_label": "Tiempo Duplicación PSA (meses)",
        "primary_tx_label": "Terapia Primaria Recibida",
        "recurrence_time_label": "Tiempo hasta Recurrencia (meses)",
        
        "rotterdam_header": "Calculadora Rotterdam Inputs",
        "age_label": "Edad (años)",
        "dre_label": "Hallazgos Tacto Rectal",
        "fam_hist_label": "¿Historia Familiar?",
        "prev_bx_label": "¿Biopsia previa negativa?",
        "dre_opts": ["Normal", "Anormal (Sospechoso)"],

        "extent_opts": ["Diagnóstico (Rotterdam & Biopsia)", "Localizado (cT1-2 N0)", "Localmente Avanzado (cT3-4 o cN1)", "Recurrencia Bioquímica (BCR)", "nmCRPC (M0 CRPC)", "Metastásico (M1)"],
        "genetic_opts": ["No realizado/Desconocido", "Negativo", "BRCA1/2 Positivo", "Otro HRR Positivo", "MSI-Alto / dMMR"],
        "pirads_opts": ["PIRADS 1-2", "PIRADS 3", "PIRADS 4-5"],
        "n_stages": ["cN0 (Ganglios Negativos)", "cN1 (Ganglios Positivos)"],
        "m_states": ["mHSPC (Hormonosensible)", "mCRPC (Resistente a Castración)"],
        "prior_opts": ["Solo ADT (Naïve)", "ADT + Docetaxel", "ADT + ARPI", "Terapia Triple"],
        "primary_tx_opts": ["Prostatectomía Radical (PR)", "Radioterapia (EBRT)"],

        "header_diag": "Diagnóstico: Decisión de Biopsia",
        "rotterdam_high": """
        🔴 **Perfil Alto Riesgo (Rotterdam)**
        *Factores:* Tacto Anormal, Densidad PSA >0.15 o Historia Familiar.
        - **Recomendación:** **mpMRI** obligatoria. Si PIRADS $\ge$ 3 **Biopsia**.
        """,
        "rotterdam_low": """
        🟢 **Perfil Bajo Riesgo**
        *Tacto Normal, Densidad PSA Baja.*
        - **Recomendación:** Considerar MRI. Si PIRADS 1-2, evitar biopsia (monitorizar PSA).
        """,
        "rec_diag_biopsy": """
        🔴 **Realizar Biopsia**
        - **Método:** Transperineal (1ª elección) o Transrectal.
        - **Objetivo:** Sistemática + Dirigida (Fusión) si PIRADS $\ge$ 3.
        """,
        "rec_diag_consider": """
        🟡 **Considerar Biopsia**
        - **Contexto:** PIRADS 3 con hallazgos límite.
        - **Decisión:** Depende de Densidad PSA ($\ge$ 0.10) y preferencia paciente.
        """,
        "rec_diag_obs": """
        🟢 **Observación**
        - **Contexto:** Baja probabilidad de cáncer significativo.
        - **Acción:** Monitorización PSA. Evitar biopsia inmediata.
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
        - **Enzalutamida** ($160$ mg OD) + ADT.
        
        ✅ **Aprobación:**
        - 🇪🇺 **EMA:** Enzalutamida aprobada para BCR Alto Riesgo (2024).
        """,
        "rec_bcr_low": """
        🟢 **BCR Bajo Riesgo (EAU)**
        *Criterio: PSADT > 1 año Y ISUP < 4.*
        - **Acción:** Observación o RT de Rescate.
        """,

        "header_nmcrpc": "nmCRPC (CRPC No Metastásico / M0)",
        "crpc_criteria": """
        **Definición CRPC (EAU):**
        1. **Testosterona Castrada:** < 50 ng/dL.
        2. **Progresión PSA:** 3 aumentos consecutivos.
        3. **Sin Metástasis:** En imagen convencional.
        """,
        "rec_nmcrpc_high": """
        🔴 **nmCRPC Alto Riesgo (PSADT < 10 meses)**
        *1ª Línea Estándar:*
        - **Apalutamida:** $240$ mg.
        - **Enzalutamida:** $160$ mg.
        - **Darolutamida:** $600$ mg 2x día.
        ✅ 🇪🇺 Aprobados.
        """,
        "rec_nmcrpc_low": """
        🟢 **nmCRPC Bajo Riesgo (PSADT > 10 meses)**
        - **Recomendación:** Observación bajo ADT.
        """,

        "bone_prot_mhspc": """
        🦴 **Osteoprotección (mHSPC)**
        *Objetivo: Prevenir osteoporosis por ADT.*
        - **Denosumab:** $60$ mg s.c. c/6 meses.
        - **Ác. Zoledrónico:** $4$ mg i.v. anual.
        - *Nota:* Dosis alta (120mg) no indicada en mHSPC estándar.
        """,
        "bone_prot_mcrpc": """
        🦴 **Prevención SRE (mCRPC)**
        *Objetivo: Prevenir fracturas patológicas.*
        - **Denosumab (Xgeva):** $120$ mg s.c. c/4 sem.
        - **Ác. Zoledrónico:** $4$ mg i.v. c/3-4 sem.
        - *Suplemento:* Calcio + Vit D obligatorio.
        """,

        "header_mhspc": "Metastásico Hormonosensible (mHSPC)",
        "rec_mhspc_high": """
        🔴 **Alto Volumen / Alto Riesgo**
        *Mets Viscerales O $\ge$4 Mets Óseas*
        
        **1ª Línea Estándar: Terapia Triple**
        1. **ADT** (Continuo).
        2. **Docetaxel:** $75 \\text{ mg/m}^2$ q3w (6 ciclos) O $50 \\text{ mg/m}^2$ q2w.
        3. **ARPI:**
           - **Darolutamida:** $600$ mg BID.
           - *O* **Abiraterona:** $1000$ mg OD + Prednisona.
        
        ✅ **Aprobaciones:**
        - 🇪🇺 **Darolutamida:** Aprobada mHSPC + Docetaxel (ARASENS).
        - 🇪🇺 **Abiraterona:** Aprobada Alto Riesgo mHSPC (LATITUDE).
        """,
        "rec_mhspc_low": """
        🟢 **Bajo Volumen**
        
        **1ª Línea Estándar: Doble + RT Local**
        1. **ADT** + **ARPI** (Enzalututamida / Apalutamida).
        2. **RT Próstata:** 55 Gy / 20 Fx (STAMPEDE H).
        
        ⛔ **No:** Evitar Docetaxel (toxicidad > beneficio).
        
        ✅ **Aprobaciones:**
        - 🇪🇺 **Enzalutamida:** $160$ mg (ARCHES).
        - 🇪🇺 **Apalutamida:** $240$ mg (TITAN).
        """,

        "header_mcrpc": "Metastásico Resistente a Castración (mCRPC)",
        
        "line1_naive": """
        **1ª Línea (Naïve a ARPI)**
        - **Enzalutamida** o **Abiraterona**.
        - *Alternativa:* Docetaxel.
        """,
        
        "line1_post_arpi": """
        **1ª/2ª Línea (Tras ARPI)**
        *¡Cambiar Mecanismo!*
        - **Docetaxel:** $75 \\text{ mg/m}^2$ q3w O $50 \\text{ mg/m}^2$ q2w (PROSTY).
        """,
        
        "line2_post_doc": """
        **2ª/3ª Línea (Tras Docetaxel)**
        - **Cabazitaxel:** $25 \\text{ mg/m}^2$ q3w.
        - **Lu-177-PSMA:** $7.4$ GBq q6w.
        - **Olaparib:** $300$ mg 2x día (si BRCA+).
        """,
        
        "rec_mcrpc_pembro": """
        **Inmunoterapia (Cualquier Línea)**
        - **Pembrolizumab:** $200$ mg q3w.
        - *Indicación:* MSI-Alto / dMMR.
        """,
        
        "rec_mcrpc_ra223": """
        **Dirigido a Hueso (3ª Línea)**
        - **Radium-223:** $55$ kBq/kg c/4sem.
        - *Indicación:* Solo hueso, no visceral.
        """
    }
}

# --- 3. Logic Functions ---

def get_diagnosis_rec(pirads, psad, dre_abnormal, fam_hist):
    if dre_abnormal or psad > 0.15 or fam_hist:
        if pirads == "PIRADS 4-5" or pirads == "PIRADS 3": return "rec_diag_biopsy"
        else: return "rec_diag_consider"
    else:
        if pirads == "PIRADS 4-5": return "rec_diag_biopsy"
        elif pirads == "PIRADS 3":
            if psad >= 0.10: return "rec_diag_consider"
            else: return "rec_diag_obs"
        else: return "rec_diag_obs"

def get_bcr_risk(primary, psadt, isup_idx, interval):
    is_high_grade = (isup_idx >= 3) # ISUP 4 or 5
    if primary == "Radical Prostatectomy (RP)":
        if psadt > 12 and not is_high_grade: return "rec_bcr_low"
        else: return "rec_bcr_embark"
    else:
        if interval > 18 and not is_high_grade: return "rec_bcr_low"
        else: return "rec_bcr_embark"

def calculate_risk_local(psa, isup_idx, t_idx):
    isup = isup_idx + 1
    if psa > 20 or isup >= 4 or t_idx >= 4: return "rec_multi_high"
    elif (psa >= 10) or (isup == 2 or isup == 3) or (t_idx >= 2):
        if psa <= 15 and isup == 1 and t_idx <= 1: return "rec_as_extended" # S3 AS
        return "rec_curative"
    else: return "rec_as_extended"

# --- 4. UI ---
with st.sidebar:
    st.header("🌐 Language")
    lang_key = st.selectbox("Select", ["English", "Deutsch", "Español"])
    t = translations[lang_key]
    
    st.markdown("---")
    st.header(t["sidebar_title"])
    
    # Genetic Status (Always visible)
    genetic_status = st.selectbox(t["genetic_label"], t["genetic_opts"])
    is_brca = "BRCA" in genetic_status
    is_msi = "MSI" in genetic_status
    
    # Phase Selection
    disease_extent = st.selectbox(t["extent_label"], t["extent_opts"])
    
    # Init vars
    bone_mets = 0
    prior = "ADT Only" 
    
    # --- A. DIAGNOSIS ---
    if disease_extent == t["extent_opts"][0]:
        st.subheader("Diagnostics")
        st.markdown(f"**{t['rotterdam_header']}**")
        in_age = st.number_input(t["age_label"], value=65, step=1)
        in_psa = st.number_input(t["psa_label"], value=5.0, step=0.1)
        in_vol = st.number_input(t["vol_label"], value=40, step=5)
        in_dre = st.radio(t["dre_label"], t["dre_opts"])
        in_fam = st.checkbox(t["fam_hist_label"])
        
        st.markdown("---")
        in_pirads = st.selectbox(t["pirads_label"], t["pirads_opts"])
        psad = in_psa / in_vol if in_vol > 0 else 0
        st.info(f"**PSA Density:** {psad:.2f}")
    
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
            
    # --- E. nmCRPC ---
    elif disease_extent == t["extent_opts"][4]:
        st.subheader("CRPC M0")
        psadt = st.number_input(t["psadt_label"], value=8.0)
            
    # --- F. METASTATIC ---
    elif disease_extent == t["extent_opts"][5]:
        st.subheader("Metastatic Details")
        m_state = st.radio(t["meta_state_label"], t["m_states"])
        is_high_vol = False
        if m_state == t["m_states"][0]: # mHSPC
            if st.checkbox("High Volume (Visceral/4+ Bone)?"): is_high_vol = True
            bone_mets = st.number_input("Bone Mets Count", 0, 20, 1)
        else: # mCRPC
            prior = st.selectbox("Prior Therapy", t["prior_opts"])
            bone_mets = st.number_input("Bone Mets Count", 0, 20, 1)

# --- 5. Main Content ---
st.title(t["title"])
st.info(t["screening_note"])

# === LOGIC & DISPLAY ===

# 1. DIAGNOSIS
if disease_extent == t["extent_opts"][0]:
    st.header(t["header_diag"])
    dre_abnormal = (in_dre == t["dre_opts"][1])
    
    if dre_abnormal or psad > 0.15 or in_fam:
        st.warning(t["rotterdam_high"])
    else:
        st.success(t["rotterdam_low"])
    st.markdown("---")
    res_key = get_diagnosis_rec(in_pirads, psad, dre_abnormal, in_fam)
    if res_key == "rec_diag_biopsy": st.error(t[res_key])
    elif res_key == "rec_diag_consider": st.warning(t[res_key])
    else: st.success(t[res_key])
        
    mermaid_code = f"""
    graph TD
    Start[Suspicion] --> Risk{{Rotterdam Risk}}
    Risk -->|High| MRI[mpMRI]
    MRI -->|PIRADS 4-5| Bx[Biopsy]
    MRI -->|PIRADS 3| PSAD{{PSAD {psad:.2f}}}
    PSAD -->|>=0.10| Bx
    PSAD -->|<0.10| Obs[Observation]
    """

# 2. LOCALIZED
elif disease_extent == t["extent_opts"][1]:
    st.header("Localized Disease")
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
    if psadt < 9:
        st.error(t["rec_bcr_embark"])
        mermaid_code = "graph TD\nStart --> Embark[Enzalutamide + ADT]"
    else:
        risk_key = get_bcr_risk(primary_tx, psadt, isup_idx, recurrence_time)
        if risk_key == "rec_bcr_embark": 
            st.warning(t["rec_bcr_embark"])
            mermaid_code = "graph TD\nStart --> HighRisk --> EarlySalvage"
        else:
            st.success(t[risk_key])
            mermaid_code = "graph TD\nStart --> LowRisk --> Obs[Observation/Salvage]"

# 5. nmCRPC
elif disease_extent == t["extent_opts"][4]:
    st.header(t["header_nmcrpc"])
    st.info(t["crpc_criteria"])
    st.markdown("---")
    if psadt < 10:
        st.error(t["rec_nmcrpc_high"])
        mermaid_code = "graph TD\nnmCRPC --> PSADT{< 10 mo}\nPSADT -->|Yes| ARPI[Apa/Enza/Daro]"
    else:
        st.success(t["rec_nmcrpc_low"])
        mermaid_code = "graph TD\nnmCRPC --> PSADT{> 10 mo}\nPSADT -->|No| Obs[Observation]"

# 6. METASTATIC
elif disease_extent == t["extent_opts"][5]:
    if m_state == t["m_states"][0]: # mHSPC
        st.header("mHSPC")
        if is_high_vol:
            st.error(t["rec_mhspc_high"])
            mermaid_code = "graph TD\nmHSPC --> Vol{High Vol}\nVol --> Triple[Triple Therapy]"
        else:
            st.success(t["rec_mhspc_low"])
            mermaid_code = "graph TD\nmHSPC --> Vol{Low Vol}\nVol --> Double[Doublet + RT]"
        
        # Bone Protection for mHSPC (Osteoprotection)
        if bone_mets > 0:
            st.info(t["bone_prot_mhspc"])

    else: # mCRPC
        st.header(t["header_mcrpc"])
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("### 1. Line / Switch")
            # Logic for sequencing
            if "ADT Only" in prior:
                st.write(t["line1_naive"])
            elif "ARPI" in prior:
                st.write(t["line1_post_arpi"]) # Docetaxel
            elif "Docetaxel" in prior:
                st.write(t["line2_post_doc"]) # Cabazitaxel
                
        with c2:
            st.markdown("### 2. Precision")
            if is_brca: st.error(f"🧬 **BRCA+**\n- Olaparib 300mg BID\n- Talazoparib 0.5mg OD")
            st.write(t["rec_mcrpc_lutetium"])
            if is_msi: st.error(t["rec_mcrpc_pembro"])
            
        with c3:
            st.markdown("### 3. Bone / Support")
            if bone_mets > 0:
                st.info(t["bone_prot_mcrpc"])
                st.write(t["rec_mcrpc_ra223"])
            
        mermaid_code = f"""
        graph TD
        mCRPC --> Prior{{{prior}}}
        Prior -->|ADT| ARPI[Enza/Abi]
        Prior -->|ARPI| Chemo[Docetaxel 75q3w/50q2w]
        Prior -->|Docetaxel| 2ndLine[Cabazitaxel/Lu177]
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
