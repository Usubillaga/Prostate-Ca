import streamlit as st

# Define translations
translations = {
    "English": {
        "title": "Prostate Cancer Treatment Algorithm",
        "description": """
This interactive app is based on the 2025 EAU (Uroweb) Guidelines and the German S3-Leitlinie Prostatakarzinom (Version 8.1, 2025). 
It guides from diagnosis to therapy, branching by localized vs. metastatic disease, and for metastatic, by androgen-sensitive (hormone-sensitive) vs. resistant (castration-resistant) status.
Therapies include notes on 'Zulassung' (approval status) where applicable, based on EMA/EU and German contexts. 
This is a simplified representation for educational purposes—consult full guidelines and a physician for clinical use.
""",
        "genetic_subheader": "Genetic Testing Recommendations",
        "genetic_write": """
- **Germline Testing (EAU/German S3)**: Recommended for all patients with metastatic prostate cancer (mPCa), high-risk localized (ISUP ≥3, T3/T4, N1), early-onset (<60 years), family history of PCa or related cancers (breast, ovarian, pancreatic), Ashkenazi Jewish or African ancestry.
- **Genes to Test**: Focus on HRR genes including BRCA1/2, ATM, CHEK2, HOXB13, PALB2; also MMR genes (MLH1, MSH2, MSH6, PMS2) for Lynch syndrome.
- **When to Perform**: At diagnosis for metastatic/high-risk; genetic counseling required prior to testing. Use NGS on blood/saliva.
- **Somatic Testing**: For metastatic (tissue/ctDNA) to identify HRR alterations; prompts germline if positive.
- **Impact**: Positive HRR (esp. BRCA2) indicates aggressive disease; eligibility for PARP inhibitors (e.g., olaparib, niraparib) in mCRPC/mHSPC; platinum chemo; influences active surveillance (cautious in BRCA+); family screening.
- **Prevalence**: 11-16% in metastatic; BRCA2 increases risk of high-grade/metastatic PCa.
""",
        "genetic_select": "Genetic Testing Results:",
        "genetic_options": ["Not Performed/Unknown", "Negative/No Pathogenic Variants", "BRCA1/2 Positive", "Other HRR Positive (e.g., ATM, CHEK2)", "MMR Deficient (MSI-H/dMMR)"],
        "parp_expander": "PARP Inhibitors in Prostate Cancer: Detailed Overview",
        "parp_content": """
PARP (Poly ADP-ribose polymerase) inhibitors are targeted therapies that exploit defects in DNA repair pathways in cancer cells, particularly those with homologous recombination repair (HRR) deficiencies. They work via "synthetic lethality," where inhibiting PARP enzymes in cells already compromised by mutations (e.g., in BRCA1/2 genes) leads to accumulated DNA damage and cell death, while sparing normal cells. In prostate cancer, they are primarily used in advanced stages, especially metastatic castration-resistant prostate cancer (mCRPC), and increasingly in combinations with androgen receptor pathway inhibitors (ARPIs) like abiraterone or enzalutamide.
    
    #### Key Drugs and Mechanisms
    | Drug | Brand Name | Mechanism Notes | Typical Dosage (Standard/Reduced) |
    |------|------------|-----------------|-----------------------------------|
    | Olaparib | Lynparza | Broad PARP1/2/3 inhibition; effective in BRCA1/2 and other HRR mutations. | Monotherapy: 300 mg BID (reduced: 250/200 mg BID). Combo with abiraterone: 300 mg BID + 1000 mg QD abiraterone (reduced: 250/200 mg BID + 500 mg QD). |
    | Niraparib | Zejula | Selective PARP1/2; potent in BRCA-mutated cases. | Combo with abiraterone: 200 mg QD + 1000 mg QD abiraterone (reduced: 100 mg QD + 1000 mg QD). |
    | Talazoparib | Talzenna | Potent PARP1/2 with DNA trapping; strong in HRR mutations. | Combo with enzalutamide: 0.5 mg QD + 160 mg QD enzalutamide (reduced: 0.35/0.25/0.1 mg QD + 120/80 mg QD). |
    | Rucaparib | Rubraca | PARP1/2/3; effective in BRCA1/2/ATM. | Monotherapy: 600 mg BID (not EU-approved for prostate cancer; FDA-approved only). |
    
    - **Emerging**: Saruparib (PARP1-selective) is in trials (e.g., with ARPIs) showing promising safety in advanced prostate cancer, but not yet approved as of 2026.
    
    #### Indications and Recommendations
    - **Primary Use**: mCRPC in patients with HRR gene alterations (e.g., BRCA1/2, ATM, CHEK2, PALB2). Not recommended for hormone-sensitive metastatic prostate cancer (mHSPC) without combinations, non-metastatic CRPC (nmCRPC), or localized disease.
      - **First-Line mCRPC (untreated)**: PARP + ARPI combos if chemotherapy (e.g., docetaxel) is not indicated and HRR/BRCA mutations are present (Strong recommendation, Level 1 evidence).
        - Examples: Abiraterone + olaparib/niraparib; Enzalutamide + talazoparib.
      - **Post-ARPI Progression**: Monotherapy (e.g., olaparib) if BRCA1/2 mutated (Strong, Level 1).
      - **Post-Docetaxel**: Include olaparib if HRR alterations (Strong).
    - **Genetic Impact**: Requires confirmed HRR defects (prevalence: 11-33% in mCRPC; BRCA1/2 ~1/3 of those). Avoid in non-mutated cases due to limited benefit and toxicity.
    - **Other Considerations**: Individualize based on ECOG status, symptoms, comorbidities, and prior therapies. Avoid ARPI sequencing; prioritize PARP if mutations present. For symptomatic bone-predominant disease, consider alternatives like radium-223.
    
    In German S3, emphasis on no routine use without HRD/HRR defects; combos only if chemo ineligible. No recommendations for mHSPC or earlier stages.
    
    #### Evidence from Key Trials (Level 1)
    | Trial | Design/Key Arms | Outcomes (HRR/BRCA Subgroups) |
    |-------|----------------|--------------------------------|
    | PROfound (Olaparib mono) | Phase 3, n=387, post-ARPI | rPFS: 7.4 vs. 3.6 mo (HR 0.34); OS: 19.1 vs. 14.7 mo (HR 0.69). Strongest in BRCA1/2. |
    | PROpel (Olaparib + abiraterone) | Phase 3, n=796 | rPFS: 25.0 vs. 16.4 mo (HR 0.67); OS: 42.1 vs. 34.7 mo (HR 0.81). BRCA: OS HR 0.29. |
    | MAGNITUDE (Niraparib + abiraterone) | Phase 3, n=765 (HRR+) | rPFS: 19.5 vs. 10.9 mo (HR 0.55); OS: 29.3 vs. 28.6 mo (HR 0.88). BRCA-driven. |
    | TALAPRO-2 (Talazoparib + enzalutamide) | Phase 3, n=805 | rPFS: NR vs. 21.9 mo (HR 0.63); HRR: HR 0.45; BRCA: HR 0.20. OS immature. |
    | TRITON-3 (Rucaparib mono) | Phase 3, n=405 | rPFS: 11.2 vs. 6.4 mo (HR 0.50); Benefit in BRCA, not ATM. |
    
    - Meta-analyses: OS benefit mainly in BRCA-mutated (HR 0.69); no OS in unselected patients. Resistance mechanisms (e.g., reversion mutations) emerging in studies.
    
    #### Zulassung (Approvals) in EU/Germany
    - **EMA/EU**: 
      - Olaparib: Approved (2020) for mCRPC with BRCA1/2 post-ARPI; combo with abiraterone (2022) if chemo ineligible.
      - Niraparib: Combo with abiraterone for BRCA1/2 mCRPC (2023).
      - Talazoparib: Combo with enzalutamide for HRR mCRPC (2023).
      - Rucaparib: Not approved for prostate cancer (only ovarian); off-label possible based on FDA.
    - **Germany (G-BA/IQWiG)**: Aligns with EMA; benefit assessments (e.g., Olaparib 2023, Niraparib 2024) confirm added value for mutated cases. Document "chemo not indicated." Some combos off-label if not fully aligned. Reimbursement via statutory health insurance for approved indications; ESMO-MCBS scores available for value assessment.
    
    #### Side Effects and Management
    Common (Grade 3/4): Anemia (46%), neutropenia, thrombocytopenia, nausea, fatigue, venous thromboembolism. Management per guidelines:
    - Blood monitoring; dose reductions (see table above).
    - Transfusions for anemia; G-CSF for febrile neutropenia (no primary prophylaxis).
    - Monitor for secondary malignancies (rare).
    - Patient education on symptoms; supportive care prioritized in S3 (Chapter 7.8.7).
    
    PARP inhibitors represent a precision medicine advance, improving outcomes in ~20-30% of advanced prostate cancer cases with HRR defects. Always consult latest guidelines and molecular boards for personalized use, as data evolves (e.g., resistance studies, new combos like saruparib). For 2026 updates, no major changes noted beyond 2025 integrations.
    """,
        "extent_select": "Select Disease Extent:",
        "extent_options": ["Localized (cT1-2, N0, M0)", "Locally Advanced (cT3-4 or N1, M0)", "Metastatic (M1)"],
        "risk_select": "Select Risk Group (based on PSA, ISUP Grade, T-stage):",
        "risk_options": ["Very Low/Low Risk (PSA <10, ISUP 1, cT1-2a)", 
                         "Intermediate Risk - Favorable (PSA 10-20 or ISUP 2-3 or cT2b, with ≤1 intermediate factor)",
                         "Intermediate Risk - Unfavorable (≥2 intermediate factors, ISUP 2-3, PSA 10-20)",
                         "High Risk (PSA >20 or ISUP ≥4 or cT2c)"],
        "recommend_subheader": "Recommended Pathways and Therapies",
        "very_low_risk_write": """
- **Primary Recommendation**: Active Surveillance (AS) – PSA every 6 months, mpMRI at 12-18 months, re-biopsy if progression indicators (e.g., PI-RADS ≥3, PSA doubling <3 years).
- If AS declined: Radical Prostatectomy (RP) or External Beam Radiotherapy (EBRT, 74-80 Gy) or Brachytherapy (LDR monotherapy).
- No ADT. No lymphadenectomy.
- **Genetic Impact**: If BRCA2+, cautious AS with intensified monitoring; may favor curative therapy.
- **Zulassung Notes**: All standard therapies approved in EU/Germany.
        """,
        "favorable_write": """
- **Options**: Active Surveillance (if no unfavorable features like cribriform pattern) or Curative Therapy.
- Curative: RP (with possible lymphadenectomy if risk >5%) or EBRT (hypofractionated, e.g., 60 Gy/20 fx) + short-term ADT (4-6 months, LHRH agonists/antagonists).
- Focal therapies (e.g., HIFU, Cryotherapy) in select cases, but not standard.
- **Genetic Impact**: BRCA+ may exclude AS; intensify with ADT.
- **Zulassung Notes**: ADT agents (e.g., GnRH analogs) approved; focal therapies may vary by center approval.
        """,
        "unfavorable_write": """
- **Curative Therapy Recommended**: RP with extended pelvic lymphadenectomy (ePLND) or EBRT + short-term ADT (4-6 months).
- Brachytherapy boost possible.
- **Genetic Impact**: HRR+ informs prognosis; consider intensification.
- **Zulassung Notes**: Approved standards; ADT combinations standard.
        """,
        "high_risk_write": """
- **Multimodal Therapy**: EBRT + long-term ADT (24-36 months) or RP + ePLND (adjuvant RT if pT3/R1).
- Brachytherapy boost for select.
- **Genetic Impact**: Recommend germline testing; if HRR+, worse prognosis, consider PARPi trials or intensification.
- **Zulassung Notes**: ADT approved; abiraterone may be considered in some high-risk but not specifically approved for non-metastatic in Germany.
        """,
        "locally_advanced_write": """
- **Risk Stratification**: High-risk features (ISUP 4-5, PSA >20, cT3-4).
- **Diagnosis/Staging**: PSMA-PET/CT recommended over conventional imaging. Recommend germline testing if family history or high-risk.
- **Therapies**: Multimodal – EBRT (IMRT/IGRT, dose-escalated) + long-term ADT (24-36 months, starting pre-RT).
- If operable: RP + ePLND, possibly adjuvant RT.
- For N1: Prostate + pelvic RT + ADT (3 years) + abiraterone (2 years) if ≥2 risk factors.
- Brachytherapy boost (HDR/LDR) for cT3a.
- **Genetic Impact**: If HRR+, consider PARPi in trials; informs prognosis.
- **Zulassung Notes**: Abiraterone not approved in Germany for this indication despite evidence (off-label possible); GnRH analogs approved.
        """,
        "androgen_select": "Select Androgen Status:",
        "androgen_options": ["Hormone-Sensitive (mHSPC)", "Castration-Resistant (mCRPC)"],
        "volume_select": "Select Disease Volume:",
        "volume_options": ["Low-Volume (≤3 bone mets, no visceral)", "High-Volume (≥4 bone mets or visceral)"],
        "mHSPC_write": """
- **Diagnosis/Staging**: PSMA-PET/CT for confirmation; strongly recommend germline testing for all mHSPC (BRCA1/2, HRR genes); somatic if tissue available.
- **Backbone**: Androgen Deprivation Therapy (ADT: GnRH agonist/antagonist or orchiectomy).
- **Add-Ons**: Within 3 months, add ARPI (apalutamide 240mg/d, enzalutamide 160mg/d, darolutamide 600mg BID) or abiraterone (1000mg/d + prednisone 5mg).
- If chemo-eligible: + Docetaxel (75mg/m² q3w, 6 cycles).
- Triple Therapy (ADT + Docetaxel + ARPI, e.g., darolutamide) for high-volume.
- Local Therapy: Prostate RT or SBRT for oligometastatic/low-volume.
- Bone Agents: Denosumab or zoledronic acid for SRE prevention.
        """,
        "low_volume_add": "- Emphasize local RT to metastases for better OS.",
        "high_volume_add": "- Triple therapy preferred.",
        "genetic_impact_hrr": "- **Genetic Impact**: HRR+ (e.g., BRCA): Consider PARP inhibitor combinations (e.g., abiraterone + olaparib/niraparib); improves rPFS/OS; platinum chemo if progression. See PARP expander for details.",
        "genetic_impact_mmr": "- **Genetic Impact**: MMR deficient: Rare; consider immunotherapy (pembrolizumab) if MSI-H.",
        "zulassung_mHSPC": """
- **Zulassung Notes**: 
  - Apalutamide (TITAN): Approved EMA for mHSPC + ADT.
  - Enzalutamide (ARCHES): Approved.
  - Darolutamide (ARANOTE/ARASENS): Approved, including triple.
  - Abiraterone (LATITUDE): Approved EMA but not in Germany for this indication (off-label).
  - Docetaxel: Approved in combination.
  - PARP inhibitors (e.g., olaparib for BRCA+): Approved for HRR mutations in mHSPC/mCRPC.
        """,
        "prior_select": "Select Prior Therapies in mHSPC Phase:",
        "prior_options": ["None/ADT only", "ARPI (e.g., enzalutamide)", "Docetaxel", "Abiraterone"],
        "mCRPC_write": """
- **Diagnosis**: Confirm CRPC (castrate T <50 ng/dl, PSA/radiologic progression); PSMA-PET/CT for imaging; strongly recommend germline/somatic testing for HRR/MMR.
- **Therapies**: Continue ADT; sequence based on prior.
- Asymptomatic: ARPI switch (e.g., if prior abiraterone → enzalutamide) or docetaxel.
- Symptomatic: Docetaxel or radium-223 (for bone-predominant).
- Post-docetaxel: Cabazitaxel, ARPI if not prior, PARP (if BRCA+).
- PSMA-lutetium-177 for PSMA-positive after ARPI/docetaxel.
- Bone agents for SRE.
- **General Sequence**: ADT + ARPI/docetaxel → switch ARPI or chemo → PARP/Ra-223/Lu-PSMA.
        """,
        "post_doc_add": "- Post-docetaxel options: Cabazitaxel (25mg/m² q3w), olaparib (BRCA+), Lu-PSMA.",
        "genetic_impact_hrr_cr": """
- **Genetic Impact**: HRR+ (esp. BRCA1/2): Prioritize PARP inhibitors (olaparib 300mg BID, rucaparib, niraparib, talazoparib) post-ARPI; combinations (e.g., enzalutamide + talazoparib); platinum (carboplatin) if PARPi failure; improves OS/rPFS (e.g., PROfound trial). See PARP expander for details.
        """,
        "genetic_impact_mmr_cr": """
- **Genetic Impact**: MMR deficient/MSI-H: Pembrolizumab (immunotherapy) approved if high TMB/MSI-H (rare in PCa).
        """,
        "zulassung_mCRPC": """
- **Zulassung Notes**:
  - Enzalutamide (PREVAIL/AFFIRM): Approved post-ADT or post-chemo.
  - Abiraterone (COU-AA-302/301): Approved, but sequencing considerations.
  - Darolutamide (ARAMIS for nmCRPC, but extends to m): Approved.
  - Docetaxel/Cabazitaxel: Approved.
  - Radium-223 (ALSYMPCA): Approved for bone mets, no visceral.
  - Lu-PSMA-617 (VISION): Approved EMA for post-ARPI/chemo.
  - PARP (olaparib PROfound, niraparib, talazoparib): Approved for HRR mutations (BRCA1/2 etc.).
  - Note: Some combinations off-label in Germany if not EMA-aligned.
        """,
        "visual_subheader": "Visual Decision Pathway",
        "references": "References: EAU 2025 Guidelines[](https://uroweb.org/guidelines/prostate-cancer); German S3-Leitlinie Version 8.1 (2025). Knowuro-inspired visualization[](https://knowuro.com). Always verify latest updates.",
        "language_select": "Select Language",
        "language_options": ["English", "Deutsch", "Español"]
    },
    "Deutsch": {
        "title": "Algorithmus zur Behandlung von Prostatakrebs",
        "description": """
Diese interaktive App basiert auf den EAU-Richtlinien 2025 (Uroweb) und der deutschen S3-Leitlinie Prostatakarzinom (Version 8.1, 2025).
Sie leitet von der Diagnose zur Therapie, unterteilt nach lokalisiertem vs. metastasiertem Krankheitsbild und für metastasiertes nach androgen-sensitiv (hormon-sensitiv) vs. resistent (kastrationsresistent) Status.
Therapien enthalten Hinweise zur 'Zulassung' (Zulassungsstatus), wo zutreffend, basierend auf EMA/EU und deutschen Kontexten.
Dies ist eine vereinfachte Darstellung zu Bildungszwecken – konsultieren Sie die vollständigen Leitlinien und einen Arzt für klinische Anwendung.
""",
        "genetic_subheader": "Empfehlungen zum Genetischen Testing",
        "genetic_write": """
- **Keimbahn-Testing (EAU/Deutsche S3)**: Empfohlen für alle Patienten mit metastasiertem Prostatakrebs (mPCa), hochrisiko-lokalisiert (ISUP ≥3, T3/T4, N1), frühem Beginn (<60 Jahre), Familiengeschichte von PCa oder verwandten Krebsen (Brust, Ovarial, Pankreas), aschkenasisch-jüdischer oder afrikanischer Abstammung.
- **Zu testende Gene**: Fokus auf HRR-Gene einschließlich BRCA1/2, ATM, CHEK2, HOXB13, PALB2; auch MMR-Gene (MLH1, MSH2, MSH6, PMS2) für Lynch-Syndrom.
- **Wann durchführen**: Bei Diagnose für metastasiertes/hochrisiko; genetische Beratung erforderlich vor Testing. Verwenden Sie NGS auf Blut/Speichel.
- **Somatisches Testing**: Für metastasiertes (Gewebe/ctDNA) zur Identifikation von HRR-Veränderungen; fordert Keimbahn auf, wenn positiv.
- **Auswirkungen**: Positives HRR (bes. BRCA2) deutet auf aggressive Erkrankung hin; Berechtigung für PARP-Inhibitoren (z.B. Olaparib, Niraparib) in mCRPC/mHSPC; Platin-Chemotherapie; beeinflusst aktive Überwachung (vorsichtig bei BRCA+); Familienscreening.
- **Prävalenz**: 11-16% in metastasiertem; BRCA2 erhöht Risiko für hochgradiges/metastasiertes PCa.
""",
        "genetic_select": "Ergebnisse des Genetischen Testings:",
        "genetic_options": ["Nicht durchgeführt/Unbekannt", "Negativ/Keine pathogenen Varianten", "BRCA1/2 Positiv", "Andere HRR Positiv (z.B. ATM, CHEK2)", "MMR-Defizient (MSI-H/dMMR)"],
        "parp_expander": "PARP-Inhibitoren bei Prostatakrebs: Detaillierter Überblick",
        "parp_content": """
PARP (Poly-ADP-Ribose-Polymerase)-Inhibitoren sind zielgerichtete Therapien, die Defekte in DNA-Reparaturwegen in Krebszellen ausnutzen, insbesondere bei Defizienzen in der homologen Rekombinationsreparatur (HRR). Sie wirken über "synthetische Letalität", bei der die Inhibition von PARP-Enzymen in Zellen, die bereits durch Mutationen (z.B. in BRCA1/2-Genen) beeinträchtigt sind, zu akkumulierten DNA-Schäden und Zelltod führt, während normale Zellen verschont werden. Bei Prostatakrebs werden sie hauptsächlich in fortgeschrittenen Stadien verwendet, insbesondere bei metastasiertem kastrationsresistentem Prostatakrebs (mCRPC), und zunehmend in Kombinationen mit Androgen-Rezeptor-Weg-Inhibitoren (ARPIs) wie Abirateron oder Enzalutamid.
    
#### Wichtige Medikamente und Mechanismen
| Medikament | Markenname | Mechanismus-Hinweise | Typische Dosierung (Standard/Reduziert) |
|------------|------------|----------------------|----------------------------------------|
| Olaparib | Lynparza | Breite PARP1/2/3-Inhibition; wirksam bei BRCA1/2 und anderen HRR-Mutationen. | Monotherapie: 300 mg BID (reduziert: 250/200 mg BID). Kombi mit Abirateron: 300 mg BID + 1000 mg QD Abirateron (reduziert: 250/200 mg BID + 500 mg QD). |
| Niraparib | Zejula | Selektiv PARP1/2; potent bei BRCA-mutierten Fällen. | Kombi mit Abirateron: 200 mg QD + 1000 mg QD Abirateron (reduziert: 100 mg QD + 1000 mg QD). |
| Talazoparib | Talzenna | Potent PARP1/2 mit DNA-Falle; stark bei HRR-Mutationen. | Kombi mit Enzalutamid: 0.5 mg QD + 160 mg QD Enzalutamid (reduziert: 0.35/0.25/0.1 mg QD + 120/80 mg QD). |
| Rucaparib | Rubraca | PARP1/2/3; wirksam bei BRCA1/2/ATM. | Monotherapie: 600 mg BID (nicht EU-zugelassen für Prostatakrebs; nur FDA-zugelassen). |
    
- **Emergent**: Saruparib (PARP1-selektiv) in Studien (z.B. mit ARPIs) mit vielversprechender Sicherheit bei fortgeschrittenem Prostatakrebs, aber noch nicht zugelassen ab 2026.
    
#### Indikationen und Empfehlungen
- **Primäre Verwendung**: mCRPC bei Patienten mit HRR-Genveränderungen (z.B. BRCA1/2, ATM, CHEK2, PALB2). Nicht empfohlen für hormon-sensitives metastasiertes Prostatakrebs (mHSPC) ohne Kombinationen, nicht-metastasiertes CRPC (nmCRPC) oder lokalisiertes Krankheitsbild.
  - **Erstlinie mCRPC (unbehandelt)**: PARP + ARPI-Kombis, wenn Chemotherapie (z.B. Docetaxel) nicht indiziert ist und HRR/BRCA-Mutationen vorliegen (Starke Empfehlung, Level 1 Evidenz).
    - Beispiele: Abirateron + Olaparib/Niraparib; Enzalutamid + Talazoparib.
  - **Nach ARPI-Progression**: Monotherapie (z.B. Olaparib), wenn BRCA1/2 mutiert (Stark, Level 1).
  - **Nach Docetaxel**: Olaparib einbeziehen, wenn HRR-Veränderungen (Stark).
- **Genetische Auswirkungen**: Erfordert bestätigte HRR-Defekte (Prävalenz: 11-33% in mCRPC; BRCA1/2 ~1/3 davon). Vermeiden bei nicht-mutierten Fällen aufgrund begrenzten Nutzens und Toxizität.
- **Andere Überlegungen**: Individualisieren basierend auf ECOG-Status, Symptomen, Komorbiditäten und vorherigen Therapien. Vermeiden ARPI-Sequenzierung; priorisieren PARP, wenn Mutationen vorliegen. Bei symptomatischer knochen-dominierter Erkrankung Alternativen wie Radium-223 in Betracht ziehen.
    
In der deutschen S3 Betonung auf keine Routineverwendung ohne HRD/HRR-Defekte; Kombis nur, wenn Chemo nicht geeignet. Keine Empfehlungen für mHSPC oder frühere Stadien.
    
#### Evidenz aus Schlüsselstudien (Level 1)
| Studie | Design/Schlüsselarme | Ergebnisse (HRR/BRCA-Subgruppen) |
|--------|----------------------|----------------------------------|
| PROfound (Olaparib mono) | Phase 3, n=387, post-ARPI | rPFS: 7.4 vs. 3.6 Mo (HR 0.34); OS: 19.1 vs. 14.7 Mo (HR 0.69). Stärkste bei BRCA1/2. |
| PROpel (Olaparib + Abirateron) | Phase 3, n=796 | rPFS: 25.0 vs. 16.4 Mo (HR 0.67); OS: 42.1 vs. 34.7 Mo (HR 0.81). BRCA: OS HR 0.29. |
| MAGNITUDE (Niraparib + Abirateron) | Phase 3, n=765 (HRR+) | rPFS: 19.5 vs. 10.9 Mo (HR 0.55); OS: 29.3 vs. 28.6 Mo (HR 0.88). BRCA-getrieben. |
| TALAPRO-2 (Talazoparib + Enzalutamid) | Phase 3, n=805 | rPFS: NR vs. 21.9 Mo (HR 0.63); HRR: HR 0.45; BRCA: HR 0.20. OS unreif. |
| TRITON-3 (Rucaparib mono) | Phase 3, n=405 | rPFS: 11.2 vs. 6.4 Mo (HR 0.50); Nutzen bei BRCA, nicht ATM. |
    
- Meta-Analysen: OS-Nutzen hauptsächlich bei BRCA-mutiert (HR 0.69); kein OS bei unselektionierten Patienten. Resistenzmechanismen (z.B. Reversionsmutationen) in Studien auftauchend.
    
#### Zulassung in EU/Deutschland
- **EMA/EU**: 
  - Olaparib: Zugelassen (2020) für mCRPC mit BRCA1/2 post-ARPI; Kombi mit Abirateron (2022), wenn Chemo nicht geeignet.
  - Niraparib: Kombi mit Abirateron für BRCA1/2 mCRPC (2023).
  - Talazoparib: Kombi mit Enzalutamid für HRR mCRPC (2023).
  - Rucaparib: Nicht zugelassen für Prostatakrebs (nur Ovarial); off-label möglich basierend auf FDA.
- **Deutschland (G-BA/IQWiG)**: Stimmt mit EMA überein; Nutzenbewertungen (z.B. Olaparib 2023, Niraparib 2024) bestätigen zusätzlichen Wert für mutierte Fälle. Dokumentieren "Chemo nicht indiziert." Einige Kombis off-label, wenn nicht vollständig EMA-konform. Erstattung über gesetzliche Krankenkassen für zugelassene Indikationen; ESMO-MCBS-Scores für Wertbewertung verfügbar.
    
#### Nebenwirkungen und Management
Häufig (Grad 3/4): Anämie (46%), Neutropenie, Thrombozytopenie, Übelkeit, Müdigkeit, venöse Thromboembolie. Management gemäß Leitlinien:
- Blutüberwachung; Dosisreduktionen (siehe Tabelle oben).
- Transfusionen für Anämie; G-CSF für fiebrige Neutropenie (keine primäre Prophylaxe).
- Überwachen auf sekundäre Malignome (selten).
- Patientenaufklärung zu Symptomen; supportive Pflege priorisiert in S3 (Kapitel 7.8.7).
    
PARP-Inhibitoren stellen einen Fortschritt in der Präzisionsmedizin dar, verbessern Ergebnisse in ~20-30% der fortgeschrittenen Prostatakrebsfälle mit HRR-Defekten. Immer aktuelle Leitlinien und molekulare Boards für personalisierte Verwendung konsultieren, da Daten sich entwickeln (z.B. Resistenzstudien, neue Kombis wie Saruparib). Für 2026-Updates keine großen Änderungen über 2025-Integrationen hinaus notiert.
    """,
        "extent_select": "Ausmaß der Erkrankung auswählen:",
        "extent_options": ["Lokalisiert (cT1-2, N0, M0)", "Lokal fortgeschritten (cT3-4 oder N1, M0)", "Metastasiert (M1)"],
        "risk_select": "Risikogruppe auswählen (basierend auf PSA, ISUP-Grad, T-Stadium):",
        "risk_options": ["Sehr niedrig/niedrig Risiko (PSA <10, ISUP 1, cT1-2a)", 
                         "Intermediäres Risiko - Günstig (PSA 10-20 oder ISUP 2-3 oder cT2b, mit ≤1 intermediärem Faktor)",
                         "Intermediäres Risiko - Ungünstig (≥2 intermediäre Faktoren, ISUP 2-3, PSA 10-20)",
                         "Hohes Risiko (PSA >20 oder ISUP ≥4 oder cT2c)"],
        "recommend_subheader": "Empfohlene Pfade und Therapien",
        "very_low_risk_write": """
- **Primäre Empfehlung**: Aktive Überwachung (AS) – PSA alle 6 Monate, mpMRI bei 12-18 Monaten, Re-Biopsie bei Progressionsindikatoren (z.B. PI-RADS ≥3, PSA-Verdopplung <3 Jahre).
- Wenn AS abgelehnt: Radikale Prostatektomie (RP) oder Externe Strahlentherapie (EBRT, 74-80 Gy) oder Brachytherapie (LDR-Monotherapie).
- Kein ADT. Keine Lymphadenektomie.
- **Genetische Auswirkungen**: Bei BRCA2+ vorsichtige AS mit intensivierter Überwachung; könnte kurative Therapie bevorzugen.
- **Zulassungs-Hinweise**: Alle Standardtherapien in EU/Deutschland zugelassen.
        """,
        "favorable_write": """
- **Optionen**: Aktive Überwachung (wenn keine ungünstigen Merkmale wie kribriformes Muster) oder Kurative Therapie.
- Kurativ: RP (mit möglicher Lymphadenektomie bei Risiko >5%) oder EBRT (hypofraktioniert, z.B. 60 Gy/20 fx) + kurzfristiges ADT (4-6 Monate, LHRH-Agonisten/Antagonisten).
- Fokale Therapien (z.B. HIFU, Kryotherapie) in ausgewählten Fällen, aber nicht Standard.
- **Genetische Auswirkungen**: BRCA+ könnte AS ausschließen; mit ADT intensivieren.
- **Zulassungs-Hinweise**: ADT-Mittel (z.B. GnRH-Analoga) zugelassen; fokale Therapien können je nach Zentrum variieren.
        """,
        "unfavorable_write": """
- **Kurative Therapie empfohlen**: RP mit erweiterter pelviner Lymphadenektomie (ePLND) oder EBRT + kurzfristiges ADT (4-6 Monate).
- Brachytherapie-Boost möglich.
- **Genetische Auswirkungen**: HRR+ informiert Prognose; Intensivierung in Betracht ziehen.
- **Zulassungs-Hinweise**: Zugelassene Standards; ADT-Kombinationen Standard.
        """,
        "high_risk_write": """
- **Multimodale Therapie**: EBRT + langfristiges ADT (24-36 Monate) oder RP + ePLND (adjuvante RT bei pT3/R1).
- Brachytherapie-Boost für ausgewählte.
- **Genetische Auswirkungen**: Keimbahn-Testing empfohlen; bei HRR+ schlechtere Prognose, PARPi-Studien oder Intensivierung in Betracht ziehen.
- **Zulassungs-Hinweise**: ADT zugelassen; Abirateron kann in einigen hochrisiko betrachtet werden, aber nicht spezifisch für nicht-metastasiertes in Deutschland zugelassen.
        """,
        "locally_advanced_write": """
- **Risikostratifizierung**: Hochrisiko-Merkmale (ISUP 4-5, PSA >20, cT3-4).
- **Diagnose/Staging**: PSMA-PET/CT empfohlen über konventionelle Bildgebung. Keimbahn-Testing empfohlen bei Familiengeschichte oder hochrisiko.
- **Therapien**: Multimodal – EBRT (IMRT/IGRT, dosis-eskaliert) + langfristiges ADT (24-36 Monate, vor RT beginnend).
- Wenn operabel: RP + ePLND, möglicherweise adjuvante RT.
- Für N1: Prostata + pelvine RT + ADT (3 Jahre) + Abirateron (2 Jahre) bei ≥2 Risikofaktoren.
- Brachytherapie-Boost (HDR/LDR) für cT3a.
- **Genetische Auswirkungen**: Bei HRR+ PARPi in Studien in Betracht ziehen; informiert Prognose.
- **Zulassungs-Hinweise**: Abirateron nicht in Deutschland für diese Indikation zugelassen trotz Evidenz (off-label möglich); GnRH-Analoga zugelassen.
        """,
        "androgen_select": "Androgen-Status auswählen:",
        "androgen_options": ["Hormon-sensitiv (mHSPC)", "Kastrationsresistent (mCRPC)"],
        "volume_select": "Krankheitsvolumen auswählen:",
        "volume_options": ["Niedriges Volumen (≤3 Knochenmetastasen, kein viszerales)", "Hohes Volumen (≥4 Knochenmetastasen oder viszerales)"],
        "mHSPC_write": """
- **Diagnose/Staging**: PSMA-PET/CT zur Bestätigung; dringend Keimbahn-Testing für alle mHSPC empfohlen (BRCA1/2, HRR-Gene); somatisch, wenn Gewebe verfügbar.
- **Backbone**: Androgen-Deprivations-Therapie (ADT: GnRH-Agonist/Antagonist oder Orchiektomie).
- **Zusätze**: Innerhalb 3 Monate ARPI hinzufügen (Apalutamid 240mg/d, Enzalutamid 160mg/d, Darolutamid 600mg BID) oder Abirateron (1000mg/d + Prednison 5mg).
- Wenn chemo-geeignet: + Docetaxel (75mg/m² q3w, 6 Zyklen).
- Triple-Therapie (ADT + Docetaxel + ARPI, z.B. Darolutamid) für hohes Volumen.
- Lokale Therapie: Prostata-RT oder SBRT für oligometastasiertes/niedriges Volumen.
- Knochenmittel: Denosumab oder Zoledronsäure zur SRE-Prävention.
        """,
        "low_volume_add": "- Betonung auf lokale RT zu Metastasen für besseres OS.",
        "high_volume_add": "- Triple-Therapie bevorzugt.",
        "genetic_impact_hrr": "- **Genetische Auswirkungen**: HRR+ (z.B. BRCA): PARP-Inhibitor-Kombinationen in Betracht ziehen (z.B. Abirateron + Olaparib/Niraparib); verbessert rPFS/OS; Platin-Chemo bei Progression. Siehe PARP-Expander für Details.",
        "genetic_impact_mmr": "- **Genetische Auswirkungen**: MMR-defizient: Selten; Immuntherapie (Pembrolizumab) in Betracht ziehen, wenn MSI-H.",
        "zulassung_mHSPC": """
- **Zulassungs-Hinweise**: 
  - Apalutamid (TITAN): EMA-zugelassen für mHSPC + ADT.
  - Enzalutamid (ARCHES): Zugelassen.
  - Darolutamid (ARANOTE/ARASENS): Zugelassen, inklusive Triple.
  - Abirateron (LATITUDE): EMA-zugelassen, aber nicht in Deutschland für diese Indikation (off-label).
  - Docetaxel: Zugelassen in Kombination.
  - PARP-Inhibitoren (z.B. Olaparib für BRCA+): Zugelassen für HRR-Mutationen in mHSPC/mCRPC.
        """,
        "prior_select": "Vorherige Therapien in mHSPC-Phase auswählen:",
        "prior_options": ["Keine/ADT nur", "ARPI (z.B. Enzalutamid)", "Docetaxel", "Abirateron"],
        "mCRPC_write": """
- **Diagnose**: CRPC bestätigen (kastrierter T <50 ng/dl, PSA/radiologische Progression); PSMA-PET/CT für Bildgebung; dringend Keimbahn/somatisches Testing für HRR/MMR empfohlen.
- **Therapien**: ADT fortsetzen; Sequenz basierend auf vorherigem.
- Asymptomatisch: ARPI-Wechsel (z.B. bei vorherigem Abirateron → Enzalutamid) oder Docetaxel.
- Symptomatisch: Docetaxel oder Radium-223 (für knochen-dominierend).
- Nach Docetaxel: Cabazitaxel, ARPI wenn nicht vorherig, PARP (bei BRCA+).
- PSMA-Lutetium-177 für PSMA-positiv nach ARPI/Docetaxel.
- Knochenmittel für SRE.
- **Allgemeine Sequenz**: ADT + ARPI/Docetaxel → ARPI-Wechsel oder Chemo → PARP/Ra-223/Lu-PSMA.
        """,
        "post_doc_add": "- Optionen nach Docetaxel: Cabazitaxel (25mg/m² q3w), Olaparib (BRCA+), Lu-PSMA.",
        "genetic_impact_hrr_cr": """
- **Genetische Auswirkungen**: HRR+ (bes. BRCA1/2): PARP-Inhibitoren priorisieren (Olaparib 300mg BID, Rucaparib, Niraparib, Talazoparib) nach ARPI; Kombinationen (z.B. Enzalutamid + Talazoparib); Platin (Carboplatin) bei PARPi-Versagen; verbessert OS/rPFS (z.B. PROfound-Studie). Siehe PARP-Expander für Details.
        """,
        "genetic_impact_mmr_cr": """
- **Genetische Auswirkungen**: MMR-defizient/MSI-H: Pembrolizumab (Immuntherapie) zugelassen, wenn hohes TMB/MSI-H (selten bei PCa).
        """,
        "zulassung_mCRPC": """
- **Zulassungs-Hinweise**:
  - Enzalutamid (PREVAIL/AFFIRM): Zugelassen nach ADT oder nach Chemo.
  - Abirateron (COU-AA-302/301): Zugelassen, aber Sequenzierungsüberlegungen.
  - Darolutamid (ARAMIS für nmCRPC, erweitert auf m): Zugelassen.
  - Docetaxel/Cabazitaxel: Zugelassen.
  - Radium-223 (ALSYMPCA): Zugelassen für Knochenmetastasen, kein viszerales.
  - Lu-PSMA-617 (VISION): EMA-zugelassen für nach ARPI/Chemo.
  - PARP (Olaparib PROfound, Niraparib, Talazoparib): Zugelassen für HRR-Mutationen (BRCA1/2 usw.).
  - Hinweis: Einige Kombinationen off-label in Deutschland, wenn nicht EMA-konform.
        """,
        "visual_subheader": "Visueller Entscheidungspfad",
        "references": "Referenzen: EAU 2025 Richtlinien[](https://uroweb.org/guidelines/prostate-cancer); Deutsche S3-Leitlinie Version 8.1 (2025). Knowuro-inspirierte Visualisierung[](https://knowuro.com). Immer neueste Updates überprüfen.",
        "language_select": "Sprache auswählen",
        "language_options": ["English", "Deutsch", "Español"]
    },
    "Español": {
        "title": "Algoritmo de Tratamiento del Cáncer de Próstata",
        "description": """
Esta aplicación interactiva se basa en las Guías EAU 2025 (Uroweb) y la Guía Alemana S3 Prostatakarzinom (Versión 8.1, 2025).
Guía desde el diagnóstico hasta la terapia, ramificando por enfermedad localizada vs. metastásica, y para metastásica, por sensible a andrógenos (sensible a hormonas) vs. resistente (resistente a la castración).
Las terapias incluyen notas sobre 'Zulassung' (estado de aprobación) donde corresponda, basado en EMA/UE y contextos alemanes.
Esta es una representación simplificada con fines educativos—consulte las guías completas y un médico para uso clínico.
""",
        "genetic_subheader": "Recomendaciones de Pruebas Genéticas",
        "genetic_write": """
- **Pruebas Germinales (EAU/S3 Alemana)**: Recomendadas para todos los pacientes con cáncer de próstata metastásico (mPCa), localizado de alto riesgo (ISUP ≥3, T3/T4, N1), inicio temprano (<60 años), historia familiar de PCa o cánceres relacionados (mama, ovario, páncreas), ascendencia judía asquenazí o africana.
- **Genes a Probar**: Enfoque en genes HRR incluyendo BRCA1/2, ATM, CHEK2, HOXB13, PALB2; también genes MMR (MLH1, MSH2, MSH6, PMS2) para síndrome de Lynch.
- **Cuándo Realizar**: En el diagnóstico para metastásico/alto riesgo; asesoramiento genético requerido antes de la prueba. Use NGS en sangre/saliva.
- **Pruebas Somáticas**: Para metastásico (tejido/ctDNA) para identificar alteraciones HRR; impulsa germinal si positivo.
- **Impacto**: HRR positivo (esp. BRCA2) indica enfermedad agresiva; elegibilidad para inhibidores PARP (ej. olaparib, niraparib) en mCRPC/mHSPC; quimio con platino; influye en vigilancia activa (cautelosa en BRCA+); cribado familiar.
- **Prevalencia**: 11-16% en metastásico; BRCA2 aumenta el riesgo de PCa de alto grado/metastásico.
""",
        "genetic_select": "Resultados de Pruebas Genéticas:",
        "genetic_options": ["No Realizada/Desconocida", "Negativa/Sin Variantes Patogénicas", "BRCA1/2 Positiva", "Otra HRR Positiva (ej. ATM, CHEK2)", "Deficiente en MMR (MSI-H/dMMR)"],
        "parp_expander": "Inhibidores PARP en Cáncer de Próstata: Visión Detallada",
        "parp_content": """
Los inhibidores PARP (Poly ADP-ribose polimerasa) son terapias dirigidas que explotan defectos en vías de reparación de ADN en células cancerosas, particularmente aquellas con deficiencias en reparación por recombinación homóloga (HRR). Funcionan a través de "letalidad sintética", donde la inhibición de enzimas PARP en células ya comprometidas por mutaciones (ej. en genes BRCA1/2) lleva a daño acumulado en ADN y muerte celular, mientras ahorra células normales. En cáncer de próstata, se usan principalmente en etapas avanzadas, especialmente cáncer de próstata metastásico resistente a la castración (mCRPC), y cada vez más en combinaciones con inhibidores de la vía del receptor de andrógenos (ARPIs) como abiraterona o enzalutamida.
    
#### Fármacos Clave y Mecanismos
| Fármaco | Nombre Comercial | Notas de Mecanismo | Dosificación Típica (Estándar/Reducida) |
|---------|------------------|--------------------|-----------------------------------------|
| Olaparib | Lynparza | Inhibición amplia PARP1/2/3; efectivo en BRCA1/2 y otras mutaciones HRR. | Monoterapia: 300 mg BID (reducida: 250/200 mg BID). Combo con abiraterona: 300 mg BID + 1000 mg QD abiraterona (reducida: 250/200 mg BID + 500 mg QD). |
| Niraparib | Zejula | Selectivo PARP1/2; potente en casos mutados BRCA. | Combo con abiraterona: 200 mg QD + 1000 mg QD abiraterona (reducida: 100 mg QD + 1000 mg QD). |
| Talazoparib | Talzenna | Potente PARP1/2 con atrapamiento de ADN; fuerte en mutaciones HRR. | Combo con enzalutamida: 0.5 mg QD + 160 mg QD enzalutamida (reducida: 0.35/0.25/0.1 mg QD + 120/80 mg QD). |
| Rucaparib | Rubraca | PARP1/2/3; efectivo en BRCA1/2/ATM. | Monoterapia: 600 mg BID (no aprobado en UE para cáncer de próstata; solo FDA). |
    
- **Emergente**: Saruparib (selectivo PARP1) en ensayos (ej. con ARPIs) mostrando seguridad prometedora en cáncer de próstata avanzado, pero no aprobado a partir de 2026.
    
#### Indicaciones y Recomendaciones
- **Uso Primario**: mCRPC en pacientes con alteraciones en genes HRR (ej. BRCA1/2, ATM, CHEK2, PALB2). No recomendado para cáncer de próstata metastásico sensible a hormonas (mHSPC) sin combinaciones, CRPC no metastásico (nmCRPC), o enfermedad localizada.
  - **Primera Línea mCRPC (sin tratar)**: Combos PARP + ARPI si quimioterapia (ej. docetaxel) no está indicada y mutaciones HRR/BRCA presentes (Recomendación fuerte, Nivel 1 de evidencia).
    - Ejemplos: Abiraterona + olaparib/niraparib; Enzalutamida + talazoparib.
  - **Progresión Post-ARPI**: Monoterapia (ej. olaparib) si mutado BRCA1/2 (Fuerte, Nivel 1).
  - **Post-Docetaxel**: Incluir olaparib si alteraciones HRR (Fuerte).
- **Impacto Genético**: Requiere defectos HRR confirmados (prevalencia: 11-33% en mCRPC; BRCA1/2 ~1/3 de esos). Evitar en casos no mutados debido a beneficio limitado y toxicidad.
- **Otras Consideraciones**: Individualizar basado en estado ECOG, síntomas, comorbilidades y terapias previas. Evitar secuenciación ARPI; priorizar PARP si mutaciones presentes. Para enfermedad ósea sintomática predominante, considerar alternativas como radium-223.
    
En S3 Alemana, énfasis en no uso rutinario sin defectos HRD/HRR; combos solo si quimio no elegible. No recomendaciones para mHSPC o etapas anteriores.
    
#### Evidencia de Ensayos Clave (Nivel 1)
| Ensayo | Diseño/Brazos Clave | Resultados (Subgrupos HRR/BRCA) |
|--------|---------------------|----------------------------------|
| PROfound (Olaparib mono) | Fase 3, n=387, post-ARPI | rPFS: 7.4 vs. 3.6 mo (HR 0.34); OS: 19.1 vs. 14.7 mo (HR 0.69). Más fuerte en BRCA1/2. |
| PROpel (Olaparib + abiraterona) | Fase 3, n=796 | rPFS: 25.0 vs. 16.4 mo (HR 0.67); OS: 42.1 vs. 34.7 mo (HR 0.81). BRCA: OS HR 0.29. |
| MAGNITUDE (Niraparib + abiraterona) | Fase 3, n=765 (HRR+) | rPFS: 19.5 vs. 10.9 mo (HR 0.55); OS: 29.3 vs. 28.6 mo (HR 0.88). Impulsado por BRCA. |
| TALAPRO-2 (Talazoparib + enzalutamida) | Fase 3, n=805 | rPFS: NR vs. 21.9 mo (HR 0.63); HRR: HR 0.45; BRCA: HR 0.20. OS inmaduro. |
| TRITON-3 (Rucaparib mono) | Fase 3, n=405 | rPFS: 11.2 vs. 6.4 mo (HR 0.50); Beneficio en BRCA, no ATM. |
    
- Meta-análisis: Beneficio OS principalmente en mutados BRCA (HR 0.69); no OS en pacientes no seleccionados. Mecanismos de resistencia (ej. mutaciones de reversión) emergiendo en estudios.
    
#### Aprobación en UE/Alemania
- **EMA/UE**: 
  - Olaparib: Aprobado (2020) para mCRPC con BRCA1/2 post-ARPI; combo con abiraterona (2022) si quimio no elegible.
  - Niraparib: Combo con abiraterona para mCRPC BRCA1/2 (2023).
  - Talazoparib: Combo con enzalutamida para mCRPC HRR (2023).
  - Rucaparib: No aprobado para cáncer de próstata (solo ovárico); off-label posible basado en FDA.
- **Alemania (G-BA/IQWiG)**: Alineado con EMA; evaluaciones de beneficio (ej. Olaparib 2023, Niraparib 2024) confirman valor agregado para casos mutados. Documentar "quimio no indicada". Algunos combos off-label si no alineados completamente con EMA. Reembolso a través de seguro de salud estatutario para indicaciones aprobadas; puntuaciones ESMO-MCBS disponibles para evaluación de valor.
    
#### Efectos Secundarios y Manejo
Comunes (Grado 3/4): Anemia (46%), neutropenia, trombocitopenia, náuseas, fatiga, tromboembolismo venoso. Manejo según guías:
- Monitoreo sanguíneo; reducciones de dosis (ver tabla arriba).
- Transfusiones para anemia; G-CSF para neutropenia febril (sin profilaxis primaria).
- Monitorear malignidades secundarias (raro).
- Educación al paciente sobre síntomas; cuidado de soporte priorizado en S3 (Capítulo 7.8.7).
    
Los inhibidores PARP representan un avance en medicina de precisión, mejorando resultados en ~20-30% de casos de cáncer de próstata avanzado con defectos HRR. Siempre consulte guías más recientes y juntas moleculares para uso personalizado, ya que los datos evolucionan (ej. estudios de resistencia, nuevos combos como saruparib). Para actualizaciones 2026, no se notan cambios mayores más allá de integraciones 2025.
    """,
        "extent_select": "Seleccionar Extensión de la Enfermedad:",
        "extent_options": ["Localizada (cT1-2, N0, M0)", "Localmente Avanzada (cT3-4 o N1, M0)", "Metastásica (M1)"],
        "risk_select": "Seleccionar Grupo de Riesgo (basado en PSA, Grado ISUP, Estadio T):",
        "risk_options": ["Muy Bajo/Bajo Riesgo (PSA <10, ISUP 1, cT1-2a)", 
                         "Riesgo Intermedio - Favorable (PSA 10-20 o ISUP 2-3 o cT2b, con ≤1 factor intermedio)",
                         "Riesgo Intermedio - Desfavorable (≥2 factores intermedios, ISUP 2-3, PSA 10-20)",
                         "Alto Riesgo (PSA >20 o ISUP ≥4 o cT2c)"],
        "recommend_subheader": "Vías y Terapias Recomendadas",
        "very_low_risk_write": """
- **Recomendación Primaria**: Vigilancia Activa (AS) – PSA cada 6 meses, mpMRI a 12-18 meses, re-biopsia si indicadores de progresión (ej. PI-RADS ≥3, duplicación PSA <3 años).
- Si AS rechazada: Prostatectomía Radical (RP) o Radioterapia de Haz Externo (EBRT, 74-80 Gy) o Braquiterapia (LDR monoterapia).
- Sin ADT. Sin linfadenectomía.
- **Impacto Genético**: Si BRCA2+, AS cautelosa con monitoreo intensificado; puede favorecer terapia curativa.
- **Notas de Aprobación**: Todas las terapias estándar aprobadas en UE/Alemania.
        """,
        "favorable_write": """
- **Opciones**: Vigilancia Activa (si no hay características desfavorables como patrón cribriforme) o Terapia Curativa.
- Curativa: RP (con posible linfadenectomía si riesgo >5%) o EBRT (hipofraccionada, ej. 60 Gy/20 fx) + ADT a corto plazo (4-6 meses, agonistas/antagonistas LHRH).
- Terapias focales (ej. HIFU, Crioterapia) en casos seleccionados, pero no estándar.
- **Impacto Genético**: BRCA+ puede excluir AS; intensificar con ADT.
- **Notas de Aprobación**: Agentes ADT (ej. análogos GnRH) aprobados; terapias focales pueden variar por centro.
        """,
        "unfavorable_write": """
- **Terapia Curativa Recomendada**: RP con linfadenectomía pélvica extendida (ePLND) o EBRT + ADT a corto plazo (4-6 meses).
- Boost de braquiterapia posible.
- **Impacto Genético**: HRR+ informa pronóstico; considerar intensificación.
- **Notas de Aprobación**: Estándares aprobados; combinaciones ADT estándar.
        """,
        "high_risk_write": """
- **Terapia Multimodal**: EBRT + ADT a largo plazo (24-36 meses) o RP + ePLND (RT adyuvante si pT3/R1).
- Boost de braquiterapia para seleccionados.
- **Impacto Genético**: Recomendar pruebas germinales; si HRR+, peor pronóstico, considerar ensayos PARPi o intensificación.
- **Notas de Aprobación**: ADT aprobado; abiraterona puede considerarse en algunos de alto riesgo pero no específicamente aprobado para no metastásico en Alemania.
        """,
        "locally_advanced_write": """
- **Estratificación de Riesgo**: Características de alto riesgo (ISUP 4-5, PSA >20, cT3-4).
- **Diagnóstico/Estadificación**: PSMA-PET/CT recomendado sobre imagen convencional. Recomendar pruebas germinales si historia familiar o alto riesgo.
- **Terapias**: Multimodal – EBRT (IMRT/IGRT, escalada de dosis) + ADT a largo plazo (24-36 meses, iniciando pre-RT).
- Si operable: RP + ePLND, posiblemente RT adyuvante.
- Para N1: Próstata + RT pélvica + ADT (3 años) + abiraterona (2 años) si ≥2 factores de riesgo.
- Boost de braquiterapia (HDR/LDR) para cT3a.
- **Impacto Genético**: Si HRR+, considerar PARPi en ensayos; informa pronóstico.
- **Notas de Aprobación**: Abiraterona no aprobada en Alemania para esta indicación a pesar de evidencia (off-label posible); análogos GnRH aprobados.
        """,
        "androgen_select": "Seleccionar Estado de Andrógenos:",
        "androgen_options": ["Sensible a Hormonas (mHSPC)", "Resistente a la Castración (mCRPC)"],
        "volume_select": "Seleccionar Volumen de Enfermedad:",
        "volume_options": ["Bajo Volumen (≤3 mets óseas, sin visceral)", "Alto Volumen (≥4 mets óseas o visceral)"],
        "mHSPC_write": """
- **Diagnóstico/Estadificación**: PSMA-PET/CT para confirmación; recomendar fuertemente pruebas germinales para todo mHSPC (BRCA1/2, genes HRR); somática si tejido disponible.
- **Base**: Terapia de Privación de Andrógenos (ADT: agonista/antagonista GnRH o orquiectomía).
- **Adiciones**: Dentro de 3 meses, agregar ARPI (apalutamida 240mg/d, enzalutamida 160mg/d, darolutamida 600mg BID) o abiraterona (1000mg/d + prednisona 5mg).
- Si elegible para quimio: + Docetaxel (75mg/m² q3w, 6 ciclos).
- Terapia Triple (ADT + Docetaxel + ARPI, ej. darolutamida) para alto volumen.
- Terapia Local: RT de próstata o SBRT para oligometastásico/bajo volumen.
- Agentes Óseos: Denosumab o ácido zoledrónico para prevención SRE.
        """,
        "low_volume_add": "- Enfatizar RT local a metástasis para mejor OS.",
        "high_volume_add": "- Terapia triple preferida.",
        "genetic_impact_hrr": "- **Impacto Genético**: HRR+ (ej. BRCA): Considerar combinaciones de inhibidores PARP (ej. abiraterona + olaparib/niraparib); mejora rPFS/OS; quimio con platino si progresión. Ver expansor PARP para detalles.",
        "genetic_impact_mmr": "- **Impacto Genético**: Deficiente en MMR: Raro; considerar inmunoterapia (pembrolizumab) si MSI-H.",
        "zulassung_mHSPC": """
- **Notas de Aprobación**: 
  - Apalutamida (TITAN): Aprobada EMA para mHSPC + ADT.
  - Enzalutamida (ARCHES): Aprobada.
  - Darolutamida (ARANOTE/ARASENS): Aprobada, incluyendo triple.
  - Abiraterona (LATITUDE): Aprobada EMA pero no en Alemania para esta indicación (off-label).
  - Docetaxel: Aprobada en combinación.
  - Inhibidores PARP (ej. olaparib para BRCA+): Aprobados para mutaciones HRR en mHSPC/mCRPC.
        """,
        "prior_select": "Seleccionar Terapias Previas en Fase mHSPC:",
        "prior_options": ["Ninguna/ADT solo", "ARPI (ej. enzalutamida)", "Docetaxel", "Abiraterona"],
        "mCRPC_write": """
- **Diagnóstico**: Confirmar CRPC (T castrado <50 ng/dl, progresión PSA/radiológica); PSMA-PET/CT para imagen; recomendar fuertemente pruebas germinales/somáticas para HRR/MMR.
- **Terapias**: Continuar ADT; secuencia basada en previo.
- Asintomático: Cambio ARPI (ej. si abiraterona previa → enzalutamida) o docetaxel.
- Sintomático: Docetaxel o radium-223 (para predominante óseo).
- Post-docetaxel: Cabazitaxel, ARPI si no previo, PARP (si BRCA+).
- PSMA-lutetio-177 para PSMA-positivo después ARPI/docetaxel.
- Agentes óseos para SRE.
- **Secuencia General**: ADT + ARPI/docetaxel → cambio ARPI o quimio → PARP/Ra-223/Lu-PSMA.
        """,
        "post_doc_add": "- Opciones post-docetaxel: Cabazitaxel (25mg/m² q3w), olaparib (BRCA+), Lu-PSMA.",
        "genetic_impact_hrr_cr": """
- **Impacto Genético**: HRR+ (esp. BRCA1/2): Priorizar inhibidores PARP (olaparib 300mg BID, rucaparib, niraparib, talazoparib) post-ARPI; combinaciones (ej. enzalutamida + talazoparib); platino (carboplatino) si fracaso PARPi; mejora OS/rPFS (ej. ensayo PROfound). Ver expansor PARP para detalles.
        """,
        "genetic_impact_mmr_cr": """
- **Impacto Genético**: Deficiente en MMR/MSI-H: Pembrolizumab (inmunoterapia) aprobado si alto TMB/MSI-H (raro en PCa).
        """,
        "zulassung_mCRPC": """
- **Notas de Aprobación**:
  - Enzalutamida (PREVAIL/AFFIRM): Aprobada post-ADT o post-quimio.
  - Abiraterona (COU-AA-302/301): Aprobada, pero consideraciones de secuenciación.
  - Darolutamida (ARAMIS para nmCRPC, se extiende a m): Aprobada.
  - Docetaxel/Cabazitaxel: Aprobadas.
  - Radium-223 (ALSYMPCA): Aprobada para mets óseas, sin visceral.
  - Lu-PSMA-617 (VISION): Aprobada EMA para post-ARPI/quimio.
  - PARP (olaparib PROfound, niraparib, talazoparib): Aprobadas para mutaciones HRR (BRCA1/2 etc.).
  - Nota: Algunas combinaciones off-label en Alemania si no alineadas con EMA.
        """,
        "visual_subheader": "Vía de Decisión Visual",
        "references": "Referencias: Guías EAU 2025[](https://uroweb.org/guidelines/prostate-cancer); Guía Alemana S3 Versión 8.1 (2025). Visualización inspirada en Knowuro[](https://knowuro.com). Siempre verifique actualizaciones más recientes.",
        "language_select": "Seleccionar Idioma",
        "language_options": ["English", "Deutsch", "Español"]
    }
}

