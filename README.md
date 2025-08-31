# PDF Document Management

[![repo-ci](https://github.com/ck999kk/PDF_DOCUMENT/actions/workflows/repo-ci.yml/badge.svg)](https://github.com/ck999kk/PDF_DOCUMENT/actions/workflows/repo-ci.yml)
[![Build and Deploy Pages](https://github.com/ck999kk/PDF_DOCUMENT/actions/workflows/pages.yml/badge.svg)](https://github.com/ck999kk/PDF_DOCUMENT/actions/workflows/pages.yml)
[![License](https://img.shields.io/github/license/ck999kk/PDF_DOCUMENT)](LICENSE)

This repository is used for managing and tracking PDF documents. It uses Git LFS for versioning large files and has a CI/CD pipeline to enforce filename conventions.

## Features

*   **Versioning:** All documents are versioned with Git, allowing for a complete history of changes.
*   **Large File Storage:** Git LFS is used to handle large PDF files efficiently.
*   **CI/CD:** A GitHub Actions workflow automatically validates new documents to ensure they follow the naming convention.

### File Structure

```
.
├── .github/
│   └── workflows/
├── docs/
├── scripts/
├── tests/
├── .editorconfig
├── .gitignore
├── .pre-commit-config.yaml
├── CODE_OF_CONDUCT.md
├── CODEOWNERS
├── CONTRIBUTING.md
├── EVIDENCE_MANIFEST.csv
├── index.html
├── index.jsonl
├── LICENSE
├── Makefile
├── README.md
├── README_PERMALINKS.md
└── requirements.txt
```

## Getting Started

To get started with this repository, you need to have Git and Git LFS installed.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ck999kk/PDF_DOCUMENT.git
    cd PDF_DOCUMENT
    ```

2.  **List the documents:**

    You can list all the documents in the repository with the following command:

    ```bash
    ls -l *.pdf
    ```

## Contributing

Contributions to this repository are welcome. Please follow these guidelines:

*   Ensure that all new documents follow the naming convention: `YYYYMMDD-Title-###.pdf`.
*   Update the documentation if you make any changes to the scripts or the workflow.

## License

This repository is licensed under the [MIT License](LICENSE).