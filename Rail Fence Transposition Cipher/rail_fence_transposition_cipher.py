import re


def cipher(text, rails_number):
    if not isinstance(rails_number, int) or rails_number <= 0:
        raise ValueError("columns_length must be a positive integer")

    text = re.sub(r'[^a-zA-Z]', '', text)  # filters letters only
    text_length = len(text)
    columns_length = text_length

    matrix = [['-'] * columns_length for row in range(rails_number)]
    matrix = insert_text_diagonatly(text, matrix, rails_number)

    ciphered_text = []
    for i in range(rails_number):
        for j in range(columns_length):
            if matrix[i][j] != '-':
                ciphered_text.append(matrix[i][j])
    result = ''.join(ciphered_text)
    return result


def decipher(text, rails_number):
    if not isinstance(rails_number, int) or rails_number <= 0:
        raise ValueError("columns_length must be a positive integer")

    text = re.sub(r'[^a-zA-Z]', '', text)  # filters letters only
    text_length = len(text)
    columns_length = text_length

    matrix = [['-'] * columns_length for row in range(rails_number)]
    ciphered_string = re.sub(r'[a-zA-Z]', '@', text)
    matrix = insert_text_diagonatly(ciphered_string, matrix, rails_number)

    count = 0
    for i in range(rails_number):
        for j in range(columns_length):
            if matrix[i][j] == '@':
                matrix[i][j] = text[count]
                count += 1

    deciphered_text = []
    descending = True
    text_chars = list(text)
    i = 0
    j = 0
    for _ in text_chars:
        if descending:
            deciphered_text.append(matrix[i][j])
            if i + 1 == rails_number:  # reached bottom
                descending = False
                i -= 1
                j += 1
            else:
                i += 1
                j += 1
        else:
            deciphered_text.append(matrix[i][j])
            if i - 1 == -1:  # reached top
                descending = True
                i += 1
                j += 1
            else:
                i -= 1
                j += 1

    result = ''.join(deciphered_text)
    return result


def insert_text_diagonatly(text, matrix, rails_number):
    descending = True
    text_chars = list(text)
    i = 0
    j = 0
    for char in text_chars:
        if descending:
            matrix[i][j] = char
            if i + 1 == rails_number:  # reached bottom
                descending = False
                i -= 1
                j += 1
            else:
                i += 1
                j += 1
        else:
            matrix[i][j] = char
            if i - 1 == -1:  # reached top
                descending = True
                i += 1
                j += 1
            else:
                i -= 1
                j += 1
    print(matrix)
    return matrix
