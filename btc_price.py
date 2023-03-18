import requests
from bs4 import BeautifulSoup
import time

def get_bitcoin_price():
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find('div', {'class': 'priceValue'})

        if price_element:
            price = price_element.get_text().replace(',', '').replace('$', '')
            return float(price)
        else:
            print("Failed to find the price element on the webpage.")
            return None
    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)
        return None

if __name__ == '__main__':
    while True:
        price = get_bitcoin_price()
        if price:
            print(f"Bitcoin price: ${price}")
        time.sleep(5)  # Wait for 1 hour (3600 seconds)
