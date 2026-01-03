<p align="right"><a href="#-descrição">Leia em Português</a></p>

# Resume Generator (ATS Sniper Edition)

![Project Screenshot](resume-generator-cv-screenshot-0.png)

## 📝 Description

This project is an advanced **"Docs as Code"** solution designed to generate high-performance, ATS-optimized resumes using **Python**. Unlike standard generators, this tool acts as an **"ATS Sniper"**: it not only creates a visually pixel-perfect PDF using HTML/CSS (WeasyPrint) but also injects hidden, high-value metadata using `pypdf`.

It automatically ensures **content freshness** (by forcing current creation dates), **company targeting** (injecting specific target-company keywords into metadata), and **semantic relevance**, ensuring your resume ranks higher in Applicant Tracking Systems (Gupy, Greenhouse, Lever, etc.).

## ✨ Key Features

- **ATS Sniper Metadata:** Automatically injects over 15 hidden metadata fields, including `/Target-Company`, `/Keywords`, `/Type: Resume`, and `/Fit-Score` triggers.
- **Freshness Boost:** Forces the PDF's `/CreationDate` and `/ModDate` to the exact moment of generation, preventing your resume from looking "old" to sorting algorithms.
- **Dynamic Customization:** Generates targeted versions via CLI (e.g., `python build.py Netflix`), automatically rewriting the summary and metadata for that specific employer.
- **Smart Validation Script:** Includes an intelligent `check_ats.py` script that automatically detects the most recently generated resume (e.g., `CV_Gabriel_Bueno_Netflix.pdf`) and runs a text extraction test to ensure ATS readability.
- **Docs as Code:** Separation of data (`content.yaml`), structure (`template.html`), and style (`style.css`) for version-controlled career management.

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

**1. Generate a Resume:**

To generate a general version:

```bash
python build.py
```

To generate a version targeted for a specific company (e.g., Google):

```bash
python build.py Google
```

_This creates a file named `CV_Gabriel_Bueno_Google.pdf` with optimized metadata._

**2. Verify ATS Compatibility:**

Run the smart check script. It will automatically find the latest generated PDF and validate its metadata and text extractability:

```bash
python check_ats.py
```

## 👨‍💻 Author

**Gabriel Bueno Hygino**

## ⚖️ License

This project is licensed under the ISC License - see the [LICENSE](LICENSE) file for more details.

---

<p align="right"><a href="#-description">Read in English</a></p>

# Resume Generator (ATS Sniper Edition)

![Screenshot do Projeto](resume-generator-cv-screenshot-0.png)

## 📝 Descrição

Este projeto é uma solução avançada de **"Docs as Code"** projetada para gerar currículos de alta performance e otimizados para ATS usando **Python**. Diferente de geradores comuns, esta ferramenta atua como um **"ATS Sniper"**: ela não apenas cria um PDF visualmente perfeito usando HTML/CSS (WeasyPrint), mas também injeta metadados ocultos de alto valor usando `pypdf`.

Ele garante automaticamente a **recência do conteúdo** (forçando datas de criação atuais), **direcionamento para empresas** (injetando palavras-chave da empresa alvo nos metadados) e **relevância semântica**, garantindo que seu currículo tenha um ranqueamento superior em Sistemas de Rastreamento de Candidatos (Gupy, Greenhouse, Lever, etc.).

## ✨ Principais Funcionalidades

- **Metadados ATS Sniper:** Injeta automaticamente mais de 15 campos de metadados ocultos, incluindo `/Target-Company`, `/Keywords`, `/Type: Resume` e gatilhos de `/Fit-Score`.
- **Impulso de Recência:** Força o `/CreationDate` e `/ModDate` do PDF para o momento exato da geração, evitando que seu currículo pareça "antigo" para algoritmos de ordenação.
- **Customização Dinâmica:** Gera versões direcionadas via CLI (ex: `python build.py Netflix`), reescrevendo automaticamente o resumo e os metadados para aquele empregador específico.
- **Script de Validação Inteligente:** Inclui um script `check_ats.py` que detecta automaticamente o currículo gerado mais recentemente (ex: `CV_Gabriel_Bueno_Netflix.pdf`) e executa um teste de extração de texto para garantir a legibilidade pelo ATS.
- **Docs as Code:** Separação de dados (`content.yaml`), estrutura (`template.html`) e estilo (`style.css`) para gestão de carreira com controle de versão.

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jinja](https://img.shields.io/badge/jinja-white?style=for-the-badge&logo=jinja&logoColor=black)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![YAML](https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515)

## 🚀 Como Executar

Siga estas etapas para gerar seu currículo localmente.

### Pré-requisitos

- Python 3.x
- GTK3 (Necessário para o WeasyPrint no Windows)

### Instalação

1.  Clone o repositório:

    ```bash
    git clone https://github.com/Buenohy/resume-generator-cv.git
    ```

2.  Navegue até o diretório do projeto:

    ```bash
    cd resume-generator-cv
    ```

3.  Instale as dependências:
    ```bash
    pip install pyyaml jinja2 weasyprint pypdf
    ```

### Uso

**1. Gerar um Currículo:**

Para gerar uma versão geral:

```bash
python build.py
```

Para gerar uma versão direcionada para uma empresa (ex: Google):

```bash
python build.py Google
```

_Isso cria um arquivo chamado `CV_Gabriel_Bueno_Google.pdf` com metadados otimizados._

**2. Verificar Compatibilidade ATS:**

Rode o script de verificação inteligente. Ele encontrará automaticamente o PDF gerado mais recentemente e validará seus metadados e capacidade de extração de texto:

```bash
python check_ats.py
```

## 👨‍💻 Autor

**Gabriel Bueno Hygino**

## ⚖️ Licença

Este projeto está licenciado sob a Licença ISC - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

```

```

```

```
