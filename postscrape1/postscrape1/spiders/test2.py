import re


html_text_arr = ["default"]

url_arr = []
with open("sample11.html","r") as r:
    html_text_arr = r.readlines()
    r.close()

print (len(html_text_arr))





for line in html_text_arr:
    regexxx = re.findall(r"href=\"(.*?)\"><h3?", line)

    for line in regexxx:   
        regex111 = re.findall(r"q=(.*?)&amp?", line)[0]
        if regex111[:4] == "http":
            url_arr.append(regex111)

print ("url_ArrL: ", url_arr[:10])