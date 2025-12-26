import json
from backend.fetcher import fetch_html
from backend.crawler import crawl
from backend.parser import extract_clean_text
from backend.extractor import extract_modules
from backend.utils import is_valid_url

def main():
    url = input("Enter documentation URL: ").strip()

    if not is_valid_url(url):
        print("Invalid URL")
        return

    html = fetch_html(url)
    if not html:
        print("Failed to fetch content")
        return

    pages = crawl(url, html)
    full_text = ""

    for page in pages.values():
        full_text += extract_clean_text(page) + "\n"

    result = extract_modules(full_text)

    print("\nFINAL JSON OUTPUT:\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
