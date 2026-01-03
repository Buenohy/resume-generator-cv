<p align="right"><a href="#-descrição">Leia em Português</a></p>

# Resume Generator (ATS Optimized)

![Project Screenshot](resume-generator-cv-screenshot-0.png)

## 📝 Description

This project is a powerful **"Docs as Code"** solution designed to generate professional, high-performance resumes using **Python** and **HTML/CSS**. Unlike traditional word processors, it separates content (YAML) from design (HTML), allowing for pixel-perfect layout control via WeasyPrint.

More importantly, it is engineered for **Applicant Tracking Systems (ATS)**. The script injects advanced metadata (XMP, Dublin Core, and PDF Info) directly into the generated PDF file using `pypdf`. This ensures the resume ranks higher in automated filters by including specific keywords, freshness data (creation dates), and targeted position details.

## ✨ Key Features

- **Docs as Code Philosophy:** Keeps content structured in `content.yaml` and styling in `style.css`/`template.html`, making updates fast and version-controllable.
- **ATS Metadata Injection:** Automatically injects hidden metadata (Keywords, Author, Subject, Language, and Creation Date) to boost ranking in recruiting software.
- **Dynamic Company Targeting:** Allows generating specific resume versions via CLI arguments (e.g., `python build.py Google`), automatically customizing the summary for that specific employer.
- **High-Fidelity PDF:** Uses CSS Paged Media standards (via WeasyPrint) to ensure the PDF looks exactly as intended, with selectable text and proper links.
- **Metadata Validation:** Includes a utility script (`check_meta.py`) to verify that the injected metadata is correct and visible to parsers.

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jinja](https://img.shields.io/badge/jinja-white?style=for-the-badge&logo=jinja&logoColor=black)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![YAML](https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515)

## 🚀 Getting Started

Follow these steps to generate your resume locally.

### Prerequisites

- Python 3.x
- GTK3 (Required for WeasyPrint on Windows)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Buenohy/resume-generator-cv.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd resume-generator-cv
    ```

3.  Install the dependencies:
    ```bash
    pip install pyyaml jinja2 weasyprint pypdf
    ```

### Usage

To generate a general resume:

```bash
python build.py
```
