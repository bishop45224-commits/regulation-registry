---
domain: Employment & Labor Technology
version: 1.1
last_verified: 2026-07-01
next_check_due: 2026-08-01
sources: [dol.gov, eeoc.gov, federalregister.gov, ecfr.gov]
applies_to_projects: []
---

# Employment & Labor Technology Regulation Reference

> **Scope:** Federal rules governing employment practices, workforce technology, hiring tools, and contractor relationships. Relevant to both operating a business with employees and building technology used in employment contexts.  
> **Weight:** Moderate velocity. Core framework stable, but AI-in-employment and gig worker classification are high-velocity sub-areas.  
> **Reminder:** This is a reference, not legal advice. Get qualified review before commercial launch.

---

## Federal Framework

### Title VII of the Civil Rights Act
**Enforced by:** EEOC  
Prohibits employment discrimination based on race, color, religion, sex, or national origin. Applies to employers with 15+ employees. Key modern relevance:
- Applies to AI/automated tools used in hiring or employment decisions
- Disparate impact (neutral practices that disproportionately affect protected groups) is prohibited
- EEOC has signaled aggressive enforcement posture toward discriminatory AI tools

### Americans with Disabilities Act (ADA)
**Enforced by:** EEOC  
Prohibits discrimination against qualified individuals with disabilities. Requires reasonable accommodation. AI hiring tools that screen out candidates based on disability-correlated characteristics are under scrutiny.

### Age Discrimination in Employment Act (ADEA)
**Enforced by:** EEOC  
Protects workers 40+ from age discrimination. Targeted job advertising (e.g., age-targeted social media ads excluding older workers) has resulted in enforcement actions.

### Fair Labor Standards Act (FLSA)
**Enforced by:** DOL Wage and Hour Division  
Governs minimum wage, overtime, and child labor. Critical for:
- Worker classification (employee vs. contractor)
- Overtime eligibility determination
- Record-keeping requirements

**🔴 Highly relevant — contractor rule reversal in progress:** DOL announced (Field Assistance Bulletin 2025-1, May 2025) it will **not enforce** the Biden-era 2024 independent contractor rule and has reverted to the earlier framework in investigations. A proposed rule to formally rescind and replace it (reviving the 2021 two-core-factor test: control and opportunity for profit/loss) was published Feb 27, 2026; comments closed April 28, 2026; **final rule pending**. Caution: the 2024 rule technically remains on the books, and courts and private plaintiffs may still apply their own economic-reality analyses — classification risk has NOT disappeared.

### National Labor Relations Act (NLRA)
**Enforced by:** NLRB  
Protects workers' rights to organize and engage in collective action. Applies to most private employers regardless of size. NLRB has taken positions that some workplace monitoring and AI tools may interfere with NLRA rights.

### Worker Adjustment and Retraining Notification Act (WARN)
Requires 60-day notice before mass layoffs (100+ employees) or plant closings. Generally not relevant at startup/small business scale but worth knowing as businesses scale.

---

## Technology-Specific Rules

### AI in Hiring
**Sources:** EEOC, DOL, state laws  
Use of AI in recruiting, screening, or hiring:
- 🟡 **EEOC AI guidance removed (Jan 2025):** The EEOC's Title VII (2023) and ADA (2022) AI technical assistance documents were taken down under new leadership; DOL AI guidance similarly rolled back. **The statutes are unchanged** — disparate impact from AI tools can still violate Title VII, and private plaintiffs, state AGs, and future administrations can still enforce. Continue bias testing.
- Employers responsible for outcomes of third-party AI hiring tools
- ADA implicated if AI screens based on disability-correlated characteristics
- NYC Local Law 144 (effective 2023): Requires annual bias audits for automated employment decision tools. First major law of its kind — model for other jurisdictions.
- Illinois AI Video Interview Act: Written notice and consent required before AI analysis of video interviews. Candidates can request information about AI criteria.
- 🔴 **Illinois HB 3773 (effective Jan 1, 2026):** Amends IL Human Rights Act — prohibits using AI that has a discriminatory effect in recruitment, hiring, promotion, discipline, discharge, or other terms of employment, and requires **notice** to employees/applicants when AI is used in such decisions. IDHR implementing rules in progress.
- 🟡 **Colorado AI Act replaced:** original SB 24-205 employment-AI obligations never took effect; replaced May 2026 by SB 26-189 (narrower ADMT disclosure framework, effective Jan 1, 2027). See ai_automation.md.
- 🟡 **Texas TRAIGA (effective Jan 1, 2026)** covers AI in consequential employment decisions — intent-based standard. See ai_automation.md.

