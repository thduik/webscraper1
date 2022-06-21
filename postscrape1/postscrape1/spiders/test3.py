import urllib.request
import re

url_arr = []
query_word = "tien+ao"
url = "https://www.google.com/search?q=%s&num=100" %(query_word)

# Perform the request
request = urllib.request.Request(url)

# Set a normal User Agent header, otherwise Google will block the request.
request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
raw_response = urllib.request.urlopen(request).read()

# Read the repsonse as a utf-8 string
html = raw_response.decode("utf-8")

# with open("sample22.html","w") as w:
#     w.write(html)
#     w.close()

# html = ""
# with open("sample22.html","r") as r:
#     html = r.read()
#     r.close()

cnt = 0
regexxx = re.findall(r"href=\"(.*?)\"", html)

for line in regexxx:   
    if line[:4]=="http":
        print ("line length [:4]==http is: ", len(line) )
        print (line)
    
    # regex111 = re.findall(r"q=(.*?)&amp?", line)
    # print ("regex111 length: ", len(regex111))
    

# for line in regexxx:   
#     print (line)
#     regex111 = re.findall(r"q=(.*?)&amp?", line)
#     if regex111[:4] == "http":
#         url_arr.append(regex111)

# print ("url_ArrL: ", url_arr[:10])