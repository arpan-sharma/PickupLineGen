import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

# Read pickup lines from a text file
pickup_lines_file = "pickup_lines.txt"

with open(pickup_lines_file, "r", encoding="utf-8") as file:
    pickup_lines = file.readlines()

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(pickup_lines)
total_words = len(tokenizer.word_index) + 1

# Convert text sequences to numerical sequences
input_sequences = []
for line in pickup_lines:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

# Padding sequences
max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

# Creating predictors and labels
X, y = input_sequences[:,:-1],input_sequences[:,-1]
y = tf.keras.utils.to_categorical(y, num_classes=total_words)

# Splitting the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
