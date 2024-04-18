import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tiket.com/review?product_type=TIXHOTEL&searchType=INVENTORY&inventory_id=monoloog-hotel-surabaya-609001695617428336&reviewSubmitColumn=RATING_SUMMARY")
    last = page.query_selector('[data-testid="last-page-pagination"]')
    for i in range(1, int(last.inner_text()) + 1):
        if page.get_by_text(str(i), exact=True):
            page.get_by_text(str(i), exact=True).click()
        else:
            page.reload()




    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
