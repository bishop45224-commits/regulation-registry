---
domain: Platform & Partner Rules (Non-Regulatory, Binding by Contract)
version: 1.0
last_verified: 2026-11-16
next_check_due: 2026-12-01
sources: [support.google.com, developers.google.com, play.google/developer-content-policy]
non_regulatory: true
applies_to_projects: []
---

# Platform & Partner Rules Reference

> **Scope:** App store, API, and AI-provider rules that are not laws but are binding by contract — violating them means removal from the platform, not a fine. Companion to standards_frameworks.md.
> **Source Note:** ⚠️ These come from platform operators (Google, Apple, AI providers), not government sources, and change on the platforms' own schedules — often faster than law. They will never surface from the government-source whitelist; verify against the platform's own policy pages, not summaries.
> **Why they're in the registry:** For a consumer app, platform rules are usually the first "regulator" encountered — Play Store review happens before any AG ever looks. Several platform rules also operationalize legal obligations (consent, disclosure, data safety).
> **Reminder:** This is a reference, not legal advice. Get qualified review before commercial launch.

---

## Google Play (Android distribution)

### User Data policy — 🔴 extended to third-party AI (July 2026)
Google's User Data requirements now expressly cover **third-party AI integrations** (products, services, code): the developer remains responsible for **limited use, disclosure, and consent** when user data flows to an AI model provider — including via SDKs that route content to one. Announced ~July 15, 2026 (per secondary write-ups; the policy page carries the wording — read Google's text in Play Console before relying). Practical reading:
- Privacy policy AND the Play **Data safety form** must both say user data leaves the app for a third-party model provider
- Prominent in-app disclosure **before** any consent request; consent via a distinct affirmative action
- Limited use: data sent to the provider is used only for the requesting feature

### Data safety form, privacy policy, account deletion
- Accurate Data safety section required for production tracks (internal test tracks are exempt from the form, not from honesty)
- If the app lets users create accounts, **in-app AND web account deletion** paths are required
- The privacy policy link must work and match actual practice (also an FTC Act §5 issue — see privacy_data.md)

### AI-Generated Content policy
Apps that generate content with AI must provide **in-app reporting** of offensive output and use the reports. Required at Play release.

### Target API level
New apps and updates must target **Android 16 (API 36) since August 31, 2026**. This ratchets annually — check each year's deadline.

---

## Google APIs (Calendar, Workspace)

### Google API Services User Data Policy (incl. Limited Use)
Google user data obtained via APIs may be used only to provide a prominent, user-facing feature with consent; no sale; no ads; no human reading except narrow cases.

### Workspace API + AI rule (Feb 2024)
Google Workspace data (incl. Calendar) may **not** be used to train generalized AI/ML models. Transfers to third-party AI tools only to provide the user-requested feature, with disclosure. The privacy policy must state this. Restricted-scope verification/assessment may apply depending on scopes used.

---

## Apple App Store (if/when iOS ships)
Placeholder — verify at the time: privacy "nutrition labels," account deletion requirement (5.1.1(v)), consent for data collection, and any AI-content rules in force then.

---

## AI provider terms (OpenRouter, Anthropic, OpenAI, Google)
Each provider's usage policy constrains what an app built on it may do (prohibited uses, requirements to disclose AI, minor protections, rate/abuse rules) and what passes through to end users. **Read each provider's current terms before release and at each renewal** — they change frequently and are not tracked item-by-item here.

## Local / bundled model licenses (Llama, Gemma, Qwen, …)
Shipping a model with an app makes its license a distribution term: attribution/notice requirements, acceptable-use policies, and version-scoped terms (e.g., Gemma's terms per version). Credit notices in-app where required.

---

## Practical Guidance
- Treat the Play Data safety form as a **legal document**: it must match the privacy policy and the code. Mismatches are both a takedown risk and an FTC §5 deception risk.
- When adding any AI feature, re-check three layers in order: platform policy (this file) → provider terms → law (other registry files).
- Platform rules change without a Federal Register notice. Re-verify this file's items against the platforms' own change logs each cycle.

---

*Sources: support.google.com/googleplay/android-developer, developers.google.com/terms/api-services-user-data-policy, workspace.google.com (2026-11-16; July 2026 Play AI change partially via secondary write-ups — read Google's announcement in Play Console)*
*Next scheduled check: 2026-12-01*
