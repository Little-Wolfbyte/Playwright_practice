import time

#testing out playwright basics

def test_playwright(playwright):
    browser = playwright.chromium.launch(headless=False) #launch chromium engine and show the it,
    # hence why headless is false
    context = browser.new_context() #open browser
    page = context.new_page() #define page object
    page.goto("https://www.google.com") #go to this page when you open your browser
    time.sleep(5)  # Keep browser open for 5 seconds