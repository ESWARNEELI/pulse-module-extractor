from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

def crawl(start_url, html, limit=30):
    visited = set()
    queue = [start_url]
    pages = {}

    domain = urlparse(start_url).netloc

    while queue and len(visited) < limit:
        url = queue.pop(0)
        if url in visited:
            continue

        visited.add(url)
        pages[url] = html

        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link["href"])
            if urlparse(full_url).netloc == domain and full_url not in visited:
                queue.append(full_url)

    return pages
