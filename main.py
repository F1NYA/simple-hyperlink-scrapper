from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import task1
import task2

if __name__ == '__main__':
    print('Refresh output data.')

    task1.clean()
    task2.clean()

    print('Cleaned redundant data.')

    crawler = CrawlerProcess(get_project_settings())

    crawler.crawl('korrespondent')
    crawler.crawl('hotline')
    crawler.start()

    print('Input data refresh complete.')

    print('Processing first task...')
    task1.parse()

    print('Processing second task...')
    task2.parse()
