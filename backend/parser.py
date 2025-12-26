from bs4 import BeautifulSoup

def extract_clean_text(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    main = soup.find("main") or soup.find("article") or soup.body
    return main.get_text("\n", strip=True) if main else ""
