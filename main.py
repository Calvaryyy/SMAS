from facebook import get_facebook_questions, run_facebook
from instagram import get_instagram_questions, run_instagram
from whatsapp import get_whatsapp_questions, run_whatsapp


PLATFORM_ACCOUNT_TYPES = {
    "facebook": {
        "personal": "Personal Account",
        "business": "Business Page",
        "group": "Facebook Group"
    },
    "instagram": {
        "personal": "Personal",
        "creator": "Creator",
        "business": "Business"
    },
    "whatsapp": {
        "messenger": "WhatsApp Messenger",
        "business": "WhatsApp Business"
    }
}


def get_user_consent():
    print("SMAS Terms and Conditions\n")
    print("By continuing, you confirm that:")
    print("1. You are the owner of the account being assessed.")
    print("2. You accept all liabilities resulting from use of this tool.")
    print("3. The developers are not responsible for misuse of this tool.\n")

    while True:
        consent = input("Do you agree to these terms? (yes/no): ").strip().lower()
        if consent == "yes":
            return True
        elif consent == "no":
            print("You must agree to continue.")
        else:
            print("Please answer yes or no.")


def choose_platforms():
    print("\nSelect platforms to assess (comma separated numbers):")
    print("1 - Facebook")
    print("2 - Instagram")
    print("3 - WhatsApp")

    platform_map = {
        "1": "facebook",
        "2": "instagram",
        "3": "whatsapp"
    }

    while True:
        choices = input("Enter selection: ").split(",")
        selected = []
        for c in choices:
            c = c.strip()
            if c in platform_map:
                selected.append(platform_map[c])
        if selected:
            return selected
        print("Invalid selection. Try again.")


def choose_account_type(platform):
    types = PLATFORM_ACCOUNT_TYPES[platform]
    print(f"\nAvailable account types for {platform.capitalize()}:")
    keys = list(types.keys())
    for i, key in enumerate(keys, 1):
        print(f"  {i} - {types[key]}")

    while True:
        choice = input("Enter number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(keys):
            return keys[int(choice) - 1]
        print("Invalid choice. Try again.")


def collect_answers(questions, answers_so_far=None):
    """
    Interactively prompts the user for each question, respecting conditional logic.
    Returns a dict of { question_id: answer }.
    """
    answers = answers_so_far or {}

    for q in questions:
        # Honour conditional visibility: skip if controlling answer doesn't match
        if "conditional" in q:
            controlling_answer = answers.get(q["conditional"])
            if controlling_answer != q.get("conditional_value"):
                continue

        options = list(q["options"].keys())
        print(f"\n  {q['question']}")
        for i, opt in enumerate(options, 1):
            print(f"    {i} - {opt.capitalize()}")

        while True:
            choice = input("  Enter number: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                answers[q["id"]] = options[int(choice) - 1]
                break
            print("  Invalid choice. Try again.")

    return answers


def generate_report(results):
    lines = ["SMAS SECURITY ASSESSMENT REPORT", "-" * 40]

    for result in results:
        lines.append(f"\nPlatform     : {result['platform']}")
        lines.append(f"Handle       : {result['handle']}")
        lines.append(f"Account Type : {result['account_type']}")
        lines.append(f"Score        : {result['score']} / 100")
        lines.append(f"Risk Level   : {result['risk_level']}")
        lines.append("Recommendations:")
        if result["recommendations"]:
            for r in result["recommendations"]:
                lines.append(f"  - {r}")
        else:
            lines.append("  No recommendations required.")

    return "\n".join(lines)


def save_report(report_text):
    filename = "smas_report.txt"
    with open(filename, "w") as f:
        f.write(report_text)
    print(f"\nReport saved as {filename}")


def main():
    if not get_user_consent():
        return

    platforms = choose_platforms()
    results = []

    for platform in platforms:
        print(f"\n--- {platform.capitalize()} Assessment ---")

        handle = input("Enter account handle (e.g. @username): ").strip() or "Unknown Account"

        account_type = choose_account_type(platform)

        # Fetch questions for this platform + account type
        if platform == "facebook":
            questions = get_facebook_questions(account_type)
        elif platform == "instagram":
            questions = get_instagram_questions(account_type)
        else:
            questions = get_whatsapp_questions(account_type)

        answers = collect_answers(questions)

        # Run assessment with correct signature: (account_type, answers)
        if platform == "facebook":
            score, risk_level, recommendations = run_facebook(account_type, answers)
        elif platform == "instagram":
            score, risk_level, recommendations = run_instagram(account_type, answers)
        else:
            score, risk_level, recommendations = run_whatsapp(account_type, answers)

        results.append({
            "platform": platform.capitalize(),
            "handle": handle,
            "account_type": PLATFORM_ACCOUNT_TYPES[platform][account_type],
            "score": score,
            "risk_level": risk_level,
            "recommendations": recommendations
        })

    report_text = generate_report(results)
    print("\nAssessment Complete.\n")
    print(report_text)

    download = input("\nWould you like to save the report? (yes/no): ").strip().lower()
    if download == "yes":
        save_report(report_text)


if __name__ == "__main__":
    main()
