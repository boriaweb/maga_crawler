import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Maga.MagaCrawler import MagaCrawler

settings_file_path = 'settings'
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)

process = CrawlerProcess(get_project_settings())

process.crawl(MagaCrawler)
process.start()