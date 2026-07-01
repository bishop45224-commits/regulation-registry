---
domain: Privacy & Data
version: 1.1
last_verified: 2026-07-01
next_check_due: 2026-08-01
sources: [ftc.gov, consumerfinance.gov, federalregister.gov]
applies_to_projects: []
---

# Privacy & Data Regulation Reference

> **Scope:** Federal privacy and data protection rules plus state laws with broad applicability.  
> **Weight:** High velocity domain. Regulations are actively expanding at both federal and state levels.  
> **Reminder:** This is a reference, not legal advice. Get qualified review before commercial launch.

---

## Federal Framework

### FTC Act — Section 5 (Unfair or Deceptive Practices)
The FTC's primary enforcement tool for privacy. No federal omnibus privacy law exists yet, but the FTC treats deceptive privacy practices as unfair trade practices. Key obligations:
- Privacy policies must accurately describe actual data practices
- Material changes to privacy policies require user notice
- Data collection must be consistent with stated purposes
- "Privacy by default" is increasingly the enforcement standard

**Status:** Active enforcement. FTC has significantly increased enforcement actions in recent years.

### Gramm-Leach-Bliley Act (GLBA)
Applies to financial institutions. Requires notice of information sharing practices and opt-out rights for non-affiliated third-party sharing (Privacy Rule / Regulation P). Safeguards Rule requires a formal written information security program.

**🔴 Breach reporting amendment (effective May 2024):** Non-banking financial institutions must notify the FTC as soon as possible and no later than **30 days** after discovering a security breach involving unencrypted customer information of **500+ consumers**. This obligation is live and enforced.

**🟡 June 2025:** FTC issued updated Safeguards Rule FAQ guidance clarifying application of the rule (including for auto dealers) — useful compliance reference.

**🟡 Related — SEC Regulation S-P amendments:** For SEC-regulated entities (broker-dealers, RIAs, funds), amended Reg S-P requires incident response programs and 30-day customer breach notification. Compliance dates: December 2025 (larger entities), **June 2026 (smaller entities — now in effect)**.

**Applies if:** Business qualifies as a financial institution (insurance agencies generally qualify).

### HIPAA
Applies to covered entities and business associates handling protected health information (PHI). Requires administrative, physical, and technical safeguards.

**Applies if:** Collecting or processing any health-related data.

### Children's Online Privacy Protection Act (COPPA)
Applies to online services directed to children under 13. Requires verifiable parental consent before collecting personal data.

