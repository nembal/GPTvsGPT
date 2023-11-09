import os
import requests

# Set up the OpenAI client with your API key
api_key = os.environ.get('OPENAI_API_KEY')
headers = {
    'Authorization': f'Bearer {api_key}',
    'OpenAI-Beta': 'assistants=v1'  # Presuming the beta header is still needed
}

def list_assistants():
    # Make a GET request to list all assistants
    response = requests.get(
        'https://api.openai.com/v1/assistants',
        headers=headers
    )
    return response.json()

# List all assistants
assistants = list_assistants()
print(assistants)
