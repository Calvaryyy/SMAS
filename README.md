# SMAS — Social Media Account Security Monitoring System

> Developed by Zoe Michael Katchy during SIWES industrial training at Octagon Cybersecurity Nig. Ltd.  
> 

---

## What is SMAS?

Small and micro businesses in Nigeria run on social media. WhatsApp Business handles customer orders. Instagram and Facebook Pages are storefronts. For many business owners, these accounts *are* the business — they represent years of followers, reviews, relationships, and revenue.

Yet most of these accounts are protected by a single weak password, no two-factor authentication, and login credentials shared with staff members who may no longer work there.

**SMAS** (Social Media Account Security Monitoring System) is a web-based security assessment tool that evaluates the security posture of social media accounts across Facebook, Instagram, and WhatsApp. It asks the right questions, scores the account against a risk model, identifies the specific vulnerabilities present, and delivers plain-language recommendations that a non-technical business owner can actually act on.

It was built to give security professionals a structured, repeatable framework for conducting social media security audits — and to give business owners a clear, honest picture of how exposed they really are.

---

## Why does this matter?

Account takeovers are one of the most damaging and underreported cyber threats facing small businesses in Nigeria. The attack surface is wide:

- **SIM-swap attacks** — an attacker bribes or social-engineers a telco agent into transferring your phone number to their SIM. Every SMS-based 2FA code, every WhatsApp account, every recovery message now goes to them.
- **Credential stuffing** — passwords reused from other sites get tested against Instagram and Facebook automatically after data breaches. If your password appeared in any previous breach, it will be tried.
- **Phishing** — fake login pages, fraudulent "account suspension" warnings, and malicious links sent through DMs are specifically designed to harvest social media credentials.
- **Insider access** — shared passwords and unrevoked staff access mean a former employee, or someone who briefly borrowed a phone, may still have full access to the account.
- **Third-party app abuse** — apps connected via "Login with Facebook" may still hold active access tokens long after you stopped using them.

When a business account is compromised, the damage is immediate: customers get scammed using the business's identity, the account gets locked or deleted, posts get wiped, and the trust built over years disappears overnight. For micro businesses with no IT department and no fallback, recovery is often impossible.

SMAS exists to catch these vulnerabilities before an attacker does.

---

## What SMAS does

### Account Security Assessment
SMAS walks through a structured set of platform-specific security questions covering:

- Authentication strength (password vs passkey, length, uniqueness)
- Two-factor / multi-factor authentication status
- Credential sharing and access control hygiene
- Session and linked device monitoring
- Admin role review practices
- Third-party app exposure
- Phishing and social engineering awareness

Each answer is scored against a weighted risk model. The account receives a score out of 100 and a risk classification:

| Score | Risk Level |
|---|---|
| 70 – 100 | ✅ Excellent |
| 50 – 69 | ⚠️ Fair |
| 0 – 49 | 🚨 Poor |

Every failing answer generates a specific, actionable recommendation — not generic advice, but a precise explanation of the threat, why it matters in plain terms, and the exact steps to fix it, including direct links to platform settings and video guides.

### Multi-Account Report
Multiple accounts across different platforms can be queued in a single session. A consolidated, printable security report is generated covering all accounts — with risk gauges, per-account scores, and a full recommendations breakdown. The report is designed to be handed directly to a business owner or included in a professional security engagement.

### Password Security Tools
Three standalone tools are built into the same interface:

**① Password Strength Checker**  
Uses the [zxcvbn](https://github.com/dwolfhub/zxcvbn-python) algorithm (developed by Dropbox) to evaluate password strength the way an attacker would — not just checking for capital letters and symbols, but detecting dictionary words, name patterns, keyboard sequences, and common substitutions. Returns a score, an estimated crack time, and specific improvement suggestions.

**② Passphrase Generator**  
Generates strong, memorable passphrases from the EFF's long wordlist using [xkcdpass](https://github.com/redacted/XKCD-password-generator). A passphrase like `correct-horse-battery-staple-42!` is both significantly harder to crack than a typical complex password and far easier to remember. Word count is configurable (4–8 words) and entropy is displayed.

**③ Password Breach Checker**  
Checks whether a password has already appeared in known data breaches using the [HaveIBeenPwned Pwned Passwords API](https://haveibeenpwned.com/API/v3#PwnedPasswords). Critically, the full password is **never transmitted** — only the first 5 characters of its SHA-1 hash are sent, using the k-anonymity model. If a password has appeared in breach databases, it should be considered compromised regardless of how strong it looks.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Frontend | Vanilla JS, HTML/CSS |
| Password strength | zxcvbn |
| Passphrase generation | xkcdpass (EFF long wordlist) |
| Breach checking | HaveIBeenPwned Pwned Passwords API |

---

## Installation

### Prerequisites
- Python 3.10 or higher
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Calvaryyy/SMAS.git
cd SMAS

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
```

Open your browser at `http://127.0.0.1:5000`.

> **Note:** The app runs with `debug=True` by default, which is suitable for local development and demos only. Set `debug=False` before any production deployment.

---

## Usage

1. Accept the Terms & Conditions on the landing page
2. Select a platform and account type
3. Enter the account handle and answer the security questions
4. Click **+ Add to Report** to queue the assessment
5. Repeat for additional accounts if needed
6. Click **Generate Full Report** to open a printable, PDF-ready report in a new tab

### CLI Mode

A command-line interface is also available:

```bash
python main.py
```

---

## Project Structure

```
SMAS/
├── app.py                  # Flask application and API routes
├── main.py                 # CLI interface
├── facebook.py             # Facebook questions, scoring, recommendations
├── instagram.py            # Instagram questions, scoring, recommendations
├── whatsapp.py             # WhatsApp questions, scoring, recommendations
├── password_strength.py    # zxcvbn-based strength checker
├── password_generator.py   # xkcdpass-based passphrase generator
├── password_breach.py      # HaveIBeenPwned k-anonymity breach checker
├── requirements.txt
└── templates/
    ├── index.html          # Main assessment UI
    └── report.html         # Printable security report
```

---

## Privacy & Security

- **No data is stored.** The tool does not collect, log, or transmit any account credentials or personal information.
- **Breach checker uses k-anonymity.** Only the first 5 characters of a SHA-1 hash are sent to the HaveIBeenPwned API. The full password never leaves the device.
- **Assessment data is session-only.** Report data lives in browser `sessionStorage` and is cleared when the tab closes.
- **No platform credentials are required.** All assessments are conducted through self-reported questionnaires — the tool never requests or handles login credentials for any social media platform.

---

## License

Copyright © 2025 Octagon Cybersecurity Nig. Ltd.  
Developed by Zoe Michael Katchy during SIWES industrial training.  
Licensed under the [MIT License](LICENSE).
