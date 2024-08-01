import json
from pyppeteer import launch

# Define la URL a verificar
url = 'https://shop.boeing.com/aviation-supply/'  # Reemplaza con la URL del sitio web que deseas verificar

async def verify_selectors(url, selectors):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)

    results = {}
    for name, selector in selectors.items():
        try:
            element = await page.querySelector(selector)
            if element:
                results[name] = True
            else:
                results[name] = False
        except Exception as e:
            results[name] = False
            print(f"Error checking selector {name}: {e}")

    await browser.close()
    return results

def main():
    with open('selectors.json', 'r') as file:
        data = json.load(file)
        selectors = data.get('selectors', {})
    
    import asyncio
    results = asyncio.get_event_loop().run_until_complete(verify_selectors(url, selectors))

    print("Selector verification results:")
    for name, exists in results.items():
        print(f"{name}: {'Found' if exists else 'Not Found'}")

if __name__ == '__main__':
    main()
