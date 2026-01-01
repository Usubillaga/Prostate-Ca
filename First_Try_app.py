import streamlit as st

# Translations (further shortened)
translations = {
    "English": {
        "title": "Prostate Cancer Algorithm",
        "description": "Simplified app based on EAU 2025 & German S3 2025 guidelines. Educational only – consult physician.",
        "genetic_subheader": "Genetic Testing",
        "genetic_write": """
- Recommended: metastatic, high-risk, early-onset (<60y), family history.
- Genes: HRR (BRCA1/2, ATM etc.); MMR.
- Impact: HRR+ → PARP eligibility, cautious AS.
""",
        "genetic_select": "Genetic Results:",
        "genetic_options": ["Unknown", "Negative", "BRCA1/2+", "Other HRR+", "MMR+"],
        "extent_select": "Disease Extent:",
        "extent_options": ["Localized", "Locally Advanced", "Metastatic"],
        "risk_select": "Risk Group:",
        "risk_options": ["Very Low/Low", "Int. Favorable", "Int. Unfavorable", "High Risk"],
        "recommend_subheader": "Therapies (key dosages)",
        "very_low_risk_write": """
- Primary: Active Surveillance (AS).
- Alternative: RP / EBRT (74-80 Gy) / LDR brachy.
- No ADT.
""",
        "favorable_write": """
- AS or curative.
- Curative: RP (± lymph) / EBRT hypo (60 Gy/20 fx) + short ADT (4-6 mo).
""",
        "unfavorable_write": """
- RP + ePLND / EBRT + short ADT (4-6 mo).
""",
        "high_risk_write": """
- EBRT + long ADT (24-36 mo) / RP + ePLND.
""",
        "locally_advanced_write": """
- EBRT + long ADT (24-36 mo).
- Operable: RP + ePLND.
- N1: RT + ADT 3y + abiraterone 1000 mg/d (2y).
""",
        "androgen_select": "Androgen Status:",
        "androgen_options": ["Hormone-Sensitive", "Castration-Resistant"],
        "volume_select": "Volume:",
        "volume_options": ["Low", "High"],
        "mHSPC_write": """
- ADT backbone.
- Add ARPI (apalutamide 240 mg/d, enzalutamide 160 mg/d, darolutamide 600 mg BID) or abiraterone 1000 mg/d.
- + Docetaxel 75 mg/m² q3w ×6 if eligible.
- High vol: Triple preferred.
- Low vol: Local RT.
- Bone: Denosumab 120 mg q4w.
""",
        "genetic_impact_hrr": "- HRR+: PARP combos (olaparib 300 mg BID etc.).",
        "genetic_impact_mmr": "- MMR+: Pembrolizumab if MSI-H.",
        "zulassung_mHSPC": "Standard combos approved.",
        "prior_select": "Prior Therapies:",
        "prior_options": ["ADT only", "ARPI", "Docetaxel", "Abiraterone"],
        "mCRPC_write": """
- Continue ADT.
- ARPI switch / docetaxel 75 mg/m² q3w.
- Bone-dominant: Radium-223 55 kBq/kg q4w ×6.
- Post-doc: Cabazitaxel 25 mg/m² q3w.
- PSMA+: Lu-177-PSMA 7.4 GBq q6w.
""",
        "post_doc_add": "- Post-doc: Cabazitaxel / Lu-PSMA / PARP if HRR+.",
        "genetic_impact_hrr_cr": "- HRR+: PARP priority (olaparib 300 mg BID etc.).",
        "zulassung_mCRPC": "Standard therapies approved.",
        "visual_subheader": "Decision Pathway",
        "references": "EAU 2025; S3 2025.",
        "language_select": "Language",
        "language_options": ["English", "Deutsch", "Español"]
    },
    "Deutsch": {
        "title": "Prostatakrebs Algorithmus",
        "description": "Vereinfachte App: EAU 2025 & S3 2025. Nur Bildung – Arzt konsultieren.",
        "genetic_subheader": "Genetisches Testing",
        "genetic_write": """
- Empfohlen: metastasiert, hochrisiko, früh (<60J), Familienanamnese.
- Gene: HRR (BRCA1/2 etc.); MMR.
- HRR+ → PARP-Berechtigung.
""",
        "genetic_select": "Genetik:",
        "genetic_options": ["Unbekannt", "Negativ", "BRCA1/2+", "Andere HRR+", "MMR+"],
        "extent_select": "Ausmaß:",
        "extent_options": ["Lokalisiert", "Lokal fortg.", "Metastasiert"],
        "risk_select": "Risiko:",
        "risk_options": ["Sehr niedrig/niedrig", "Int. günstig", "Int. ungünstig", "Hoch"],
        "recommend_subheader": "Therapien (Dosierungen)",
        "very_low_risk_write": """
- Primär: Aktive Überwachung (AS).
- Alt: RP / EBRT (74-80 Gy) / LDR-Brachy.
- Kein ADT.
""",
        "favorable_write": """
- AS oder kurativ.
- Kurativ: RP (± Lymph) / EBRT + kurzes ADT (4-6 Mo).
""",
        "unfavorable_write": """
- RP + ePLND / EBRT + kurzes ADT.
""",
        "high_risk_write": """
- EBRT + langes ADT (24-36 Mo) / RP + ePLND.
""",
        "locally_advanced_write": """
- EBRT + langes ADT.
- Operabel: RP + ePLND.
- N1: RT + ADT + Abirateron 1000 mg/d.
""",
        "androgen_select": "Androgen-Status:",
        "androgen_options": ["Hormon-sensitiv", "Kastrationsresistent"],
        "volume_select": "Volumen:",
        "volume_options": ["Niedrig", "Hoch"],
        "mHSPC_write": """
- ADT.
- + ARPI (Apalutamid 240 mg/d etc.) oder Abirateron 1000 mg/d.
- + Docetaxel 75 mg/m² ×6.
- Hoch: Triple.
- Knochen: Denosumab.
""",
        "genetic_impact_hrr": "- HRR+: PARP-Kombis.",
        "genetic_impact_mmr": "- MMR+: Pembrolizumab.",
        "zulassung_mHSPC": "Standard zugelassen.",
        "prior_select": "Vortherapien:",
        "prior_options": ["ADT", "ARPI", "Docetaxel", "Abirateron"],
        "mCRPC_write": """
- ADT fortsetzen.
- ARPI-Wechsel / Docetaxel.
- Knochen: Radium-223.
- Post-Doc: Cabazitaxel / Lu-PSMA.
""",
        "post_doc_add": "- Nach Doc: Cabazitaxel / PARP bei HRR+.",
        "genetic_impact_hrr_cr": "- HRR+: PARP priorisieren.",
        "zulassung_mCRPC": "Standard zugelassen.",
        "visual_subheader": "Entscheidungspfad",
        "references": "EAU 2025; S3 2025.",
        "language_select": "Sprache",
        "language_options": ["English", "Deutsch", "Español"]
    },
    "Español": {
        "title": "Algoritmo Cáncer Próstata",
        "description": "App simplificada: Guías EAU 2025 & S3 2025. Educativo – consultar médico.",
        "genetic_subheader": "Pruebas Genéticas",
        "genetic_write": """
- Recomendadas: metastásico, alto riesgo, inicio temprano, historia familiar.
- Genes: HRR (BRCA1/2 etc.); MMR.
- HRR+ → elegible PARP.
""",
        "genetic_select": "Genética:",
        "genetic_options": ["Desconocida", "Negativa", "BRCA1/2+", "Otra HRR+", "MMR+"],
        "extent_select": "Extensión:",
        "extent_options": ["Localizada", "Local avanzada", "Metastásica"],
        "risk_select": "Riesgo:",
        "risk_options": ["Muy bajo/bajo", "Int. favorable", "Int. desfavorable", "Alto"],
        "recommend_subheader": "Terapias (dosis clave)",
        "very_low_risk_write": """
- Primaria: Vigilancia Activa (AS).
- Alt: RP / EBRT (74-80 Gy) / Braqui LDR.
- Sin ADT.
""",
        "favorable_write": """
- AS o curativa.
- Curativa: RP (± linf) / EBRT + ADT corto (4-6 mes).
""",
        "unfavorable_write": """
- RP + ePLND / EBRT + ADT corto.
""",
        "high_risk_write": """
- EBRT + ADT largo (24-36 mes) / RP + ePLND.
""",
        "locally_advanced_write": """
- EBRT + ADT largo.
- Operable: RP + ePLND.
- N1: RT + ADT + abiraterona 1000 mg/d.
""",
        "androgen_select": "Estado Andrógenos:",
        "androgen_options": ["Sensible hormonas", "Resistente castración"],
        "volume_select": "Volumen:",
        "volume_options": ["Bajo", "Alto"],
        "mHSPC_write": """
- ADT.
- + ARPI (apalutamida 240 mg/d etc.) o abiraterona 1000 mg/d.
- + Docetaxel 75 mg/m² ×6.
- Alto: Triple.
- Óseo: Denosumab.
""",
        "genetic_impact_hrr": "- HRR+: Combinaciones PARP.",
        "genetic_impact_mmr": "- MMR+: Pembrolizumab.",
        "zulassung_mHSPC": "Combinaciones estándar.",
        "prior_select": "Terapias Previas:",
        "prior_options": ["ADT", "ARPI", "Docetaxel", "Abiraterona"],
        "mCRPC_write": """
- Continuar ADT.
- Cambio ARPI / Docetaxel.
- Óseo: Radium-223.
- Post-doc: Cabazitaxel / Lu-PSMA.
""",
        "post_doc_add": "- Post-doc: Cabazitaxel / PARP si HRR+.",
        "genetic_impact_hrr_cr": "- HRR+: Priorizar PARP.",
        "zulassung_mCRPC": "Terapias estándar.",
        "visual_subheader": "Vía Decisión",
        "references": "EAU 2025; S3 2025.",
        "language_select": "Idioma",
        "language_options": ["English", "Deutsch", "Español"]
    }
}

