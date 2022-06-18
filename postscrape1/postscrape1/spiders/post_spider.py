import scrapy
from scrapy_splash import SplashRequest
import re

class PostSpider(scrapy.Spider):
    name = "spider1"

    query_keyword = "co_phieu"
    start_urls = [
        # "https://www.facebook.com/nghethuatcoding/"
        # "https://docs.python.org/3/library/re.html",
        "https://www.google.com/search?q=%s&num=100" %(query_keyword),
        # "https://www.google.com/search?q=%s&num=100&start=100" %(query_keyword),
        # "https://www.google.com/search?q=%s&num=100&start=200" %(query_keyword)
    ]
    
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url, self.parse,
    #             endpoint='render.html',
    #             args={'wait': 0.5},
    #         )

    def parse(self,response):
        page = response.url.split('/')[-1]
        filename = "posts-%s.html" %(page)
        

        

        h3lol = response.css('h3').getall()
        spanlol = response.css('span').getall()
        h3lol.extend(spanlol)

        # resultz = re.findall(r'h3>(.*?)</h3',h3lol)
        print ("")
        print ("   == begin of data ==")
        print ("")
        print ("response body:")

        res_dict = {}
        cnt_tuples = []
        excluded_words = set(["and", "the", "in", "of", "to"])
        for senlol in h3lol:
            resz = re.findall(r'>(\w.*?)<',senlol)
            for sent in resz:
                words = sent.lower().split(" ")
                for w in words:
                    if w in res_dict:
                        res_dict[w] += 1
                    else:
                        res_dict[w] = 1
        
        for w in res_dict:
            cnt_tuples.append((w, res_dict[w]))
        
        cnt_tuples.sort(key = lambda x:x[1], reverse=True)
        
        cnt_tuples = list( filter(lambda x:x[0].lower() not in excluded_words, cnt_tuples) )
        
        print (cnt_tuples[:100])
            
        print ("")
        print("")
        print ("                     == end of data ==  ")

        return []