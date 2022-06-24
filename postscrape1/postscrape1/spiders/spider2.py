
import scrapy
from scrapy_splash import SplashRequest
import re
from scrapy.crawler import CrawlerProcess
import asyncio
import urllib.request
import datetime


def parse_google_res_html(html_text):

    print ("wtfff")
    print ("parse_goolge_res")
    
    url_arr1 = []
    for linelol in html_text:
        regexxx = re.findall(r"href=\"(.*?)\"><h3?", linelol)
        for line in regexxx:   
            regex111 = re.findall(r"q=(.*?)&amp?", line)[0]
            if regex111[:4] == "http":
                url_arr1.append(regex111)
    print ("url_arr1: ", url_arr1[:6])
    return url_arr1
def add_to_dct(word, dct):
    if word in dct:
        dct[word] += 1
    else:
        dct[word] = 1
def parse_text_1(text):
    re_res = [] #[string]
    
    re_arr = re.findall(r">(.*?)<", text)
    for reslol in re_arr:
        if len(reslol) > 0:
            re_res.append(reslol)
    return re_res #[string]


class SpiderScraperThree(scrapy.Spider):

   

    name = "spiderThree"
    custom_settings = {
        "CONCURRENT_REQUESTS":200,
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

    # def start_requests(self):
    #     print ("spider three start request", len(web_scrape_urls))
    #     for url in web_scrape_urls:
            
    #         yield scrapy.Request(url, dont_filter=True)
    
        
    
        
        

def replace_xa0_text_arr(text_arr):
        res = []
        for text7 in text_arr:
            text_arr = re.sub("\\xa0", " ", text7)
            res.append(text_arr)
        return res



class GoogleCrawlerPro():
    # query_keyword = "con+cac"
    web_scrape_urls = []  #append urls to here lmao
    w_dct_single = {}
    w_dict_double = {}
    w_dict_triple = {}
    w_dict_quadle = {}

    def handle_data(self, text_arr):
    
        #text_arr = [string]
        re_res = []
        for text5 in text_arr:
            parse_res = parse_text_1(text5) #[tring]
            reslmao = replace_xa0_text_arr(parse_res) #[string]
            if len(reslmao) > 0:
                re_res.extend(reslmao)
        
        # print ("re res handle data: ", len(re_res) )
        
        
        #re_res is now [string]
        for text in re_res:
            text_arr = text.split(" ")
            for i in range(len(text_arr)):
                single_word = text_arr[i].lower()
                add_to_dct(single_word, self.w_dct_single)
                if i < len(text_arr) - 1:
                    double_word = " ".join( text_arr[i:i+2] ).lower()
                    add_to_dct(double_word, self.w_dict_double)
                if i < len(text_arr) - 2:
                    triple_word = " ".join( text_arr[i:i+3] ).lower()
                    add_to_dct(triple_word, self.w_dict_triple)
                if i < len(text_arr) - 3:
                    quad_word = " ".join( text_arr[i:i+4] ).lower()
                    add_to_dct(quad_word, self.w_dict_quadle)
                

        return {"single_dict":self.w_dct_single, "double_dict":self.w_dict_double}  

    
    def parse_scrapy_response(self, response):
    
        print ("parse_scrapy_response (scraperTHree result html) in spider pro called")

        url_arr = []
        
        #testing parsing 100 website html success
        p_arr = response.css('p').getall()
        h1_arr = response.css('h1').getall()
        h3_arr = response.css('h3').getall()
        h4_arr = response.css('h4').getall()
        
        self.handle_data(p_arr)
        self.handle_data(h1_arr)
        self.handle_data(h3_arr)
        self.handle_data(h4_arr)

        return []

    def parse_res_dict(self, w_dct):
        tuple_arr = [] #[(word, count)]
        for w in w_dct:
            tuple_arr.append((w,w_dct[w]))
        return sorted(tuple_arr, key=lambda x:x[1], reverse=True)

    async def output_result(self, begin):
        # print ("wait_and_output_resul called")
        
        single_res = self.parse_res_dict(self.w_dct_single)
        double_res = self.parse_res_dict(self.w_dict_double)
        triple_res = self.parse_res_dict(self.w_dict_triple)
        quadle_res = self.parse_res_dict(self.w_dict_quadle)
        print ("result is here boi")
        print (" ")
        print (" single words: ")
        print (single_res[100:150])
        print ("")
        print ("double words: ")
        print (double_res[:300])
        print ("")
        print ("triple words: ")
        print (triple_res[:300])
        print ("")
        print ("quad words: ")
        print (quadle_res[:300])
        print ("")

        
        end = datetime.datetime.now()
        diff = end - begin
        print ("time benchmark: ", diff.total_seconds())
        return 0
    


    def execute_step1(self, keyword_query):

        url_arr = []
        
        urls = [
            "https://www.google.com/search?q=%s&num=100" %(keyword_query)
            # , "https://www.google.com/search?q=%s&num=100&start=100" %(keyword_query)
        ]
        
        for url in urls:
            # Perform the request
            request = urllib.request.Request(url)

            # Set a normal User Agent header, otherwise Google will block the request.
            request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
            raw_response = urllib.request.urlopen(request).read()

            # Read the repsonse as a utf-8 string
            html = raw_response.decode("utf-8")



            cnt = 0
            regexxx = re.findall(r"href=\"(.*?)\"", html)

            for line in regexxx:   
                if line[:4]=="http":
                    # print ("line length [:4]==http is: ", len(line) )
                    # print (line)
                    url_arr.append(line)

            self.web_scrape_urls.extend(url_arr)
        
        
    

    async def execute_step2(self):
        #crawl the google search result urls received in step 1
        print ("execute_step_2")

        process = CrawlerProcess()
        process.crawl(SpiderScraperThree, urls=self.web_scrape_urls, parse_func = self.parse_scrapy_response )
        process.start()
        return 0


    async def crawl_keyword(self, keyword_query):
        begin = datetime.datetime.now()
        self.web_scrape_urls = []
        self.execute_step1(keyword_query)
        
        # print ("webscrape urls: ", web_scrape_urls[:1])
        task1 = asyncio.create_task(
            self.execute_step2()
        )
        
        task2 = asyncio.create_task(
            self.output_result(begin)
        )

        await task1
        await task2
        end = datetime.datetime.now()
        diff = end - begin

        # await asyncio.sleep(5)
        
    
async def main():
    crawler_pro = GoogleCrawlerPro()
    

    await crawler_pro.crawl_keyword("nha+dat+facebook") 
    
    # print ("time benchmark: ", diff.total_seconds())

asyncio.run(main())