# Language Selector
language = st.selectbox(translations["English"]["language_select"], translations["English"]["language_options"])

t = translations[language]

# Prostate Cancer Treatment Algorithm App
st.title(t["title"])
st.markdown(t["description"])

# Genetic Testing Section
st.subheader(t["genetic_subheader"])
st.write(t["genetic_write"])

genetic_status = st.selectbox(
    t["genetic_select"],
    t["genetic_options"]
)

# PARP Inhibitors Details Expander
with st.expander(t["parp_expander"]):
    st.markdown(t["parp_content"])

# Step 1: Disease Extent
disease_extent = st.selectbox(
    t["extent_select"],
    t["extent_options"]
)

risk_group = None
androgen_status = None
volume = None
prior_therapy = []

if disease_extent == t["extent_options"][0]:  # Localized
    risk_group = st.selectbox(
        t["risk_select"],
        t["risk_options"]
    )
    
    st.subheader(t["recommend_subheader"])
    if t["risk_options"][0] in risk_group:
        st.write(t["very_low_risk_write"])
    elif t["risk_options"][1] in risk_group:
        st.write(t["favorable_write"])
    elif t["risk_options"][2] in risk_group:
        st.write(t["unfavorable_write"])
    elif t["risk_options"][3] in risk_group:
        st.write(t["high_risk_write"])

