# GitHub Profile Configuration Companion

This repository is a small, public companion for maintaining a GitHub profile repository. It is documentation and configuration guidance—not an application, service, or source of personal profile data.

## Active profile README

The active public profile README is maintained in **[bastiendfd/bastiendfd](https://github.com/bastiendfd/bastiendfd)**. GitHub displays that repository's `README.md` on the `bastiendfd` profile because its repository name matches the account name.

Use this repository to review a generic profile setup checklist and to keep reusable, non-personal configuration guidance separate from the public profile itself.

## Contents

- [`PROFILE-CHECKLIST.md`](PROFILE-CHECKLIST.md) — generic checklist and Markdown template for a profile README.
- [`SECURITY.md`](SECURITY.md) — instructions for reporting security concerns.
- [`.github/workflows/validate.yml`](.github/workflows/validate.yml) — lightweight, dependency-free static validation.

## Scope and privacy

Keep this repository generic. Do not commit contact details, location, employer information, credentials, access tokens, private project links, or other personal/sensitive data. Add profile-specific content only to the active profile repository after reviewing it for public visibility.

## Local validation

Run the same static check used by CI:

```sh
python scripts/validate_profile_config.py
```

The validator uses only Python's standard library and checks the repository structure, required documentation headings, placeholder-based template, and workflow configuration.
