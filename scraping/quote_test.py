from goodreads_quotes import Goodreads

fetch_quote = Goodreads.get_daily_quote()

print fetch_quote['quote']
print fetch_quote['author']
#print quote
#print type(fetch_quote)
#print fetch_quote[quote]