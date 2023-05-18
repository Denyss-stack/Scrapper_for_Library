import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/books/'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
links = soup.find_all('a')
book_titles = []

book_list = soup.select_one('body > div > div > div.col-sm-10')

if book_list:
    book_elements = book_list.find_all('li')
    for book in book_elements:
        title = book.text.strip()
        book_titles.append(title)

    for title in book_titles:
        print({title})
else:
    print("Список книжок не знайдено.")

print("\nAll site links\n")
for link in links:
    href = link.get('href')
    print(href)






