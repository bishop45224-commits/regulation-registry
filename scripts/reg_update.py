#!/usr/bin/env python3
"""
Regulation Registry Update Script
==================================
Checks freshness of registry files, pulls from approved sources,
diffs against current content, logs deltas with severity, and
activates state sources when declared in project manifests.

Usage:
    python reg_update.py                    # Check all registries
    python reg_update.py --project PATH     # Check for a specific project manifest
    python reg_update.py --force            # Force update regardless of freshness
    python reg_update.py --activate-state OH insurance financial  # Activate a state for domains
"""

import json
import os
import sys
import argparse
import hashlib
import logging
from datetime import datetime, timedelta
from pathlib import Path
import urllib.request
import urllib.error

# ─────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────

REGISTRY_ROOT = Path.home() / "regulatory"
REGISTRY_DIR  = REGISTRY_ROOT / "registry"
SOURCES_DIR   = REGISTRY_ROOT / "sources"
MANIFESTS_DIR = REGISTRY_ROOT / "manifests"
LOGS_DIR      = REGISTRY_ROOT / "logs"

APPROVED_SOURCES_FILE = SOURCES_DIR / "approved_sources.json"
STATE_SOURCES_FILE    = SOURCES_DIR / "state_sources.json"

FRESHNESS_THRESHOLD_DAYS = 7    # New project check
BUILD_CYCLE_DAYS         = 30   # Active build check
DORMANT_THRESHOLD_DAYS   = 60   # Dormant project re-check

SEVERITY_LEVELS = {
    "green":    "🟢 INFORMATIONAL — No action required",
    "advisory": "🟡 ADVISORY — Review at next natural checkpoint",
    "red":      "🔴 MATERIAL — Surface immediately, review before proceeding"
}

# Keywords that elevate a change to material severity
MATERIAL_KEYWORDS = [
    "enforcement action", "effective immediately", "penalty", "violation",
    "prohibited", "banned", "injunction", "consent order", "fine",
    "new requirement", "mandatory", "compliance deadline", "takes effect"
]

ADVISORY_KEYWORDS = [
    "proposed rule", "notice of proposed rulemaking", "nprm", "draft",
    "comment period", "guidance", "bulletin", "advisory", "updated",
    "amended", "revised", "clarification"
]

# ─────────────────────────────────────────────
# Logging Setup
# ─────────────────────────────────────────────

def setup_logging():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOGS_DIR / f"reg_update_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return log_file

# ─────────────────────────────────────────────
# Source Whitelist Enforcement
# ─────────────────────────────────────────────

def load_approved_sources() -> dict:
    """Load and return the approved sources whitelist."""
    if not APPROVED_SOURCES_FILE.exists():
        logging.error(f"Approved sources file not found: {APPROVED_SOURCES_FILE}")
        sys.exit(1)
    with open(APPROVED_SOURCES_FILE) as f:
        return json.load(f)

def get_all_approved_domains(sources: dict) -> set:
    """Extract all approved domains from the sources config."""
    domains = set()
    for category, data in sources.items():
        if category.startswith("_"):
            continue
        for source in data.get("sources", []):
            domains.add(source["domain"])
    return domains

def is_domain_approved(domain: str, approved_domains: set) -> bool:
    """Check if a domain is on the approved whitelist."""
    domain = domain.lower().strip()
    return any(domain == d or domain.endswith("." + d) for d in approved_domains)

# ─────────────────────────────────────────────
# Freshness Checks
# ─────────────────────────────────────────────

def parse_date(date_str: str) -> datetime:
    """Parse a YYYY-MM-DD date string."""
    return datetime.strptime(date_str, "%Y-%m-%d")

def days_since(date_str: str) -> int:
    """Return number of days since a date string."""
    if not date_str:
        return 9999
    return (datetime.now() - parse_date(date_str)).days

def check_registry_freshness(threshold_days: int = FRESHNESS_THRESHOLD_DAYS) -> dict:
    """
    Check freshness of all registry files.
    Returns dict of {domain: {stale: bool, days_old: int, last_verified: str}}
    """
    results = {}
    for md_file in REGISTRY_DIR.glob("*.md"):
        domain = md_file.stem
        last_verified = None

        with open(md_file) as f:
            for line in f:
                if line.startswith("last_verified:"):
                    last_verified = line.split(":", 1)[1].strip()
                    break

        age = days_since(last_verified)
        results[domain] = {
            "stale": age > threshold_days,
            "days_old": age,
            "last_verified": last_verified,
            "file": str(md_file)
        }

    return results

