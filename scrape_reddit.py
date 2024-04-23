import os
import praw

from dotenv import load_dotenv

load_dotenv()

# Replace with your Reddit app credentials (refer to point 1 in previous explanation)
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')

# Define scraping parameters (refer to point 3 in previous explanation)
subreddit_list = ['AskReddit', 'worldnews', 'funny', 'gaming', 'pics', 'books', 'CryptoCurrency', 'gamedev', 'Economics']  # List your subreddits here (be mindful of scraping limits)
limit_per_subreddit = 100  # Adjust this to scrape a different number of posts per subreddit

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

# Open the file in append mode to accumulate data from multiple subreddits
with open("train.txt", "a", encoding="utf-8") as f:
    total_scraped = 0
    for subreddit_name in subreddit_list:
        subreddit = reddit.subreddit(subreddit_name)
        top_posts = subreddit.hot(limit=limit_per_subreddit)

        for submission in top_posts:
            # Extract data (modify as needed)
            data_to_save = submission.title + "\n" + submission.selftext + "\n"

            f.write(data_to_save)
            total_scraped += 1

print(f"Scraped a total of {total_scraped} posts from various subreddits and appended data to train.txt")
