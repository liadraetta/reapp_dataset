import json
import os

target_words = [
    " anomalo ", " checca ", " chiappa ", " culattone ", " finocchi ",
    "finocchietto ", "finocchio ", "frocio ", "invertito ",
    "stesso sesso", "travestiti", "travestito ", "frocia ", "ricchione ", "ricchioni ", "trans "
]


def contains_target_word(text):
    for word in target_words:
        if word in text.lower():
            print("word", word)
            print("text", text)
            return True
    return False


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
    total_tweets += 1
    tweet_text = tweet.get("extended_tweet", {}).get("full_text", tweet.get("text", ""))
    if contains_target_word(tweet_text):
        filtered_tweets.append(tweet)
        filtered_tweets_count += 1

output_file_path = os.path.join(os.getcwd(), 'filtered_tweets_2021.json')

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(filtered_tweets, output_file, ensure_ascii=False, indent=4)

print(f"Total tweets processed: {total_tweets}")
print(f"Filtered tweets containing forbidden words: {filtered_tweets_count}")
