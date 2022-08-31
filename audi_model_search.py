import requests
import time
import urllib.parse
import argparse

from googlesearch import search
from bs4 import BeautifulSoup

dealer_source = 'https://www.autodealerlocator.com/auto/audi/?cpage='
num_pages = 8

arg_parser = argparse.ArgumentParser(description='search audi dealers for specific model')
arg_parser.add_argument('--model', metavar='<model name>', required=True, type=str, help='model to search for')
args = arg_parser.parse_args()

def run():
    print('Beginning Search')
    
    for page_index in range(1, num_pages):
        dealer_list_response = requests.get(f'{dealer_source}{page_index}', 
        headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70' })
        
        if dealer_list_response.status_code != 200:
            print (f'Could not retrieve dealer list on page {page_index}')
            continue
        
        parsed = BeautifulSoup(dealer_list_response.text, features='html.parser')
        for dealer in parsed.find_all('span', {'class': 'home-dealer-listing-heading'}):
            dealer_name = dealer.text
            try:
                for result in search(dealer_name, num_results=3):
                    if 'audi' not in result:
                        continue
                    
                    response = requests.get(result + 'apis/widget/INVENTORY_LISTING_DEFAULT_AUTO_NEW:inventory-data-bus1/getFacets')
                    
                    if args.model not in response.text:
                        break
                    
                    print(f'{result}new-inventory/index.htm?model={urllib.parse.quote(args.model)}')
                    break
                time.sleep(0.1)
            except:
                continue
    
    print('Search Complete')

if __name__ == '__main__':
    run()