from bs4 import BeautifulSoup

def extract_content(soup: BeautifulSoup):
    # remove noise
    for tag in soup(["nav", "footer", "header", "script", "style", "aside"]):
        tag.decompose()

    main = soup.find("main") or soup.find("article") or soup.body
    if not main:
        return []

    content = []

    for tag in main.find_all(["h1", "h2", "h3", "p", "li"], recursive=True):
        text = tag.get_text(strip=True)
        if len(text) > 40:   # avoids junk headings
            content.append((tag.name, text))

    return content
