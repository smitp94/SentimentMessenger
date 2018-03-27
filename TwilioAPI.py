from twilio.rest import Client


def send_message(message, cust_number):
    account_sid = "ACf1596917f7b259277ce4b6189701d9d5"
    auth_token = "3f219a60b6d3e33a647a73d69d1d7fb8"

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=cust_number,
        from_="+16098178080",
        body=message)


# Phone Number is +16098178080
