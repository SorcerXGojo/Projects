import re

# Function to check password length
def check_password_length(password):
    password_length = len(password)
    if password_length < 6:
        return "Very Weak"
    elif 6 <= password_length < 8:
        return "Weak"
    elif 8 <= password_length <= 12:
        return "Medium"
    elif 13 <= password_length <= 16:
        return "Strong"
    else:
        return "Very Strong"

# Function to analyze password complexity
def analyze_complexity(password):
    special_chars = r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]"
    complexity = {
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "numbers": bool(re.search(r'[0-9]', password)),
        "special": bool(re.search(special_chars, password))
    }
    return complexity

# Function to detect common patterns
def detect_common_patterns(filename, password):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip() == password:
                    return True
            return False
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Function to detect repeated or sequential characters
def detect_weak_patterns(password):
    # Check for repeated characters
    if re.search(r'(.)\1{2,}', password):  # 3 or more repeated characters
        return True
    # Check for sequential characters (e.g., "12345", "abcdef")
    if re.search(r'(abc|123|xyz|234|345|456|567|678|789|890)', password.lower()):
        return True
    return False

# Main function
if __name__ == "__main__":
    password_input = input("Enter Your Password To Check Strength: ")
    filename = "common_pass.txt"
    
    # Check password length
    strength = check_password_length(password_input)
    print(f"Password Strength: {strength}")
    
    # Analyze complexity
    complexity = analyze_complexity(password_input)
    print("Feedback:")
    if all(complexity.values()):
        print("- Contains uppercase, lowercase, numbers, and special characters.")
    else:
        if not complexity["uppercase"]:
            print("- Password does not contain any uppercase letters.")
        if not complexity["lowercase"]:
            print("- Password does not contain any lowercase letters.")
        if not complexity["numbers"]:
            print("- Password does not contain any numbers.")
        if not complexity["special"]:
            print("- Password does not contain any special characters.")
    
    # Detect common passwords
    if detect_common_patterns(filename, password_input):
        print("- Password is too common.")
    else:
        print("- Password is not a common password.")
    
    # Detect weak patterns
    if detect_weak_patterns(password_input):
        print("- Password contains repeated or sequential characters.")
    else:
        print("- No weak patterns detected.")