**🔴 2025 COPPA Rule amendments — compliance deadline April 22, 2026 (PASSED — now fully enforceable):** Final amendments published April 2025 (effective June 23, 2025) expanded operator obligations: data retention limits (cannot retain children's data longer than needed for documented collection purposes; indefinite retention prohibited), enhanced direct-notice content requirements, separate verifiable parental consent for third-party disclosures/targeted advertising, and expanded definitions (biometric identifiers; mobile numbers as online contact info for text-based consent). FTC leadership has flagged COPPA enforcement as a priority.

**Applies if:** Any product that could be used by or directed at minors.

### FTC Safeguards Rule (Updated 2023)
Expanded scope requiring non-banking financial institutions (including insurance) to implement formal cybersecurity programs. Requirements include: designated security officer, risk assessments, encryption, multi-factor authentication, and incident response plans. Breach reporting to FTC required since May 2024 (see GLBA section above).

**Status:** In effect. Compliance required. FTC FAQ guidance issued June 2025.

---

## State Laws — High Priority

### California — CCPA/CPRA
**Enforced by:** California Privacy Protection Agency (CPPA)  
**Effective:** CCPA 2020, CPRA amendments 2023  
Applies to businesses meeting revenue/data volume thresholds. Grants consumers rights to know, delete, correct, opt-out of sale, and limit sensitive data use. Private right of action for data breaches.

**Threshold:** Applies if: >$25M annual revenue, OR processes data of 100K+ consumers/households, OR derives 50%+ revenue from selling data.

**🔴 CPPA regulations on ADMT, risk assessments, and cybersecurity audits — effective January 1, 2026:** Finalized September 2025. Businesses using automated decision-making technology (ADMT) for "significant decisions" (finances, housing, education, employment, healthcare) must provide pre-use notice, opt-out, and access rights — full ADMT compliance required by **April 1, 2027**. Risk assessment obligations began **January 1, 2026** (initial assessments for existing processing due December 31, 2027; first CPPA submissions April 1, 2028). Cybersecurity audit certifications phase in April 2028–2030 by revenue tier.

### Virginia — VCDPA
**Enforced by:** AG's office  
**Effective:** 2023  
Similar to CCPA. Applies to businesses processing data of 100K+ consumers annually or 25K+ consumers where 50%+ revenue from data sales. No private right of action.

### Colorado, Connecticut, Texas, Oregon, Montana, Nebraska, New Hampshire, New Jersey, Delaware, Indiana, Iowa, Kentucky, Maryland, Minnesota, Rhode Island, Tennessee
All have enacted comprehensive consumer privacy laws in the 2023–2025 wave. Most follow the Virginia model with variations on thresholds and enforcement. **~20 state comprehensive privacy laws are now in effect as of 2026.**

**Recent effective dates:**
- **Tennessee (TIPA):** effective July 1, 2025
- **Minnesota (MCDPA):** effective July 31, 2025 — unique consumer right to question profiling results in significant decisions
- **Maryland (MODPA):** effective October 1, 2025 — 🔴 strictest data-minimization requirements of any state law (collection limited to what is reasonably necessary; sensitive data sale broadly prohibited)
- **🔴 Indiana (ICDPA), Kentucky (KCDPA), Rhode Island (RIDTPPA): all effective January 1, 2026.** Indiana and Kentucky track the Virginia model (penalties up to $7,500/violation, 30-day cure). Rhode Island has notably **low applicability thresholds** (35K consumers, or 10K if >20% revenue from data sales), penalties up to $10,000/violation, and **no cure period**.

**Pattern across these states:** Controller/processor framework, consumer rights (access/delete/correct/portability/opt-out of profiling), data protection assessments for high-risk processing, no private right of action (except Delaware for some provisions).

### Illinois — BIPA (Biometric Information Privacy Act)
**Enforced by:** Private right of action (significant litigation risk)  
Applies to any collection or use of biometric identifiers (fingerprints, facial recognition, voiceprints). Requires written notice and consent before collection. Statutory damages: $1,000–$5,000 per violation.

**Risk level:** Extremely high if any biometric data is involved. BIPA litigation is one of the most active privacy enforcement areas in the US.

---

## Emerging / Watch Areas

### Federal Comprehensive Privacy Law
🟡 APRA is dead. The current vehicle is the **SECURE Data Act** (House Energy & Commerce, introduced April 2026) — would establish a single federal privacy law and **preempt the state patchwork**. Also introduced: Consumer Data Privacy and Security Act of 2026 (Senate). No passage yet; preemption scope is the key fight. Watch closely — passage would restructure this entire file.

### AI-Specific Privacy Rules
FTC has signaled that automated decision-making using personal data will face heightened scrutiny. Several states are moving on AI-specific rules that overlap with privacy (profiling, discrimination in automated decisions). California's CPPA ADMT regulations (effective Jan 1, 2026 — see CCPA section) are the most concrete. 🟡 Note: the December 2025 federal executive order pushing preemption of state AI laws (see ai_automation.md) creates uncertainty for state ADMT/profiling rules, but state laws remain enforceable unless a court or Congress says otherwise.

### Data Broker Regulation
Several states have passed laws requiring data brokers to register and/or allow consumers to opt out. Vermont, California, Oregon, and Texas have active regimes.

---

## Key Obligations Checklist (General)

- [ ] Privacy policy that accurately reflects all data practices
- [ ] Mechanism for consumer data rights requests (access, delete, correct)
- [ ] Data minimization — only collect what you need
- [ ] Vendor/processor agreements for any third party handling data
- [ ] Incident response plan and breach notification procedures
- [ ] Security safeguards appropriate to data sensitivity
- [ ] Special handling for sensitive categories (health, financial, biometric, children's data)

---

*Last verified against: ftc.gov, federalregister.gov, consumerfinance.gov, cppa.ca.gov (2026-07-01)*  
*Next scheduled check: 2026-08-01*
