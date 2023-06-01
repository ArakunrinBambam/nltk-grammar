import nltk
from nltk.tokenize import word_tokenize


training_data = [
    {"pattern": "bawo ni", "response": "Mo wa pa"},
    {"pattern": "baba", "response": "Okunrin ti o je obi eni"},
    {"pattern": "iya", "response": "Obinrin ti o je obi eni"},
    {"pattern": "obi", "response": "baba ati iya eniyan"},
    {"pattern": "ana", "response": "eni ti o di ebi nitori igbeyawo"},
    {"pattern": "eniyan", "response": "Eni ti o le yan fun ara re"},
    {"pattern": "o dabo", "response": "E se pupo fun asiko yin "},
    # Add more patterns and responses
]


# def chatbot_response(user_input):
#     for data in training_data:
#         if data["pattern"] in user_input:
#             return data["response"]
#     return "Ema binu! Ohun ti e te ko ye mi ooo."
def chatbot_response(user_input):
    tokens = word_tokenize(user_input)

    for word in tokens: 
        for data in training_data:
            if data["pattern"] == word:
                return data["response"]
    return "Ema binu! Ohun ti e te ko ye mi ooo."    
    # for data in training_data:
    #     if data["pattern"] in user_input:
    #         return data["response"]
    

user_input = ""

while user_input.lower() != "o dabo":
    user_input = input("User(Olulo): ")
    response = chatbot_response(user_input.lower())
    print("ChatBot(Ero): ", response)