# Constants for character types
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", "`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    """Checks if a word exists in a given file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_word = line.strip()
                if case_sensitive:
                    if word == line_word:
                        return True
                else:
                    if word.lower() == line_word.lower():
                        return True
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return False

def word_has_character(word, character_list):
    """Checks if the word contains any character from the provided list."""
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    """Calculates complexity (0-4) based on character types present."""
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    """Calculates strength from 0-5 based on security requirements."""
    
    # 1. Check Dictionary (Case Insensitive)
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0
    
    # 2. Check Top Passwords (Case Sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    # 3. Check Minimum Length
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    # 4. Check Strong Length
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    # 5. Calculate Complexity Strength
    complexity_score = word_complexity(password)
    strength = 1 + complexity_score
    print(f"Password complexity score is {complexity_score}.")
    return strength

def main():
    """Main input loop for the password checker."""
    print("--- Password Strength Checker ---")
    print("Enter 'q' to quit.")
    
    while True:
        user_input = input("\nEnter a password to test: ")
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        
        strength_result = password_strength(user_input)
        print(f"Overall Password Strength: {strength_result}/5")

if __name__ == "__main__":
    main()