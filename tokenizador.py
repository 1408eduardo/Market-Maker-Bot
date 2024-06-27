import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def chatbot_response(user_input):
    # Tokenize user input
    tokens = word_tokenize(user_input)
    # Lemmatize tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    # Determine response based on tokens
    if 'investment' in tokens:
        return 'Here are some investment opportunities in cryptocurrency: Bitcoin, Ethereum, and Litecoin.'
    elif 'price' in tokens:
        return 'The current price of Bitcoin is $43,000. Would you like to know more about its market trends?'
    elif 'help' in tokens:
        return 'I can assist you with cryptocurrency-related queries. What would you like to know?'
    else:
        return 'I didn\'t understand that. Can you please rephrase?'

def cryptocurrency_app():
    print('Welcome to CryptoChat!')
    while True:
        user_input = input('You: ')
        response = chatbot_response(user_input)
        print('CryptoChat: ' + response)

cryptocurrency_app()
