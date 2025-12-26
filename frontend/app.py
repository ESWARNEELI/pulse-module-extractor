# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# import streamlit as st
# import json
# from backend.fetcher import fetch_html
# from backend.crawler import crawl
# from backend.parser import extract_clean_text
# from backend.extractor import extract_modules
# from backend.utils import is_valid_url

# st.set_page_config(page_title="Pulse Module Extractor", layout="wide")

# st.title("📦 Pulse – Module Extraction AI Agent")

# url = st.text_input("Enter Documentation URL")

# if st.button("Extract Modules"):
#     if not is_valid_url(url):
#         st.error("Invalid URL")
#     else:
#         with st.spinner("Processing documentation..."):
#             html = fetch_html(url)
#             pages = {url: html}   # DO NOT crawl for now
#             result = extract_modules(pages)

#         st.success("Extraction Complete")
#         st.json(result)


# import streamlit as st
# import subprocess

# st.title("Pulse – Module Extraction AI Agent")

# urls = st.text_area("Enter documentation URLs (one per line)")

# if st.button("Extract Modules"):
#     url_list = [u.strip() for u in urls.splitlines() if u.strip()]
#     result = subprocess.run(
#         ["python", "module_extractor.py", "--urls"] + url_list,
#         capture_output=True,
#         text=True
#     )
#     st.code(result.stdout, language="json")


import streamlit as st
import subprocess
import sys

st.title("Pulse – Module Extraction AI Agent")

urls = st.text_area("Enter documentation URLs (one per line)")

if st.button("Extract Modules"):
    url_list = [u.strip() for u in urls.splitlines() if u.strip()]

    if not url_list:
        st.warning("Please enter at least one URL")
    else:
        with st.spinner("Extracting modules..."):
            process = subprocess.Popen(
                [sys.executable, "module_extractor.py", "--urls"] + url_list,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            stdout, stderr = process.communicate()

        if stderr:
            st.error("Error occurred:")
            st.code(stderr)
        else:
            st.success("Extraction completed")
            st.code(stdout, language="json")

