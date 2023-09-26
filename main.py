import requests
from bs4 import BeautifulSoup

with open('index.html') as f:
    file = f.read()

# contentData = requests.get(url)
# htmlContent = contentData.content

soup = BeautifulSoup(file, 'html.parser')

# print(soup.prettify())

# print(soup.title)

# print(soup.find_all('p'))

# print(soup.find_all('div'))

# print(soup.find(id="dropdown-item3"))
# OR
# print(soup.find("a", id="dropdown-item3"))

# print(soup.find_all("a", class_="dropdown-item3"))

# for i in soup.find_all('a'):
#     print(i)
#     print(i.get_text())
#     print(i.get('href'))

# SELECT ELEMENTS THROUGH CSS SELECTORS
# print(soup.select('div.alert-primary'))

# print(soup.select('a.dropdown-item3'))

# print(soup.select('a#dropdown-item3'))

# print(soup.select('a#dropdown-item3'))

