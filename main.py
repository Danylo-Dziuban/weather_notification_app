import requests
import smtplib as sm
from twilio.rest import Client


EMAIL_API_KEY = '08bd2fd4191c50dd378617aa34784b10'
SMS_AUTH_KEY = 'ee20a9e305d23eeb7cfcfc0374b79b81'
SMS_SID = 'ACcedcbc2a5dc9f1bc2a0dcc02d31e9b8e'
HOST_EMAIL = 'dz.danylo@gmail.com'
HOST_PASS = 'sahu imqp pdui ikos'

params = {
    'lat': 49.839684,
    'lon': 24.029716,
    'cnt': 4,
    'appid': EMAIL_API_KEY,
}

response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast', params=params)

print(response.status_code)
print(str(response.json()['list'][0]['weather'][0]['id'])[0])

data = response.json()
check = False

for item in data['list']:
    print(1)
    if int(str(item['weather'][0]['id'])[0]) < 7:
        check = True

if check:
    client = Client(SMS_SID, SMS_AUTH_KEY)
    message = client.messages.create(
        body="It might rain today! Don't forget your umbrella!",
        from_='+12515511517',
        to='+380687085034'
    )

    print(message.status)
