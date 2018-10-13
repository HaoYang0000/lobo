from twilio.rest import Client


def sample():
    # Sample code from https://www.twilio.com/docs/libraries/python
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+15558675309",
        from_="+15017250604",
        body="Hello from Python!")
    print(message.sid)

