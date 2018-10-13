from twilio.rest import Client

TWILIO_SID = "ACdd642b34373efb1b5a0862da3e49e029"
TWILIO_TOKEN = "b30d202074736e8f7b2ff102a7bd42e3"


def send_sms(to_number, body, from_number="+15735500003"):
    global TWILIO_SID
    global TWILIO_TOKEN

    # https://www.twilio.com/docs/libraries/python
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body=body)
    return message
