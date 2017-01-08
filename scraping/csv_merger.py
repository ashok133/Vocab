import csv

with open("final_list.csv","a") as fout:
	for num in range(01,15):
		for line in open("word_list_"+str(num)+".csv"):
			fout.write(line)

with open("final_list.csv",'rb') as fp:
	reader = csv.reader(fp)
	final_word_list = list(reader)
	final_word_list.sort()

with open('final_list.csv','wb') as fp:
	w = csv.writer(fp)
	w.writerows(final_word_list)
