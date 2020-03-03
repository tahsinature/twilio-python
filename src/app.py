from twilio.rest import Client
from environment import check_env, env_vars

check_env()
#
print()


client = Client(
    account_sid=env_vars["TWILIO_ACCOUNT_SID"], password=env_vars["TWILIO_AUTH_TOKEN"])


message = client.messages.create(
    body="after setting pylint", from_=env_vars["TWILIO_PHONE_NUMBER"], to="+<destination number>")

print(message.sid)
