import sys
import asyncio

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())



import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_static(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        if res.status_code == 200:
            return res.text
    except Exception:
        pass
    return ""

def is_js_rendered(html):
    soup = BeautifulSoup(html, "html.parser")
    text_len = len(soup.get_text(strip=True))
    return text_len < 500 or "id=\"root\"" in html.lower() or "react" in html.lower()

def fetch_with_js(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_load_state("networkidle")
        content = page.content()
        browser.close()
        return content

def fetch_html(url):
    # Zendesk / SPA docs – force JS
    if any(x in url for x in ["neo.space", "zluri.com", "chargebee.com"]):
        return fetch_with_js(url)

    html = fetch_static(url)
    if is_js_rendered(html):
        return fetch_with_js(url)

    return html
