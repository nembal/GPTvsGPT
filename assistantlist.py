import os
import requests
import json

# Set up the OpenAI client with your API key
api_key = os.environ.get('OPENAI_API_KEY')
headers = {
    'Authorization': f'Bearer {api_key}',
    'OpenAI-Beta': 'assistants=v1'
}

def list_assistants():
    # Make a GET request to list all assistants
    response = requests.get(
        'https://api.openai.com/v1/assistants',
        headers=headers
    )
    return response.json()

# Call the list_assistants function and store the result in the assistants variable
assistants = list_assistants()

# Now iterate over the assistants
for assistant in assistants.get('data', []):  # Safely get the 'data' list, default to empty if not found
    # Convert the assistant dictionary to a formatted string
    formatted_assistant = json.dumps(assistant, indent=2)
    print(formatted_assistant)
    print()  # Print a newline for better separation
