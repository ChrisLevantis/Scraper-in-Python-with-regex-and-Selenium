## Here we download the page and we store it in a html file (1 LEVEL SCRAP)
import urllib.request
import requests

## REGUEST SE PAGE 
url = "https://www.plaisio.gr/pc-perifereiaka/laptops/apple-macbook"
html = requests.get(url)
html_data = html.text
##print(html_data)

## Write the code you have done before request and write it ti a file...
with open('html_code_2.html', 'w', encoding='utf8') as fp:
    fp.write(html_data)
fp.close()









