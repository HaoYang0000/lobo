from twilio.rest import Client

TWILIO_SID = "AC85c1c30bfe9391295b4d83a51a820738"
TWILIO_TOKEN = "75bbea7d2a442e81a244925717668cde"


def send_sms(to_number, body, from_number="3145961729"):
    global TWILIO_SID
    global TWILIO_TOKEN

    # https://www.twilio.com/docs/libraries/python
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body=body)
    return message
