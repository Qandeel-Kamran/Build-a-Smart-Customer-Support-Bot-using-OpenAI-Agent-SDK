# guardrails.py

# List of words to detect as offensive or negative
offensive_words = ["stupid", "idiot", "dumb", "hate", "angry", "upset", "complain"]

def detect_offensive_input(user_input: str) -> bool:
    """Return True if input contains any offensive/negative word."""
    return any(word in user_input.lower() for word in offensive_words)
