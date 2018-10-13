from twilio.rest import Client

TWILIO_SID = "AC85c1c30bfe9391295b4d83a51a820738"
TWILIO_TOKEN = "75bbea7d2a442e81a244925717668cde"


def send_sms(to_number, body, from_number="3145961729"):
    # Sample code from https://www.twilio.com/docs/libraries/python
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+15558675309",
        from_="+15017250604",
        body="Hello from Python!")
    return message
