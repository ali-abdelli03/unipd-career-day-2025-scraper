# UNIPD Career Day IES 2025 — Keyword Scraper

A simple, fast scraper that scans the **Università Aperta IES 2025** career day company profiles and highlights those that match your interests.

This helps you quickly see **which companies you should visit** during the event based on keywords such as:

```

security, cloud, embedded, finance, research, python, ml

```

## Purpose

This tool helps you **prioritize which companies to talk to** during the career fair, saving you hours of manual research.

## Usage

```bash
# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python -m src.scraper
```

When asked, enter keywords separated by commas:

```
security,python,cloud
```

The script will print:

- Company name
- Which section matched (Profile / Opportunities / Requirements)
- Relevant text context
