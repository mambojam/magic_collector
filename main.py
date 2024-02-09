import requests
from bs4 import BeautifulSoup
import readData

# Import card data
my_cards = readData.my_cards

# Find card prices
for card in my_cards:
    try:
        # Generate dynamic URL
        url = f'https://www.bigorbitcards.co.uk/magic-the-gathering/{card["Set"]}/{card["Name"]}.html'
        response = requests.get(url) # Send request to URL
        soup = BeautifulSoup(response.text, 'html.parser') # Parse HTML response
        # Find the price in the <span class="product-price"> tag
        price_span = soup.find('span', class_='product-price')
        # Print the price
        price = price_span.text
        print(f"{card['Name']} is worth {price}")
    # Error if car/price not found
    except AttributeError:
        print("Price not found")



