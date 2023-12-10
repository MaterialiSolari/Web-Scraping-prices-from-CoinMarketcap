import requests
from bs4 import BeautifulSoup

def getDataAndPrices():
    url = requests.get('https://coinmarketcap.com/currencies/xrp/')
    soup = BeautifulSoup(url.text, 'html.parser') 
    current_price = soup.find('span', class_= 'sc-f70bb44c-0 jxpCgO base-text')
    
    percentage = soup.find('p', class_="sc-4984dd93-0 sc-58c82cf9-1 fwNMDM")
    
    
    if current_price: print(f'The current price of XRP: {current_price.text.strip()}')
    return percentage


def determining_The_Percentage(data):
    percentage = data
    data_change, color = percentage.get('data-change'), percentage.get('color')
    current_percentage = percentage.text.strip()
    if data_change == 'down' and color == 'red':
        print(f'Today the percentage decreased by f{current_percentage}')
    elif data_change == 'up' and color == 'green':
        print(f'Today the price increased by {current_percentage}')   
    

data = getDataAndPrices()
determining_The_Percentage(data)