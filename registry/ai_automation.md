---
domain: AI & Automation
version: 1.3
last_verified: 2026-11-16
next_check_due: 2026-12-01
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

### Federal Executive Orders on AI — 🔴 Major Reversal
The Oct 2023 Biden AI EO was **rescinded in January 2025** (EO 14179, "Removing Barriers to American Leadership in AI"). Federal posture is now deregulatory.

**🔴 December 11, 2025 EO — "Ensuring a National Policy Framework for Artificial Intelligence":** Directs a whole-of-government effort to **preempt state AI laws**:
- DOJ **AI Litigation Task Force** created to challenge state AI laws in court
- FTC directed to issue a policy statement on when state laws requiring alterations to truthful AI model outputs are preempted by the FTC Act
- Commerce directed to evaluate conditioning federal (e.g., broadband) funding on states not enacting "onerous" AI laws

**🟡 FTC proposed policy statement — "Suppression of Accuracy in Artificial Intelligence Systems" (July 2026):** Published for comment July 7, 2026 (docket FTC-2026-0859; comments closed July 31). Theory: undisclosed ideological steering of AI outputs can be a deceptive omission under Section 5, and state laws that push companies toward such alteration (Colorado's revised AI act named) may be **impliedly preempted**. **Still proposed, not final, as of 2026-11-16**; the implied-preemption theory is untested in court and drew substantial pushback in comments.

**Practical status:** An EO cannot itself overturn state law — state AI laws **remain enforceable** unless Congress or the courts act. No DOJ AI Litigation Task Force suit against a state had been found as of 2026-11-16. Continue complying with applicable state laws, but expect litigation and possible federal preemption legislation. Highest-volatility item in this registry.

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
- 🟡 EEOC's AI technical assistance documents (Title VII 2023, ADA 2022) were **removed from eeoc.gov in January 2025**. The underlying statutory obligations are unchanged — disparate impact from AI tools can still violate Title VII/ADA, and private plaintiffs and states can still sue.
- NYC Local Law 144: Requires bias audits for automated employment decision tools (model for other jurisdictions)
- Illinois AI Video Interview Act: Requires notice and consent for AI analysis of video interviews
- 🔴 Illinois HB 3773 (amends IL Human Rights Act): **effective January 1, 2026** — prohibits AI use with discriminatory effect in employment decisions and requires notice to employees/applicants when AI is used. IDHR implementing rules in progress (draft notice rules published).

---

## State AI Laws — Active

### Colorado — 🔴 REPLACED (May 2026)
Original SB 24-205 (high-risk AI, duty of care, impact assessments) **never took effect**. Timeline: delayed from Feb 1, 2026 to June 30, 2026 (SB 25B-004, Aug 2025), then **replaced by SB 26-189 (signed May 14, 2026)** — significantly scaled back. The new framework drops the algorithmic-discrimination duty of care, deployer risk-management programs, and impact assessments, in favor of **disclosure/transparency requirements for automated decision-making technologies (ADMT)**. **Effective January 1, 2027.** Re-verify obligations against SB 26-189, not SB 24-205.

### Texas — 🔴 TRAIGA (effective January 1, 2026)
Texas Responsible AI Governance Act (signed June 2025). Applies to anyone developing/deploying AI in Texas or offering products used by Texas residents. **Intent-based liability** (not risk-tiered): prohibits AI intentionally designed to manipulate behavior, unlawfully discriminate (disparate impact alone is insufficient), infringe constitutional rights, or produce unlawful explicit content. **Safe harbor** for substantial compliance with NIST AI RMF. AG exclusive enforcement (no private right of action); penalties $10K–$200K per violation plus daily penalties; 60-day cure period. Includes regulatory sandbox.

### California
- **🔴 SB 53 — Transparency in Frontier AI Act (effective January 1, 2026):** First state frontier-model safety law. Applies to developers of models trained with >10^26 FLOPs; extra obligations for developers with >$500M revenue. Requires published safety frameworks, transparency reports, and incident reporting.
- **🔴 CPPA ADMT regulations finalized (Sept 2025), effective January 1, 2026:** notice, opt-out, and access rights for ADMT used in significant decisions; full ADMT compliance by April 1, 2027 (see privacy_data.md).
- SB 243 (companion chatbots): disclosure and minor-protection requirements for bots that meet social needs and sustain a relationship; excludes operational bots (a scheduler/task assistant that stays in scope is outside it) — verify current status if building conversational AI.

### Illinois
- BIPA (biometric data) intersects heavily with AI. Any AI system analyzing faces, voices, or other biometrics triggers BIPA requirements.
- HB 3773 (AI in employment decisions) effective January 1, 2026 — see Employment AI section.
- **🔴 Artificial Intelligence Safety Measures Act (SB 315) — signed July 6, 2026, effective January 1, 2027:** Frontier-model safety law, currently the nation's most stringent. Applies to "large frontier developers" (≥$500M annual revenue). Requires published safety plans addressing "catastrophic risk" (defined to include AI materially contributing to death/serious injury of 50+ people or expert-level assistance creating CBRN weapons), **first-in-nation annual independent third-party audits**, critical-safety-incident reporting to the state within 72 hours (24 hours if imminent risk of death/serious injury), and whistleblower protections. Fines up to $3M per violation. Compare CA SB 53 (transparency-only, no audit mandate). Note: prime target for the federal preemption fight — watch DOJ AI Litigation Task Force response.

### New York — 🔴 RAISE Act (effective January 1, 2027)
Responsible AI Safety and Education Act, signed December 19, 2025 and **amended by chapter amendment signed March 27, 2026** (the operative version). Frontier-model law converging with California's SB 53: large frontier developers must publish a "frontier AI framework" (same term as CA), file a disclosure statement with the regulator, and pay an assessment before developing/deploying a frontier model in New York. Oversight by a new office within the **Department of Financial Services** (rulemaking authority); NY AG has exclusive enforcement. Expect a federal preemption challenge.

### Utah — AI Policy Act (as amended 2025)
Original 2024 act required disclosure that a consumer is interacting with generative AI. **As amended (SB 226/SB 332, 2025):** disclosure on clear request applies to regulated-occupation and consumer-transaction contexts; *prominent upfront* disclosure required only for "high-risk" generative AI interactions (sensitive data + advice for significant decisions). Safe harbor for regulatory mitigation. The Policy Act chapter carries a **July 1, 2027 repeal date** (commentators note the disclosure provisions codified separately may survive — verify against current Utah Code before relying). Additional 2026 Utah laws: Digital Content Provenance Standards Act (in force Jan 1, 2027).

### Other 2026-session state AI laws (🟡 verify before relying)
- **California (2026 session):** two dozen+ privacy/AI bills signed, incl. **AB 1883** (bars workplace AI tools inferring employees' emotional states or collecting neural data — effective Jan 1, 2027)
- **Washington:** generative AI disclosure law, effective Feb 1, 2027

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
- 🔴 **CORRECTION — one-to-one consent rule is DEAD:** The Eleventh Circuit vacated the FCC's one-to-one consent rule (*Insurance Marketing Coalition v. FCC*, Jan 24, 2025) and the FCC formally repealed the language. Lead-gen consent standard reverts to pre-2023 status quo: prior express written consent, no one-to-one constraint.
- 🟡 **Consent revocation rules:** Most of the FCC's 2024 revocation order took effect April 11, 2025 (honor reasonable opt-out methods, 10-business-day processing window, expanded opt-out keywords). The "revoke-all" provision (one revocation cuts off all unrelated calls/texts) has been **delayed to January 31, 2027** and may be modified.

### Bot Disclosure
California B.O.T. Disclosure Act: Bots communicating with Californians in commerce must disclose they are not human. Several other states have similar or pending laws.

---

## Emerging / Watch Areas

- **🔴 Federal preemption fight** — the Dec 2025 EO, DOJ AI Litigation Task Force, and pending FTC preemption policy statement are the dominant storyline. Congress may attach AI preemption to must-pass legislation. State compliance obligations could shift quickly.
- **Federal AI legislation** — multiple bills active in Congress; preemption-focused proposals now most likely vehicle.
- **🔴 EU AI Act + Digital Omnibus (updated):** Article 50 transparency obligations (tell people they're dealing with AI; label deepfakes) **in force since August 2, 2026** — NOT delayed. The **Digital Omnibus on AI** (Council final approval June 29, 2026) postponed the high-risk obligations: Annex III standalone systems to **December 2, 2027**, Annex I embedded/regulated-product AI to **August 2, 2028**. Art. 50(2) machine-readable marking of AI-generated content for systems already on the market before Aug 2, 2026 applies from **~December 2, 2026** (sources differ slightly — read the Official Journal text before relying). Commission Art. 50 guidelines adopted July 20, 2026. Applies to anyone offering AI-enabled products in the EU.
- **Liability for AI outputs** — courts and legislatures actively working on questions of who bears liability for harmful AI-generated content or decisions.
- **AI in insurance** — NAIC model bulletin now adopted by 24 states + DC (see insurance_tech.md).
- **State session wave** — more state AI bills passing despite federal pressure; re-check state list monthly.

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

*Last verified against: nist.gov, ftc.gov, federalregister.gov, governor.ny.gov, le.utah.gov, EU sources (secondary — see note) (2026-11-16)*  
*Next scheduled check: 2026-12-01*
