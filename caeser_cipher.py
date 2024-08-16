def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            encrypted_text += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            decrypted_text += chr((ord(char) - base - shift_amount) % 26 + base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice! Please choose 'e' for encryption or 'd' for decryption.")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print(f"Encrypted text: {encrypted_text}")
    else:
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
