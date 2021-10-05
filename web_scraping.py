from bs4 import BeautifulSoup # import to parse data
import requests # import to request from website
import csv

source = requests.get('https://www.philstar.com/tags/covid-19-tally-philippines').text # get contents of the site
soup = BeautifulSoup(source, 'lxml')

csv_file = open('output.csv', 'w') # create and open a csv file
csv_writer = csv.writer(csv_file) # call the created file then write in it
csv_writer.writerow(['Title', 'Content']) # write rows in the file

for article in soup.find_all('div', class_='tiles late'): # look for every article
    title = article.find('div', class_='news_title').text # find the article's title
    content = article.find('div', class_='news_summary').text # find the summary of the article

    csv_writer.writerow([title, content])

csv_file.close()





