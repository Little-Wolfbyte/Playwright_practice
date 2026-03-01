from asyncio import wait

from playwright.sync_api import Page
import time
#testing out playwright basics

#def test_playwright(playwright):
#    browser = playwright.chromium.launch(headless=False) #launch chromium engine and show the it,
#    # hence why headless is false
#    context = browser.new_context() #open browser
#    page = context.new_page() #define page object
#    page.goto("https://www.planit.com/") #go to this page when you open your browser
#    time.sleep(5)  # Keep browser open for 5 seconds

def test_corelocaters(page: Page):
    page.goto("https://rahulshettyacademy.com/")
    # Dismiss banner ONLY IF it appears
    try:
        close_button = page.get_by_label("Dismiss banner")
        close_button.wait_for(state="visible", timeout=5000)
        close_button.click()
    except:
        pass

    page.get_by_role("navigation").get_by_role("link", name="Learning Paths").click()
    time.sleep(5)