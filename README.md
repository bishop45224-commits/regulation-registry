# Regulation Registry
**Version:** 1.0  
**Created:** 2026-05-02  
**Owner:** Alvertis Bishop III

---

## What This Is

A local, centrally maintained reference of laws and regulations relevant to commercial projects. It is a working reference — equivalent to reading authoritative articles and understanding their implications — not a substitute for qualified legal advice.

**Always get legal review before commercial launch of any product.**

---

## Directory Structure

```
~/regulatory/
├── registry/               ← Core regulation reference files (markdown)
│   ├── privacy_data.md
│   ├── ai_automation.md
│   ├── insurance_tech.md
│   ├── financial_services.md
│   └── employment_tech.md
├── sources/                ← Source configuration (DO NOT EDIT casually)
│   ├── approved_sources.json     ← Whitelist of approved domains
│   └── state_sources.json        ← All 50 states, dormant until activated
├── manifests/              ← Project manifest schema
│   └── manifest_schema.json      ← Copy this into each project as reg_manifest.json
├── scripts/                ← Automation
│   └── reg_update.py
└── logs/                   ← Auto-generated
    ├── delta_log.json            ← All detected changes with severity
    └── reg_update_[datetime].log ← Per-run logs
```

---

## The Workflow

```
NEW PROJECT
    │
    ▼
1. Copy manifest_schema.json into project root as reg_manifest.json
   Fill in: project name, domains, states
    │
    ▼
2. Run: python ~/regulatory/scripts/reg_update.py --project ./reg_manifest.json
   • <7 days since last update → proceeds
   • >7 days → pulls from approved sources, diffs, logs deltas
    │
    ▼
3. Review Reg Risk Score (P / V / C) generated against current registry
    │
    ▼
BUILD
    │
    ├── Run update script monthly (or set up cron — see below)
    ├── 🔴 Material changes surface immediately in logs
    └── If scope changes, re-run manually
    │
    ▼
BUILD COMPLETE
    → Set "build_complete": true in reg_manifest.json
    → Review violations and gray areas flagged
    │
    ▼
LAUNCH DECISION
    → Script will remind you legal review is required
    → Set "legal_review_complete": true ONLY after actual review
```

---

## Reg Risk Stamp

Every project gets scored on three dimensions (each 1–5):

| Code | Dimension | Measures |
|------|-----------|----------|
| P | Privacy Exposure | Personal data collected, stored, or transmitted |
| V | Regulatory Velocity | How fast law is moving in this domain |
| C | Compliance Gap | Distance from current build to known requirements |

**Format:** `⚖️ REG RISK | P:X V:X C:X | 🟢/🟡/🔴 LEVEL`

- 🟢 Low: avg ≤ 2.3 — Proceed
- 🟡 Medium: avg 2.4–3.5 — Note attached, review before launch
- 🔴 High: avg > 3.5 — Flag prominently, get legal eyes before any commercial deployment

**Generate a stamp manually:**
```bash
python ~/regulatory/scripts/reg_update.py --score 3 4 2
```

---

## Source Governance

The update script **only pulls from domains on the approved whitelist** in `sources/approved_sources.json`. No open web crawling.

**Source tiers:**
- Tier 1 (Federal): federalregister.gov, regulations.gov, congress.gov, ecfr.gov
- Tier 2 (Domain agencies): ftc.gov, nist.gov, cftc.gov, sec.gov, dol.gov, eeoc.gov, consumerfinance.gov
- Tier 2.5 (Quasi-governmental): naic.org — weight accordingly

---

## State Activation

All 50 states are pre-seeded in `sources/state_sources.json` but dormant. A state activates when a project manifest declares it.

**To manually activate a state:**
```bash
python ~/regulatory/scripts/reg_update.py --activate-state OH \
  --domains insurance financial privacy \
  --project-name bishops_friendly
```

This appends the relevant state agency URLs to the approved sources for that project and logs the activation date.

---

## Setting Up Monthly Cron (Optional)

To automate monthly pulls across all active projects:

```bash
# Edit crontab
crontab -e

# Add this line (runs at 8am on the 1st of each month):
0 8 1 * * python3 ~/regulatory/scripts/reg_update.py --force >> ~/regulatory/logs/cron.log 2>&1
```

---

## Change Severity Levels

| Level | Trigger | Action |
|-------|---------|--------|
| 🟢 Informational | Minor wording changes, no impact keywords | Logged only |
| 🟡 Advisory | Proposed rules, guidance, updates, amendments | Surfaces at next checkpoint |
| 🔴 Material | Enforcement actions, new requirements, deadlines, penalties | Surfaces immediately |

---

## Domain Reference Files

| File | Domain | Key Sources |
|------|--------|-------------|
| privacy_data.md | Privacy & Data | FTC, CFPB, state privacy laws |
| ai_automation.md | AI & Automation | NIST, FTC, state AI laws |
| insurance_tech.md | Insurance Tech | NAIC (Tier 2.5), federal insurance law |
| financial_services.md | Financial Services | CFTC, SEC, CFPB |
| employment_tech.md | Employment & Labor | DOL, EEOC, state labor laws |

---

## Important Reminders

1. **This is a reference, not legal advice.** Treat it like reading well-sourced articles.
2. **Legal review is required before any commercial launch.** No exceptions.
3. **URLs in state_sources.json should be verified before first use.** Pre-seeded to best available knowledge — verify at activation time.
4. **The registry is only as good as its last update.** The 7-day freshness rule exists for a reason.
5. **Scope changes during a build require re-running the update.** If you add a feature that touches a new domain or state, declare it in the manifest and re-run.
