---
domain: AI & Automation
version: 1.0
last_verified: 2026-05-02
next_check_due: 2026-06-01
sources: [nist.gov, ftc.gov, federalregister.gov, congress.gov]
applies_to_projects: []
---

# AI & Automation Regulation Reference

> **Scope:** Federal and emerging state rules governing AI systems, automated decision-making, and automation tools used commercially.  
> **Weight:** Highest velocity domain in the registry. Regulations are being drafted and passed rapidly. Check frequently.  
> **Reminder:** This is a reference, not legal advice. Get qualified review before commercial launch.

---

## Federal Framework

### NIST AI Risk Management Framework (AI RMF 1.0)
**Source:** nist.gov  
**Status:** Voluntary framework, but increasingly referenced in enforcement and contracts  
Provides structure for identifying, assessing, and managing AI risks across four functions: Govern, Map, Measure, Manage. Not legally binding but establishes the standard of care that regulators and courts are beginning to reference.

**Practical impact:** Building against NIST AI RMF reduces risk exposure even where not required.

### FTC Guidance on AI
**Source:** ftc.gov  
The FTC has issued multiple guidance documents asserting authority over AI under Section 5 (unfair/deceptive practices). Key positions:
- AI systems that discriminate or produce biased outputs against protected classes may constitute unfair practices
- Marketing claims about AI capabilities must be truthful and substantiated
- AI used in consumer credit, employment, or housing decisions faces heightened scrutiny
- "Loot box" style monetization in AI products is under review

**Status:** Guidance only — but FTC has brought enforcement actions. Treat as binding in practice.

### Executive Order on AI (Oct 2023) — Ongoing Implementation
Required federal agencies to develop AI standards and guidance. Most relevant outputs:
- NIST AI Safety Institute guidance
- OMB guidance on federal AI procurement (signals what "responsible AI" means to government)
- Sector-specific guidance from financial regulators

**Status:** Implementation ongoing. Watch for agency-specific rules flowing from this.

### Algorithmic Accountability
No federal law yet, but multiple bills introduced. The Algorithmic Accountability Act (various versions) would require impact assessments for automated decision systems. Not passed as of this writing but has significant momentum.

---

## Sector-Specific AI Rules

### Financial Services / Insurance (AI in Underwriting and Pricing)
**Sources:** CFPB, FTC, state insurance regulators  
Using AI/ML in insurance underwriting, pricing, or claims is under active scrutiny:
- AI-based underwriting must comply with Fair Credit Reporting Act (FCRA) if using consumer report data
- AI decisions affecting consumers may trigger Equal Credit Opportunity Act (ECOA) adverse action notice requirements
- NAIC has issued model bulletin on use of AI by insurers — states are adopting versions of this
- Proxy discrimination (using neutral variables that correlate with protected class) is an enforcement risk even without discriminatory intent

### Employment AI
**Sources:** EEOC, DOL  
AI used in hiring, promotion, or workforce management:
- EEOC guidance: AI tools that produce disparate impact on protected classes may violate Title VII
- NYC Local Law 144: Requires bias audits for automated employment decision tools (model for other jurisdictions)
- Illinois AI Video Interview Act: Requires notice and consent for AI analysis of video interviews

---

## State AI Laws — Active

### Colorado
SB 205 (AI systems in consequential decisions affecting consumers) — signed 2024. Applies to developers and deployers of high-risk AI systems. Requires disclosure, impact assessments, and mechanisms for consumers to appeal automated decisions.

### California
Multiple AI-related bills active. CPPA has issued draft rules on automated decision-making technology. Expect formal rules 2025–2026.

### Illinois
BIPA (biometric data) intersects heavily with AI. Any AI system analyzing faces, voices, or other biometrics triggers BIPA requirements.

### Texas, Virginia, Connecticut, Montana
Privacy laws include provisions on profiling and automated decisions — opt-out rights required.

---

## Automation-Specific Considerations

### Web Scraping
- No federal law explicitly governs web scraping
- Computer Fraud and Abuse Act (CFAA) may apply if scraping violates terms of service
- *hiQ v. LinkedIn* established some protections for scraping public data, but landscape is unsettled
- If scraping produces personal data, state privacy laws apply to that data

### Automated Messaging / Communications
- Telephone Consumer Protection Act (TCPA): Strict rules on automated calls and texts. Requires prior express written consent for marketing. Significant litigation risk.
- CAN-SPAM: Applies to commercial email. Opt-out mechanisms required.
- FCC has tightened TCPA rules — one-to-one consent requirement in effect 2025.

### Bot Disclosure
California B.O.T. Disclosure Act: Bots communicating with Californians in commerce must disclose they are not human. Several other states have similar or pending laws.

---

## Emerging / Watch Areas

- **Federal AI legislation** — multiple bills active in Congress. First federal AI law likely within 1–2 years.
- **EU AI Act** — if any commercial activity touches EU users, the EU AI Act applies. Tiered risk system with significant obligations for high-risk AI systems.
- **Liability for AI outputs** — courts and legislatures actively working on questions of who bears liability for harmful AI-generated content or decisions.
- **AI in insurance** — NAIC model bulletin adoption by states is accelerating. Expect formal state rules on algorithmic underwriting within 2 years.

---

## Key Obligations Checklist (General)

- [ ] Disclose to users when they are interacting with an AI system
- [ ] Substantiate any capability claims made about AI features
- [ ] Test AI outputs for disparate impact on protected classes before deployment
- [ ] Document the data used to train or inform AI systems
- [ ] Provide human review option for consequential automated decisions
- [ ] TCPA compliance for any automated outreach (calls, texts, emails)
- [ ] Bot disclosure for any automated conversational interfaces

---

*Last verified against: nist.gov, ftc.gov, federalregister.gov*  
*Next scheduled check: 2026-06-01*
