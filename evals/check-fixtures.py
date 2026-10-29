#!/usr/bin/env python3
"""Exercise briefing validation using synthetic positive and negative fixtures."""
from __future__ import annotations

import copy
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("package_check", ROOT / "scripts/check_package.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def run() -> dict:
    cases = json.loads((ROOT / "references/briefing-cases.json").read_text(encoding="utf-8"))["cases"]
    checks = []
    for case in cases:
        errors = module.validate_brief(case)
        checks.append({"case": f"accept {case['id']}", "passed": not errors, "observed_errors": errors})
    base = cases[0]
    mutations = [
        ("missing decision", lambda c: c.pop("decision"), "decision must be nonempty text"),
        ("unsupported mode", lambda c: c.update(mode="independent-by-prompt"), "mode must be simulated or isolated"),
        ("duplicate mandates", lambda c: c["seats"][1].update(mandate=c["seats"][0]["mandate"]), "duplicate mandates"),
        ("no adversarial seat", lambda c: [s.update(adversarial=False) for s in c["seats"]], "an adversarial analyst is required"),
        ("missing chair", lambda c: c.update(chair=""), "chair must be nonempty text"),
        ("zero rounds", lambda c: c.update(rounds=0), "rounds must be a positive integer"),
        ("boolean rounds", lambda c: c.update(rounds=True), "rounds must be a positive integer"),
        ("missing confidence output", lambda c: c["required_outputs"].remove("confidence"), "required synthesis fields are missing"),
        ("malformed seat", lambda c: c["seats"].append("reviewer"), "each seat must be an object"),
        ("invalid evidence type", lambda c: c.update(evidence=[]), "evidence must be nonempty text"),
    ]
    for name, mutate, expected in mutations:
        case = copy.deepcopy(base)
        mutate(case)
        errors = module.validate_brief(case)
        checks.append({"case": f"reject {name}", "passed": expected in errors, "expected_error": expected, "observed_errors": errors})
    technical = copy.deepcopy(cases[-1])
    technical["required_outputs"].remove("validation_status")
    errors = module.validate_brief(technical)
    checks.append({"case": "reject technical briefing without validation status", "passed": "technical brief requires validation_status" in errors, "observed_errors": errors})
    return {"run_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version.split()[0], "model_calls": 0, "checks": checks, "passed": all(c["passed"] for c in checks), "passed_count": sum(c["passed"] for c in checks), "check_count": len(checks), "limits": "These fixtures test local input validation, not model behavior or factual accuracy."}


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(0 if result["passed"] else 1)
