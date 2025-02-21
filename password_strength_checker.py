import re
import string
import random
import tkinter as tk
from tkinter import messagebox
from zxcvbn import zxcvbn

def entropy(password):
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)
    if charset_size == 0:
        return 0
    return len(password) * (charset_size.bit_length())

def suggest_improvements(password):
    suggestions = []
    if len(password) < 16:
        suggestions.append("Increase password length to at least 16 characters.")
    if not re.search(r'[A-Z]', password):
        suggestions.append("Include at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        suggestions.append("Include at least one lowercase letter.")
    if not re.search(r'\d', password):
        suggestions.append("Include at least one numeric digit.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Include at least one special character.")
    return suggestions if suggestions else ["Your password is very strong! No changes needed."]

def generate_password_report(password):
    strength, criteria = check_password_strength(password)
    suggestions = suggest_improvements(password)
    report = f"Password Strength: {strength}\n"
    report += "\nCriteria met:\n"
    for key, value in criteria.items():
        report += f"{key.capitalize()}: {'✔' if isinstance(value, bool) and value else value}\n"
    report += "\nSuggestions for Improvement:\n"
    report += "\n".join(suggestions)
    return report

def generate_random_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    strength_criteria = {
        'length': len(password) >= 16,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        'zxcvbn_score': zxcvbn(password)['score'],
        'entropy': entropy(password) >= 100
    }
    
    strength_score = sum(1 for v in strength_criteria.values() if isinstance(v, bool) and v)
    zxcvbn_score = strength_criteria['zxcvbn_score']
    
    if strength_score >= 6 and zxcvbn_score == 4:
        strength = "Very Strong"
    elif strength_score >= 5:
        strength = "Strong"
    elif strength_score >= 4:
        strength = "Moderate"
    elif strength_score >= 3:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return strength, strength_criteria

def check_password_gui():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return
    report = generate_password_report(password)
    messagebox.showinfo("Password Strength Report", report)

def generate_password_gui():
    length = length_entry.get()
    try:
        length = int(length) if length else 16
        new_password = generate_random_password(length)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, new_password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

app = tk.Tk()
app.title("Password Strength Checker")

tk.Label(app, text="Enter Password:").grid(row=0, column=0, padx=5, pady=5)
password_entry = tk.Entry(app, width=30)
password_entry.grid(row=0, column=1, padx=5, pady=5)

check_button = tk.Button(app, text="Check Strength", command=check_password_gui)
check_button.grid(row=0, column=2, padx=5, pady=5)

tk.Label(app, text="Generate Password Length:").grid(row=1, column=0, padx=5, pady=5)
length_entry = tk.Entry(app, width=5)
length_entry.grid(row=1, column=1, padx=5, pady=5)

generate_button = tk.Button(app, text="Generate Password", command=generate_password_gui)
generate_button.grid(row=1, column=2, padx=5, pady=5)

app.mainloop()
