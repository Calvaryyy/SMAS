# facebook.py

def get_account_types():
    return {
        "personal": "Personal Account",
        "business": "Business Page",
        "group": "Facebook Group"
    }


def get_facebook_questions(account_type):

    if account_type in ["personal", "business"]:
        return [
            {
                "id": "auth_method",
                "question": "Do you use password or passkey?",
                "options": {"password": 0, "passkey": 20}
            },
            {
                "id": "password_length",
                "question": "Is your password longer than 8 characters?",
                "options": {"yes": 5, "no": 0},
                "conditional": "auth_method",
                "conditional_value": "password"
            },
            {
                "id": "password_unique",
                "question": "Is your Facebook password unique?",
                "options": {"yes": 5, "no": 0},
                "conditional": "auth_method",
                "conditional_value": "password"
            },
            {
                "id": "twofa",
                "question": "Do you use 2FA/MFA?",
                "options": {"yes": 20, "no": 0}
            },
            {
                "id": "credential_sharing",
                "question": "Does anyone else know your login credentials?",
                "options": {"yes": 0, "no": 20}
            },
            {
                "id": "friend_request",
                "question": "Would you accept a friend request from someone you do not know?",
                "options": {"yes": 0, "no": 20}
            },
            {
                "id": "suspicious_link",
                "question": "Would you click a suspicious link?",
                "options": {"yes": 0, "no": 20}
            }
        ]

    else:  # group
        return [
            {
                "id": "password_length",
                "question": "Is your password longer than 8 characters?",
                "options": {"yes": 5, "no": 0}
            },
            {
                "id": "password_unique",
                "question": "Is your Facebook password unique?",
                "options": {"yes": 5, "no": 0}
            },
            {
                "id": "twofa",
                "question": "Do you use 2FA/MFA?",
                "options": {"yes": 20, "no": 0}
            },
            {
                "id": "credential_sharing",
                "question": "Does anyone else know your login credentials?",
                "options": {"yes": 0, "no": 20}
            },
            {
                "id": "admin_review",
                "question": "How often do you review admin roles?",
                "options": {"periodically": 15, "rarely": 5, "never": 0}
            },
            {
                "id": "login_monitor",
                "question": "How often do you monitor login activity?",
                "options": {"periodically": 15, "rarely": 5, "never": 0}
            },
            {
                "id": "third_party",
                "question": "Do you monitor connected third party apps?",
                "options": {"not applicable": 20, "yes": 20, "no": 0}
            }
        ]


