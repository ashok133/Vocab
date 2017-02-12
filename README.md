# Vocab
A simple Python CLI to help me add and memorise English words and their meanings through quiz, with data scraped from an online resource and stored locally.

## What can it do?
* Scrape for frequent words as found on www.majortests.com
* Merge scraped words and meanings to readable CSV
* Send daily SMS, mail notifications with new words and a Goodreads quote 
* Add words
* Search for words
* Run a quiz

I wanted a list of most frequent GRE words, and there are quite a few resources online. 

One particularly useful resource was http://www.majortests.com/gre/. They have a comprehensive list of useful words with their meanings divided into 15 lists, each containing roughly 100 words. I was not going to go through each list and copy paste the words with their meanings. Even after doing that, I would've had to manually enter all the entries in my Vocab words list. 

BeautifulSoup came to my rescue. I scraped through the website and extracted the word lists by writing a script (scraping_list.py). After extracting the 15 lists from 15 separate web pages, I merged and exported them into a single CSV file (final_list.csv)

I've also made use of Synch and Twilio, as well as smtplib for daily notifications (SMS, mail) with new words and a quote from Goodreads.

Github doesn't allow more than a 100 files to be uploaded at once. Meh. Complete code - bit.ly/vocab_apk

Python makes lives a little more easier.

