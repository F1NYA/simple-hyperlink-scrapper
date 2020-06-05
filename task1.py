from lxml import etree
import os

def clean():
    try:
        os.remove("korrespondent.xml")
    except OSError:
        pass

def parse():
    print("KORRESPONDENT")
    root = etree.parse("./korrespondent.xml")
    pages = root.xpath("//page")

    print("NUM OF TEXT FRAGMENTS")
    for page in pages:
        print(int(page.xpath('count(fragment[@type="text"])')))
