from string import Template

script_template = Template('''
    import asyncio
    import urllib
    import math
    import re
    import json
    from typing import Any

    from playwright.async_api import Page
    
    from harambe import SDK
    from harambe import PlaywrightUtils as Pu

    @SDK.scraper(domain="$domain", stage="$stage")
    async def scrape(sdk: SDK, current_url: str, context: dict, *args: Any, **kwargs: Any) -> None:
        page: Page = sdk.page
        await page.wait_for_selector("$page_loaded_indicator")

        $loop_content

        await sdk.save_data({
            'title': title,
            'sku': sku if sku else None,
            'description': description if description else None,
            'type': type if type else None,
            'price': final_price,
            'images': images,
            'features': features,
            'attributes': attributes,
            'interchange': [],
            'fitment': fitment
        })
        
    if __name__ == "__main__":
        asyncio.run(
            SDK.run(
                scrape,"$url", headless=$headless,schema=None
            )
        )
''')