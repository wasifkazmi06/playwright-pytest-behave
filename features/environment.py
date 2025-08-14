from playwright.sync_api import sync_playwright


def before_all(context):
    """Set up Playwright before all tests."""
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)


def before_scenario(context, scenario):
    """Set up a new browser page before each scenario."""
    context.page = context.browser.new_page()


def after_scenario(context, scenario):
    """Capture a screenshot on failure and close the page."""
    if scenario.status == "failed":
        screenshot_path = f"reports/screenshots/{scenario.name}.png"
        context.page.screenshot(path=screenshot_path)
    context.page.close()


def after_all(context):
    """Close the browser and stop Playwright after all tests."""
    context.browser.close()
    context.playwright.stop()