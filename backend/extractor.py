from bs4 import BeautifulSoup

def extract_modules(html_pages):
    modules_map = {}

    for html in html_pages.values():
        soup = BeautifulSoup(html, "html.parser")

        current_module = None
        current_submodule = None

        for tag in soup.find_all(["h1", "h2", "h3", "p"]):
            text = tag.get_text(strip=True)
            if len(text) < 8:
                continue

            # h1 → Module
            if tag.name == "h1":
                if text not in modules_map:
                    modules_map[text] = {
                        "module": text,
                        "Description": "",
                        "Submodules": {}
                    }
                current_module = modules_map[text]
                current_submodule = None

            # h2 / h3 → Submodule
            elif tag.name in ["h2", "h3"] and current_module:
                if text not in current_module["Submodules"]:
                    current_module["Submodules"][text] = ""
                current_submodule = text

            # p → Description
            elif tag.name == "p" and current_module:
                if not current_module["Description"]:
                    current_module["Description"] = text
                elif current_submodule and not current_module["Submodules"][current_submodule]:
                    current_module["Submodules"][current_submodule] = text

    return list(modules_map.values())
