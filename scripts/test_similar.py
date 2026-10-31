#!/usr/bin/env python3
"""Regression test for `kg.py similar` (run: python3 scripts/test_similar.py).

PARAPHRASES must score >= THRESHOLD against the expected existing node.
DISTINCT topics are referenced by existing articles as separate nodes, so they must score
below THRESHOLD against every article (checked only while they are still unwritten).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kg  # noqa: E402

THRESHOLD = 0.5

PARAPHRASES = [
    ("Governor Limit", "kt:governor-limits"), ("Apex Governor Limits", "kt:governor-limits"),
    ("Gvernor Limits", "kt:governor-limits"), ("Async Apex", "kt:asynchronous-apex"),
    ("Asynchronous Apex Jobs", "kt:asynchronous-apex"),
    ("Master-Detail vs Lookup Relationships", "kt:lookup-vs-master-detail"),
    ("Platform Event", "kt:platform-events"), ("Role Hierarchies", "kt:role-hierarchy"),
    ("Omnichannel", "kt:omni-channel"), ("Omni Channel Routing", "kt:omni-channel"),
    ("Well Architected", "kt:well-architected-framework"),
    ("Salesforce Well-Architected Framework", "kt:well-architected-framework"),
    ("Connected App", "kt:connected-apps"), ("Multi-Tenancy", "kt:multitenancy"),
    ("Multitenant Architecture", "kt:multitenancy"), ("Environment Strategies", "kt:environment-strategy"),
    ("Rollup Summary Fields", "kt:roll-up-summary-field"), ("ALM", "kt:application-lifecycle-management"),
    ("Change Set", "kt:change-sets"), ("Data Skews", "kt:data-skew"), ("Ownership Data Skew", "kt:data-skew"),
    ("Flow Builder Tool", "kt:flow-builder"), ("Salesforce Order of Execution", "kt:order-of-execution"),
    ("Metadata API (MDAPI)", "kt:metadata-api"), ("Public Sector Solution", "kt:public-sector-solutions"),
    ("Agent Development Life Cycle", "kt:agent-development-lifecycle"),
]

DISTINCT = {
    "kt:apex-triggers": "Apex Triggers", "kt:agentforce": "Agentforce", "kt:record-locking": "Record Locking",
    "kt:record-triggered-flow": "Record-Triggered Flow", "kt:salesforce-sharing-model": "Salesforce Sharing Model",
    "kt:sandbox-types": "Sandbox Types", "kt:service-cloud": "Service Cloud", "kt:apex-testing": "Apex Testing",
    "kt:object-relationships": "Object Relationships", "kt:sharing-recalculation": "Sharing Recalculation",
    "kt:external-client-apps": "External Client Apps", "kt:salesforce-cli": "Salesforce CLI",
    "kt:salesforce-dx": "Salesforce DX", "kt:salesforce-architect": "Salesforce Architect",
    "kt:salesforce-data-mask": "Salesforce Data Mask", "kt:batch-apex": "Batch Apex",
    "kt:queueable-apex": "Queueable Apex", "kt:apex": "Apex", "kt:screen-flow": "Screen Flow",
    "kt:process-builder": "Process Builder", "kt:change-data-capture": "Change Data Capture",
    "kt:org-strategy": "Org Strategy", "kt:sandbox-templates": "Sandbox Templates",
    "kt:large-data-volumes": "Large Data Volumes", "kt:junction-object": "Junction Object",
    "kt:agentforce-testing-center": "Agentforce Testing Center",
    "kt:metadata-driven-architecture": "Metadata-Driven Architecture",
}


def best(sim, arts, query):
    scored = []
    for a in arts:
        labels = [a.get("title", "")] + list(a.get("aliases") or [])
        s = max(sim(query, x) for x in labels)
        if kg.norm(query) in {kg.norm(x) for x in labels}:
            s = 1.0
        scored.append((s, a["id"]))
    return max(scored)


def main() -> int:
    arts, errs = kg.load_articles()
    if errs:
        print("\n".join(errs))
        return 1
    sim = kg.LabelSimilarity(arts)
    written = {a["id"] for a in arts}
    fails = []
    for q, expected in PARAPHRASES:
        if expected not in written:
            continue
        s, got = best(sim, arts, q)
        if s < THRESHOLD or got != expected:
            fails.append(f"missed paraphrase: '{q}' -> {got} {s:.2f} (expected {expected})")
    for node, title in DISTINCT.items():
        if node in written:
            continue
        s, got = best(sim, arts, title)
        if s >= THRESHOLD:
            fails.append(f"false match: '{title}' -> {got} {s:.2f}")
    for f in fails:
        print("FAIL", f)
    print("OK" if not fails else f"{len(fails)} failure(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
