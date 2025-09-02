# PDF Document Management

This repository is used for managing and tracking PDF documents. It uses Git LFS for versioning large files and has a CI/CD pipeline to enforce filename conventions.

## Features

*   **Versioning:** All documents are versioned with Git, allowing for a complete history of changes.
*   **Large File Storage:** Git LFS is used to handle large PDF files efficiently.
*   **CI/CD:** A GitHub Actions workflow automatically validates new documents to ensure they follow the naming convention.

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

## Search Interface

A GitHub Pages site provides a searchable interface for browsing documents: [PDF Document Search](https://ck999kk.github.io/PDF_DOCUMENT/).

1. Open the link above in your browser.
2. Enter keywords in the search box to find matching documents.
3. Click a result to view the corresponding PDF.

## Merged Text Access

A single plain-text file containing all PDF contents is available at [merged_texts.txt](https://raw.githubusercontent.com/ck999kk/PDF_DOCUMENT/main/merged_texts.txt). AI tools can read this link directly.

## Contributing

Contributions to this repository are welcome. Please follow these guidelines:

*   Ensure that all new documents follow the naming convention: `YYYYMMDD-Title-###.pdf`.
*   Update the documentation if you make any changes to the scripts or the workflow.

## License

This repository is licensed under the [MIT License](LICENSE).
