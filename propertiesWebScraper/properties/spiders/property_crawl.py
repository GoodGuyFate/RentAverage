from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.exceptions import CloseSpider
import re
from properties.items import PropertyItem


# Change URL based on which neighborhood prices you want to scrape

class PropertySpider(CrawlSpider):
    name = "propertycrawl"
    allowed_domains = [""]
    start_urls = [
        ""
    ]
    rules = (
        Rule(
            LinkExtractor(allow=r"\?page=\d+"),  # Adjusted regex for "?" and digits
            callback='parse',
            follow=True
        ),
    )

    current_page = 1  # Initialize page counter

    def parse(self, response):
        # Track current page number
        self.current_page += 1

        if self.current_page >= 17:
            # Stop crawling after x pages
            raise CloseSpider("Crawling completed")

        sel = Selector(response)
        prices = sel.xpath("")

        for price in prices:
            item = PropertyItem()
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
