with open('assistants_list.txt', 'w') as file:
    for assistant in assistants.get('data', []):
        formatted_assistant = json.dumps(assistant, indent=2)
        file.write(formatted_assistant + "\n\n")
