import re

def password_strength(password):
    # Initialize score
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1

    # Check for digits
    if re.search(r'\d', password):
        score += 1

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    # Provide feedback based on the score
    if score <= 1:
        return "Weak password. Consider using more characters, digits, and special characters."
    elif score == 2 or score == 3:
        return "Medium password. Add more variety for improved security."
    elif score >= 4:
        return "Strong password. Your password is secure!"
    
# Test the function
password = input("Enter your password: ")
result = password_strength(password)
print(result)