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
