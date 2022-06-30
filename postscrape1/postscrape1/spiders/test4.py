import re
import urllib.request



multiple_urls_per_domain = True #whether to scrape multiple urls per domain
max_urls_per_domain = 1

domain_dict = {}


def qualify_url(url, domain_dict):
    #domain_dict keep track of count of each domain
    #domain_dict = {domain:count} #{string:int}
    #max_urls_per_domain = max number of urls per domain
    #multiple_urls_per_domain  = whether to scrape multple urls per domain

    re_arr = re.findall(r"\/\/(.+?)\/", url)
    if max_urls_per_domain < 1:
        raise Exception("max_urls_per_domain cannot be less than 1")
    if len(re_arr) > 1:
        raise Exception("qualify_url error, len findall > 1")
    if len(re_arr) == 0:
        print ("empty re arr qualify_url")
        return False
    domain = re_arr[0]    
    if domain in domain_dict:
        if multiple_urls_per_domain and domain_dict[domain] >= max_urls_per_domain:
            return False
        else:
            domain_dict[domain] += 1
            return True

    domain_dict[domain] = 1
    return True

html_text = ''
urls = []
keyword_arr = ["kinh+te"]
for keyword in keyword_arr:
    urls.append( "https://www.google.com/search?q=%s&num=5" %(keyword) )

# Perform the request
print ("Called google search for url", urls)
request = urllib.request.Request(urls[0])
# Set a normal User Agent header, otherwise Google will block the request.
request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
raw_response = urllib.request.urlopen(request).read()
# Read the repsonse as a utf-8 string
html_text = raw_response.decode("utf-8")
print ("html_text length: ", len(html_text))

url_arr = []
web_scrape_urls = []
# regexxx = re.findall(r"href=\"(.*?)\" ping", html_text)
regexxx = re.findall(r"href=\"(.*?)\"", html_text)
for line in regexxx:   
    cond1 = line[:4]=="http"
    cond2 = qualify_url(line, domain_dict)
    if cond1 and cond2:
        url_arr.append(line)

web_scrape_urls.extend(url_arr)

print ("web_scrape_urls leng: ", len(web_scrape_urls) )

for url in web_scrape_urls:
    print (url)