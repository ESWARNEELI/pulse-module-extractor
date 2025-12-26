
# print("MODULE EXTRACTOR STARTED")
import argparse
import json
from backend.crawler import crawl_docs
from backend.parser import extract_content
from backend.extractor import build_modules
from backend.utils import is_valid_url

def main(urls):
    all_pages = []

    for url in urls:
        if not is_valid_url(url):
            print(f"Invalid URL skipped: {url}")
            continue

        pages = crawl_docs(url)
        for soup in pages.values():
            all_pages.append(extract_content(soup))

    modules = build_modules(all_pages)

    output = []
    for m, data in modules.items():
        output.append({
            "module": m,
            "Description": data["Description"].strip(),
            "Submodules": {
                k: v.strip() for k, v in data["Submodules"].items()
            }
        })

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", nargs="+", required=True)
    args = parser.parse_args()
    main(args.urls)
