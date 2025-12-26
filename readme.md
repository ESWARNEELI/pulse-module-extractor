## Demo Walkthrough

A 3-minute video demonstration explaining:
- Project motivation
- Module extraction logic
- Folder structure
- Docker usage
- Sample output
**************************************************************************************
Video Link: https://drive.google.com/file/d/1SPjmLd13UqZLR7k20L-RtqE6RgDtJLot/view
**************************************************************************************

Pulse – Module Extraction AI Agent
Overview

This project is an automated documentation crawler that extracts modules and submodules from product help or documentation websites and represents them in a structured JSON format.

The system works purely on the content available at the provided URLs. It crawls relevant pages, removes non-content elements, infers logical groupings, and generates descriptions based only on the extracted documentation text.

The main goal of this project is to demonstrate content understanding, structure inference, and robust crawling, not just simple scraping.

Features

Accepts one or more documentation URLs

Recursively crawls internal documentation pages

Filters out headers, footers, navigation, and scripts

Infers:

Modules

Submodules

Descriptions

Outputs clean, structured JSON

Includes both CLI and Streamlit UI

Fully Dockerized for easy setup and portability

Project Structure
pulse-module-extractor/
│
├── backend/
│   ├── crawler.py
│   ├── parser.py
│   ├── extractor.py
│   └── utils.py
│
├── frontend/
│   └── app.py
│
├── module_extractor.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md

Tech Stack

Python 3.10+

Requests

BeautifulSoup4

Streamlit

Docker

Setup Instructions
Option 1: Run Locally (Without Docker)
git clone <your-repository-url>
cd pulse-module-extractor

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
streamlit run frontend/app.py


Open in browser:

http://localhost:8501

Option 2: Run Using Docker (Recommended)
git clone <your-repository-url>
cd pulse-module-extractor

docker build -t pulse-module-extractor .
docker run -p 8501:8501 pulse-module-extractor


Open in browser:

http://localhost:8501


Docker ensures the application runs consistently across different machines without manual environment setup.

CLI Usage
python module_extractor.py --urls https://help.zluri.com/


You can pass multiple URLs:

python module_extractor.py --urls https://help.zluri.com/ https://wordpress.org/documentation/

Sample Output
[
  {
    "module": "Documentation Overview",
    "Description": "This documentation explains the core features and workflows of the product.",
    "Submodules": {
      "Getting Started": "Introduces the platform and initial setup steps.",
      "Account Management": "Explains how to manage users, roles, and settings."
    }
  }
]

Design Decisions

Documentation websites do not follow a single structural standard

The extractor uses flexible heuristics instead of rigid rules

At least one top-level module is always created to avoid empty outputs

All descriptions are generated strictly from extracted content

This approach prioritizes robustness and consistency across different documentation styles.

Assumptions

Documentation is primarily HTML-based

Headings and paragraphs provide enough structural cues

Only internal links are crawled

JavaScript-rendered content may have limited extraction

Known Limitations

Very deep nesting may be flattened

Some sites restrict crawling aggressively

Tables are treated as text

No semantic AI/LLM is used for interpretation
