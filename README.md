# Password Strength Checker

## Overview
The **Password Strength Checker** is a Python-based application that evaluates the strength of a given password and provides suggestions for improvement. It also includes a feature to generate strong random passwords.

The program uses the `zxcvbn` library for strength analysis and a GUI built with Tkinter for ease of use.

## Features
- **Password Strength Evaluation:** Analyzes passwords based on length, character diversity, entropy, and `zxcvbn` score.
- **Improvement Suggestions:** Provides recommendations to enhance password security.
- **Password Generation:** Generates secure random passwords of a specified length.
- **GUI Interface:** A simple and intuitive Tkinter-based graphical user interface.

## Installation
To run this project, ensure you have Python installed and then install the required dependencies:

```bash
pip install tkinter zxcvbn
```

## Usage
Run the script to launch the GUI:

```bash
python password_strength_checker.py
```

### GUI Instructions
1. **Check Password Strength:**
   - Enter a password in the input field.
   - Click the "Check Strength" button to receive feedback on its security.

2. **Generate a Secure Password:**
   - Enter a desired password length (default: 16 characters).
   - Click the "Generate Password" button to create a secure password.

## How It Works
1. The script evaluates passwords based on:
   - Length (minimum recommended: 16 characters)
   - Presence of uppercase letters, lowercase letters, numbers, and special characters
   - Entropy calculation
   - `zxcvbn` score (ranging from 0 to 4)
   
2. It provides a strength rating: `Very Weak`, `Weak`, `Moderate`, `Strong`, or `Very Strong`.
3. If a password is weak, the program suggests improvements.

## Example Output
```
Password Strength: Strong

Criteria met:
Length: ✔
Uppercase: ✔
Lowercase: ✔
Digit: ✔
Special: ✘
Zxcvbn Score: 3
Entropy: 120

Suggestions for Improvement:
Include at least one special character.
```

## Contributing
Feel free to fork the repository and submit pull requests for enhancements or bug fixes.

## License
This project is open-source and available under the MIT License.

---

### Author
Developed by [Akashhorambe]

