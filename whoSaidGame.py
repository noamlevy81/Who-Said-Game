import scraping
from time import time
from random import choice
import cache
import os.path


def hintsManager(curr,guesses_left):
	x = curr.get("name")
	if guesses_left == 3:
		return "Here is a hint: The author was born on " + curr['hint']
	elif guesses_left == 2: 
		return f"Here is a hint: The author's first name starts with a: {x[0]}"
	elif guesses_left == 1: 
		return f"Here is a hint: The author's last name starts with a {x[x.index(' ') + 1]}"
	else :
		return ""

def runGame(quotesList):
	while True and quotesList:						
		guesses_left = 4
		curr_quote = choice(quotesList)
		guess = ""
		author = curr_quote.get("name")
		print(curr_quote.get("quote"))
		while guess.lower() != author.lower() and guesses_left:
				print(f"Guesses Left: {guesses_left}")
				guess = input()
				if guess != author:
					guesses_left-=1
					print(hintsManager(curr_quote,guesses_left))

		if guesses_left:
			print ("Good Job! You Guessed right!\n\n")
		else:
			print(f"The author is: {author}")
		stopGame =""
		while  stopGame not in ('n','no','y','yes'):
			stopGame = input("Would you like to continue? (y/n)").lower()
			
		if stopGame in ('n','no'):
			break
		guesses_left = 4
		quotesList.pop(quotesList.index(curr_quote))


TRASH_HOLD = 604800 #number of seconds in a week
fromCache = True #if the data read from cache
try:
	mod_time = os.path.getmtime(cache.FILE)
except:
	mod_time = 0
if time()-mod_time > TRASH_HOLD:
	quotes = scraping.scrape_data()
	fromCache = False
else:
	quotes = cache.readFromCache()

runGame(quotes)
if not fromCache:
	cache.writeToCache(quotes)