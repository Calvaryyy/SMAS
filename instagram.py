# instagram.py

def get_account_types():
    return {
        "personal": "Personal",
        "creator": "Creator",
        "business": "Business"
    }


def get_instagram_questions(account_type):

    if account_type == "personal":
        return [
            {
                "id": "password_length",
                "question": "Is your password longer than 8 characters",
                "options": {"yes": 25, "no": 0}
            },
            {
                "id": "password_unique",
                "question": "Is your Instagram password unique",
                "options": {"yes": 25, "no": 0}
            },
            {
                "id": "twofa",
                "question": "Do you use 2FA/MFA",
                "options": {"yes": 25, "no": 0}
            },
            {
                "id": "credential_sharing",
                "question": "Does anyone else know your Instagram login credentials",
                "options": {"no": 25, "yes": 0}
            }
        ]

    else:  # creator or business
        return [
            {
                "id": "password_length",
                "question": "Is your password longer than 8 characters",
                "options": {"yes": 20, "no": 0}
            },
            {
                "id": "password_unique",
                "question": "Is your Instagram password unique",
                "options": {"yes": 20, "no": 0}
            },
            {
                "id": "twofa",
                "question": "Do you use 2FA/MFA",
                "options": {"yes": 20, "no": 0}
            },
            {
                "id": "credential_sharing",
                "question": "Does anyone else know your Instagram login credentials",
                "options": {"no": 20, "yes": 0}
            },
            {
                "id": "login_monitor",
                "question": "How often do you monitor login activity",
                "options": {"periodically": 20, "rarely": 15, "never": 0}
            },
            {
                "id": "third_party",
                "question": "Do you monitor connected third party apps",
                "options": {"not applicable": 20, "yes": 20, "no": 0}
            }
        ]


def run_instagram(account_type, answers):

    score = 0
    recommendations = []

    questions = get_instagram_questions(account_type)

    for q in questions:
        answer = answers.get(q["id"])
        score += q["options"].get(answer, 0)

        if q["id"] == "password_length" and answer == "no":
            recommendations.append(
                "Your Instagram password should be longer than 8 characters. "
                "Short passwords are easy targets — automated hacking tools can guess millions of "
                "combinations per second, meaning a short password could be cracked in minutes. "
                "Aim for at least 12 characters using a mix of uppercase letters, lowercase letters, "
                "numbers, and special characters like ! or @. "
                "A trick is to think of a sentence and use the first letter of each word, "
                "for example: 'I love Lagos in the morning 2024!' becomes 'IlLitm2024!'. "
                "Watch: https://www.youtube.com/results?search_query=how+to+create+a+strong+password"
            )

        if q["id"] == "password_unique" and answer == "no":
            recommendations.append(
                "You must use a unique password for Instagram — different from every other account you have. "
                "Reusing passwords is one of the biggest security mistakes people make. "
                "If any other app or website you use gets breached, hackers will immediately test "
                "that same password on Instagram, your email, and other platforms. "
                "This attack is so common it has a name: credential stuffing. "
                "Use a free password manager like Bitwarden or Google Password Manager "
                "to create and remember strong unique passwords for every account. "
                "Watch: https://www.youtube.com/results?search_query=best+free+password+manager+2024"
            )

        if q["id"] == "twofa" and answer == "no":
            if account_type == "personal":
                recommendations.append(
                    "Turn on Two-Factor Authentication (2FA) for your Instagram account. "
                    "2FA adds a second step when you log in — after entering your password, "
                    "Instagram will send a code to your phone that you also need to enter. "
                    "This means that even if a hacker has your password, they still cannot get in "
                    "without also having your phone. It takes less than 2 minutes to set up "
                    "and is one of the most effective security measures available. "
                    "To enable: go to Profile > Settings > Accounts Center > Password and Security > Two-Factor Authentication. "
                    "Watch: https://www.youtube.com/results?search_query=how+to+enable+2FA+on+instagram"
                )
            else:
                recommendations.append(
                    "Enable Two-Factor Authentication (2FA) on your Instagram account right away. "
                    "As a creator or business, your account is a high-value target — it represents your brand, "
                    "your audience, and potentially your income. A compromised account can result in "
                    "lost followers, damaged reputation, and financial harm. "
                    "2FA ensures that even if your password is stolen, nobody can log in without "
                    "a second code sent to your phone. "
                    "To enable: go to Profile > Settings > Accounts Center > Password and Security > Two-Factor Authentication. "
                    "Watch: https://www.youtube.com/results?search_query=how+to+enable+2FA+on+instagram+business"
                )

        if q["id"] == "credential_sharing" and answer == "yes":
            if account_type == "personal":
                recommendations.append(
                    "Do not share your Instagram login credentials with anyone. "
                    "Once someone else knows your password, you have no guarantee of your account's security. "
                    "Even a trusted person could accidentally expose your details, use a compromised device, "
                    "or — in worst cases — misuse access to your account. "
                    "Change your password immediately: go to Profile > Settings > Security > Password. "
                    "Watch: https://www.youtube.com/results?search_query=how+to+change+instagram+password"
                )
            else:
                recommendations.append(
                    "Do not share your Instagram login credentials with team members or managers. "
                    "Instead, use Instagram's official tools for collaboration: "
                    "Creator accounts can add team members through Meta Business Suite, "
                    "and Business accounts can assign partner access through the Business Manager. "
                    "This gives others the access they need without exposing your password. "
                    "Change your password now and revoke shared access: "
                    "go to Profile > Settings > Security > Password. "
                    "Watch: https://www.youtube.com/results?search_query=instagram+business+manager+add+team+member"
                )

        if q["id"] == "login_monitor" and answer != "periodically":
            recommendations.append(
                "You should regularly check where your Instagram account is currently logged in. "
                "Instagram allows you to see every device and location that has an active session on your account. "
                "If you spot a device or location you do not recognise, it could mean your account has been accessed "
                "without your permission — and you can immediately log that session out remotely. "
                "To check: go to Profile > Settings > Security > Login Activity. "
                "Make this a habit at least once a month. "
                "Watch: https://www.youtube.com/results?search_query=how+to+check+instagram+login+activity"
            )

        if q["id"] == "third_party" and answer == "no":
            recommendations.append(
                "Check which third-party apps have access to your Instagram account. "
                "You may have connected your Instagram to scheduling tools, analytics platforms, "
                "contests, or other apps over time. Some of these may no longer be maintained "
                "or may have been sold to unknown parties — and they could still be reading "
                "or posting to your account without your knowledge. "
                "To review and remove: go to Profile > Settings > Security > Apps and Websites. "
                "Remove any app you no longer actively use. "
                "Watch: https://www.youtube.com/results?search_query=how+to+remove+third+party+apps+instagram"
            )

    risk_level = "Excellent" if score >= 70 else "Fair" if score >= 50 else "Poor"

    return score, risk_level, recommendations
