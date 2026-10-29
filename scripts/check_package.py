#!/usr/bin/env python3
"""Check the portable package and synthetic briefings without model calls."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FIELDS = {"recommendation", "evidence", "disagreements", "confidence", "revision_conditions", "next_action"}


def validate_brief(case: dict) -> list[str]:
    """Validate the example briefing contract, not the reasoning of any model."""
    errors = []
    if not isinstance(case, dict):
        return ["briefing must be an object"]
    for field in ("id", "decision", "context", "evidence", "constraints", "chair"):
        if not isinstance(case.get(field), str) or not case[field].strip():
            errors.append(f"{field} must be nonempty text")
    if case.get("template") not in {"everyday", "research", "decision", "technical"}:
        errors.append("unknown template")
    if case.get("mode") not in {"simulated", "isolated"}:
        errors.append("mode must be simulated or isolated")
    if type(case.get("rounds")) is not int or case["rounds"] < 1:
        errors.append("rounds must be a positive integer")
    seats = case.get("seats")
    if not isinstance(seats, list) or len(seats) < 2:
        errors.append("at least two analyst mandates are required")
        seats = []
    roles, mandates = [], []
    for seat in seats:
        if not isinstance(seat, dict):
            errors.append("each seat must be an object")
            continue
        for field, seen in (("role", roles), ("mandate", mandates)):
            value = seat.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"seat {field} must be nonempty text")
            else:
                seen.append(" ".join(value.casefold().split()))
        if type(seat.get("adversarial")) is not bool:
            errors.append("seat adversarial flag must be boolean")
    if len(roles) != len(set(roles)):
        errors.append("duplicate roles")
    if len(mandates) != len(set(mandates)):
        errors.append("duplicate mandates")
    if not any(isinstance(s, dict) and s.get("adversarial") is True for s in seats):
        errors.append("an adversarial analyst is required")
    outputs = case.get("required_outputs")
    if not isinstance(outputs, list) or not all(isinstance(x, str) for x in outputs):
        errors.append("required_outputs must be a list of field names")
    elif not OUTPUT_FIELDS.issubset(outputs):
        errors.append("required synthesis fields are missing")
    elif case.get("template") == "technical" and "validation_status" not in outputs:
        errors.append("technical brief requires validation_status")
    return errors


def run() -> dict:
    checks = []

    def record(name: str, errors: list[str]) -> None:
        checks.append({"name": name, "passed": not errors, "errors": errors})

    required = ["README.md", "SKILL.md", "SPEC.md", "RELEASE_NOTES.md", "agents/openai.yaml", "references/source-notes.md", "references/council-workflow.md", "references/glossary.md", "references/benchmark-protocol.md", "references/briefing-cases.json", "references/package-manifest.json", "evals/check-fixtures.py"]
    record("required files", [p for p in required if not (ROOT / p).is_file()])
    if any(not (ROOT / p).is_file() for p in required):
        return {"checks": checks, "passed": False, "model_calls": 0}
    manifest = json.loads((ROOT / "references/package-manifest.json").read_text(encoding="utf-8"))
    skill_bytes = (ROOT / "SKILL.md").read_bytes()
    skill = skill_bytes.decode("utf-8")
    skill_sha = hashlib.sha256(skill_bytes).hexdigest()
    record("skill fingerprint", [] if skill_sha == manifest["skill_sha256"] else ["SKILL.md differs from the recorded export"])
    record("skill metadata", [] if re.search(r"\A---\s*\nname: ai-council\s*\n", skill) and re.search(r"(?m)^description: .+", skill) else ["missing name or description"])
    record("all four source templates", [title for title in manifest["templates"] if f"## {title}" not in skill])
    record("complete source sections", [title for title in ["Role Reference", "Failure Modes to Watch For", "Evaluation Criteria", "Usage Notes for Agents"] if f"## {title}" not in skill])
    record("execution safeguards", [term for term in ["simulated", "isolated", "separate initial contexts", "authorization", "Confidence labels", "budget", "Verify technical findings"] if term not in skill])
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    headings = re.findall(r"(?m)^## (.+)$", readme)
    record("reference README heading order", [] if headings == manifest["readme_h2"] else ["H2 headings differ from the reference contract"])
    record("assistant setup subsection", [] if "### Use the skill in your assistant" in readme else ["missing installation subsection"])
    agent = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    record("agent invocation", [] if 'display_name: "AI Council"' in agent and "$ai-council" in agent else ["agent name or invocation mismatch"])
    links, fences, private = [], [], []
    patterns = [r"[A-Za-z]:[\\/]Users[\\/]", r"/Users/[^/]+/", r"\[\[", r"\bgh[pousr]_[A-Za-z0-9]{20,}\b", r"\bgithub_pat_[A-Za-z0-9_]{20,}\b", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"]
    markdowns = sorted(ROOT.rglob("*.md"))
    for path in markdowns:
        content = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT).as_posix()
        if len(re.findall(r"(?m)^```", content)) % 2:
            fences.append(relative)
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            clean = unquote(target.split("#", 1)[0].strip("<>"))
            resolved = (path.parent / clean).resolve()
            if ROOT not in resolved.parents or not resolved.exists():
                links.append(f"{relative}: {target}")
        if any(re.search(pattern, content) for pattern in patterns):
            private.append(relative)
    record("internal file links", links)
    record("balanced code fences", fences)
    record("specified private-path credential and vault-link patterns", private)
    record("no em dash punctuation", [p.relative_to(ROOT).as_posix() for p in markdowns if "\u2014" in p.read_text(encoding="utf-8")])
    fixture = json.loads((ROOT / "references/briefing-cases.json").read_text(encoding="utf-8"))
    cases = fixture["cases"]
    families = {case.get("template") for case in cases}
    record("four briefing families", [] if families == {"everyday", "research", "decision", "technical"} else ["missing template family"])
    for case in cases:
        record(f"briefing {case.get('id', 'unknown')}", validate_brief(case))
    return {"run_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version.split()[0], "package_version": manifest["package_version"], "skill_sha256": skill_sha, "model_calls": 0, "checks": checks, "passed": all(c["passed"] for c in checks), "passed_count": sum(c["passed"] for c in checks), "check_count": len(checks), "limits": "Structural package and briefing validation only; no host installation, model behavior, latency, or cost measurement."}


if __name__ == "__main__":
    try:
        result = run()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result = {"passed": False, "error": str(exc), "model_calls": 0}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(0 if result["passed"] else 1)
