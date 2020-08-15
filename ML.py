import requests
import json
import urllib.parse
import sys


Product_Search_URL='https://api.mercadolibre.com/sites/MLA/search?category=MLA1246&q={}' #variable is product name as text
Review_URL='https://api.mercadolibre.com/reviews/item/{}' #variable is the product ID
Product_URL='https://api.mercadolibre.com/items/{}' #variable is the productID

Product=sys.argv[1]

Product=urllib.parse.quote(Product)

r=requests.get(Product_Search_URL.format(Product))

product_list=list()

if r.status_code == 200:
    dict1=json.loads(r.text)
    for item in dict1['results']:
        product_item={'id':item['id'],'title':item['title'],'thumbnail':item['thumbnail'],'image':''}
        product_list.append(product_item)

    for item in product_list:
        index=product_list.index(item)
        r1=requests.get(Product_URL.format(item['id']))
        if r1.status_code == 200:
            response=json.loads(r1.text)
            picture=response['pictures'][0]['url']
            product_list[index]['image']=picture

    for item in product_list:
        print(item)






'''


link=dict1['results'][0]['permalink']
        

id=dict1['results'][0]['id']

r=requests.get(Review_URL.format(id))

if r.status_code == 200:
    dict1=json.loads(r.text)
    for item in dict1['reviews']:
        print(item['content'])
        print(item['rate'])

'''

