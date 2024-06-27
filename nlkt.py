import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding

lemmatizer = WordNetLemmatizer()

# Load pre-trained word embeddings (e.g. GloVe)
embeddings_index = {}
with open('glove.6B.100d.txt', 'r') as f:
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs

# Define the RNN model
model = Sequential()
model.add(Embedding(input_dim=100, output_dim=128, input_length=max_length))
model.add(LSTM(64, dropout=0.2))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(intent_labels), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Load the intent labels
intent_labels = ['investment', 'price', 'help', 'unknown']

# Define the chatbot response function
def chatbot_response(user_input):
    # Tokenize user input
    tokens = word_tokenize(user_input)
    # Lemmatize tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    # Convert tokens to numerical input
    input_seq = []
    for token in tokens:
        if token in embeddings_index:
            input_seq.append(embeddings_index[token])
        else:
            input_seq.append(np.zeros(100))  # unknown token
    input_seq = np.array(input_seq)
    # Pad input sequence to max length
    input_seq = np.pad(input_seq, (0, max_length - len(input_seq)), 'constant')
    # Reshape input sequence for RNN
    input_seq = input_seq.reshape((1, max_length, 100))
    # Predict intent using RNN model
    output = model.predict(input_seq)
    # Determine response based on predicted intent
    intent = np.argmax(output)
    if intent == 0:
        return 'Here are some investment opportunities in cryptocurrency: Bitcoin, Ethereum, and Litecoin.'
    elif intent == 1:
        return 'The current price of Bitcoin is $43,000. Would you like to know more about its market trends?'
    elif intent == 2:
        return 'I can assist you with cryptocurrency-related queries. What would you like to know?'
    else:
        return 'I didn\'t understand that. Can you please rephrase?'

# Update the app.py file to use the new chatbot response function
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = chatbot_response(user_input)
    return jsonify({'response': response})
