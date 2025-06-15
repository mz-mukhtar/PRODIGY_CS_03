import getpass
import string


def check_length(password): 
	return len(password) >= 8
def check_lowercase(password):
	return any(char.islower() for char in password)

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_special_char(password):
    return any(char in string.punctuation for char in password)

def evaluate_password(password):
    score = 0
    checks = []

    if check_length(password):
        score += 1
        checks.append("Length is 8+ characters")
    else:
        checks.append("Length is too short")

    if check_lowercase(password):
        score += 1
        checks.append("Contains lowercase letter")
    else:
        checks.append("Missing lowercase letter")

    if check_uppercase(password):
        score += 1
        checks.append("Contains uppercase letter")
    else:
        checks.append("Missing uppercase letter")

    if check_digit(password):
        score += 1
        checks.append("Contains digit")
    else:
        checks.append("Missing digit")

    if check_special_char(password):
        score += 1
        checks.append("Contains special character")
    else:
        checks.append("Missing special character")


    return score, checks

def main():
    print("Welcome to the Password Complexity Checker!\n")
    password = getpass.getpass("Enter your password: ")

    print("\n Analyzing password...\n")

    score, results = evaluate_password(password)
    for r in results:
        print(r)

    print(f"\n Score: {score}/5")

    # Strength rating
    if score <= 2:
        print("Strength: Weak")
    elif score == 3:
        print("Strength: Moderate")
    else:
        print("Strength: Strong")

    # Suggestions
    print("\n Suggestions to improve:")
    if not check_length(password):
        print("- Use at least 8 characters")
    if not check_lowercase(password):
        print("- Add some lowercase letters (a–z)")
    if not check_uppercase(password):
        print("- Add uppercase letters (A–Z)")
    if not check_digit(password):
        print("- Include digits (0–9)")
    if not check_special_char(password):
        print("- Use special characters (!@#$ etc.)")

if __name__ == "__main__":
    main()
