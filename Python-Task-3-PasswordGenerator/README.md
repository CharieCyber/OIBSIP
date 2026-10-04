# Random Password Generator

A Python tool that generates strong, random passwords based on user-defined criteria. Available as both a command-line version and a secure GUI version with clipboard copy and history tracking.

## Features

### Beginner (CLI)

- Prompts for desired password length (minimum 8 characters enforced)
- Lets user choose which character types to include: uppercase, lowercase, numbers, symbols
- Requires at least 2 character types to be selected
- Generates a random password matching the selected criteria
- Option to generate another password without restarting the program

### Advanced (GUI)

- Graphical interface with a length spinbox and checkboxes for character type selection
- Uses Python's `secrets` module for cryptographically secure password generation
- Guarantees at least one character from each selected type appears in the password
- Option to exclude ambiguous characters (0, O, l, 1)
- Password strength indicator (Weak / Medium / Strong) based on length and character diversity
- One-click "Copy to Clipboard" button
- Displays the last 5 generated passwords in a session history list

## Requirements

- Python 3.x
- tkinter (comes built-in with Python — no install needed)

## How to Run

1. Make sure Python is installed on your system
2. Run either version from your terminal:

```console
python password_generator.py        # Beginner CLI version
python password_generator_gui.py    # Advanced GUI version
```

## Screenshots

**CLI version:**
![Password Generator CLI output]("C:\Users\Dell\Documents\Internship projects\password generator\Screenshots\cli_ouput.png")

**GUI version with strength indicator and history:**
![Password Generator GUI result]("C:\Users\Dell\Documents\Internship projects\password generator\Screenshots\gui_output.png")

**Ambiguous characters excluded:**
![Password Generator with ambiguous characters excluded]("C:\Users\Dell\Documents\Internship projects\password generator\Screenshots\ambiguous_excluded.png")

## Security Design Notes

**Why `secrets` instead of `random`:** Python's `random` module is designed for general-purpose randomness (like simulations or games) and is predictable if someone knows the internal algorithm's state — it should never be used for anything security-sensitive. The `secrets` module is specifically built for cryptographic purposes, like generating passwords, tokens, and API keys, making it the correct choice here.

**Why guarantee one character per selected type:** Randomly picking characters from a combined pool doesn't guarantee every selected type actually appears in the final password — especially with shorter lengths, it's possible (by pure chance) to get a password using only some of the selected types. This program explicitly picks one guaranteed character from each selected type first, then fills the rest randomly, then shuffles everything together so the guaranteed characters aren't predictably placed at the start.

**How password strength is scored:** The strength indicator considers both length and character diversity:

- **Strong:** 12+ characters and 3+ character types used
- **Medium:** 8+ characters and 2+ character types used
- **Weak:** anything below those thresholds
