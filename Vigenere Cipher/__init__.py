from vigenere_cipher import cipher, decipher

cypher_type = input("Type 0 to encrypt the text and 1 to decrypt it: ")
text = input("Enter some text: ").upper()
key = input("What's the key? ").upper()

if cypher_type == "0":
    ciphered_text = cipher(text, key)
    print("Encrypted:", ciphered_text)
elif cypher_type == "1":
    deciphered_text = decipher(text, key)
    print("Decrypted:", deciphered_text)
else:
    print("Invalid option.")
