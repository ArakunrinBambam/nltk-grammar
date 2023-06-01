import nltk
from nltk.tokenize import word_tokenize

sentence = "Hello, how are you?"
tokens = nltk.word_tokenize(sentence)
# print(tokens)

training_data = [
    {"pattern": "hi", "response": "Hello!"},
    {"pattern": "how are you", "response": "I'm good, thanks."},
    {"pattern": "father", "response": "A male parent"},
    {"pattern": "mother", "response": "A female parent"},
    {"pattern": "parent", "response": "A person's father or mother."},
    {"pattern": "inlaw", "response": "A relative because of marriage"},
    {"pattern": "person", "response": "a human being regarded as an individual."},
    {"pattern": "bye", "response": "Thanks for your time!"},
    # Add more patterns and responses
]


def chatbot_response(user_input):
    for data in training_data:
        if data["pattern"] in user_input:
            return data["response"]
    return "Sorry, I don't understand."

user_input = ""

while user_input.lower() != "bye":
    user_input = input("User: ")
    response = chatbot_response(user_input.lower())
    print("ChatBot: ", response)