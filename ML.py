import requests
import json
import urllib.parse
import sys
import threading


Product_Search_URL='https://api.mercadolibre.com/sites/MLA/search?category=MLA1246&q={}' #variable is product name as text
Review_URL='https://api.mercadolibre.com/reviews/item/{}' #variable is the product ID
Product_URL='https://api.mercadolibre.com/items/{}' #variable is the productID


class myThread (threading.Thread):
   def __init__(self, threadID, product_id):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = product_id
   def run(self):
      get_image(self.product_id)

def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

def get_image_by_product_id(product_id='MLA773625202'):
    product_request=requests.get(Product_URL.format(product_id))

    if product_request.status_code == 200:
        response=json.loads(product_request.text)
        picture=response['pictures'][0]['url']
        return (picture)







def get_products_by_name(product_name='kerastase'):
    
    product_name=urllib.parse.quote(product_name)
    products_request=requests.get(Product_Search_URL.format(product_name))
    
    if products_request.status_code == 200:
        product_list=list()
        request_text=json.loads(products_request.text)
        
        for item in request_text['results']:
            product_item={'id':item['id'],'title':item['title'],'thumbnail':item['thumbnail'],'image':''}
            product_list.append(product_item)

        for item in product_list:
            index=product_list.index(item)
            product_request=requests.get(Product_URL.format(item['id']))
            if product_request.status_code == 200:
                response=json.loads(product_request.text)
                picture=response['pictures'][0]['url']
                product_list[index]['image']=picture
        return (product_list)

def get_reviews_by_product_id(product_id='MLA773625202'):
    review_request=requests.get(Review_URL.format(id))
    
    review_list=list()
    if review_request.status_code == 200:
        request_text=json.loads(review_request.text)
        for item in request_text['reviews']:
            review_item={'content':item['content'],'rate':item['rate']}
            review_list.append(review_item)
        return (review_list)
        

    


































