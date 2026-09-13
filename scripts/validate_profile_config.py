#!/usr/bin/env python
"""Dependency-free static checks for this profile-configuration companion."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "README.md": (
        "# GitHub Profile Configuration Companion",
        "## Active profile README",
        "bastiendfd/bastiendfd",
        "## Local validation",
    ),
    "PROFILE-CHECKLIST.md": (
        "# Generic GitHub Profile README Checklist",
        "## Before publishing",
        "## Minimal template",
        "[Display name or handle]",
    ),
    "SECURITY.md": (
        "# Security Policy",
        "## Reporting a vulnerability",
    ),
    ".gitignore": (".env", "*.pem", "__pycache__/"),
    ".github/workflows/validate.yml": (
        "name: Validate profile configuration",
        "python scripts/validate_profile_config.py",
        "actions/checkout@v4",
    ),
}


def main() -> int:
    failures: list[str] = []
    for relative_path, required_text in REQUIRED_FILES.items():
        path = ROOT / relative_path
        if not path.is_file():
            failures.append(f"missing required file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in required_text:
            if needle not in text:
                failures.append(f"{relative_path}: missing required text: {needle!r}")

    if failures:
        print("Validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Validation passed: {len(REQUIRED_FILES)} required files checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
