---
domain: Security & Assurance Frameworks (Non-Regulatory)
version: 1.0
last_verified: 2026-07-07
next_check_due: 2026-08-01
sources: [nist.gov, ftc.gov, naic.org]
non_regulatory: true
applies_to_projects: []
---

# Standards & Assurance Frameworks Reference

> **Scope:** Voluntary certification and attestation frameworks (ISO, SOC, NIST) that overlap with, help satisfy, or are contractually demanded alongside the legal obligations tracked in this registry.
> **Source Note:** ⚠️ These are NOT laws or regulations. They come from standards bodies (ISO), the AICPA (SOC), and NIST (voluntary frameworks). They will never surface from the approved government-source whitelist — this file must be maintained manually or via separately approved sources (iso.org, aicpa-cima.com, nist.gov).
> **Why they're in the registry anyway:** (1) Customers, carriers, and enterprise procurement demand them contractually even where no law requires them. (2) Regulators and courts increasingly treat them as evidence of the standard of care. (3) Some laws now reference them directly (e.g., TRAIGA's NIST AI RMF safe harbor; Illinois SB 315's independent audit mandate).
> **Reminder:** This is a reference, not legal advice. Get qualified review before commercial launch.

---

## Certification & Attestation Frameworks

### ISO/IEC 27001 — Information Security Management
Certifiable international standard for an Information Security Management System (ISMS): risk assessment, Annex A controls, management review, continual improvement. Certification by an accredited body, 3-year cycle with annual surveillance audits.

**When it matters:** Enterprise sales, vendor due diligence, international customers (more recognized than SOC 2 outside the US).
**Legal overlap:** Substantially covers FTC Safeguards Rule and NAIC Model 668 program requirements (designated owner, risk assessment, incident response, vendor oversight) — but certification does not equal legal compliance; map controls explicitly.

**Related ISO standards for AI work:**
- **ISO/IEC 42001 (AI Management System)** — certifiable AIMS standard; the emerging "ISO 27001 for AI." Directly pertinent to demonstrating responsible-AI governance under TRAIGA-style safe harbors and NAIC AI bulletin model-governance expectations.
- **ISO/IEC 27701** — privacy extension to 27001 (maps to GLBA privacy, state privacy law programs).
- **ISO/IEC 23894** — AI risk management guidance (non-certifiable; companion to 42001).

### SOC 1 (SSAE 18) — Internal Control over Financial Reporting
CPA attestation on controls relevant to customers' **financial reporting** (payroll processors, TPAs, claims administrators). Type 1 = design at a point in time; Type 2 = operating effectiveness over a period (typically 6–12 months).

**When it matters:** Only if your service affects customers' financial statements (e.g., processing premiums/claims/payments on their behalf). Their auditors will ask for it.
**Legal overlap:** Minimal direct regulatory overlap; driven by customers' SOX/audit needs.

### SOC 2 Type 2 — Trust Services Criteria
CPA attestation (also under SSAE 18) against the Trust Services Criteria: Security (required), plus optional Availability, Confidentiality, Processing Integrity, Privacy. **Type 2** (operating effectiveness over a review period) is the de facto B2B SaaS requirement; Type 1 is a stopgap.

**When it matters:** Almost any B2B software sale, carrier/aggregator tech due diligence, embedded insurance partnerships.
**Legal overlap:** Security criterion maps well to Safeguards Rule / Model 668 obligations. Confidentiality + Privacy criteria support GLBA/state privacy compliance narratives. A current SOC 2 Type 2 materially shortens security questionnaires.

### NIST Cybersecurity Framework (CSF 2.0)
Voluntary; not certifiable. Common language for security programs (Govern, Identify, Protect, Detect, Respond, Recover). Often the internal skeleton onto which ISO/SOC controls are mapped.

### NIST AI Risk Management Framework (AI RMF 1.0 + Generative AI Profile)
Voluntary; not certifiable — but the most legally significant framework in this file for AI work:
- **TRAIGA (TX):** substantial compliance with the current NIST AI RMF (incl. GenAI Profile) is an affirmative defense.
- **NAIC AI Model Bulletin (24 states + DC):** model-governance expectations track AI RMF structure.
- **Colorado SB 26-189 / CPPA ADMT rules:** documentation and governance expectations align with RMF functions.
- Referenced in federal procurement and enforcement conversations as the standard of care.

---

## Framework ↔ Legal Obligation Map

| Framework | Registry obligations it helps satisfy |
| --- | --- |
| ISO 27001 / SOC 2 (Security) | FTC Safeguards Rule; NAIC Model 668; state breach-preparedness expectations |
| ISO 27701 / SOC 2 (Privacy, Confidentiality) | GLBA Privacy Rule; state comprehensive privacy laws (program evidence) |
| ISO 42001 / NIST AI RMF | TRAIGA safe harbor; NAIC AI bulletin governance; CO SB 26-189; CPPA ADMT risk assessments |
| SOC 1 Type 2 | Customers' SOX/financial-audit requirements (contractual) |
| NIST CSF 2.0 | Underlying structure for all of the above |
| Independent AI safety audits | Illinois SB 315 (frontier developers only, eff. 2027-01-01) — first law converting third-party AI audits from voluntary to mandatory |

---

## Practical Guidance

- **Sequence for a small tech company:** NIST CSF-aligned internal program → SOC 2 Type 1 → SOC 2 Type 2 → ISO 27001 only if selling internationally/enterprise. Add ISO 42001 or documented AI RMF alignment when AI features become customer-facing.
- **Don't certify for its own sake:** attestations are sales enablers and evidence of care; the binding obligations remain the laws in the other five registry files.
- **Watch:** regulators increasingly hard-wiring frameworks into law (TRAIGA, IL SB 315). Expect more statutes to reference NIST AI RMF and independent audits — this file's velocity is rising.

---

*Non-regulatory reference. Sources: nist.gov, aicpa-cima.com, iso.org (not on approved whitelist — manual verification), ftc.gov, naic.org (2026-07-07)*
*Next scheduled check: 2026-08-01*
