# Install dependencies if not already installed:
# pip install cryptography pyperclip

import os
import json
import random
import string
import pyperclip
from cryptography.fernet import Fernet
from getpass import getpass

# ---- Step 1: Encryption key ----
KEY_FILE = "secret.key"

def generate_key(master_password):
    # derive key from master password (must be 32 bytes)
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key(master_password):
    if os.path.exists(KEY_FILE):
        return open(KEY_FILE, "rb").read()
    return generate_key(master_password)

# ---- Step 2: Password generation ----
def generate_password(length=12, use_symbols=True):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    return "".join(random.choices(chars, k=length))

# ---- Step 3: Load/save encrypted passwords ----
PASSWORD_FILE = "passwords.json"

def load_passwords(fernet):
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "rb") as f:
            encrypted_data = f.read()
            if encrypted_data:
                decrypted_data = fernet.decrypt(encrypted_data)
                return json.loads(decrypted_data)
    return {}

def save_passwords(passwords, fernet):
    data = json.dumps(passwords).encode()
    encrypted_data = fernet.encrypt(data)
    with open(PASSWORD_FILE, "wb") as f:
        f.write(encrypted_data)

# ---- Step 4: Manager functions ----
def add_password(service, fernet):
    passwords = load_passwords(fernet)
    length = int(input("Password length (default 12): ") or 12)
    use_symbols = input("Include symbols? (y/n, default y): ").lower() != "n"
    password = generate_password(length, use_symbols)
    passwords[service] = password
    save_passwords(passwords, fernet)
    pyperclip.copy(password)
    print(f"Password for '{service}' saved and copied to clipboard.")

def get_password(service, fernet):
    passwords = load_passwords(fernet)
    if service in passwords:
        pyperclip.copy(passwords[service])
        print(f"Password for '{service}' copied to clipboard.")
    else:
        print(f"No password found for '{service}'")

# ---- Step 5: Main loop with master password ----
if __name__ == "__main__":
    print("=== Secure Password Manager ===")
    master_password = getpass("Enter master password: ")
    key = load_key(master_password)
    fernet = Fernet(key)
    
    while True:
        print("\n1. Add password\n2. Get password\n3. Exit")
        choice = input("Choose option: ")
        
        if choice == "1":
            svc = input("Enter service name: ")
            add_password(svc, fernet)
        elif choice == "2":
            svc = input("Enter service name: ")
            get_password(svc, fernet)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")
