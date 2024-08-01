import json
import asyncio
from playwright.async_api import async_playwright

# URLs de inicio de sesión y base
BASE_URL = "https://shop.boeing.com/aviation-supply/"
LOGIN_URL = "https://shop.boeing.com/aviation-supply/login"


async def login(page, login_url, credentials):
    await page.goto(login_url)
    await page.fill('input[name="username"]', credentials['username'])
    await page.fill('input[name="password"]', credentials['password'])
    await page.click('button[type="submit"]')
    await page.wait_for_navigation()

async def verify_selectors(page, selectors):
    results = {}
    for selector, description in selectors.items():
        try:
            element = await page.query_selector(selector)
            if element:
                results[selector] = 'Found'
            else:
                results[selector] = 'Not Found'
        except Exception as e:
            results[selector] = f'Error: {e}'
    return results

async def main():
    with open('selectors.json') as f:
        selectors = json.load(f)

    credentials = {
        'username': '',  # Replace with your actual username
        'password': ''   # Replace with your actual password
    }
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Navigate to login page and perform login
        await login(page, LOGIN_URL, credentials)
        
        # Navigate to target page
        await page.goto(BASE_URL)
        
        # Verify selectors
        results = await verify_selectors(page, selectors)
        print(json.dumps(results, indent=4))
        
        await browser.close()

asyncio.run(main())
