# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial setup of the repository.
- Basic CI/CD workflows.
- Documentation files (README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY).
- Git LFS configuration.
- Semantic PR and Dependabot configuration.
- Makefile for common commands.
- EditorConfig for consistent code style.
- Pre-commit hooks for code formatting and linting.
- Docstrings and header comments for Python scripts.
- Unit tests for filename validation script.
- Link check in CI.

### Changed
- Renamed repository from PDF_DOUCUMENT to PDF_DOCUMENT.
- Updated base URL in build_index.py.
- Updated pdfminer.six version in requirements.txt.
- Moved index.jsonl to docs directory.
- Updated auto-merge workflow to use gh pr merge.
- Cleaned up unnecessary files and updated .gitignore.

### Removed
- Old log files.
- Old index.jsonl, merged_texts.txt, OCR_CHECK.csv.
- _text/ directory.
