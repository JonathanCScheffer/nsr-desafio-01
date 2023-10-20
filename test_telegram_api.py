import requests

# Replace 'YOUR_API_TOKEN' with the API token you received from BotFather.
TOKEN = '6681889492:AAF2iDFVyPMilUOkoh1fubO633211lpXjm0'

# Set the base URL for the Telegram API.
base_url = f'https://api.telegram.org/bot{TOKEN}'

# Create a new message using the sendMessage endpoint.
message = "Hello, this is your Telegram Bot!"

# Specify the chat ID (recipient) where you want to send the message.
chat_id = 'YOUR_CHAT_ID'  # Replace with the actual chat ID.

# Create a dictionary containing the message data.
data = {
    'chat_id': chat_id,
    'text': message
}

# Send the message using the sendMessage endpoint.
response = requests.post(f'{base_url}/sendMessage', data=data)

if response.status_code == 200:
    print("Message sent successfully.")
else:
    print(f"Failed to send the message. Status code: {response.status_code}")
