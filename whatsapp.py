# whatsapp.py

def get_account_types():
    return {
        "messenger": "WhatsApp Messenger",
        "business": "WhatsApp Business"
    }


def get_whatsapp_questions(account_type):

    return [
        {
            "id": "two_step",
            "question": "Do you have 2-step verification enabled",
            "options": {"yes": 50, "no": 0}
        },
        {
            "id": "linked_devices",
            "question": "Do you periodically monitor linked devices and login activity",
            "options": {"not applicable": 25, "yes": 25, "no": 0}
        },
        {
            "id": "recovery_email",
            "question": "Do you have account recovery email set up",
            "options": {"yes": 25, "no": 0}
        }
    ]


def run_whatsapp(account_type, answers):

    score = 0
    recommendations = []

    questions = get_whatsapp_questions(account_type)

    for q in questions:
        answer = answers.get(q["id"])
        score += q["options"].get(answer, 0)

        if q["id"] == "two_step" and answer == "no":
            recommendations.append(
                "Enable 2-Step Verification on WhatsApp as soon as possible. "
                "Without it, anyone who gets hold of your SIM card or phone number — "
                "through SIM swapping, phone theft, or network exploits — "
                "can register your WhatsApp number on their own device and take over your account entirely. "
                "2-Step Verification adds a 6-digit PIN that is required whenever your number is "
                "registered on any device, making it nearly impossible for someone to hijack your account. "
                "To enable: open WhatsApp > Settings > Account > Two-Step Verification > Enable. "
                "Watch this guide: "
                "https://www.youtube.com/results?search_query=how+to+enable+whatsapp+two+step+verification"
            )

        if q["id"] == "linked_devices" and answer == "no":
            recommendations.append(
                "Regularly check the devices linked to your WhatsApp account. "
                "WhatsApp allows you to use your account on up to 4 additional devices "
                "(such as a tablet, laptop, or another phone) at the same time. "
                "If someone gained brief access to your unlocked phone in the past, "
                "they could have silently linked their own device — and they would still be able "
                "to read all your messages even after you got your phone back. "
                "To review: open WhatsApp > Settings > Linked Devices, "
                "and tap on any device you do not recognise to log it out. "
                "Do this check at least once a month. "
                "Watch: https://www.youtube.com/results?search_query=whatsapp+linked+devices+how+to+check+and+remove"
            )

        if q["id"] == "recovery_email" and answer == "no":
            recommendations.append(
                "Add a recovery email address to your WhatsApp account. "
                "If you ever forget your 2-Step Verification PIN, WhatsApp can send a reset link "
                "to your email — but only if you have one saved. "
                "Without a recovery email, forgetting your PIN could lock you out of your own account "
                "permanently, with no way to recover it. "
                "To add one: open WhatsApp > Settings > Account > Two-Step Verification > Add Email Address. "
                "Make sure the email you use is one you actively check and is also secured with a strong password and 2FA. "
                "Watch: https://www.youtube.com/results?search_query=whatsapp+two+step+verification+recovery+email"
            )

    risk_level = "Excellent" if score >= 70 else "Fair" if score >= 50 else "Poor"

    return score, risk_level, recommendations
