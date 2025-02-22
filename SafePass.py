import random
import string 

# ========================== MASTER PASSWORD CHECK ==========================
print("==================================")
master_pwd = "secure@127"  # Predefined master password (change as needed)
input_pwd = input("Please type your master password: ")

# Check if entered password is correct
if master_pwd != input_pwd:
    print("❌ Incorrect master password! Access Denied.")
    exit()  # Exit the program if the password is incorrect

# ========================== PASSWORD VALIDATION FUNCTION ==========================
def is_valid_password(password):
    """Checks if a password contains at least one special character and one digit."""
    has_special = False  
    has_digit = False  
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~"

    for char in password:
        if char in special_chars:
            has_special = True  
        if char.isdigit():
            has_digit = True  

    if not has_special or not has_digit:
        print("❌ Password must include at least one special character and one number!")
        return False  # Return False if password is invalid
    
    return True  # Return True if password is valid

# ========================== FUNCTION TO ADD PASSWORD ==========================
def add():
    """Adds a new account with an encrypted password and saves it to a file."""
    user = input("Account name: ")

    # Prompt password guidelines
    print("🔹 Your password must be at least 8 characters long and include special symbols like @, #, $, or & for better security!")

    while True:
        pwd = input("Password: ")
        
        # Validate password before proceeding
        if is_valid_password(pwd):
            break  # Exit loop if password is valid
        print("⚠ Please enter a stronger password!")

    # Generate 5 random lowercase letters for encryption padding
    random_st = ''.join(random.choices(string.ascii_lowercase, k=5))
    random_end = ''.join(random.choices(string.ascii_lowercase, k=5))

    # Encrypt password by shuffling characters
    even_chars = pwd[::2]  # Characters at even indices (0, 2, 4,...)
    odd_chars = pwd[1::2]  # Characters at odd indices (1, 3, 5,...)
    new_pass = random_st + even_chars + odd_chars + random_end  

    # Save encrypted password to file
    with open('password.txt', 'a') as f:
        f.write(f"Name:{user} | Password:{new_pass}\n")  
    print("✅ Password saved successfully!\n")

# ========================== FUNCTION TO VIEW PASSWORDS ==========================
def view():
    """Retrieves and decrypts stored passwords from the file."""
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.strip()  # Remove trailing spaces and newline characters
                
                # Extract stored username and encrypted password
                user, pwd = data.split("|")  
                user = user.replace("Name:", "").strip()
                en_pwd = pwd.replace("Password:", "").strip()

                # Remove encryption padding (first 5 and last 5 characters)
                decrypt_pwd = en_pwd[5:-5]

                # Split the password into two halves
                half_len = (len(decrypt_pwd) + 1) // 2  
                first_half = decrypt_pwd[:half_len]  
                second_half = decrypt_pwd[half_len:]  

                # Merge the characters back into the original password
                org_pwd = ''.join(a + b for a, b in zip(first_half, second_half))

                # If the original password had an odd length, append the last character
                if len(first_half) > len(second_half):
                    org_pwd += first_half[-1]

                print(f"🔹 Name: {user} | Password: {org_pwd}")

    except FileNotFoundError:
        print("⚠ No saved passwords found! Please add some first.\n")

# ========================== MAIN LOOP ==========================
while True:
    mode = input("\nWould you like to add a new password or view stored ones? (Type 'view', 'add', or 'q' to quit): ").lower()

    if mode == "q":
        print("🔒 Password Manager Closed.")
        print("========================================")
        break  

    elif mode == "add":
        add()

    elif mode == "view":
        view()

    else:
        print("❌ Invalid option! Please enter 'add', 'view', or 'q' to quit.")
