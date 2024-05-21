from scrapy import Spider
from scrapy.selector import Selector
import re

from properties.items import PropertyItem

# Change URL based on which neighborhood prices you want to scrape

class PropertySpider(Spider):
    name = "property"
    allowed_domains = [""]
    start_urls = [
        ""
    ]

    def parse(self, response):
        prices = Selector(response).xpath("")

        for price in prices:
            item = PropertyItem()
            # Remove all non-numeric characters except ".", "+" or "-".
            price_text = re.sub(r"[^\d\-+\.]", "", price.xpath("").get("").strip())

            # Check if there's any price text remaining
            if price_text:
                # Further validation using a regular expression (optional)
                match = re.search()
                if match:
                    item["price"] = match.group(1)
                else:
                    # Skip price if it doesn't match the expected format
                    continue
            else:
                # Skip price if there's no numeric content
                continue

            yield item