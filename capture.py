import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 1200, 'height': 800})
        
        urls = [
            ("https://www.maniinfra.com/", "maniinfra.jpg"),
            ("https://www.starsafetyrain.in/", "starsafetyrain.jpg"),
            ("https://www.casameerilahi.com/", "casameerilahi.jpg"),
            ("https://www.guidefintax.com/", "guidefintax.jpg"),
            ("https://guideglobalschool.com/", "guideglobalschool.jpg"),
            ("https://sablasinghacademy.com/", "sablasinghacademy.jpg")
        ]
        
        for url, name in urls:
            try:
                page = await context.new_page()
                print(f"Loading {url}...")
                await page.goto(url, wait_until='networkidle', timeout=30000)
                await page.wait_for_timeout(5000)
                await page.screenshot(path=f"assets/projects/{name}", type='jpeg', quality=85)
                print(f"Captured {name}")
                await page.close()
            except Exception as e:
                print(f"Failed {name}: {e}")
                
        await browser.close()

asyncio.run(capture())
