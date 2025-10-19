from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("encryption_key.key", "rb").read()

def encrypt_text(plain_text, key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(plain_text.encode())
    return cipher_text

def decrypt_text(cipher_text, key):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    return plain_text

def main():
    # Step 4: Generate a random encryption key
    generate_key()

    # Step 8: Test encryption and decryption modules
    key = load_key()

    # Encryption
    plain_text = "Hello, this is a test message for encryption."
    encrypted_text = encrypt_text(plain_text, key)
    print(f"Original Text: {plain_text}")
    print(f"Encrypted Text: {encrypted_text}")

    # Decryption
    decrypted_text = decrypt_text(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
