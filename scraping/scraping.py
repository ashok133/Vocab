from bs4 import BeautifulSoup
import urllib2
import re
import csv

majortest = "http://www.majortests.com/gre/wordlist_15"
page = urllib2.urlopen(majortest)
soup = BeautifulSoup(page)
table = soup.find("div", { "class" : "grid_9 alpha" })

word_dict = {}
word_list = []
count = 0

#headers = soup.find("h3")

for row in table.findAll("tr"):
	word = row.findAll("th")
	#word.replace('<th>','')
	#word = re.sub('[<[]th/>]','',word)
	meaning = row.findAll("td")
	for wrapper1 in word:
		key = wrapper1.text
	for wrapper2 in meaning:
		value = wrapper2.text
	#print wrapper.text
	#print word.text, ": ",meaning.text
	count += 1
	word_dict.update({key:value})

print "Total",count ,"words found!"
for i in word_dict:
	print i,"\t:",word_dict[i]

word_list = word_dict.items()
word_list.sort()

with open('word_list_15.csv','wb') as fp:
	w = csv.writer(fp)
	w.writerows(word_list)

#print word_list
#print table