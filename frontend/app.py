import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st
import json
from backend.fetcher import fetch_html
from backend.crawler import crawl
from backend.parser import extract_clean_text
from backend.extractor import extract_modules
from backend.utils import is_valid_url

st.set_page_config(page_title="Pulse Module Extractor", layout="wide")

st.title("📦 Pulse – Module Extraction AI Agent")

url = st.text_input("Enter Documentation URL")

if st.button("Extract Modules"):
    if not is_valid_url(url):
        st.error("Invalid URL")
    else:
        with st.spinner("Processing documentation..."):
            html = fetch_html(url)
            pages = {url: html}   # DO NOT crawl for now
            result = extract_modules(pages)

        st.success("Extraction Complete")
        st.json(result)