### Workplace Monitoring
Remote work and employee monitoring technology:
- No comprehensive federal law on employee monitoring
- Employees generally have limited privacy expectations in employer-provided systems
- State laws vary significantly (Connecticut, New York, Delaware require notice of electronic monitoring)
- NLRB has scrutinized monitoring that chills protected concerted activity

### Background Checks in Hiring
- FCRA applies to third-party background check services
- "Ban the Box" laws (federal contractors and many states/localities) restrict when criminal history can be asked about
- EEOC guidance on use of criminal records — must be job-related and consistent with business necessity

### Gig / Platform Work
**Highly active area:**
- DOL 2024 independent contractor rule — multi-factor economic reality test
- Several states (CA AB5, NY, NJ) have passed laws reclassifying many gig workers as employees
- Misclassification risk: wage and hour liability, benefits obligations, tax liability
- If building a platform that engages workers, classification analysis is essential before launch

### Job Posting and Advertising
- Age-targeted advertising that excludes older workers has been challenged under ADEA
- AI-powered targeted advertising to exclude certain demographics from job ads is under FTC and EEOC scrutiny
- Some states require salary range disclosure in job postings (CO, NY, CA, WA, others)

---

## Emerging / Watch Areas

- **Federal AI employment regulation** — direction reversed: the Dec 2025 federal AI EO pushes **preemption of state AI laws** (including employment AI rules) rather than new federal requirements. State laws remain enforceable pending litigation. High volatility.
- **Gig worker classification** — DOL final rescission/replacement rule pending (see FLSA section). State-level reclassification rules (CA AB5, NJ, NY) unaffected by the federal rollback.
- **🔴 Non-compete agreements — federal ban is DEAD:** The FTC's 2024 non-compete rule was vacated (N.D. Tex.); the FTC dropped its appeals in September 2025 and removed the rule from the CFR effective Feb 12, 2026. **State law now governs** — and many states restrict non-competes. FTC continues case-by-case Section 5 enforcement against egregious non-compete use.
- **Workplace AI monitoring** — NLRB and state agencies actively developing rules. High velocity sub-area.
- **Pay transparency** — state pay transparency laws continue expanding; verify per-state before posting roles.

---

## Key Obligations Checklist (As Employer)

- [ ] Job descriptions and hiring criteria are facially neutral and job-related
- [ ] Any AI hiring tools tested for disparate impact before deployment
- [ ] FCRA compliance for background check services
- [ ] Worker classification analyzed before engaging contractors
- [ ] I-9 employment eligibility verification for all employees
- [ ] FLSA record-keeping and overtime practices compliant
- [ ] Employee monitoring notice where required by state
- [ ] Non-compete agreements reviewed under applicable STATE law (federal FTC ban vacated/removed)

## Key Obligations Checklist (Building Employment Tech)

- [ ] Bias audit capability built into AI hiring/screening tools
- [ ] Disclosure mechanism for AI use in employment decisions
- [ ] ADA accommodation pathway for AI-driven processes
- [ ] NYC LL 144 compliance if tool will be used in NYC
- [ ] FCRA compliance if product generates consumer reports
- [ ] Salary range disclosure features for applicable states

---

*Last verified against: dol.gov, eeoc.gov, federalregister.gov, ftc.gov (2026-07-01)*  
*Next scheduled check: 2026-08-01*
