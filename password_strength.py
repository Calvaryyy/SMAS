# password_strength.py
# Dependency: pip install zxcvbn
# Source: https://github.com/dwolfhub/zxcvbn-python

from zxcvbn import zxcvbn


def check_password_strength(password: str) -> dict:
    """
    Checks password strength using the zxcvbn algorithm (Dropbox).

    Returns a dict with:
        - score: 0 (very weak) to 4 (very strong)
        - label: human-readable strength label
        - crack_time: estimated crack time string
        - feedback: list of suggestion strings
        - warning: single warning string (may be empty)
    """
    if not password:
        return {
            "score": 0,
            "label": "No Password",
            "crack_time": "instant",
            "feedback": ["Please enter a password."],
            "warning": ""
        }

    result = zxcvbn(password)

    score = result["score"]

    score_labels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Strong",
        4: "Very Strong"
    }

    label = score_labels.get(score, "Unknown")

    # Use the online throttled crack time as it's the most realistic
    crack_time = result["crack_times_display"]["online_throttling_100_per_hour"]

    suggestions = result["feedback"].get("suggestions", [])
    warning = result["feedback"].get("warning", "")

    return {
        "score": score,
        "label": label,
        "crack_time": crack_time,
        "feedback": suggestions,
        "warning": warning
    }
