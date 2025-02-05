import nltk
import random
import string
import pandas as pd
from nltk.chat.util import Chat, reflections

# Load chatbot responses from CSV file
def load_responses(csv_file):
    df = pd.read_csv(csv_file, header=0)
    df.columns = df.columns.str.strip()  # Remove any leading/trailing spaces
    pairs = [(row['Pattern'], [row['Response']]) for _, row in df.iterrows()]
    return pairs

# Load responses from CSV
pairs = load_responses('responses.csv')

# Create chatbot
chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input(">> ").lower()
        if user_input == 'bye':
            print("Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(response)

if __name__ == "__main__":
    chat()