# ─────────────────────────────────────────────
# Source Fetching (Whitelist-Enforced)
# ─────────────────────────────────────────────

def fetch_url(url: str, approved_domains: set) -> str | None:
    """
    Fetch content from a URL only if the domain is on the approved whitelist.
    Returns page text or None on failure.
    """
    from urllib.parse import urlparse
    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "")

    if not is_domain_approved(domain, approved_domains):
        logging.warning(f"BLOCKED: {url} — domain '{domain}' is not on the approved whitelist.")
        return None

    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "RegulationRegistry/1.0 (compliance reference tool)"}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as e:
        logging.warning(f"Failed to fetch {url}: {e}")
        return None

# ─────────────────────────────────────────────
# Delta Detection and Severity Classification
# ─────────────────────────────────────────────

def hash_content(content: str) -> str:
    """Return MD5 hash of content for change detection."""
    return hashlib.md5(content.encode()).hexdigest()

def classify_severity(new_content: str, old_content: str) -> str:
    """
    Classify the severity of a change based on content keywords.
    Returns: 'red', 'advisory', or 'green'
    """
    diff_text = new_content.lower()

    for keyword in MATERIAL_KEYWORDS:
        if keyword in diff_text:
            return "red"

    for keyword in ADVISORY_KEYWORDS:
        if keyword in diff_text:
            return "advisory"

    return "green"

