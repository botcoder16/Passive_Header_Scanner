import pickle
# Path to the .pickle file
pickle_file_path = "word_frequency_2021.pickle"

# Load the .pickle file
with open(pickle_file_path, "rb") as file:
    words_frequency = pickle.load(file)

# Extract and print the categories
categories = list(words_frequency.keys())
print("Categories:", categories)
