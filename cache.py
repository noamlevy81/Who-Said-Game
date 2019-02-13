from csv import DictWriter 
from csv import DictReader

FILE = "quotes-cache.csv"
def writeToCache(quotes):
	with open(FILE,'w',encoding='utf-8') as cache:
		headers = ['name','quote','hint']
		writer = DictWriter(cache, fieldnames=headers)
		writer.writeheader()
		for quote in quotes:
			writer.writerow(quote)

def readFromCache():
	with open(FILE,'r',encoding='utf-8') as file:
		return list(DictReader(file))
