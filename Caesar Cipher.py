def CaesarCipher(message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = message.lower()
    result = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.find(letter) 
            index = (index + shift)%(len(alphabet))
            if index < 0:
                index = index + len(alphabet)
            result = result + alphabet[index]
        else:
            result = result + letter
    return result
def CaesarCipherSolver(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = message.lower()
    for key in range(len(alphabet)):
            result = ""
            for letter in message:
                if letter in alphabet:
                    index = alphabet.find(letter) 
                    index = (index + key)%(len(alphabet))
                    if index < 0:
                        index = index + len(alphabet)
                    result = result + alphabet[index]
                else:
                    result = result + letter
            print("Shift #%s: %s" %(26-key, result))

def decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted_message += shifted_char
        else:
            decrypted_message += char
    return decrypted_message
choice = input("Press 1 to encrypt or 2 to decrypt: ")
if choice == "1":
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted = CaesarCipher(message, shift)
    print("Encrypted message:", encrypted)
elif choice == "2":
    encrypted_message = input("Enter the message to decrypt: ")
    choice1 = input("press yes if You Know key or no if you don't: ")
    if choice1 == "yes":
        shift = int(input("Enter the shift value: "))
        decrypted = decrypt(encrypted_message, shift)
        print("Decrypted message:", decrypted)
    elif choice1 == "no":
        CaesarCipherSolver(encrypted_message)
    else:
        print("Invalid choice. Please press yes if you know shift or no if you don't.")
else:
    print("Invalid choice. Please press 1 to encrypt or 2 to decrypt.")
