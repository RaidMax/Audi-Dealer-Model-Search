import requests
import time
import urllib.parse
import argparse
import json

from googlesearch import search
from bs4 import BeautifulSoup

dealer_source = 'https://www.autodealerlocator.com/auto/audi/?cpage='
num_pages = 8
limit_results = 999
limit_dealers = 999

arg_parser = argparse.ArgumentParser(description='search audi dealers for specific model')
arg_parser.add_argument('--model', metavar='<model name>', required=True, type=str, help='model to search for')
arg_parser.add_argument('--diff', help='compare last run to only see new results',  action='store_true')
args = arg_parser.parse_args()

def run():
    print('Beginning Search')
    
    last_run = []
    
    if args.diff:
        try:
            with open('results.json', 'r') as file:
                last_run = json.load(file)
        except:
            pass

    dealer_count = 0
    results_count = 0
    for page_index in range(1, num_pages):
        dealer_list_response = requests.get(f'{dealer_source}{page_index}', 
        headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70' })
        
        if dealer_list_response.status_code != 200:
            print (f'Could not retrieve dealer list on page {page_index}')
            continue
        
        parsed = BeautifulSoup(dealer_list_response.text, features='html.parser')
        for dealer in parsed.find_all('span', {'class': 'home-dealer-listing-heading'}):
            dealer_count += 1
            
            if dealer_count > limit_dealers:
                break
            
            dealer_name = dealer.text
            try:
                for result in search(dealer_name, num_results=3):
                    if 'audi' not in result:
                        continue
                    
                    results_count += 1
                    
                    if results_count > limit_results:
                        break
                    
                    response = requests.get(f'{result}apis/widget/INVENTORY_LISTING_DEFAULT_AUTO_NEW:inventory-data-bus1/getInventory?model={args.model}')
                    
                    if response.status_code != 200:
                        continue
                    
                    try:
                        response = response.json()
                    except:
                        continue
                    
                    if response['pageInfo']['totalCount'] == 0:
                        break
                    
                    for vehicle in response['pageInfo']['trackingData']:
                        url = f'{result}' + vehicle['link'][1:]
                        
                        if args.diff and url in last_run:
                            continue
                    
                        data = f"""----------------------------------
{vehicle['address']['accountName']}
{vehicle['modelYear']} - {vehicle['model']} - {vehicle['exteriorColor']}
Options:
{vehicle['optionCodes']}
{url}"""
                        print(data)
                        last_run.append(url)
                time.sleep(0.025)
            except Exception as ex:
                continue

    if args.diff:
        with open('results.json', 'w+') as file:
            json.dump(last_run, file)
    print('Search Complete')

if __name__ == '__main__':
    run()