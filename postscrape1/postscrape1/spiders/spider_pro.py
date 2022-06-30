import asyncio
import scrapy
from scrapy.crawler import CrawlerProcess
import datetime
import urllib
import test2
import re
import spider_three

class GoogleCrawlerPro():
    # query_keyword = "con+cac"
    web_scrape_urls = []  #append urls to here lmao
    html_parser = test2.MyHtmlParser()

    #dependencies
    multiple_urls_per_domain = True
    max_urls_per_domain = False


    def reset_data(self):
        self.web_scrape_urls = []  
        self.w_dct_single = {}
        self.w_dict_double = {}
        self.w_dict_triple = {}
        self.w_dict_quadle = {}

    def handle_data(self, html_text):
        self.html_parser.handle_data(html_text)
    
    def return_data(self):
        return self.html_parser.return_data()

    def parse_scrapy_response(self, response):
        # print ("parse_scrapy_response (scraperTHree result html) in spider pro called")
        url_arr = []
        html_lol = response.text
        self.handle_data(html_lol)

        return []

    

    async def output_result(self, begin):
        #begin = datetime.datetime.now() obbject
        # print ("wait_and_output_resul called")
        res_dct = self.html_parser.return_data()
        
        print ("")
        print ("single_dict")
        res_arr_single = self.html_parser.parse_res_dict(res_dct["single_dict"])
        print (res_arr_single[:100])
        print ("double_dict")
        res_arr_double = self.html_parser.parse_res_dict(res_dct["double_dict"])
        print (res_arr_double[:100])
        print ("")

        
        end = datetime.datetime.now()
        diff = end - begin
        print ("time benchmark: ", diff.total_seconds())
        return 0
    


    def execute_step1(self, keyword_arr):
        url_arr = []
        
        
        urls = [
           
            # , "https://www.google.com/search?q=%s&num=100&start=100" %(keyword_query)
            # , "https://www.google.com/search?q=%s&num=100" %("kinh+te")
        ]

        for keyword in keyword_arr:
            urls.append( "https://www.google.com/search?q=%s&num=2" %(keyword) )
        print ("keyword_arr: ", keyword_arr, urls)
        for url in urls:
            # Perform the request
            print ("Called google search for url")
            request = urllib.request.Request(url)
            # Set a normal User Agent header, otherwise Google will block the request.
            request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
            raw_response = urllib.request.urlopen(request).read()

            # Read the repsonse as a utf-8 string
            html = raw_response.decode("utf-8")
            cnt = 0
            regexxx = re.findall(r"href=\"(.*?)\"?", html)
            for line in regexxx:   
                if line[:4]=="http":
                    # print ("line length [:4]==http is: ", len(line) )
                    # print (line)
                    url_arr.append(line)

            self.web_scrape_urls.extend(url_arr)

        print ("web_scrape_urls leng: ", len(self.web_scrape_urls) )
        for url in self.web_scrape_urls:
            print (url)
        
        
    

    async def execute_step2(self):
        print ("step2_executed", len(self.web_scrape_urls))
        #crawl the google search result urls received in step 1
        

        process = CrawlerProcess()
        process.crawl(spider_three.SpiderScraperThree, urls=self.web_scrape_urls, parse_func = self.parse_scrapy_response )
        process.start()
        return 0


    async def crawl_keywords(self, keyword_arr):
        self.reset_data()
        begin = datetime.datetime.now()
        self.web_scrape_urls = []
        self.execute_step1(keyword_arr)
        
        # print ("webscrape urls: ", web_scrape_urls[:1])
        task1 = asyncio.create_task(
            self.execute_step2()
        )
        
        

        await task1
        
        end = datetime.datetime.now()
        diff = end - begin

        # await asyncio.sleep(5)
        
        await self.output_result(begin)