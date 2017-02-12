import time
from sinchsms import SinchSMS

number = '+917977553949'
message = 'Hello Ashok, SMS from terminal'

client = SinchSMS('b66931dc-b6aa-49a8-9736-7e6c083e97e0', 'J0GWmBIRTEuaSPf1j3eI0g==')

print("Sending '%s' to %s" % (message, number))
response = client.send_message(number, message)
message_id = response['messageId']

response = client.check_status(message_id)
while response['status'] != 'Successful':
    print(response['status'])
    time.sleep(1)
    response = client.check_status(message_id)
print(response['status'])