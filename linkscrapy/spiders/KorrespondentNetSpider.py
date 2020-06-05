from scrapy import Spider, Request


def is_not_empty_string(string_var):
    return len(string_var) > 0


class KorrespondentNetSpider(Spider):
    name = 'korrespondent'
    allowed_domains = ['korrespondent.net']
    start_urls = ['https://korrespondent.net']

    fields = {
        'img': "//img/@data-src[starts-with(., 'http')]",
        'text': '//*[not(self::script)][not(self::style)][string-length(normalize-space(text())) > 20]/text()',
        'link': '//a/@href'
    }

    def parse(self, response):
        texts = response.xpath(self.fields["text"])
        images = response.xpath(self.fields["img"])

        yield {
            'url': response.url,
            'payload':
                [
                    {
                        'type': 'text',
                        'data': text.get().strip()
                    } for text in texts
                ] +
                [
                    {
                        'type': 'image',
                        'data': image.get()
                    } for image in images
                ]
        }

        startUrl = self.start_urls[0]
        if response.url == startUrl:
            links_elements = response.xpath(self.fields['link'])
            links = [link.get() for link in links_elements if link.get() != '/']
            for link in links[:20]:
                if link.startswith('/'):
                    link = startUrl + link
                try:
                    yield Request(link, self.parse)
                except ValueError:
                    pass
