


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_docs(start_url, max_pages=60):
    visited = set()
    to_visit = [start_url]
    pages = {}

    base_domain = urlparse(start_url).netloc

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        try:
            # r = requests.get(url, timeout=10)

            headers = {
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
             }
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code != 200:
                continue

            soup = BeautifulSoup(r.text, "html.parser")
            pages[url] = soup
            visited.add(url)

            for a in soup.find_all("a", href=True):
                link = urljoin(url, a["href"])
                if base_domain in link and link not in visited:
                    to_visit.append(link)

        except:
            continue

    return pages
