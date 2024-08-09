import json
from playwright.async_api import async_playwright

async def verify_selectors(url, selectors):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)

        results = {}

        for selector in selectors:
            try:
                await page.wait_for_selector(selector, timeout=5000)
                results[selector] = "Present"
            except:
                results[selector] = "Not Present"

        await browser.close()
        return results

async def main():
    url = 'https://shop.boeing.com/aviation-supply/'
    with open('selectors.json', 'r') as file:
        data = json.load(file)
    selectors = list(data['selectors'].keys())
    results = await verify_selectors(url, selectors)
    print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
