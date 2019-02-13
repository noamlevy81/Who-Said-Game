import requests
from bs4 import BeautifulSoup
from time import sleep
URL = "http://quotes.toscrape.com/"
def scrape_data():
	curr_query = ""
	quotesList = []
	while True:
		response = requests.get(URL+curr_query)
		soup = BeautifulSoup(response.text,"html.parser")
		body = soup.body
		quotes = soup.find_all(class_="quote")
		for quote in quotes:
			q =quote.find(class_="text").get_text()
			name =quote.find(class_="author").get_text()

			#for getting the first hint
			authorBioRes = requests.get(URL + quote.find('a')["href"]) 
			currSoup = BeautifulSoup(authorBioRes.text,"html.parser")
			hint =f"{currSoup.find(class_='author-born-date').get_text()} {currSoup.find(class_='author-born-location').get_text()}"
			quotesList.append({"name":name,
							"quote":q,
							"hint":hint})
				
		curr_query = soup.find(class_="next")
		if not curr_query: 						#exit loop when scraped all pages
			break
		curr_query = curr_query.find("a")["href"]
		sleep(0.5) #for server overloading
	return quotesList
