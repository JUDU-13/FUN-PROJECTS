import requests
import json

# Set up the API key and endpoint
api_key = 'YOUR_API_KEY'
endpoint = 'https://newsapi.org/v2/top-headlines'

# Set up the parameters for the API request
params = {
    'country': 'us',
    'apiKey': api_key
}

# Make the API request
response = requests.get(endpoint, params=params)

# Parse the JSON response
data = json.loads(response.text)

# Print the headlines
for article in data['articles']:
    print(article['title'])
