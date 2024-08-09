import asyncio
from playwright.async_api import async_playwright
import json

# URL de la página a verificar
URL = "https://shop.boeing.com/aviation-supply/"

async def verify_selectors(url, selectors):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)

        results = {}
        for selector in selectors:
            try:
                await page.wait_for_selector(selector, timeout=5000)
                results[selector] = 'Present'
            except:
                results[selector] = 'Not Present'

        await browser.close()
        return results

async def main():
    # Leer selectores del archivo JSON
    with open('selectors.json') as f:
        selectors = json.load(f)

    # Verificar los selectores en la URL
    results = await verify_selectors(URL, selectors)
    print(results)

# Ejecutar el script
asyncio.run(main())
