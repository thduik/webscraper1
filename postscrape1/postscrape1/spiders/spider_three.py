import scrapy

class SpiderScraperThree(scrapy.Spider):
    
    name = "spiderThree"
    custom_settings = {
        "CONCURRENT_REQUESTS":500,
        "CONCURRENT_REQUESTS_PER_DOMAIN":3,
        "RETRY_ENABLED":False
    }


    def parse_lmao():
        raise Exception("wrong parse function SpiderScraperThree")

    # start_urls = []
    def __init__(self, *args, **kwargs):
        super(SpiderScraperThree, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get("urls")
        self.parse_lmao = kwargs.get("parse_func")
    def start_requests(self):
        
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True, callback=self.parse_lmao)
