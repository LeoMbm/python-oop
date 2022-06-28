import requests
from bs4 import BeautifulSoup
from sys import exit


ask = input('Do you want to scrap? Y or N: ')

if ask != 'Y':
    print('Exit Script')
    exit()
else:
    url = "https://www.i-comparateur.com/comparer-prix-x10c0061b112.htm"
    response = requests.get(url)
    page = response.content

    soup = BeautifulSoup(page, "html.parser")
    class_name = "Z"
    title = soup.find_all("tr", class_=class_name)
# print(title)

    all_prices = []

    for price in title:
        all_prices.append(str(price))

    print('Data availible in scrap.txt')
    files = open("scrap.txt", "r+")
    files.write(str(all_prices))
    files.close()
