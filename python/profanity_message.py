from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACef5493b1dee6706a7dc873151ff2cc51"
# Your Auth Token from twilio.com/console
auth_token  = "810b5a5f872e4ae810e85116e90e61d4"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+9647700254324", 
    from_="+14158181647",
    body="Hello from Python!, i love make things working from the first try .. luv me")
print(message.sid)