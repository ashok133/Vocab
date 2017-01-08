import csv 
import operator
from pprint import pprint

#helper function to print structures in readable format
def printplus(obj):
    """
    Pretty-prints the object passed in.

    """
    # Dict
    if isinstance(obj, dict):
        for k, v in sorted(obj.items()):
            print u'{0}: {1}'.format(k, v)

    # List or tuple            
    elif isinstance(obj, list) or isinstance(obj, tuple):
        for x in obj:
            print x

    # Other
    else:
        print obj

word_list_1 = {}

read = csv.reader(open('word_list_1.csv','r'))

for row in read:
	k,v = row
	word_list_1[k] = v

#sorted_list = sorted(word_list_1.items(), key=operator.itemgetter(0))

#for i in word_list_1:
#	print i,"\t\t: ", word_list_1[i]

printplus(word_list_1)

#for i in range (0,len(sorted_list)):
#	print i,"\t: ",sorted_list[i]
#print sorted_list