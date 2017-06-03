# Text file data from Google Keep note, created on June 2, 2017

word_list = []
word_dict = {}
import csv
import unicodecsv

with open ('keep_words.txt','rb') as fp:
	word_list = fp.readlines()
	# for item in words:
	# 	word_list.append(words.strip())
	# #word_list = 

print word_list

for item in word_list:
	# item = item.replace(' ','')
	print item+"***********"
	if item.strip():
		word = item.split('-')[0]
		print "WORDFOUND"+word
		meaning = item.split('-')[1]
		word_dict.update({word:meaning})

for w,m in word_dict.iteritems():
	print w,":",m

c = 0

with open('keep_words.csv','wb') as f:
    w = csv.writer(f)
    w.writerow(['Name','Meaning'])
    for k,v in word_dict.iteritems():
    	try:
    		w.writerow([k,v])
    		c+=1
    	except UnicodeEncodeError:
    		pass
print "Words added to CSV: ",c
