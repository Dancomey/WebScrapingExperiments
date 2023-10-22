# This program downloads all of the articles on Paul Graham's website and saves them to a folder as PDFs
# By: Dan Comey

import requests
import os
import bs4
import pdfkit


#starting URL
url = 'http://www.paulgraham.com/articles.html'

#store articles in /PaulGrahamArticles
os.makedirs('PaulGrahamArticles',exist_ok=True)
os.chdir('PaulGrahamArticles')


#create a list of all of the article URLs

res1 = requests.get(url)
res1.raise_for_status()

soup1 = bs4.BeautifulSoup(res1.text, features="lxml")

#Creating a list of article URLs
URL_list = []

for a in soup1.select('a[href]'):
	url = a['href']
	
	#removes a few unwanted URLs. The URLs we want are all similar to the following: 'charisma.html'
	if '.html' in url:
		URL_list.append(a['href'])

# #for testing
# counter = 0

for URL in URL_list:
	full_URL = 'http://www.paulgraham.com/' + URL
	
	print('Downloading page %s...' % full_URL)
	
	res2 = requests.get(full_URL)
	res2.raise_for_status()

	soup2 = bs4.BeautifulSoup(res2.text, features="lxml")

	text_elems = soup2.find_all('font')
	
	article_text = ''

	for element in text_elems:
		article_text += element.text + ' '

	file_name = URL.replace(".html", ".txt")

	file = open(file_name, 'w', encoding='utf-8')

	# Write the text to the file
	file.write(article_text)

	# Close the file
	file.close()

	# # for testing
	# counter += 1
	# if counter == 2:
	# 	break