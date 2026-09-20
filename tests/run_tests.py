#!/usr/bin/env python3
"""Deterministic package checks for the Elonize skill and its eval manifest."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "tests" / "adversarial_cases.json"

REQUIRED_REFERENCES = {
    "doctrine.md",
    "context-ingestion-and-compression.md",
    "provenance.md",
    "temporal-truth-and-contradictions.md",
    "causal-and-dependency-graphs.md",
    "bottlenecks-and-critical-path.md",
    "recursive-time-compression.md",
    "resources-parallelization-and-automation.md",
    "anti-delusion-and-feasibility.md",
    "rolling-replanning.md",
    "execution-loop.md",
    "output-contracts.md",
}

REQUIRED_CATEGORIES = {
    "context",
    "provenance",
    "temporal-truth",
    "causal-graph",
    "critical-path",
    "time-compression",
    "resources",
    "anti-delusion",
    "replanning",
    "execution",
    "authority",
}

REQUIRED_IDEAS = {
    "compress causes": "compress causes of elapsed time",
    "smallest sufficient state": "smallest sufficient state",
    "recoverable provenance": "provenance",
    "deadline skepticism": "deadline",
    "validated state change": "validated state change",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_cases(errors: list[str]) -> dict:
    if not CASES_PATH.is_file():
        fail(errors, f"missing {CASES_PATH.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(CASES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"cannot parse adversarial cases: {exc}")
        return {}


def check_cases(errors: list[str]) -> None:
    manifest = load_cases(errors)
    cases = manifest.get("cases", []) if isinstance(manifest, dict) else []
    if manifest.get("schema_version") != "1.0":
        fail(errors, "adversarial case schema_version must be 1.0")
    if len(cases) < 16:
        fail(errors, "adversarial suite must contain at least 16 cases")

    seen_ids: set[str] = set()
    categories: set[str] = set()
    module_coverage: set[str] = set()
    required_fields = {
        "id",
        "category",
        "prompt",
        "traps",
        "must",
        "must_not",
        "fatal_failures",
        "modules",
    }

    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            fail(errors, f"case {index} is not an object")
            continue
        missing = required_fields - set(case)
        if missing:
            fail(errors, f"case {index} missing fields: {sorted(missing)}")
            continue
        case_id = case["id"]
        if case_id in seen_ids:
            fail(errors, f"duplicate case id: {case_id}")
        seen_ids.add(case_id)
        categories.add(case["category"])
        module_coverage.update(case["modules"])
        for field in ("traps", "must", "must_not", "fatal_failures", "modules"):
            if not isinstance(case[field], list) or not case[field]:
                fail(errors, f"{case_id}.{field} must be a non-empty list")
        if len(case["prompt"].strip()) < 80:
            fail(errors, f"{case_id}.prompt is too shallow for an adversarial case")

    missing_categories = REQUIRED_CATEGORIES - categories
    if missing_categories:
        fail(errors, f"missing adversarial categories: {sorted(missing_categories)}")
    missing_module_coverage = REQUIRED_REFERENCES - module_coverage
    if missing_module_coverage:
        fail(
            errors,
            f"references without behavioral coverage: {sorted(missing_module_coverage)}",
        )


def check_skill(errors: list[str]) -> None:
    skill = ROOT / "SKILL.md"
    if not skill.is_file():
        fail(errors, "missing SKILL.md")
        return
    text = skill.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > 260:
        fail(errors, f"SKILL.md is not compact: {len(lines)} lines (max 260)")
    if len(text.encode("utf-8")) > 18_000:
        fail(errors, "SKILL.md is not compact: exceeds 18 KB")

    frontmatter = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not frontmatter:
        fail(errors, "SKILL.md lacks valid YAML frontmatter delimiters")
    else:
        header = frontmatter.group(1)
        if not re.search(r"^name:\s*elonize\s*$", header, flags=re.MULTILINE):
            fail(errors, "SKILL.md frontmatter name must be elonize")
        description = re.search(r"^description:\s*(.+)$", header, flags=re.MULTILINE)
        if not description or len(description.group(1).strip(" '\"")) < 60:
            fail(errors, "SKILL.md needs a discriminating description")

    lowered = text.lower()
    for label, phrase in REQUIRED_IDEAS.items():
        if phrase not in lowered:
            fail(errors, f"SKILL.md omits core idea: {label}")

    linked = set(re.findall(r"references/([a-z0-9-]+\.md)", text))
    missing_links = REQUIRED_REFERENCES - linked
    if missing_links:
        fail(errors, f"SKILL.md does not route to: {sorted(missing_links)}")


def check_references(errors: list[str]) -> None:
    reference_dir = ROOT / "references"
    for filename in sorted(REQUIRED_REFERENCES):
        path = reference_dir / filename
        if not path.is_file():
            fail(errors, f"missing references/{filename}")
            continue
        text = path.read_text(encoding="utf-8")
        if len(text.strip()) < 500:
            fail(errors, f"references/{filename} is too thin")
        if re.search(r"\b(TODO|TBD|FIXME|PLACEHOLDER)\b", text, re.IGNORECASE):
            fail(errors, f"references/{filename} contains unfinished placeholders")

    for markdown in [ROOT / "SKILL.md", *reference_dir.glob("*.md")]:
        if not markdown.is_file():
            continue
        for target in re.findall(r"\[[^\]]+\]\(([^)#]+\.md)(?:#[^)]+)?\)", markdown.read_text(encoding="utf-8")):
            resolved = (markdown.parent / target).resolve()
            if not resolved.is_file():
                fail(errors, f"broken link in {markdown.relative_to(ROOT)}: {target}")


def check_package(errors: list[str]) -> None:
    openai_yaml = ROOT / "agents" / "openai.yaml"
    if not openai_yaml.is_file():
        fail(errors, "missing agents/openai.yaml")
    else:
        metadata = openai_yaml.read_text(encoding="utf-8")
        if "$elonize" not in metadata:
            fail(errors, "agents/openai.yaml default_prompt must mention $elonize")
        if not re.search(r"allow_implicit_invocation:\s*true\b", metadata):
            fail(errors, "Elonize should allow implicit invocation")
    workflow = ROOT / ".github" / "workflows" / "validate.yml"
    if not workflow.is_file():
        fail(errors, "missing GitHub validation workflow")
    elif "python3 tests/run_tests.py" not in workflow.read_text(encoding="utf-8"):
        fail(errors, "GitHub validation workflow does not run the package tests")
    evaluator = ROOT / "tests" / "EVALUATOR.md"
    if not evaluator.is_file():
        fail(errors, "missing tests/EVALUATOR.md")


def main() -> int:
    errors: list[str] = []
    check_cases(errors)
    check_skill(errors)
    check_references(errors)
    check_package(errors)
    if errors:
        print("RED: Elonize package validation failed")
        for error in errors:
            print(f"- {error}")
        return 1
    print("GREEN: Elonize package and adversarial manifest passed deterministic checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
