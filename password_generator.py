# password_generator.py
# Dependency: pip install xkcdpass
# Source: https://github.com/redacted/XKCD-password-generator

import random
import string
from xkcdpass import xkcd_password as xp


def generate_passphrase(num_words: int = 5, delimiter: str = "-") -> dict:
    """
    Generates a strong, memorable passphrase using EFF's long wordlist
    via the xkcdpass library.

    The passphrase is structured as:
        Word-Word-Word-Word-Word-Number-Symbol
    for a balance of memorability and strength.

    Args:
        num_words: Number of words in the passphrase (default: 5)
        delimiter:  Separator between words (default: "-")

    Returns a dict with:
        - passphrase: the generated passphrase string
        - word_count: number of words used
        - estimated_strength: a human-readable entropy note
    """
    # Load the EFF long wordlist (built into xkcdpass)
    wordfile = xp.locate_wordfile()
    words = xp.generate_wordlist(
        wordfile=wordfile,
        min_length=4,
        max_length=8
    )

    # Generate the base passphrase
    base = xp.generate_xkcdpassword(words, numwords=num_words, delimiter=delimiter)

    # Append a random 2-digit number and a symbol for extra entropy
    number = str(random.randint(10, 99))
    symbol = random.choice("!@#$%&*")

    passphrase = f"{base}{delimiter}{number}{symbol}"

    # Entropy note based on word count
    # EFF long wordlist has 7776 words → log2(7776) ≈ 12.9 bits per word
    bits_per_word = 12.9
    total_bits = round(bits_per_word * num_words + 10, 1)  # +10 for number+symbol
    strength_note = f"~{total_bits} bits of entropy"

    return {
        "passphrase": passphrase,
        "word_count": num_words,
        "estimated_strength": strength_note
    }
