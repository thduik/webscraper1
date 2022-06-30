import re

import urllib.request



web_scrape_urls = []  #append urls to here lmao



class MyHtmlParser:
    w_dct_single = {}
    w_dict_double = {}
    w_dict_triple = {}
    w_dict_quadle = {}

    def parse_res_dict(self, w_dct):
        
        tuple_arr = [] #[(word, count)]
        for w in w_dct:
            tuple_arr.append((w,w_dct[w]))
        return sorted(tuple_arr, key=lambda x:x[1], reverse=True)

    def add_to_dct(self, word, dct):
        if word in dct:
            dct[word] += 1
        else:
            dct[word] = 1



    def replace_xa0_text_arr(self, text_arr):
        res = []
        for text7 in text_arr:
            text_arr = re.sub("\\xa0", " ", text7)
            res.append(text_arr)
        return res


    def parse_text_1(self, text):
        re_res = [] #[string]
        # print ("parse_text_1 text is: ", len(text) )
        re_arr = re.findall(r">(.*?)<", text)
        for reslol in re_arr:
            if len(reslol) > 0:
                re_res.append(reslol)
        return re_res #[string]

    def populate_res_dict(self, text_arr):
        for i in range(len(text_arr)):
            single_word = text_arr[i].lower()
            self.add_to_dct(single_word, self.w_dct_single)     
            if i < len(text_arr) - 1:
                double_word = " ".join( text_arr[i:i+2] ).lower()
                self.add_to_dct(double_word, self.w_dict_double)
            if i < len(text_arr) - 2:
                triple_word = " ".join( text_arr[i:i+3] ).lower()
                self.add_to_dct(triple_word, self.w_dict_triple)
            if i < len(text_arr) - 3:
                quad_word = " ".join( text_arr[i:i+4] ).lower()
                self.add_to_dct(quad_word, self.w_dict_quadle)

    def handle_data(self, text_html):

        #text_arr = [string]
        re_res = []
        
        parse_res = self.parse_text_1(text_html) #[tring]
        reslmao = self.replace_xa0_text_arr(parse_res) #[string]
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
        
        # print ("re_res length: ", len(re_res))
        self.populate_res_dict(re_res)
        #re_res is now [string]
        
        
        
        # print ("text is", text)
        
                
        
        return {}

    def return_data(self):
        #return the res_dicts' current state
        return {
            "single_dict":self.w_dct_single,
            "double_dict":self.w_dict_double,
            "triple_dict":self.w_dict_triple,
            "quad_dict":self.w_dict_quadle
        }

webscrape_urls = []

def execute_step1_test():
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
    
    my_parser = MyHtmlParser()
    my_parser.handle_data(html)
    res_dct = my_parser.return_data()

    
    # print ("")
    # print ("single_dict")
    # res_arr_single = my_parser.parse_res_dict(res_dct["single_dict"])
    # print (res_arr_single[:100])
    # print ("double_dict")
    # res_arr_double = my_parser.parse_res_dict(res_dct["double_dict"])
    # print (res_arr_double[:100])
    # print ("")




