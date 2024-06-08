import random

# List of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey, how are you?"],
    "hi": ["Hi there!", "Hello!", "Hey, how are you?"],
    "how are you": ["I'm doing well, thanks for asking!", "I'm doing great, thanks!", "I'm doing okay, thanks."],
    "what's your name": ["I'm a chatbot!", "I'm a friendly AI.", "I'm a helpful assistant."],
    "quit": ["Goodbye!", "See you later!", "It was nice chatting with you."],
    "default": ["I didn't understand that. Can you please rephrase?", "Sorry, I didn't catch that. Can you try again?", "I'm not sure what you mean. Can you explain?"]
}

# Main function
def chatbot():
    print("Welcome to the chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in responses:
            response = random.choice(responses[user_input.lower()])
            print("Chatbot: " + response)
        elif user_input.lower() == "quit":
            print(responses["quit"][0])
            break
        else:
            print(responses["default"][0])

# Start the chatbot
chatbot()