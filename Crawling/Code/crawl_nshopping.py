from crawl_HTML import crawl_page
from bs4 import BeautifulSoup as bs

import json

html = crawl_page('https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000', 'naver_shopping.txt')
soup = bs(html, 'html.parser')

li_target = soup.find_all('li',{'class':'_itemSection'})
print(li_target)

json_obj = {}

for target in li_target:
    name = target.find('img')['alt']
    price = target.find('span', {'class' : 'low'}).text + " " + target.find('span', {'class', 'num'}).text
    json_obj[name] = price

print(json.dumps(json_obj, ensure_ascii=False, indent='\t'))

with open('nshopping.json', 'w', encoding='utf-8') as f:
    json.dump(json_obj, f, ensure_ascii=False, indent='\t')