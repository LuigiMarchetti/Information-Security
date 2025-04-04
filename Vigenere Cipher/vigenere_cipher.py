def cipher(text, key):
    validations(key, text)

    key_size = len(key)
    chars_key = list(key)
    chars_text = list(text)

    alphabet_map = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z') + 1)}
    reverse_alphabet_map = {v: k for k, v in alphabet_map.items()}

    key_count = 0
    ciphered_text = []
    for char in chars_text:
        if char == " ":
            ciphered_text.append(" ")
            continue

        key_letter = chars_key[key_count % key_size]
        key_letter_pos = alphabet_map[key_letter]

        current_position = alphabet_map[char]
        total_position = (current_position + key_letter_pos) % 26

        ciphered_letter = reverse_alphabet_map[total_position]
        ciphered_text.append(ciphered_letter)

        key_count += 1

    return ''.join(ciphered_text)


def decipher(text, key):
    if not all(c.isupper() or c == " " for c in text):
        raise ValueError("Text must contain only uppercase letters and spaces.")
    if not key.isalpha() or not key.isupper():
        raise ValueError("Key must contain only uppercase letters.")

    key_size = len(key)
    chars_key = list(key)
    chars_text = list(text)

    alphabet_map = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z') + 1)}
    reverse_alphabet_map = {v: k for k, v in alphabet_map.items()}

    key_count = 0
    deciphered_text = []
    for char in chars_text:
        if char == " ":
            deciphered_text.append(" ")
            continue

        key_letter = chars_key[key_count % key_size]
        key_letter_pos = alphabet_map[key_letter]

        current_position = alphabet_map[char]
        total_position = (current_position - key_letter_pos + 26) % 26

        deciphered_letter = reverse_alphabet_map[total_position]
        deciphered_text.append(deciphered_letter)

        key_count += 1

    return ''.join(deciphered_text)


def validations(key, text):
    if not all(c.isupper() or c == " " for c in text):
        raise ValueError("Text must contain only uppercase letters and spaces.")
    if not key.isalpha() or not key.isupper():
        raise ValueError("Key must contain only uppercase letters.")
