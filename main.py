import json
import os

# List of forbidden words we want to search for in the text field
forbidden_words = [
    " anomalo ", " checca ", " chiappa ", " culattone ", " finocchi ",
    "finocchietto ", "finocchio ", "frocio ", "invertito ",
    "stesso sesso", "travestiti", "travestito ", "frocia ", "ricchione ", "ricchioni ", "trans "
]


# Function to check if any of the forbidden words appear in the text
def contains_forbidden_word(text):
    for word in forbidden_words:
        if word in text.lower():
            print("word", word)
            print("text", text)
            return True  # Return True if a forbidden word is found
    return False  # Return False if no forbidden word is found


# Load the JSON file from the current directory
json_file_path = os.path.join(os.getcwd(), 'filtered_tweets_reapp_2021.json')  # Adjust the file name if necessary

# Open and read the JSON file
with open(json_file_path, 'r', encoding='utf-8') as file:
    tweets_data = json.load(file)  # Load the JSON data into a Python object

total_tweets = 0  # Counter for total tweets processed
filtered_tweets_count = 0  # Counter for tweets containing forbidden words

filtered_tweets = []

# Iterate over each tweet in the tweets_data
for tweet in tweets_data:
    total_tweets += 1  # Increment the total tweet counter
    # Get the full text of the tweet, if available (i.e., check for extended_tweet field)
    tweet_text = tweet.get("extended_tweet", {}).get("full_text", tweet.get("text", ""))
    if contains_forbidden_word(tweet_text):
        filtered_tweets.append(tweet)
        filtered_tweets_count += 1 # Add the tweet to the filtered list

output_file_path = os.path.join(os.getcwd(), 'filtered_tweets_2021.json')

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(filtered_tweets, output_file, ensure_ascii=False, indent=4)

print(f"Total tweets processed: {total_tweets}")
print(f"Filtered tweets containing forbidden words: {filtered_tweets_count}")
