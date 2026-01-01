import streamlit as st

# Define translations (kept but simplified where possible)
translations = {
    "English": {
        "title": "Prostate Cancer Treatment Algorithm",
        "description": """
This interactive app is based on the 2025 EAU Guidelines and German S3-Leitlinie Prostatakarzinom (v8.1, 2025). 
Simplified educational tool – always consult full guidelines and a physician.
""",
        "genetic_subheader": "Genetic Testing Recommendations",
        "genetic_write": """
- Recommended for metastatic, high-risk localized, early-onset (<60y), family history.
- Focus: HRR genes (BRCA1/2, ATM, CHEK2, PALB2 etc.); MMR for Lynch.
- Perform at diagnosis (high-risk/metastatic); genetic counseling required.
- Impact: HRR+ → aggressive disease, PARP eligibility, cautious AS.
""",
        "genetic_select": "Genetic Testing Results:",
        "genetic_options": ["Not Performed/Unknown", "Negative", "BRCA1/2 Positive", "Other HRR Positive", "MMR Deficient"],
        "extent_select": "Select Disease Extent:",
        "extent_options": ["Localized (cT1-2 N0 M0)", "Locally Advanced (cT3-4/N1 M0)", "Metastatic (M1)"],
        "risk_select": "Select Risk Group:",
        "risk_options": ["Very Low/Low Risk", "Intermediate Favorable", "Intermediate Unfavorable", "High Risk"],
        "recommend_subheader": "Recommended Therapies (with typical dosages)",
        "very_low_risk_write": """
- Primary: Active Surveillance (AS) – PSA q6mo, mpMRI 12-18mo, re-biopsy if progression.
- If declined: RP or EBRT (74-80 Gy) or LDR brachytherapy.
- No ADT.
- Genetic: BRCA2+ → intensified monitoring.
""",
        "favorable_write": """
- AS (if no unfavorable features) or curative therapy.
- Curative: RP (± lymphadenectomy) or hypofractionated EBRT (60 Gy/20 fx) + short ADT (4-6 mo; e.g., leuprolide 22.5 mg/3mo or relugolix 120 mg/d).
- Focal therapies (HIFU/cryo) select cases.
""",
        "unfavorable_write": """
- Curative: RP + ePLND or EBRT + short ADT (4-6 mo).
- Brachy boost possible.
""",
        "high_risk_write": """
- Multimodal: EBRT + long ADT (24-36 mo) or RP + ePLND (± adj RT).
- Brachy boost select cases.
""",
        "locally_advanced_write": """
- Multimodal: EBRT (dose-escalated) + long ADT (24-36 mo).
- Operable: RP + ePLND (± adj RT).
- N1: Pelvic RT + ADT 3y + abiraterone 1000 mg/d + prednisone 5 mg/d (2y) if ≥2 risks.
- Brachy boost for cT3a.
""",
        "androgen_select": "Androgen Status:",
        "androgen_options": ["Hormone-Sensitive (mHSPC)", "Castration-Resistant (mCRPC)"],
        "volume_select": "Disease Volume:",
        "volume_options": ["Low-Volume", "High-Volume"],
        "mHSPC_write": """
- Backbone: ADT (GnRH agonist/antagonist or orchiectomy).
- Add: ARPI (apalutamide 240 mg/d, enzalutamide 160 mg/d, darolutamide 600 mg BID) or abiraterone 1000 mg/d + prednisone 5 mg/d.
- Chemo-eligible: + docetaxel 75 mg/m² q3w ×6.
- High-volume: Prefer triple therapy.
- Low-volume: Local RT/SBRT to metastases/prostate.
- Bone protection: Denosumab 120 mg q4w or zoledronic acid 4 mg q3-4w.
""",
        "genetic_impact_hrr": "- HRR+ (esp. BRCA): Consider PARP combos (e.g., olaparib 300 mg BID + abiraterone; talazoparib 0.5 mg/d + enzalutamide).",
        "genetic_impact_mmr": "- MMR deficient (rare): Pembrolizumab if MSI-H.",
        "zulassung_mHSPC": """
Zulassung notes: All standard ARPIs/docetaxel approved in combination; some restrictions for abiraterone in Germany.
""",
        "prior_select": "Prior Therapies (mHSPC phase):",
        "prior_options": ["None/ADT only", "ARPI", "Docetaxel", "Abiraterone"],
        "mCRPC_write": """
- Continue ADT.
- Asymptomatic: ARPI switch or docetaxel 75 mg/m² q3w.
- Symptomatic/bone-dominant: Docetaxel or radium-223 55 kBq/kg q4w ×6.
- Post-docetaxel: Cabazitaxel 20-25 mg/m² q3w.
- PSMA+: Lu-177-PSMA 7.4 GBq q6w ×4-6.
- Bone protection as above.
""",
        "post_doc_add": "- Post-docetaxel: Cabazitaxel, PARP if HRR+, Lu-PSMA.",
        "genetic_impact_hrr_cr": """
- HRR+ (esp. BRCA1/2): Prioritize PARP (olaparib 300 mg BID mono; talazoparib 0.5 mg/d + enzalutamide; niraparib 200 mg/d + abiraterone).
""",
        "zulassung_mCRPC": """
Zulassung notes: All listed therapies EMA-approved for indicated settings; some combos off-label in Germany.
""",
        "visual_subheader": "Visual Decision Pathway",
        "references": "EAU 2025 Guidelines; German S3 v8.1 2025. Always verify latest.",
        "language_select": "Language",
        "language_options": ["English", "Deutsch", "Español"]
    },
    "Deutsch": {
        # Similar structure with German translations and shortened texts
        "title": "Prostatakrebs Therapie-Algorithmus",
        "description": """
Vereinfachte App basierend auf EAU 2025 und S3-Leitlinie 2025. Bildungszweck – Leitlinien/Arzt konsultieren.
""",
        "genetic_subheader": "Genetisches Testing",
        "genetic_write": """
- Empfohlen bei metastasiert, hochrisiko, früh (<60J), Familienanamnese.
- HRR-Gene (BRCA1/2 etc.); MMR.
- Bei Diagnose; Beratung erforderlich.
- HRR+ → aggressiv, PARP-Berechtigung.
""",
        "genetic_select": "Genetisches Testing:",
        "genetic_options": ["Nicht durchgeführt", "Negativ", "BRCA1/2 positiv", "Andere HRR positiv", "MMR defizient"],
        "extent_select": "Erkrankungsausmaß:",
        "extent_options": ["Lokalisiert", "Lokal fortgeschritten", "Metastasiert"],
        "risk_select": "Risikogruppe:",
        "risk_options": ["Sehr niedrig/niedrig", "Intermediär günstig", "Intermediär ungünstig", "Hochrisiko"],
        "recommend_subheader": "Empfohlene Therapien (mit Dosierungen)",
        "very_low_risk_write": """
- Primär: Aktive Überwachung (AS).
- Alternativ: RP / EBRT (74-80 Gy) / LDR-Brachy.
- Kein ADT.
""",
        "favorable_write": """
- AS oder kurativ.
- Kurativ: RP (± Lymph) oder EBRT hypo + kurzes ADT (4-6 Mo).
""",
        "unfavorable_write": """
- RP + ePLND oder EBRT + kurzes ADT.
""",
        "high_risk_write": """
- EBRT + langes ADT (24-36 Mo) oder RP + ePLND.
""",
        "locally_advanced_write": """
- EBRT + langes ADT.
- Operabel: RP + ePLND.
- N1: RT + ADT + Abirateron 1000 mg/d + Prednison 5 mg/d.
""",
        "androgen_select": "Androgen-Status:",
        "androgen_options": ["Hormon-sensitiv (mHSPC)", "Kastrationsresistent (mCRPC)"],
        "volume_select": "Volumen:",
        "volume_options": ["Niedrig", "Hoch"],
        "mHSPC_write": """
- ADT-Backbone.
- + ARPI (Apalutamid 240 mg/d, Enzalutamid 160 mg/d, Darolutamid 600 mg BID) oder Abirateron 1000 mg/d + Prednison.
- + Docetaxel 75 mg/m² q3w ×6.
- Hochvolumen: Triple bevorzugt.
- Knochen: Denosumab/Zoledronat.
""",
        "genetic_impact_hrr": "- HRR+: PARP-Kombis (Olaparib 300 mg BID etc.).",
        "genetic_impact_mmr": "- MMR+: Pembrolizumab bei MSI-H.",
        "zulassung_mHSPC": "Zulassungen: Standardkombinationen zugelassen.",
        "prior_select": "Vortherapien:",
        "prior_options": ["Keine/ADT", "ARPI", "Docetaxel", "Abirateron"],
        "mCRPC_write": """
- ADT fortsetzen.
- ARPI-Wechsel oder Docetaxel 75 mg/m².
- Symptomatisch: Radium-223 55 kBq/kg q4w ×6.
- Post-Doc: Cabazitaxel 20-25 mg/m².
- PSMA+: Lu-177-PSMA.
""",
        "post_doc_add": "- Nach Docetaxel: Cabazitaxel, PARP bei HRR+.",
        "genetic_impact_hrr_cr": "- HRR+: PARP priorisieren (Olaparib 300 mg BID etc.).",
        "zulassung_mCRPC": "Zulassungen: Standardtherapien zugelassen.",
        "visual_subheader": "Visueller Pfad",
        "references": "EAU 2025; S3 2025.",
        "language_select": "Sprache",
        "language_options": ["English", "Deutsch", "Español"]
    },
    "Español": {
        # Similar shortened Spanish translations
        "title": "Algoritmo Tratamiento Cáncer Próstata",
        "description": """
App simplificada basada en Guías EAU 2025 y S3 Alemana 2025. Uso educativo – consultar guías/médico.
""",
        "genetic_subheader": "Pruebas Genéticas",
        "genetic_write": """
- Recomendadas en metastásico, alto riesgo, inicio temprano, historia familiar.
- Genes HRR (BRCA1/2 etc.); MMR.
- Al diagnóstico; asesoramiento requerido.
- HRR+ → agresivo, elegible PARP.
""",
        "genetic_select": "Resultados Genéticos:",
        "genetic_options": ["No realizada", "Negativa", "BRCA1/2 positiva", "Otra HRR positiva", "MMR deficiente"],
        "extent_select": "Extensión Enfermedad:",
        "extent_options": ["Localizada", "Localmente avanzada", "Metastásica"],
        "risk_select": "Grupo Riesgo:",
        "risk_options": ["Muy bajo/bajo", "Intermedio favorable", "Intermedio desfavorable", "Alto riesgo"],
        "recommend_subheader": "Terapias Recomendadas (con dosis)",
        "very_low_risk_write": """
- Primaria: Vigilancia Activa (AS).
- Alternativa: RP / EBRT (74-80 Gy) / Braquiterapia LDR.
- Sin ADT.
""",
        "favorable_write": """
- AS o curativa.
- Curativa: RP (± linf) o EBRT hipo + ADT corto (4-6 mes).
""",
        "unfavorable_write": """
- RP + ePLND o EBRT + ADT corto.
""",
        "high_risk_write": """
- EBRT + ADT largo (24-36 mes) o RP + ePLND.
""",
        "locally_advanced_write": """
- EBRT + ADT largo.
- Operable: RP + ePLND.
- N1: RT + ADT + abiraterona 1000 mg/d + prednisona.
""",
        "androgen_select": "Estado Andrógenos:",
        "androgen_options": ["Sensible hormonas (mHSPC)", "Resistente castración (mCRPC)"],
        "volume_select": "Volumen:",
        "volume_options": ["Bajo", "Alto"],
        "mHSPC_write": """
- Base: ADT.
- + ARPI (apalutamida 240 mg/d, enzalutamida 160 mg/d, darolutamida 600 mg BID) o abiraterona 1000 mg/d + prednisona.
- + Docetaxel 75 mg/m² q3s ×6.
- Alto volumen: Triple preferida.
- Óseo: Denosumab/Zoledrónico.
""",
        "genetic_impact_hrr": "- HRR+: Combinaciones PARP (olaparib 300 mg BID etc.).",
        "genetic_impact_mmr": "- MMR+: Pembrolizumab si MSI-H.",
        "zulassung_mHSPC": "Aprobaciones: Combinaciones estándar.",
        "prior_select": "Terapias Previas:",
        "prior_options": ["Ninguna/ADT", "ARPI", "Docetaxel", "Abiraterona"],
        "mCRPC_write": """
- Continuar ADT.
- Cambio ARPI o docetaxel 75 mg/m².
- Sintomático: Radium-223 55 kBq/kg q4s ×6.
- Post-doc: Cabazitaxel 20-25 mg/m².
- PSMA+: Lu-177-PSMA.
""",
        "post_doc_add": "- Post-docetaxel: Cabazitaxel, PARP si HRR+.",
        "genetic_impact_hrr_cr": "- HRR+: Priorizar PARP (olaparib 300 mg BID etc.).",
        "zulassung_mCRPC": "Aprobaciones: Terapias estándar.",
        "visual_subheader": "Vía Visual",
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

if disease_extent == t["extent_options"][0]:  # Localized
    risk_group = st.selectbox(t["risk_select"], t["risk_options"])
    st.subheader(t["recommend_subheader"])
    if risk_group == t["risk_options"][0]:
        st.write(t["very_low_risk_write"])
    elif risk_group == t["risk_options"][1]:
        st.write(t["favorable_write"])
    elif risk_group == t["risk_options"][2]:
        st.write(t["unfavorable_write"])
    elif risk_group == t["risk_options"][3]:
        st.write(t["high_risk_write"])

elif disease_extent == t["extent_options"][1]:
    st.subheader(t["recommend_subheader"])
    st.write(t["locally_advanced_write"])

else:  # Metastatic
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
        elif "MMR" in genetic_status:
            st.write(t["genetic_impact_mmr_cr"])
        st.write(t["zulassung_mCRPC"])

# Concise Mermaid with abbreviations and proper quoting to ensure rendering
st.subheader(t["visual_subheader"])
mermaid_code = "graph TD\n"
mermaid_code += "A[Diagnosis] --> B{Genetic}\n"
mermaid_code += f'B -->|"{genetic_status}"| C{{Extent}}\n'
mermaid_code += f'C -->|"{disease_extent}"| D\n'

if "Localized" in disease_extent or "Lokalisiert" in disease_extent or "Localizada" in disease_extent:
    mermaid_code += f'D[Risk: "{risk_group}"] --> E[Therapy]\n'
    if "Very Low" in risk_group or "Sehr niedrig" in risk_group or "Muy bajo" in risk_group:
        mermaid_code += "E --> F[AS primary]\nE --> G[RP/EBRT/Brachy]\n"
    elif "Favorable" in risk_group or "günstig" in risk_group or "favorable" in risk_group:
        mermaid_code += "E --> H[AS or Curative + short ADT]\n"
    elif "Unfavorable" in risk_group or "ungünstig" in risk_group or "desfavorable" in risk_group:
        mermaid_code += "E --> I[RP+ePLND / EBRT+short ADT]\n"
    else:
        mermaid_code += "E --> J[EBRT+long ADT / RP+ePLND]\n"
elif "Advanced" in disease_extent:
    mermaid_code += "D --> K[EBRT+long ADT / RP+ePLND]\n"
else:
    mermaid_code += f'D --> L{{Androgen: "{androgen_status}"}}\n'
    if "Sensitive" in androgen_status or "sensitiv" in androgen_status or "Sensible" in androgen_status:
        mermaid_code += f'L --> M[Volume: "{volume}"]\nM --> N[ADT + ARPI/Docetaxel]\n'
        if "High" in volume:
            mermaid_code += "N --> O[Triple preferred]\n"
        else:
            mermaid_code += "N --> P[Local RT]\n"
    else:
        mermaid_code += "L --> Q[Continue ADT]\nQ --> R[ARPI switch / Docetaxel / Ra-223]\nR --> S[Post-doc: Cabazitaxel / Lu-PSMA]\n"

if "Positive" in genetic_status or "positiv" in genetic_status:
    mermaid_code += "B --> T[HRR+/MMR+ impact on therapy]\nT -.-> E\nT -.-> N\nT -.-> Q\n"

st.markdown(f"```mermaid\n{mermaid_code}\n```")

st.info(t["references"])
