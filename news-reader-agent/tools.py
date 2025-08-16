import time
from crewai_tools import SerperDevTool
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()


def scrape_tool(url: str) -> str:
    """
    Scrape the content of a given URL\
    In case the website is not available, return "Website not available"
    Input: URL
    Output: Scraped content
    """

    print(f"Scraping URL: {url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(url)

        time.sleep(5)

        content = page.content()

        browser.close()

        soup = BeautifulSoup(content, "html.parser")

        unwanted_tags = [
            "header",
            "footer",
            "nav",
            "aside",
            "script",
            "style",
            "noscript",
            "iframe",
            "form",
            "button",
            "input",
            "select",
            "textarea",
            "img",
            "svg",
            "canvas",
            "audio",
            "video",
            "embed",
            "object",
        ]

        for tag in soup.find_all(unwanted_tags):
            tag.decompose()

        content = soup.get_text(separator="\n", strip=True)

        return content if content else "Website not available"


print(
    scrape_tool(
        "https://www.nytimes.com/2025/08/16/us/politics/biden-federal-reserve.html"
    )
)
