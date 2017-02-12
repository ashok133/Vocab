import pickle
import time
from sinchsms import SinchSMS

filename = 'vocab_append.txt'
file_content = {}

with open(filename,'r+') as fp2:
	while 1:
		try:
			file_content.update(pickle.load(fp2))
		except EOFError:
			break 
	print "Total number of words: ",len(file_content)
	#print file_content
	for i in file_content:
		print i,"\t: ",file_content[i]