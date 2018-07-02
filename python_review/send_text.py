from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC518390529635772fa1042d147e150e64'
auth_token = '7fa597770c644bacacad99ba1b6c9353'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!, learn to code is fun ',
                              from_='+12062032912 ',
                              to='+17472170328'
                          )

print(message.sid)