language = st.selectbox(translations["English"]["language_select"], translations["English"]["language_options"])
t = translations[language]

st.title(t["title"])
st.markdown(t["description"])

st.subheader(t["genetic_subheader"])
st.write(t["genetic_write"])

genetic_status = st.selectbox(t["genetic_select"], t["genetic_options"])

disease_extent = st.selectbox(t["extent_select"], t["extent_options"])

risk_group = None
androgen_status = None
volume = None
prior_therapy = []

if disease_extent == t["extent_options"][0]:
    risk_group = st.selectbox(t["risk_select"], t["risk_options"])
    st.subheader(t["recommend_subheader"])
    if risk_group == t["risk_options"][0]:
        st.write(t["very_low_risk_write"])
    elif risk_group == t["risk_options"][1]:
        st.write(t["favorable_write"])
    elif risk_group == t["risk_options"][2]:
        st.write(t["unfavorable_write"])
    else:
        st.write(t["high_risk_write"])

elif disease_extent == t["extent_options"][1]:
    st.subheader(t["recommend_subheader"])
    st.write(t["locally_advanced_write"])

else:
    androgen_status = st.selectbox(t["androgen_select"], t["androgen_options"])
    if androgen_status == t["androgen_options"][0]:
        volume = st.selectbox(t["volume_select"], t["volume_options"])
        st.subheader(t["recommend_subheader"])
        st.write(t["mHSPC_write"])
        if "HRR" in genetic_status or "BRCA" in genetic_status:
            st.write(t["genetic_impact_hrr"])
        elif "MMR" in genetic_status:
            st.write(t["genetic_impact_mmr"])
        st.write(t["zulassung_mHSPC"])
    else:
        prior_therapy = st.multiselect(t["prior_select"], t["prior_options"])
        st.subheader(t["recommend_subheader"])
        st.write(t["mCRPC_write"])
        if "Docetaxel" in prior_therapy:
            st.write(t["post_doc_add"])
        if "HRR" in genetic_status or "BRCA" in genetic_status:
            st.write(t["genetic_impact_hrr_cr"])
        st.write(t["zulassung_mCRPC"])

