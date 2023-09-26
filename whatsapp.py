from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
numbers = ['+923418357982']
for i in numbers:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Your appointment is coming up on July 21 at 3PM',
        to=f'whatsapp:{i}'
    )
    print(message.sid)
