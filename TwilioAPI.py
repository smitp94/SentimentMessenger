from twilio.rest import Client


def send_message(message, cust_number):
    account_sid = "<ACC_ID>"
    auth_token = "<key>"

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=cust_number,
        from_="+16098178080",
        body=message)


# Phone Number is +16098178080