elif disease_extent == t["extent_options"][1]:  # Locally Advanced
    st.subheader(t["recommend_subheader"])
    st.write(t["locally_advanced_write"])

elif disease_extent == t["extent_options"][2]:  # Metastatic
    androgen_status = st.selectbox(
        t["androgen_select"],
        t["androgen_options"]
    )
    
    if androgen_status == t["androgen_options"][0]:  # mHSPC
        volume = st.selectbox(
            t["volume_select"],
            t["volume_options"]
        )
        
        st.subheader(t["recommend_subheader"])
        st.write(t["mHSPC_write"])
        if t["volume_options"][0] in volume:
            st.write(t["low_volume_add"])
        else:
            st.write(t["high_volume_add"])
        
        genetic_impact = ""
        if "BRCA" in genetic_status or "HRR" in genetic_status:
            genetic_impact = t["genetic_impact_hrr"]
        elif "MMR" in genetic_status:
            genetic_impact = t["genetic_impact_mmr"]
        
        st.write(genetic_impact)
        
        st.write(t["zulassung_mHSPC"])
    
    else:  # mCRPC
        prior_therapy = st.multiselect(
            t["prior_select"],
            t["prior_options"]
        )
        
        st.subheader(t["recommend_subheader"])
        st.write(t["mCRPC_write"])
        
        if any("Docetaxel" in p for p in prior_therapy):
            st.write(t["post_doc_add"])
        
        genetic_impact = ""
        if "BRCA" in genetic_status or "HRR" in genetic_status:
            genetic_impact = t["genetic_impact_hrr_cr"]
        elif "MMR" in genetic_status:
            genetic_impact = t["genetic_impact_mmr_cr"]
        
        st.write(genetic_impact)
        
        st.write(t["zulassung_mCRPC"])

