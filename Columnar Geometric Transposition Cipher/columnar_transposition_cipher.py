import math
import re


def cipher(text, columns_length):
    if not isinstance(columns_length, int) or columns_length <= 0:
        raise ValueError("columns_length must be a positive integer")

    text = re.sub(r'[^a-zA-Z]', '', text)  # filters letters only

    text_length = len(text)
    rows_length = math.ceil(text_length / columns_length)

    matrix = [['X'] * columns_length for row in range(rows_length)]
    count = 0
    for i in range(rows_length):
        for j in range(columns_length):
            if count < text_length:
                matrix[i][j] = text[count]
                count += 1
    print(matrix)

    ciphered_text = []
    for j in range(columns_length):
        for i in range(rows_length):
            ciphered_text.append(matrix[i][j])
    result = ''.join(ciphered_text)
    return result


def decipher(text, columns_length):
    if not isinstance(columns_length, int) or columns_length <= 0:
        raise ValueError("columns_length must be a positive integer")

    text = re.sub(r'[^a-zA-Z] ', '', text)  # filters letters and spaces only

    text_length = len(text)
    if text_length % columns_length != 0:
        raise ValueError("The text length must be divisible by columns_length")

    rows_length = int(text_length / columns_length)

    matrix = [[0] * columns_length for row in range(rows_length)]
    count = 0
    for j in range(columns_length):
        for i in range(rows_length):
            matrix[i][j] = text[count]
            count += 1
    print(matrix)

    deciphered_text = []
    for i in range(rows_length):
        for j in range(columns_length):
            deciphered_text.append(matrix[i][j])
    result = ''.join(deciphered_text)
    return result
