from scrapy import Spider

class HotlineUaSpider(Spider):
    name = 'hotline'
    allowed_domains = ['hotline.ua']
    start_urls = [
        'https://hotline.ua/bt/kaminy/'
        'https://hotline.ua/bt/vinnye-shkafy/',
        'https://hotline.ua/bt/stiralnye-i-sushilnye-mashiny/',
        'https://hotline.ua/bt/meteostancii-termometry-gigrometry/'
    ]

    fields = {
        'product': ".//div[@id='catalog-products']//li[contains(@class, 'product-item')]",
        'description': ".//div[contains(@class, 'text')]/p/text()",
        'price': ".//span[contains(@class, 'value')]/text()",
        'image': ".//img[contains(@class, 'img-product')]/@src"
    }

    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 0,
        'CLOSESPIDER_ITEMCOUNT': 20
    }

    def parse(self, response):
        for product in response.xpath(self.fields['product'])[:20]:
            description = product.xpath(self.fields['description']).get()
            price = product.xpath(self.fields['price']).get()
            image = product.xpath(self.fields['image']).get()

            if description is None or price is None or image is None:
                pass
            else:
                yield {
                    'description': description.strip().translate({ord('&#10;'): None}),
                    'price': price.strip(),
                    'image': image.strip()
                }
