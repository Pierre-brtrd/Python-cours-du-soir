from bs4 import BeautifulSoup
import requests

requette = requests.get('https://pierre-bertrand-marketing.com')

soup = BeautifulSoup(requette.text, "html.parser")

head = soup.find('head')

title = head.find('title')

paragraphe = soup.find_all('p')

conteur = 0

for p in paragraphe:
    conteur += 1

div = soup.find('div', class_="about-summery")

section = soup.find('section', class_="service-part")

print(section.text)
