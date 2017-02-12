import sys
from random import randint

prompt = 'y'
score = 0
count = 0

word_list = {
'LOQUACIOUS' 	: 'Tending to talk a lot, talkative', 
'COMATOSE'		: 'State of deep unconsciousness',
'BELEAGUERED' 	: 'Put in a very difficult situation', 
'SERMONIZING' 	: 'Deliver an opinionated and dogmatic talk',
'SOLIPSISM'		: 'The quality of being self-centered and selfish'
}

print "Welcome to vocab!"

#word = raw_input("Enter a word: ") 

#print "Meaning of the entered word is: ", word_list[word]

choice = raw_input ("What would you like to do? \n\t[1]Add words\n\t[2]Guess meanings")
print "Choice registered: ", choice

if(choice == 1):
	#if body here
	word_key = raw_input ("Word: ")
	word_value = raw_input ("Meaning: ")
	word_list.update({word_key:word_value})
	print word_list

else:
	while (prompt!='n'):
		count += 1
		word_index = randint(0,len(word_list)-1)
		print "Word Number: ", word_index
	#curr_word = word_list[word_index]
		curr_word = word_list.keys()[word_index]
		print "Guess the meaning of ", curr_word
	#print "The meaning of %s is %s", %(curr_word,word_list[curr_word])
		done = raw_input("Press 'y' when done!")
		if (done == 'y'):
			print 'The meaning of', curr_word, 'is ',word_list[curr_word]
	#print "Did you guess it right?"
			guess = raw_input("Did you guess it right? (y/n)")
			if (guess == 'y' or guess == 'Y'):
				score += 1
			prompt = raw_input("Try more words? (y/n)")	
		else: 
			print "If not done, please take your time instead of fooling around.";
			print "-1 for misconduct"
	
	print "Your total score is ", score, "/", count


	


