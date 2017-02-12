import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from goodreads_quotes import Goodreads

#sender and receiver email ids
fromaddr = 'ashok05@somaiya.edu'
toaddr = 'ashok05@somaiya.edu'
self_addr = 'ashok05@somaiya.edu'
to_sheetal = 'sheetal.thakkar@somaiya.edu'

#MIMEMultipart helps add subject to the mail along with plain body
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Vocab Digest"

#fetching a quote from Goodreads
fetch_quote = Goodreads.get_daily_quote()
quote = fetch_quote['quote']
author = fetch_quote['author']

#Words and their meanings
word1 = "Abberation" 
mean1 = "deviation from normal"
word2 = "Abjure"
mean2 = "swear to refrain from something"
word3 = "Abrasion"
mean3 = "damage to skin OR scraping, rubbing"

body = "Good morning Sheetal! \nReady to learn something new? \n\nHere are your words for today\n\n 1. "+word1+": "+mean1+"\n 2. "+word2+": "+mean2+"\n 3. "+word3+": "+mean3+"\n\nQuote of the day:\n\n"+quote+"\n- "+author+"\n\nPS - This is an automated mail, kindly excuse formatting errors and brevity wherever used."

msg.attach(MIMEText(body.encode('utf-8'),'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,"Drakeash133@somaiya")

text = msg.as_string()
server.sendmail(self_addr,to_sheetal,text)
server.quit()