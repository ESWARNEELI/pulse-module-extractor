def build_modules(parsed_pages):
    modules = {
        "Documentation Overview": {
            "Description": "",
            "Submodules": {}
        }
    }

    current_module = "Documentation Overview"
    current_sub = None

    for page in parsed_pages:
        for tag, text in page:

            # Promote headings to submodules
            if tag in ["h1", "h2", "h3"]:
                current_sub = text
                if current_sub not in modules[current_module]["Submodules"]:
                    modules[current_module]["Submodules"][current_sub] = ""
                continue

            # Paragraph content
            if tag == "p":
                if current_sub:
                    modules[current_module]["Submodules"][current_sub] += " " + text
                else:
                    modules[current_module]["Description"] += " " + text

    return modules
