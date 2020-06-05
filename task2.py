from lxml import etree
import os

def clean():
    try:
        os.remove('hotline.xml')
        os.remove('hotline.xslt')
        os.remove('processed/hotline.html')
    except OSError:
        pass


def parse():
    print("HOTLINE")
    dom = etree.parse('./hotline.xml')
    xslt = etree.parse('./hotline-transform.xslt')

    transform = etree.XSLT(xslt)
    transformed_dom = transform(dom)

    serialized_dom = etree.tostring(transformed_dom, pretty_print=True, encoding='UTF-8')
    with open('processed/hotline.html', 'wb') as f:
        f.write(serialized_dom)
