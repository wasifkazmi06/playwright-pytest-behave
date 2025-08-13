from playwright.sync_api import sync_playwright


def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)


def after_scenario(context, scenario):
    context.browser.close()
    context.playwright.stop()