st.subheader(t["visual_subheader"])
mermaid_code = "graph TD\n"
mermaid_code += "A[Diagnosis] --> B{Genetic}\n"
mermaid_code += f'B -->|"{genetic_status}"| C{{Extent}}\n'
mermaid_code += f'C -->|"{disease_extent}"| D\n'

if disease_extent == t["extent_options"][0]:
    mermaid_code += f'D[Risk: "{risk_group}"] --> E[Therapy]\n'
    if t["risk_options"][0] in risk_group:
        mermaid_code += "E --> F[AS]\nE --> G[RP/EBRT/Brachy]\n"
    elif t["risk_options"][1] in risk_group:
        mermaid_code += "E --> H[AS / Curative + short ADT]\n"
    elif t["risk_options"][2] in risk_group:
        mermaid_code += "E --> I[RP+ePLND / EBRT+short ADT]\n"
    else:
        mermaid_code += "E --> J[EBRT+long ADT / RP]\n"
elif disease_extent == t["extent_options"][1]:
    mermaid_code += "D --> K[EBRT+long ADT / RP]\n"
else:
    mermaid_code += f'D --> L{{Androgen: "{androgen_status}"}}\n'
    if androgen_status == t["androgen_options"][0]:
        mermaid_code += f'L --> M[Vol: "{volume}"]\nM --> N[ADT+ARPI/Docetaxel]\n'
    else:
        mermaid_code += "L --> O[ADT + switch/chemo]\nO --> P[Post-doc options]\n"

if genetic_status not in [t["genetic_options"][0], t["genetic_options"][1]]:
    mermaid_code += "B --> Q[Genetic impact]\nQ -.-> E\nQ -.-> N\nQ -.-> O\n"

st.markdown(f"```mermaid\n{mermaid_code}\n```")

st.info(t["references"])
