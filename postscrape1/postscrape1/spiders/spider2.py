from concurrent.futures import process
from urllib.request import Request
import scrapy
from scrapy_splash import SplashRequest
import re
from scrapy.crawler import CrawlerProcess
import asyncio



web_scrape_urls = ["https://topi.vn/co-phieu-la-gi.html"]
w_dct_single = {}
w_dict_double = {}

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

def replace_xa0_text_arr(text_arr):
    res = []
    for text7 in text_arr:
        text_arr = re.sub("\\xa0", " ", text7)
        res.append(text_arr)
    return res

def handle_data(text_arr):
    
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
        for i in range(len(text_arr)-1):
            single_word = text_arr[i].lower()
            double_word = " ".join( text_arr[i:i+2] ).lower()
            add_to_dct(single_word, w_dct_single)
            add_to_dct(double_word, w_dict_double) 


def parse_res_dict(w_dct):
    tuple_arr = [] #[(word, count)]
    for w in w_dct:
        tuple_arr.append((w,w_dct[w]))
    return sorted(tuple_arr, key=lambda x:x[1], reverse=True)

async def wait_and_output_result():
    print ("wait_and_output_resul called")
    await asyncio.sleep(7)
    single_res = parse_res_dict(w_dct_single)
    double_res = parse_res_dict(w_dict_double)
    print ("result is here boi")
    print (" ")
    print (" single words: ")
    print (single_res[:50])
    print ("")
    print ("double words: ")
    print (double_res[:50])
    print ("")


class SpiderNumberTwo(scrapy.Spider):
    name = "spider2"

    query_keyword = "co_phieu"
    start_urls = [

        "https://www.google.com/search?q=%s&num=100" %(query_keyword),
        # "https://www.google.com/search?q=%s&num=100&start=100" %(query_keyword),
        
    ]
    
    

    def parse(self,response):
        
        url_arr = []

        # resultz = re.findall(r'h3>(.*?)</h3',h3lol)
        
        

        text_arr_1 = response.css('a').getall()
        for textlol in text_arr_1:
            
            res_arr = re.findall(r"href=\"(.*)/3\" ", textlol)
            url_arr.extend(res_arr)



        print ("")
        print ("   == begin of data ==")
        print ("")
        # print ("response body:", res[:30])

        for url in url_arr[:3]:
            print (url)
            
        print ("")
        print("")
        print ("     == end of data ==  ")


        
        return []


class SpiderScraperThree(scrapy.Spider):
    name = "spiderThree"
   
    start_urls = []
    # def __init__(self, url_arr):
    #     super(SpiderScraperThree, self).__init__()
    #     self.start_urls = url_arr
    
    def start_requests(self):
        print ("spider three start request", len(web_scrape_urls))
        for url in web_scrape_urls:
            
            yield scrapy.Request(url, dont_filter=True)

    def parse(self,response):
        
        url_arr = []

        
        #testing parsing 100 website html success
        p_arr = response.css('p').getall()
        h1_arr = response.css('h1').getall()
        h3_arr = response.css('h3').getall()
        h4_arr = response.css('h4').getall()
        
        handle_data(p_arr)
        handle_data(h1_arr)
        handle_data(h3_arr)
        handle_data(h4_arr)


        
        return []


# process = CrawlerProcess()
# process.crawl(SpiderNumberTwo)
# process.start()

# print ("Wtff")


html_text = "wtf"
with open('sample.txt') as f:
    html_text = f.readlines()
    f.close()
# print ("text is: ", html_text[:5])


url_arr = []



for linelol in html_text:
    regexxx = re.findall(r"href=\"(.*?)\"><h3?", linelol)
    
    for line in regexxx:   
        regex111 = re.findall(r"q=(.*?)&amp?", line)[0]
        
        if regex111[:4] == "http":
            
            url_arr.append(regex111)

cnt = 0



web_scrape_urls = url_arr
print ("web_scrape_urls", len(web_scrape_urls))

process = CrawlerProcess()
process.crawl( SpiderScraperThree )
process.start()

asyncio.run( wait_and_output_result() )


