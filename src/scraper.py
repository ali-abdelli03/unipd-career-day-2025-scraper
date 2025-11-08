import requests
from bs4 import BeautifulSoup

URL = "https://www.universitaperta-unipd.it/eventi/universita-aperta-ies/universita-aperta-ies-2025"

def safe_text(element):
    return element.get_text(strip=True) if element else ""

def main():
    session = requests.Session()
    response = session.get(URL, timeout=10)
    soup = BeautifulSoup(response.text, "lxml")

    print("===================================")
    keywords = input("Please enter keywords separated by commas (e.g., cyber, cloud, java): ").lower().split(",")
    keywords = [k.strip() for k in keywords if k.strip()]  # clean list

    companies = soup.find_all("div", class_="modal-content")

    for company in companies:
        header = company.find("div", class_="modal-header")
        name = safe_text(header)[1:] if header else "Unknown"

        panels = company.select("div.modal-body div.panel.panel-default div.panel-body")
        profile, opportunities, requirements = (safe_text(panels[i]) if i < len(panels) else "" for i in range(3))

        data = {
            "Profile": profile.lower(),
            "Opportunities": opportunities.lower(),
            "Requirements": requirements.lower()
        }

        matched = False
        for section, text in data.items():
            for kw in keywords:
                if kw in text:
                    if not matched:
                        print(f"\n🔹 Company: {name}")
                        matched = True
                    print(f"  - Match in **{section}** → '{kw}'")
                    # Print original (non-lowered) text for readability
                    print(f"    {locals()[section.lower()] if section.lower() in locals() else text}")
        if matched:
            print("------------------------------------------------")

    print("\n===================================")

if __name__ == "__main__":
    main()
