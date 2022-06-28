import scrapy
from scrapy_splash import SplashRequest
import re
from scrapy.crawler import CrawlerProcess
import asyncio
import urllib.request


# class SpiderScraperThree(scrapy.Spider):

   

#     name = "spiderThree"

#     def parse_lmao():
#         print ("old func")

#     # start_urls = []
#     def __init__(self, *args, **kwargs):
#         super(SpiderScraperThree, self).__init__(*args, **kwargs)
#         self.start_urls = kwargs.get("urls")
#         self.parse_lmao = kwargs.get("parse_func")
    
#     def start_requests(self):
        
#         for url in self.start_urls:
#             yield scrapy.Request(url, dont_filter=True, callback=self.parse_lmao)

#     def parse(self,response):
        
#         html = "test_result"

        
#         return []

# def parse_lol(response):
#     print ("new functiossssn", response.text[:100])

# class SpiderWrapper():
#     html = "?"
#     def parse_res(self, html_text):
#         print ("spiderWrapper parse_res called: ", html_text)
    
#     def crawl_lol(self):
#         process = CrawlerProcess()
#         process.crawl(SpiderScraperThree, urls=["https://stackoverflow.com/questions/38619478/google-search-web-scraping-with-python"], parse_func = self.parse_res )
#         process.start()

# spider_wrapper = SpiderWrapper()
# spider_wrapper.crawl_lol()