# Refined Visual Flowchart Section
st.subheader(t["visual_subheader"])
mermaid_code = "graph TD\n"
mermaid_code += "Start[Diagnosis: PSA/DRE/mpMRI/Biopsy] --> Genetic{Genetic Testing?}\n"
mermaid_code += f"Genetic -->|Result: {genetic_status}| Extent{{Disease Extent?}}\n"

# Translate mermaid nodes based on language (simplified, keeping medical terms)
if language == "Deutsch":
    mermaid_code = mermaid_code.replace("Diagnosis: PSA/DRE/mpMRI/Biopsy", "Diagnose: PSA/DRE/mpMRI/Biopsie")
    mermaid_code = mermaid_code.replace("Genetic Testing?", "Genetisches Testing?")
    mermaid_code = mermaid_code.replace("Disease Extent?", "Ausmaß der Erkrankung?")
    # Add more translations for other nodes as needed
elif language == "Español":
    mermaid_code = mermaid_code.replace("Diagnosis: PSA/DRE/mpMRI/Biopsy", "Diagnóstico: PSA/DRE/mpMRI/Biopsia")
    mermaid_code = mermaid_code.replace("Genetic Testing?", "¿Pruebas Genéticas?")
    mermaid_code = mermaid_code.replace("Disease Extent?", "¿Extensión de la Enfermedad?")
    # Add more

