
import scrapy
from scrapy_splash import SplashRequest
import re
from scrapy.crawler import CrawlerProcess
import asyncio
import urllib.request


query_keyword = "dau+tu"
web_scrape_urls = []  #append urls to here lmao
w_dct_single = {}
w_dict_double = {}


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

def handle_url_arr(url_arr):
    web_scrape_urls.extend(url_arr)
    




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

def output_result():
    # print ("wait_and_output_resul called")
    
    single_res = parse_res_dict(w_dct_single)
    double_res = parse_res_dict(w_dict_double)
    print ("result is here boi")
    print (" ")
    print (" single words: ")
    print (single_res[100:150])
    print ("")
    print ("double words: ")
    print (double_res[:300])
    print ("")




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




#begin of action

#step1: open and parse google result html
# html_text = "wtf"
# with open('sample.txt') as f:
#     html_text = f.readlines()
#     f.close()


def execute_step1():
    url_arr = []
    
    urls = [
        "https://www.google.com/search?q=%s&num=100" %(query_keyword),
        "https://www.google.com/search?q=%s&num=100&start=100" %(query_keyword)
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

        web_scrape_urls.extend(url_arr)
    
    


def execute_step2():
    #crawl the google search result urls received in step 1
    print ("execute_step_2")

    process = CrawlerProcess()
    process.crawl( SpiderScraperThree )
    process.start()

    
async def main():
    execute_step1()
    await asyncio.sleep(2)
    # print ("webscrape urls: ", web_scrape_urls[:1])
    execute_step2()
    # await asyncio.sleep(5)
    output_result()

asyncio.run(main())