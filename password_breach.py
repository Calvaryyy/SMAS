# password_breach.py
# Uses the HaveIBeenPwned (HIBP) Pwned Passwords API
# API Docs: https://haveibeenpwned.com/API/v3#PwnedPasswords
#
# IMPORTANT: This module uses the k-anonymity model — only the first 5
# characters of the SHA-1 hash are sent to the API. The full password
# is NEVER transmitted. This is privacy-safe by design.
#
# No API key is required for the Pwned Passwords endpoint.
# No pip install needed — uses Python's built-in hashlib and urllib.

import hashlib
import urllib.request
import urllib.error


def check_password_breach(password: str) -> dict:
    """
    Checks if a password has appeared in known data breaches using
    the HaveIBeenPwned Pwned Passwords API (k-anonymity model).

    The full password is NEVER sent over the network. Only the first
    5 characters of its SHA-1 hash are transmitted.

    Args:
        password: The plaintext password to check.

    Returns a dict with:
        - breached: True if found in breaches, False otherwise
        - breach_count: Number of times seen across breaches (0 if none)
        - message: Human-readable summary
        - error: Error string if API call failed, else None
    """
    if not password:
        return {
            "breached": False,
            "breach_count": 0,
            "message": "No password provided.",
            "error": None
        }

    # Step 1: SHA-1 hash the password
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    # Step 2: Query HIBP with only the prefix (k-anonymity)
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "SMAS-SecurityTool"})
        with urllib.request.urlopen(req, timeout=5) as response:
            body = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        return {
            "breached": False,
            "breach_count": 0,
            "message": "Could not connect to breach database. Check your internet connection.",
            "error": str(e)
        }
    except Exception as e:
        return {
            "breached": False,
            "breach_count": 0,
            "message": "An unexpected error occurred while checking breaches.",
            "error": str(e)
        }

    # Step 3: Search response for our suffix
    # Response lines are in the format: SUFFIX:COUNT
    breach_count = 0
    for line in body.splitlines():
        parts = line.split(":")
        if len(parts) == 2:
            hash_suffix, count = parts
            if hash_suffix == suffix:
                breach_count = int(count)
                break

    # Step 4: Build result
    if breach_count > 0:
        message = (
            f"This password has been found in {breach_count:,} known data breach(es). "
            f"It is strongly recommended that you stop using it immediately."
        )
        breached = True
    else:
        message = "Good news — this password was not found in any known data breaches."
        breached = False

    return {
        "breached": breached,
        "breach_count": breach_count,
        "message": message,
        "error": None
    }
