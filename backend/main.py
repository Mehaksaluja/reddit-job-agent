from fastapi import FastAPI
from reddit_client import get_posts_from_subreddit
from ai_analyzer import analyze_post_with_ai

app = FastAPI()

# For now, we will define our skills here. Later, this will come from the UI.
# IMPORTANT: Change these skills to match your own!
MY_SKILLS = ["Video Editing", "Adobe Premiere Pro", "After Effects", "Motion Graphics"]


@app.get("/")
def find_relevant_jobs():
    """
    Fetches posts from Reddit, analyzes them with AI, and returns only the relevant job posts.
    """
    # Get the latest 15 posts to have a good pool to filter from
    all_posts = get_posts_from_subreddit("forhire", 15)

    relevant_posts = []

    print("Starting analysis of fetched posts...")

    for post in all_posts:
        # For each post, call our AI analyzer
        # We need to get the post's body text (selftext) as well
        is_relevant = analyze_post_with_ai(
            post_title=post["title"],
            post_body=post.get("body", ""), # Use post body if available, otherwise empty string
            user_skills=MY_SKILLS
        )

        if is_relevant:
            relevant_posts.append(post)

    print(f"Analysis complete. Found {len(relevant_posts)} relevant posts.")

    return {"relevant_posts": relevant_posts}