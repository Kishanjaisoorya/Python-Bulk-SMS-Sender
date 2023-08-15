from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

# List of recipient phone numbers
recipients = ['+1234567890', '+9876543210']  # Add more phone numbers as needed

# Send SMS to each recipient
for recipient in recipients:
    message = client.messages.create(
        to=recipient,
        from_='your_twilio_phone_number',
        body='Hello from Twilio!'
    )

    print(f"Message sent to {recipient}, SID: {message.sid}")
