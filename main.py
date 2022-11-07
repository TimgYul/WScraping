import bs4
import requests
from constants import HEADERS
import re

KEYWORDS = ['docker', 'аналитик', 'программирования', 'google']

url = 'https://tproger.ru/'

response = requests.get(url)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all("article")

result = ()

for article in articles:
    posts = article.find_all("p")
    for post in posts:
        results = re.split(" ", post.text)
        for element in results:
            if element.lower() in KEYWORDS:
                href = article.find(class_="article__link").attrs["href"]
                print(f"{post.text} ===> {href}")

