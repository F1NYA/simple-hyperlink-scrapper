# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from lxml import etree

class LinkscrapyPipeline:
    def open_spider(self, spider):
        self.root = etree.Element('data')

    def close_spider(self, spider):
        str_data = etree.tostring(self.root, encoding="UTF-8", pretty_print=True, xml_declaration=True)
        with open(spider.name + '.xml', 'wb') as f:
            f.write(str_data)

    def process_item(self, item, spider):
        elem = None

        if spider.name == 'hotline':
            elem = etree.Element('product')
            elem.append(etree.Element('description', text=item['description']))
            elem.append(etree.Element('price', text=item['price']))
            elem.append(etree.Element('image', text=item['image']))
        else:
            elem = etree.Element('page', url=item['url'])
            for payload in item["payload"]:
                fragment = etree.Element('fragment', type=payload['type'], text=payload['data'])
                elem.append(fragment)

        self.root.append(elem)

        return item
