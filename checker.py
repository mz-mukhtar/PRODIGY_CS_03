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
    special_characters = string.punctuation
    return any(char in special_characters for char in password)

def main():
    print("Welcome to the Password Complexity Checker!\n")
    
    password = getpass.getpass("Enter your password: ")
    
    print("\n Analyzing password...\n")
    
    score = 0
    
    if check_length(password):
        print("Length is 8+ characters")
        score += 1
    else:
        print("Too short (minimum 8 characters)")

    if check_lowercase(password):
        print("Contains lowercase letter")
        score += 1
    else:
        print("Missing lowercase letter")

    if check_uppercase(password):
        print("Contains uppercase letter")
        score += 1
    else:
        print("Missing uppercase letter")

    if check_digit(password):
        print("Contains digit")
        score += 1
    else:
        print("Missing digit")

    if check_special_char(password):
        print("Contains special character")
        score += 1
    else:
        print("Missing special character")
    
    # Summary
    print(f"\n Score: {score}/5")
    
    if score == 5:
        print(" Strength: Very Strong")
    elif score >= 3:
        print(" Strength: Moderate")
    else:
        print(" Strength: Weak")

    # Suggestions
    if score == 5:
        print("\n Your password is very strong. No suggestions needed!")
    else:
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
