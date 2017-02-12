# we import the Twilio client from the dependency we just installed
from twilio.rest import TwilioRestClient

# the following line needs your Twilio Account SID and Auth Token
client = TwilioRestClient("AC390468027a70ccf77b7939d7aff49f70", "02dcab038e215da7c27766b94bfb7980")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+917977553949", from_="+16822311724", 
                       body="Hello from Python!")