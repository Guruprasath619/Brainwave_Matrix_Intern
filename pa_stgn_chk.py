def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    score = 0
    unmet_criteria = []

    if length >= 8:
        score += 1
    else:
        unmet_criteria.append("at least 8 characters long")

    if has_upper:
        score += 1
    else:
        unmet_criteria.append("at least one uppercase letter")

    if has_lower:
        score += 1
    else:
        unmet_criteria.append("at least one lowercase letter")

    if has_digit:
        score += 1
    else:
        unmet_criteria.append("at least one digit")

    if has_special:
        score += 1
    else:
        unmet_criteria.append("at least one special character")

    if score == 0:
        strength = "Weak"
        color = "red"
        feedback = "Your password is extremely weak. Consider using a mix of uppercase letters, lowercase letters, digits, and special characters."
    elif score <= 3:
        strength = "Medium"
        color = "yellow"
        feedback = "Your password is medium strength. Try to include more character types and increase its length for better security."
    else:
        strength = "Strong"
        color = "green"
        feedback = "Your password is strong! Great job! Consider making it even longer for added security."

    return strength, score, color, unmet_criteria, feedback

# Example usage
password = input("Enter your password: ")
strength, score, color, feedback_criteria, feedback_message = check_password_strength(password)

print(f"Password strength: {strength} ({score}/5)")
print(f"Color: {color}")
if feedback_criteria:
    print("Unmet criteria:", ", ".join(feedback_criteria))
print("Feedback:", feedback_message)
