from columnar_transposition_cipher import cipher
from columnar_transposition_cipher import decipher

cypher_type = input("Type 0 to encrypt the text and 1 to decrypt it: ")
text = input("Enter some text: ")
columns = input("How many columns? ")

if cypher_type == "0":
    ciphered_text = cipher(text, int(columns))
    print(ciphered_text)
elif cypher_type == "1":
    deciphered_text = decipher(text, int(columns))
    print(deciphered_text)