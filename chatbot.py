import spacy

nlp = spacy.load("en_core_web_sm")

intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "farewell"],
    "name": ["your name", "who are you", "what's your name"],
    "help": ["help me", "can you help", "i need help", "assist me"],
    "age": ["how old are you", "your age"],
    "weather": ["weather", "is it raining", "temperature", "forecast"],
    "thankyou": ["thank you", "thanks", "appreciate it"],
    "feeling": ["how are you", "how do you feel", "how's it going"],
}

responses = {
    "greeting": "Hi! How can I help you today?",
    "goodbye": "Goodbye! Have a great day!",
    "name": "I'm a simple spaCy chatbot.",
    "help": "Sure! I'm here to help you with simple questions.",
    "age": "I don't have an age, but I'm always learning!",
    "weather": "Sorry, I can't check live weather yet, but I hope it's nice where you are!",
    "thankyou": "You're welcome!",
    "feeling": "I'm just a bot, but I'm doing great! Thanks for asking.",
}

def get_intent(text):
    doc = nlp(text.lower())
    lemmas = [token.lemma_ for token in doc]
    text_lower = text.lower()
    for intent, keywords in intents.items():
        for kw in keywords:
            if kw in lemmas or kw in text_lower:
                return intent
    return None

def chatbot():
    print("Chatbot: Hi! Ask me anything. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        intent = get_intent(user_input)
        if intent:
            print("Chatbot:", responses[intent])
        else:
            print("Chatbot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()