def run_facebook(account_type, answers):

    score = 0
    recommendations = []

    questions = get_facebook_questions(account_type)

    for q in questions:

        if "conditional" in q:
            if answers.get(q["conditional"]) != q.get("conditional_value"):
                continue

        answer = answers.get(q["id"])
        score += q["options"].get(answer, 0)

        if q["id"] == "auth_method" and answer == "password":
            recommendations.append(
                "Consider switching to a passkey instead of a password. "
                "A passkey lets you log in using your fingerprint, face scan, or phone PIN — "
                "no password to remember, and much harder for hackers to steal. "
                "Facebook supports passkeys on mobile devices. "
                "Watch this short guide to learn how to set one up: "
                "https://www.youtube.com/results?search_query=how+to+set+up+facebook+passkey"
            )

        if q["id"] == "password_length" and answer == "no":
            recommendations.append(
                "Your password should be longer than 8 characters. "
                "Short passwords can be cracked by attackers very quickly using automated tools — "
                "sometimes in just a few seconds. A good password should be at least 12 characters long "
                "and include a mix of letters, numbers, and symbols. Even better, use a passphrase: "
                "a string of random words like 'RedTableChair92!' which is both long and easy to remember. "
                "Watch: https://www.youtube.com/results?search_query=how+to+create+a+strong+password"
            )

        if q["id"] == "password_unique" and answer == "no":
            recommendations.append(
                "Use a unique password specifically for Facebook — do not reuse passwords from other websites. "
                "If you use the same password everywhere and one website gets hacked, attackers will "
                "automatically try that same password on Facebook, your email, your bank, and more. "
                "This is called a credential stuffing attack and it is extremely common. "
                "Consider using a free password manager like Bitwarden to generate and store unique passwords. "
                "Watch: https://www.youtube.com/results?search_query=why+you+should+not+reuse+passwords"
            )

        if q["id"] == "twofa" and answer == "no":
            recommendations.append(
                "Enable Two-Factor Authentication (2FA) on your Facebook account immediately. "
                "2FA means that even if someone steals your password, they still cannot log in — "
                "because they would also need a one-time code sent to your phone. "
                "Think of it like your front door having both a lock and a bolt. "
                "To enable it: go to Settings > Accounts Center > Password and Security > Two-Factor Authentication. "
                "Watch this step-by-step tutorial: "
                "https://www.youtube.com/results?search_query=how+to+enable+2FA+on+facebook"
            )

        if q["id"] == "credential_sharing" and answer == "yes":
            recommendations.append(
                "Do not share your Facebook login credentials with anyone — not even family members or close friends. "
                "Once someone else has your password, you lose full control over your account. "
                "They could post on your behalf, read your private messages, or accidentally expose your account. "
                "If you shared access for a reason such as managing a page, use Facebook's official Page Roles feature "
                "instead, which grants access without sharing your password. "
                "Change your password now: Settings > Accounts Center > Password and Security > Change Password."
            )

        if q["id"] == "friend_request" and answer == "yes":
            recommendations.append(
                "Be cautious about accepting friend requests from people you do not know. "
                "Fake accounts are commonly used by scammers to gather personal information about you, "
                "send you phishing links, or impersonate you to your other contacts. "
                "A common trick is creating a fake profile that looks like someone you already know. "
                "Always verify through another channel before accepting. "
                "Watch: https://www.youtube.com/results?search_query=facebook+fake+account+scam+how+to+spot"
            )

        if q["id"] == "suspicious_link" and answer == "yes":
            recommendations.append(
                "Never click on suspicious or unexpected links, even if they appear to come from a friend. "
                "This is one of the most common ways people get hacked — it is called phishing. "
                "Attackers send links that look real but secretly steal your login details "
                "or install harmful software on your device. "
                "Before clicking any link, check the sender carefully and verify the URL looks legitimate. "
                "When in doubt, do not click. "
                "Watch: https://www.youtube.com/results?search_query=what+is+phishing+how+to+avoid+it"
            )

        if q["id"] == "admin_review" and answer != "periodically":
            recommendations.append(
                "Review your Facebook Group admin and moderator roles regularly — at least once every few months. "
                "People who were trusted admins in the past may have left or had their own accounts compromised. "
                "An old admin account in the wrong hands gives an attacker full control over your group. "
                "To manage roles: go to your Group > Settings > Manage Admins and Moderators "
                "and remove anyone who no longer needs access. "
                "Watch: https://www.youtube.com/results?search_query=how+to+manage+facebook+group+admin+roles"
            )

        if q["id"] == "login_monitor" and answer != "periodically":
            recommendations.append(
                "Check your Facebook login activity regularly to see if anyone else has accessed your account. "
                "Facebook shows you every device and location your account has been logged into. "
                "If you see an unfamiliar device or location, someone may have gained unauthorised access. "
                "To check: go to Settings > Accounts Center > Password and Security > Where You're Logged In "
                "and log out of any devices you do not recognise. "
                "Watch: https://www.youtube.com/results?search_query=how+to+check+facebook+login+activity"
            )

        if q["id"] == "third_party" and answer == "no":
            recommendations.append(
                "Review the third-party apps and websites connected to your Facebook account. "
                "Over time, you may have used Facebook to sign in to other apps such as games or quizzes. "
                "These apps may still have access to your profile data even if you have stopped using them — "
                "and some of them may be insecure or malicious. "
                "To review: go to Settings > Security > Apps and Websites "
                "and remove anything you no longer use or trust. "
                "Watch: https://www.youtube.com/results?search_query=how+to+remove+third+party+apps+facebook"
            )

    risk_level = "Excellent" if score >= 70 else "Fair" if score >= 50 else "Poor"

    return score, risk_level, recommendations