if disease_extent == t["extent_options"][0]:
    mermaid_code += f"Extent -->|Localized| Risk{{Risk Group?}}\n"
    mermaid_code += f"Risk -->|{risk_group}| Staging[Staging: No additional imaging for low-risk]\n"
    mermaid_code += "Staging --> TherapyOptions{Therapy?}\n"
    if t["risk_options"][0] in risk_group:
        mermaid_code += "TherapyOptions -->|Primary| AS[Active Surveillance: PSA/mpMRI/re-biopsy]\n"
        mermaid_code += "TherapyOptions -->|If declined| Curative[RP or EBRT 74-80Gy or LDR Brachy]\n"
        mermaid_code += "Curative --> NoADT[No ADT/Lymphadenectomy]\n"
    elif t["risk_options"][1] in risk_group:
        mermaid_code += "TherapyOptions --> ASorCurative[AS (if no unfavorable) or Curative]\n"
        mermaid_code += "ASorCurative --> CurativeDetails[RP +/- Lymph or EBRT hypofrac + short ADT 4-6m]\n"
        mermaid_code += "CurativeDetails --> Focal[Focal therapies select, not standard]\n"
    elif t["risk_options"][2] in risk_group:
        mermaid_code += "TherapyOptions --> Curative[RP + ePLND or EBRT + short ADT 4-6m]\n"
        mermaid_code += "Curative --> Boost[Brachy boost possible]\n"
    elif t["risk_options"][3] in risk_group:
        mermaid_code += "TherapyOptions --> Multimodal[EBRT + long ADT 24-36m or RP + ePLND + adj RT if pT3/R1]\n"
        mermaid_code += "Multimodal --> Boost[Brachy boost select]\n"
    mermaid_code += "TherapyOptions --> PostTx[Post-Treatment: Monitor for BCR]\n"
    mermaid_code += "PostTx --> BCR{{BCR?}}\n"
    mermaid_code += "BCR -->|Yes| Imaging[PSMA PET/CT if PSA >0.2]\n"
    mermaid_code += "Imaging --> Salvage[Salvage RT + ADT or Monitoring based on risk]\n"
