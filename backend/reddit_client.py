import os
import praw
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get credentials from environment variables
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")

# Initialize the Reddit instance
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
)

def get_posts_from_subreddit(subreddit_name: str, limit: int):
    """
    Fetches a specified number of hot posts from a given subreddit.
    """
    subreddit = reddit.subreddit(subreddit_name)
    posts_list = []
    print(f"Fetching {limit} posts from r/{subreddit_name}...")
    for post in subreddit.hot(limit=limit):
        posts_list.append({
            "title": post.title,
            "url": post.url,
            "score": post.score,
            "body": post.selftext  # <-- IMPORTANT: We added this line to get the post's body text
        })
    print("Fetching complete.")
    return posts_list
