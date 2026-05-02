---
domain: Financial Services
version: 1.0
last_verified: 2026-05-02
next_check_due: 2026-06-01
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

### FinCEN / Beneficial Ownership Rule (2024)
Corporate Transparency Act requires most small businesses to report beneficial ownership information to FinCEN. Applies to most LLCs and corporations.

**Status:** Implementation underway. Deadlines have shifted — verify current status.

---

## Fintech-Specific Considerations

### Payment Services
- Money transmission licenses required in most states for money movement businesses
- Federal: Prepaid cards governed by Regulation E (Electronic Fund Transfer Act)
- Real-time payments: FedNow and RTP network participation has compliance requirements

### Digital Assets / Cryptocurrency
- SEC and CFTC dispute jurisdiction over various digital assets
- Bitcoin: CFTC commodity
- Most tokens: SEC treats as securities (Howey test)
- Stablecoins: Active federal legislation pending
- If any product involves digital assets, specialized legal review essential

### Buy Now Pay Later (BNPL)
CFPB has issued interpretive rule applying credit card rules to BNPL products. Rapidly evolving area.

### Open Banking / Data Sharing
CFPB Section 1033 rule (finalized 2024) requires financial institutions to share consumer data upon consumer request. Creates new obligations and opportunities for fintech.

---

## Emerging / Watch Areas

- **Federal digital asset legislation** — active in Congress, likely to pass within 1–2 years. Will significantly reshape crypto regulation.
- **CFPB UDAAP enforcement** — CFPB has expanded UDAAP to cover discrimination, not just traditional deception. Significant enforcement risk for algorithmic products.
- **AI in financial decisions** — CFPB and OCC issuing guidance on model risk management and algorithmic fairness.
- **Open banking implementation** — Section 1033 creates both compliance obligations and potential business opportunities.

---

## Key Obligations Checklist

- [ ] Determine if any activity triggers securities registration requirements
- [ ] Series 3 license maintained if any commodity advisory activity
- [ ] FCRA compliance for any use of consumer report data
- [ ] Adverse action notice process in place for automated decisions
- [ ] BSA/AML program if financial institution definition applies
- [ ] Beneficial ownership reporting to FinCEN (Corporate Transparency Act)
- [ ] CFPB UDAAP standards applied to all consumer-facing products
- [ ] State money transmission license if moving consumer funds

---

*Last verified against: cftc.gov, sec.gov, consumerfinance.gov, federalregister.gov*  
*Next scheduled check: 2026-06-01*
