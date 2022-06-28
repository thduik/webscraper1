import re

import urllib.request

web_scrape_urls = []  #append urls to here lmao
w_dct_single = {}
w_dict_double = {}
w_dict_triple = {}
w_dict_quadle = {}

def add_to_dct(word, dct):
    if word in dct:
        dct[word] += 1
    else:
        dct[word] = 1



def replace_xa0_text_arr(text_arr):
        res = []
        for text7 in text_arr:
            text_arr = re.sub("\\xa0", " ", text7)
            res.append(text_arr)
        return res


def parse_text_1(text):
    re_res = [] #[string]
    
    re_arr = re.findall(r">(.*?)<", text)
    for reslol in re_arr:
        if len(reslol) > 0:
            re_res.append(reslol)
    return re_res #[string]

def handle_data(text_arr):

    #text_arr = [string]
    re_res = []
    for text5 in text_arr:
        parse_res = parse_text_1(text5) #[tring]
        reslmao = replace_xa0_text_arr(parse_res) #[string]
        reslol = []
        for s in reslmao:
            reslol.extend(s.split(" "))
        # print ("")
        # print ("reslmao start: ")
        # for item in reslol:
        #     print (item)
        #     print ("       =item=")
        # print ("reslmao end")
        # print ("")
        if len(reslol) > 0:
            re_res.extend(reslol)
    
    print ("re_res length: ", len(re_res))
    
    #re_res is now [string]
    single_w_cnt = 0
    double_w_cnt = 0
    for text in re_res:
        text_arr = text.split(" ")
        # print ("text is", text)
        for i in range(len(text_arr)):
            single_w_cnt += 1
            single_word = text_arr[i].lower()
            add_to_dct(single_word, w_dct_single)
            # if single_word == "improve":
            #     print ("improve text is", text)
            if i < len(text_arr) - 1:
                double_w_cnt += 1
                double_word = " ".join( text_arr[i:i+2] ).lower()
                add_to_dct(double_word, w_dict_double)
            if i < len(text_arr) - 2:
                triple_word = " ".join( text_arr[i:i+3] ).lower()
                add_to_dct(triple_word, w_dict_triple)
            if i < len(text_arr) - 3:
                quad_word = " ".join( text_arr[i:i+4] ).lower()
                add_to_dct(quad_word, w_dict_quadle)
            
    
    return {}
    
webscrape_urls = []

def execute_step1():

    url_arr = []
    
    urls = [
       
        # , "https://www.google.com/search?q=%s&num=100&start=100" %(keyword_query)
       "https://stackoverflow.com/questions/29269370/how-to-properly-create-and-run-concurrent-tasks-using-pythons-asyncio-module",
    ]
    
    
    
    # Perform the request
    request = urllib.request.Request(urls[0])
    # Set a normal User Agent header, otherwise Google will block the request.
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    raw_response = urllib.request.urlopen(request).read()
    # Read the repsonse as a utf-8 string
    html = raw_response.decode("utf-8")
    
    handle_data(html)



execute_step1()
