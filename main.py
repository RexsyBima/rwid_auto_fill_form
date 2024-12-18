from playwright.sync_api import sync_playwright, Page
import json
from typing import Any
from enum import Enum
import time
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("URL")
assert isinstance(URL, str)


def fill_form(page: Page, label: str, value: Any):
    field = page.get_by_label(label)
    field.fill(value)


def main():
    print("Hello from googleform-auto-fill!")


class Kelas(Enum):
    backend = "Python Backend"
    scraping = "Python Scraping"


if __name__ == "__main__":
    D = open("input.txt", "r").readlines()
    OUTPUT = open("done.txt", "r").readlines()
    FINAL_OUTPUT = []

    print(D)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        with browser.new_page() as page:
            for lines in D:
                url, title = lines.split("|")
                page.goto(URL)
                fill_form(page, "Nama Mentor", "Rexsy Bima Trima Wahyu")
                fill_form(
                    page,
                    "Judul Materi -- Gunakan format sbb:",
                    title.strip(),
                )
                kelas = page.get_by_role("radio", name=Kelas.backend.value)
                kelas.click()
                fill_form(
                    page,
                    "Link File Video (Google Drive atau Penyimpanan Cloud lainnya, bukan link Youtube pribadi)",
                    url.strip(),
                )
                btn = page.get_by_role("button", name="Submit")
                time.sleep(5)
                btn.click()
                time.sleep(5)

    with open("done.txt", "w") as f:
        D = [d + "\n" for d in D]
        OUTPUT = [d + "\n" for d in OUTPUT]
        FINAL_OUTPUT.extend(D)
        FINAL_OUTPUT.extend(OUTPUT)
        f.writelines(FINAL_OUTPUT)
    browser.close()
