import os
import time  # <-- Import the time library
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Use the latest recommended model
model = genai.GenerativeModel('gemini-1.5-flash')

def analyze_post_with_ai(post_title: str, post_body: str, user_skills: list[str]):
    """
    Uses Gemini to analyze if a Reddit post is a relevant job opportunity.
    """
    # Convert the list of skills into a comma-separated string
    skills_string = ", ".join(user_skills)

    # This is the prompt we send to the AI. We give it context and clear instructions.
    prompt = f"""
    Analyze the following Reddit post to determine if it is a relevant job opportunity for me.
    My skills are: {skills_string}.

    Post Title: {post_title}
    Post Body: {post_body}

    Is this post a hiring opportunity AND does it match my skills?
    Respond with only one word: YES or NO.
    """

    try:
        # Wait for 2 seconds before making the API call to respect rate limits
        time.sleep(2)  # <-- Add this pause

        # Send the prompt to the model
        response = model.generate_content(prompt)
        # Clean up the response text (remove whitespace and make uppercase)
        decision = response.text.strip().upper()

        # A print statement for us to see the AI's thought process in the terminal
        print(f"Analyzing Post: '{post_title}' -> AI Decision: {decision}")

        if decision == "YES":
            return True
        else:
            return False
    except Exception as e:
        # If anything goes wrong with the API call, we print the error and assume it's not a match.
        print(f"An error occurred during AI analysis: {e}")
        return False