from string import Template

script_template = Template('''
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.$browser_type.launch(headless=$headless)
    page = browser.new_page()
    page.goto("$url")
    page.screenshot(path="$screenshot_path")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
''')

