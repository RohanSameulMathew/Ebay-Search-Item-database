import argparse
import requests
from bs4 import BeautifulSoup
import json

total_items = []


### Setup argparse
parser = argparse.ArgumentParser(description="Enter ebay search term")
parser.add_argument('product', nargs = '+', help = "Enter name of interested product")
parser.add_argument('--num_pages', default=10)   
args = parser.parse_args()
product = args.product

query = '+'.join(product)


for page_number in range(1,int(args.num_pages)+1):

    url='https://www.ebay.com/sch/i.html?_nkw=' + query + '&_sacat=0&_from=R40&__pgn=' + str(page_number) + '&rt=nc'
    print(url)

    search = requests.get(url)
    status = search.status_code
    print("status=", status)
    html = search.text
    # print ('html=', html[:50])
    # download the search pages

######
    soup = BeautifulSoup(html, 'html.parser')
    
    tags_items = soup.select(".s-item__info.clearfix")
    for tag_item in tags_items:
###
        name = None
        tags_name = tag_item.select(".s-item__title")
        for tag in tags_name:
            name = tag.text
###
        freereturns = False
        tags_freereturns = tag_item.select(".s-item__free-returns.s-item__freeReturnsNoFee")
        for tag in tags_freereturns:
            freereturns= True
###
        sold = ''
        number = ''
        tags_sold = tag_item.select('.s-item__dynamic.s-item__quantitySold')
        for tag in tags_sold:
            text = tag.get_text(strip=True)
            for char in text:
                if char in '0123456789':
                    number += char
        if number:       
                sold = int(number)
        else:
            sold = None

###
        status = None
        tags_status = tag_item.select('.SECONDARY_INFO')
        for tag in tags_status:
            text = tag.get_text(strip=True)
            status = ''
            status += text
###
        shipping = 0
        s_price = ''
        tags_shipping = tag_item.select(".s-item__shipping.s-item__logisticsCost")
        for tag in tags_shipping:
            text = tag.get_text(strip=True)
            for char in text:
                if char in '0123456789':
                    s_price += char
            
            if s_price:
                shipping += int(s_price)
            else:
                shipping+=0
###     
        price = 0
        str_p = ''
        tags_price = tag_item.select(".s-item__price")
        for tag in tags_price:
            text = tag.get_text(strip=True)
            for char in text:
                if char in '0123456789':
                    str_p += char
            price += int(str_p)


        item = {
            'Name': name,
            'Price': price,
            'Free_returns': freereturns,
            'Quantity_sold': sold,
            'Status': status,
            'Shipping_cost': shipping,
            }
        total_items.append(item)



print(total_items)
print('len(total_items)',len(total_items))

#### FILE SETUP
filename = '/Users/rohanmathew/Downloads/JSON product output/' + query + '.json'
with open(filename, 'w', encoding='ascii') as f:
    f.write(json.dumps(total_items))