def log_delta(domain: str, severity: str, summary: str, delta_log_file: Path):
    """Append a delta entry to the delta log."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "domain": domain,
        "severity": severity,
        "severity_label": SEVERITY_LEVELS[severity],
        "summary": summary
    }

    existing = []
    if delta_log_file.exists():
        with open(delta_log_file) as f:
            try:
                existing = json.load(f)
            except json.JSONDecodeError:
                existing = []

    existing.append(entry)

    with open(delta_log_file, "w") as f:
        json.dump(existing, f, indent=2)

    return entry

# ─────────────────────────────────────────────
# State Activation
# ─────────────────────────────────────────────

def load_state_sources() -> dict:
    """Load state sources file."""
    if not STATE_SOURCES_FILE.exists():
        logging.error(f"State sources file not found: {STATE_SOURCES_FILE}")
        return {}
    with open(STATE_SOURCES_FILE) as f:
        return json.load(f)

def activate_state(state_code: str, domains: list[str], project_name: str) -> dict:
    """
    Activate a state for specific domains on behalf of a project.
    Returns the activated sources for that state.
    """
    state_code = state_code.upper()
    data = load_state_sources()

    if state_code not in data.get("state_sources", {}):
        logging.error(f"State code '{state_code}' not found in state_sources.json")
        return {}

    state = data["state_sources"][state_code]

    if state.get("activated") and project_name in state.get("activated_by", []):
        logging.info(f"{state_code} already activated for {project_name}")
        return state

    # Activate
    state["activated"] = True
    state["activated_date"] = datetime.now().strftime("%Y-%m-%d")
    if project_name not in state.get("activated_by", []):
        state.setdefault("activated_by", []).append(project_name)

    # Log activation
    activation_entry = {
        "state": state_code,
        "project": project_name,
        "domains": domains,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    data["_meta"].setdefault("activation_log", []).append(activation_entry)

    with open(STATE_SOURCES_FILE, "w") as f:
        json.dump(data, f, indent=2)

    activated_sources = {}
    for domain in domains:
        url = state.get(domain)
        if url:
            activated_sources[domain] = url
            logging.info(f"  ✅ Activated {state_code} / {domain} → {url}")
        else:
            logging.info(f"  ⚠️  {state_code} / {domain} → null (defers to federal source)")

    notes = state.get("_notes")
    if notes:
        logging.warning(f"  📌 State note for {state_code}: {notes}")

    return activated_sources

# ─────────────────────────────────────────────
# Manifest Handling
# ─────────────────────────────────────────────

def load_manifest(manifest_path: Path) -> dict:
    """Load a project manifest."""
    if not manifest_path.exists():
        logging.error(f"Manifest not found: {manifest_path}")
        return {}
    with open(manifest_path) as f:
        return json.load(f)

def update_manifest(manifest_path: Path, updates: dict):
    """Update specific fields in a manifest file."""
    manifest = load_manifest(manifest_path)
    manifest.update(updates)
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

def check_dormant(manifest: dict) -> bool:
    """Check if a project has been dormant for more than DORMANT_THRESHOLD_DAYS."""
    last_active = manifest.get("project", {}).get("last_active")
    if not last_active:
        return False
    return days_since(last_active) > DORMANT_THRESHOLD_DAYS

# ─────────────────────────────────────────────
# Reg Risk Scoring
# ─────────────────────────────────────────────

def generate_risk_stamp(P: int, V: int, C: int, notes: str = "") -> str:
    """Generate the Reg Risk stamp string."""
    avg = (P + V + C) / 3
    if avg <= 2.3:
        level = "🟢 LOW"
    elif avg <= 3.5:
        level = "🟡 MEDIUM"
    else:
        level = "🔴 HIGH"

    stamp = f"⚖️  REG RISK  |  P:{P}  V:{V}  C:{C}  |  {level}"
    if notes and avg > 2.3:
        stamp += f"\n   └─ {notes}"
    return stamp

# ─────────────────────────────────────────────
# Main Update Flow
# ─────────────────────────────────────────────

def run_update(project_manifest_path: Path = None, force: bool = False):
    """
    Main update routine.
    1. Check registry freshness
    2. Pull and diff stale domains (whitelist-enforced)
    3. Log deltas with severity
    4. If project manifest provided, handle state activation and dormancy check
    """
    log_file = setup_logging()
    approved_sources = load_approved_sources()
    approved_domains = get_all_approved_domains(approved_sources)
    delta_log = LOGS_DIR / "delta_log.json"

    logging.info("=" * 60)
    logging.info("Regulation Registry — Update Check")
    logging.info(f"Timestamp: {datetime.now().isoformat()}")
    logging.info("=" * 60)

    # ── Project Manifest Handling ──
    manifest = None
    if project_manifest_path:
        manifest = load_manifest(project_manifest_path)
        project_name = manifest.get("project", {}).get("name", "unknown")
        logging.info(f"Project: {project_name}")

        # Dormancy check
        if check_dormant(manifest):
            logging.warning(
                f"⚠️  DORMANT PROJECT: '{project_name}' has been inactive for "
                f"{days_since(manifest['project']['last_active'])} days. "
                f"Forcing full registry refresh."
            )
            force = True

        # State activation
        declared_states = manifest.get("states", [])
        declared_domains = manifest.get("domains", [])
        if declared_states:
            logging.info(f"Activating states: {declared_states}")
            for state in declared_states:
                activate_state(state, declared_domains, project_name)

    # ── Freshness Check ──
    threshold = FRESHNESS_THRESHOLD_DAYS if not manifest else BUILD_CYCLE_DAYS
    freshness = check_registry_freshness(threshold)

    material_changes = []
    advisory_changes = []

    for domain, info in freshness.items():
        if not force and not info["stale"]:
            logging.info(f"✅ {domain}: Fresh ({info['days_old']} days old)")
            continue

        logging.info(f"🔄 {domain}: Stale ({info['days_old']} days old) — checking sources...")

        # Get approved source URLs for this domain
        domain_sources = approved_sources.get(domain, {}).get("sources", [])
        if not domain_sources:
            # Try federal as fallback
            domain_sources = approved_sources.get("federal", {}).get("sources", [])

        changes_found = False
        for source in domain_sources[:2]:  # Check first two sources per domain
            url = f"https://{source['domain']}"
            content = fetch_url(url, approved_domains)

            if not content:
                continue

            content_hash = hash_content(content[:5000])  # Hash first 5k chars as fingerprint

            # Compare with stored hash if exists
            hash_file = LOGS_DIR / f"{domain}_{source['domain'].replace('.', '_')}.hash"
            if hash_file.exists():
                stored_hash = hash_file.read_text().strip()
                if stored_hash != content_hash:
                    severity = classify_severity(content, "")
                    summary = f"{domain} — change detected at {source['domain']}"
                    delta = log_delta(domain, severity, summary, delta_log)

                    if severity == "red":
                        material_changes.append(delta)
                    elif severity == "advisory":
                        advisory_changes.append(delta)

                    changes_found = True
                    logging.info(f"  {SEVERITY_LEVELS[severity]}")
            else:
                logging.info(f"  📥 First pull from {source['domain']} — baseline recorded")

            # Update stored hash
            hash_file.write_text(content_hash)

        # Update last_verified in registry file
        reg_file = REGISTRY_DIR / f"{domain}.md"
        if reg_file.exists():
            content = reg_file.read_text()
            today = datetime.now().strftime("%Y-%m-%d")
            next_check = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

            # Update dates in frontmatter
            lines = content.split("\n")
            updated_lines = []
            for line in lines:
                if line.startswith("last_verified:"):
                    updated_lines.append(f"last_verified: {today}")
                elif line.startswith("next_check_due:"):
                    updated_lines.append(f"next_check_due: {next_check}")
                else:
                    updated_lines.append(line)
            reg_file.write_text("\n".join(updated_lines))

        if not changes_found:
            logging.info(f"  No changes detected — last_verified updated")

    # ── Summary Report ──
    logging.info("\n" + "=" * 60)
    logging.info("UPDATE SUMMARY")
    logging.info("=" * 60)

    if material_changes:
        logging.warning(f"🔴 {len(material_changes)} MATERIAL CHANGE(S) — Immediate review required:")
        for c in material_changes:
            logging.warning(f"   • {c['domain']}: {c['summary']}")

    if advisory_changes:
        logging.info(f"🟡 {len(advisory_changes)} ADVISORY CHANGE(S) — Review at next checkpoint:")
        for c in advisory_changes:
            logging.info(f"   • {c['domain']}: {c['summary']}")

    if not material_changes and not advisory_changes:
        logging.info("🟢 No regulatory changes detected across monitored domains")

    logging.info(f"\nLog saved to: {log_file}")
    logging.info(f"Delta log: {delta_log}")

    # ── Launch Reminder ──
    if manifest:
        launch_info = manifest.get("launch", {})
        if launch_info.get("build_complete") and not launch_info.get("legal_review_complete"):
            logging.warning("\n" + "⚠️ " * 20)
            logging.warning("LAUNCH REMINDER: Build is marked complete but legal review is NOT recorded.")
            logging.warning("DO NOT launch commercially until legal review is complete.")
            logging.warning("Update 'launch.legal_review_complete' and 'launch.legal_review_date' in your manifest.")
            logging.warning("⚠️ " * 20)

# ── Auto-commit and push changes to GitHub ──
    if material_changes or advisory_changes:
        try:
            import subprocess
            commit_msg = f"chore: registry update {datetime.now().strftime('%Y-%m-%d')} — {len(material_changes)} material, {len(advisory_changes)} advisory"
            subprocess.run(["git", "add", "-A"], cwd=REGISTRY_ROOT, check=True)
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=REGISTRY_ROOT, check=True)
            subprocess.run(["git", "push"], cwd=REGISTRY_ROOT, check=True)
            logging.info("✅ Registry changes committed and pushed to GitHub")
        except Exception as e:
            logging.warning(f"Git push failed — changes saved locally only: {e}")

    return {
        "material_changes": material_changes,
        "advisory_changes": advisory_changes,
        "freshness": freshness
    }

# ─────────────────────────────────────────────
# CLI Entry Point
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Regulation Registry Update Tool")
    parser.add_argument("--project",        type=str,  help="Path to project reg_manifest.json")
    parser.add_argument("--force",          action="store_true", help="Force update regardless of freshness")
    parser.add_argument("--activate-state", type=str,  help="State code to activate (e.g. OH)")
    parser.add_argument("--domains",        nargs="+", help="Domains for state activation")
    parser.add_argument("--project-name",   type=str,  help="Project name for state activation logging")
    parser.add_argument("--score",          nargs=3,   type=int, metavar=("P", "V", "C"),
                        help="Generate a Reg Risk stamp: --score P V C")

    args = parser.parse_args()

    # Standalone state activation
    if args.activate_state:
        setup_logging()
        domains = args.domains or ["insurance", "financial", "privacy", "employment"]
        project = args.project_name or "manual_activation"
        result = activate_state(args.activate_state, domains, project)
        print(json.dumps(result, indent=2))
        return

    # Standalone risk stamp
    if args.score:
        P, V, C = args.score
        print(generate_risk_stamp(P, V, C))
        return

    # Main update
    manifest_path = Path(args.project) if args.project else None
    run_update(manifest_path, force=args.force)

if __name__ == "__main__":
    main()
