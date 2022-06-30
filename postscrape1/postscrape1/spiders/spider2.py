
import scrapy
import re
from scrapy.crawler import CrawlerProcess
import asyncio
import urllib.request
import datetime
import test2


def parse_google_res_html(html_text):

    
    
    url_arr1 = []
    for linelol in html_text:
        regexxx = re.findall(r"href=\"(.*?)\"><h3?", linelol)
        for line in regexxx:   
            regex111 = re.findall(r"q=(.*?)&amp?", line)[0]
            if regex111[:4] == "http":
                url_arr1.append(regex111)
   
    return url_arr1






async def test1():

    #testing solely exectue step 2
    crawler_pro = GoogleCrawlerPro()
    crawler_pro.web_scrape_urls = ["https://stackoverflow.com/questions/29269370/how-to-properly-create-and-run-concurrent-tasks-using-pythons-asyncio-module"]

    task1 = asyncio.create_task(
            crawler_pro.execute_step2()
        )
        
    # task2 = asyncio.create_task(
    #         crawler_pro.output_result(datetime.datetime.now())
    #     )

    await task1
    res_dct = crawler_pro.return_data()
    print ("")
    print ("single_dict")
    res_arr_single = crawler_pro.my_parser.parse_res_dict(res_dct["single_dict"])
    print (res_arr_single[:100])
    print ("double_dict")
    res_arr_double = crawler_pro.my_parser.parse_res_dict(res_dct["double_dict"])
    print (res_arr_double[:100])
    print ("")
    
    
    # await task2
    

async def main():
    print ("main called")
    
    crawler_pro = GoogleCrawlerPro()
    keyword_arr = []
    s = ""
    while s != "go":
        print ("enter a keyword, or go to start crawling")
        s = input()
        word = "+".join( s.split(" ") )
        keyword_arr.append(word)
    
    await crawler_pro.crawl_keywords(keyword_arr) 
    
    # print ("time benchmark: ", diff.total_seconds())



asyncio.run( main() )