---
domain: Financial Services
version: 1.1
last_verified: 2026-07-01
next_check_due: 2026-08-01
sources: [cftc.gov, sec.gov, federalregister.gov, ecfr.gov, consumerfinance.gov]
applies_to_projects: []
---

# Financial Services Regulation Reference

> **Scope:** Federal rules governing financial products, securities, commodities, and fintech operations.  
> **Weight:** Moderate velocity. Rules are well-established but enforcement posture and fintech-specific guidance are actively evolving.  
> **Reminder:** This is a reference, not legal advice. Get qualified review before commercial launch.

---

## Federal Framework

### Securities Act of 1933 / Securities Exchange Act of 1934
**Enforced by:** SEC  
Governs issuance and trading of securities. Relevant if any business activity involves:
- Raising capital from investors
- Operating an investment platform
- Providing investment advice (see Investment Advisers Act)
- Token or digital asset offerings that may qualify as securities

### Investment Advisers Act of 1940
**Enforced by:** SEC  
Registration and conduct requirements for investment advisers. Applies to anyone providing advice about securities for compensation.

**Relevant threshold:** Advisers with <$100M AUM register with state; >$110M AUM register with SEC.

### Commodity Exchange Act (CEA)
**Enforced by:** CFTC  
Governs commodity futures, options, and swaps. Relevant to:
- Series 3 license holders (commodity trading advisors, introducing brokers)
- Any fintech product involving commodity derivatives
- Certain digital assets that CFTC claims jurisdiction over

**Directly relevant:** Series 3 license is a CFTC-regulated credential.

### Dodd-Frank Act
Broad financial reform law. Key provisions for smaller operators:
- Swap dealer and major swap participant registration thresholds
- Volcker Rule (limits proprietary trading — mainly affects banks)
- CFPB authority over consumer financial products and services

### Consumer Financial Protection Act / CFPB Authority
**Enforced by:** CFPB  
The CFPB has authority over "unfair, deceptive, or abusive acts or practices" (UDAAP) in consumer financial products. This is broad and increasingly applied to fintech and adjacent services.

**Applies if:** Any consumer-facing financial product or service.

### Equal Credit Opportunity Act (ECOA) / Regulation B
Prohibits discrimination in credit on basis of protected characteristics. Requires adverse action notices when credit is denied. Increasingly applied to algorithmic underwriting and automated decisions.

### Fair Credit Reporting Act (FCRA)
**Enforced by:** CFPB and FTC  
Governs use of consumer reports. Applies when using credit reports, background checks, or other consumer report data in:
- Credit decisions
- Insurance underwriting (in states that allow credit scoring)
- Employment decisions
- Tenant screening

**Obligations:** Permissible purpose required, adverse action notice required, dispute process required.

### Bank Secrecy Act (BSA) / AML
**Enforced by:** FinCEN  
Requires financial institutions to maintain AML programs, file Suspicious Activity Reports (SARs), and comply with Customer Due Diligence (CDD) rules. Threshold for what constitutes a "financial institution" is broad.

### FinCEN / Beneficial Ownership Rule — 🔴 DOMESTIC COMPANIES NOW EXEMPT
FinCEN's interim final rule (March 26, 2025) removed BOI reporting requirements for **all U.S.-formed entities and U.S. persons**. "Reporting company" now means only entities **formed under foreign law** that registered to do business in the U.S. — and even those need not report U.S.-person beneficial owners. The Eleventh Circuit has since upheld the CTA's constitutionality, but the domestic exemption stands under the FinCEN rule.

**Status:** U.S. LLCs/corporations have no federal BOI filing obligation. Watch: rule could be revised; some **states** (e.g., New York's LLC Transparency Act) have their own disclosure regimes.

---

## Fintech-Specific Considerations

### Payment Services
- Money transmission licenses required in most states for money movement businesses
- Federal: Prepaid cards governed by Regulation E (Electronic Fund Transfer Act)
- Real-time payments: FedNow and RTP network participation has compliance requirements

### Digital Assets / Cryptocurrency
- **🔴 GENIUS Act (signed July 18, 2025):** First federal stablecoin law. Only "permitted issuers" (insured-depository subsidiaries, federal-qualified nonbanks, or state-qualified issuers) may issue payment stablecoins for U.S. persons. 1:1 liquid reserves and monthly public reserve disclosures required. **Implementing rules from OCC/FDIC/NCUA/Treasury/FinCEN/OFAC are due by July 18, 2026 — imminent.** If any product touches stablecoins, track these rules directly.
- **🟡 CLARITY Act (market structure):** Passed House 2025; Senate Banking Committee advanced it May 14, 2026; now on Senate calendar. Would give CFTC exclusive jurisdiction over "digital commodity" spot markets while SEC keeps investment-contract assets. Passage would substantially resolve SEC/CFTC jurisdictional disputes.
- SEC enforcement posture toward digital assets has softened under current leadership; Howey analysis still governs whether a token is a security.
- If any product involves digital assets, specialized legal review essential.

### Buy Now Pay Later (BNPL)
🔴 CFPB **revoked** its 2024 interpretive rule treating BNPL like credit cards (2025) and stated it will not prioritize BNPL enforcement. Regulation Z credit-card protections no longer imputed to BNPL at the federal level; state law and general UDAAP still apply.

### Open Banking / Data Sharing
🔴 CFPB Section 1033 rule (finalized Oct 2024) is **enjoined** — E.D. Kentucky preliminary injunction bars enforcement while CFPB rewrites the rule (ANPR issued Aug 2025). The first compliance date (April 1, 2026) passed without effect. Rule is enjoined, not vacated; a revised rule is expected. Don't build compliance or product plans on the 2024 rule's specifics.

---

## Emerging / Watch Areas

- **🔴 GENIUS Act implementing rules** — statutory deadline July 18, 2026. Comment periods closed June 2026; final rules imminent.
- **🟡 CLARITY Act** — on Senate calendar as of June 2026. Passage would reshape digital asset market structure.
- **🟡 CFPB posture shift** — CFPB withdrew 67 guidance documents (May 2025), rescinded the BNPL rule, and scaled back enforcement broadly. The earlier UDAAP-as-discrimination expansion is no longer active policy. Caution: statutes are unchanged — posture can reverse with the next administration, and state AGs/state UDAP laws remain active.
- **AI in financial decisions** — federal guidance rolled back, but ECOA/FCRA adverse-action requirements still fully apply to algorithmic underwriting.
- **Open banking rewrite** — revised Section 1033 rule expected; both compliance obligations and data-access opportunities in flux.

---

## Key Obligations Checklist

- [ ] Determine if any activity triggers securities registration requirements
- [ ] Series 3 license maintained if any commodity advisory activity
- [ ] FCRA compliance for any use of consumer report data
- [ ] Adverse action notice process in place for automated decisions
- [ ] BSA/AML program if financial institution definition applies
- [ ] Beneficial ownership reporting — U.S.-formed entities currently EXEMPT (verify state-level requirements, e.g., NY)
- [ ] CFPB UDAAP standards applied to all consumer-facing products
- [ ] State money transmission license if moving consumer funds

---

*Last verified against: cftc.gov, sec.gov, consumerfinance.gov, federalregister.gov, fincen.gov, occ.gov, congress.gov (2026-07-01)*  
*Next scheduled check: 2026-08-01*
