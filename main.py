#this is for the cription

# function for cryption
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Verifică dacă e literă
            shift = key % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char  # Lasă simbolurile și spațiile neatinse
    return encrypted_text

# Introducerea textului și a cheii
message = input("write the message you Want to encrypt: ")
key = int(input("write the number you Want tu encript.. a key...număr): "))

# Cryption
encrypted_message = encrypt(message, key)
print("Mesaj criptat:", encrypted_message)

#this is for the Decriptyon

# Function for decription
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Verifică dacă e literă
            shift = key % 26
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char  # Lasă simbolurile și spațiile neatinse
    return decrypted_text

# Introducerea textului criptat și a cheii
encrypted_message = input("write the message you Want decript: ")
key = int(input("chose the number theat the message is encripted whit): "))

# decription
decrypted_message = decrypt(encrypted_message, key)
print("mesajage Fully decripted:", decrypted_message)