elif disease_extent == t["extent_options"][1]:
    mermaid_code += f"Extent -->|Locally Advanced| Staging[Staging: PSMA-PET/CT]\n"
    mermaid_code += "Staging --> Therapy{{Therapy?}}\n"
    mermaid_code += "Therapy --> Multimodal[EBRT IMRT/IGRT + long ADT 24-36m]\n"
    mermaid_code += "Therapy --> Operable[If operable: RP + ePLND + adj RT]\n"
    mermaid_code += "Therapy --> N1[For N1: Pelvic RT + ADT 3y + abiraterone 2y if ≥2 risks]\n"
    mermaid_code += "Therapy --> Boost[Brachy boost for cT3a]\n"
elif disease_extent == t["extent_options"][2]:
    mermaid_code += f"Extent -->|Metastatic| Androgen{{Androgen Status?}}\n"
    mermaid_code += f"Androgen -->|{androgen_status}| Staging[Staging: PSMA-PET/CT]\n"
    if androgen_status == t["androgen_options"][0]:
        mermaid_code += f"Staging --> Volume{{Volume?}}\n"
        mermaid_code += f"Volume -->|{volume}| Backbone[ADT Backbone: GnRH or orchiectomy]\n"
        mermaid_code += "Backbone --> AddOns[Add ARPI/abiraterone within 3m]\n"
        mermaid_code += "AddOns --> Chemo[If eligible: + Docetaxel 6 cycles]\n"
        mermaid_code += "Chemo --> Triple[Triple Therapy for high-volume]\n"
        mermaid_code += "Triple --> Local[Local RT/SBRT for low-volume/oligo]\n"
        mermaid_code += "Local --> Bone[Bone agents: Denosumab/zoledronic]\n"
    else:
        mermaid_code += f"Staging --> Prior[Prior Therapies: {', '.join(prior_therapy)}]\n"
        mermaid_code += "Prior --> Confirm[Confirm CRPC: T<50, progression]\n"
        mermaid_code += "Confirm --> Therapies[Continue ADT; ARPI switch or Docetaxel]\n"
        mermaid_code += "Therapies --> Symptomatic[If symptomatic: Docetaxel or Ra-223 bone-predom]\n"
        mermaid_code += "Therapies --> PostDoc[Post-docetaxel: Cabazitaxel, ARPI, PARP if HRR+]\n"
        mermaid_code += "PostDoc --> LuPSMA[Lu-PSMA-617 if PSMA+ post ARPI/chemo]\n"
        mermaid_code += "LuPSMA --> Bone[Bone agents for SRE]\n"

if genetic_status != t["genetic_options"][0] and genetic_status != t["genetic_options"][1]:
    if "BRCA" in genetic_status or "HRR" in genetic_status:
        mermaid_code += "Genetic -->|Positive| GeneticImpact[HRR+: PARP combos, platinum]\n"
    elif "MMR" in genetic_status:
        mermaid_code += "Genetic -->|Positive| GeneticImpact[MMR+: Pembrolizumab if MSI-H]\n"
    mermaid_code += "GeneticImpact -.-> TherapyOptions\n"
    mermaid_code += "GeneticImpact -.-> Therapies\n"

st.markdown(f"```mermaid\n{mermaid_code}\n```")

st.markdown("---")
st.info(t["references"])
