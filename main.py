print("Welcome to ChatBot! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you today?")
    
    elif "your name" in user_input:
        print("Bot: I'm a simple rule-based chatbot.")
    
    elif "how are you" in user_input:
        print("Bot: I'm just code, but I'm functioning as expected!")
    
    elif "help" in user_input:
        print("Bot: Sure, I can help you. What do you need help with?")
    
    elif "weather" in user_input:
        print("Bot: Sorry, I can't provide real-time weather updates right now.")
    
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: I'm not sure I understand. Can you rephrase?")

