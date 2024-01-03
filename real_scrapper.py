from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get('https://quotes.toscrape.com').text
soup = BeautifulSoup(html_text, 'lxml')
quotes_list = soup.find_all('span', attrs={"class":"text"})
author_list = soup.find_all('small', attrs={"class":"author"})

file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["Quotes" , "Author"])


for quotes, author in zip(quotes_list, author_list):
    print(quotes.text+' - '+author.text)
    writer.writerow([quotes.text, author.text])
file.close()

