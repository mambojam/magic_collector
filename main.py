import requests
from bs4 import BeautifulSoup

library = [("core-set-2021", "vito-thorn-of-the-dusk-rose"),
           ("throne-of-eldraine", "garruk-cursed-huntsman"),
           ("the-lord-of-the-rings-tales-of-middle-earth", "frodo-baggins")]

for card in library:
    url = f'https://www.bigorbitcards.co.uk/magic-the-gathering/{card[0]}/{card[1]}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # find the price in the <span class="product-price"> tag
    price_span = soup.find('span', class_='product-price')
    # print the price
    price = price_span.text
    print(f"{card[1]} is worth {price}")



# webpage we're scraping
# url = 'https://www.bigorbitcards.co.uk/magic-the-gathering/the-lord-of-the-rings-tales-of-middle-earth/frodo-baggins.html'

# # send http request to the url
# response = requests.get(url)
#
# # parse the HTML content of the page
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # find the price in the <span class="product-price"> tag
# price_span = soup.find('span', class_='product-price')
#
# # print the price
# price = price_span.text
# print(price)
#

