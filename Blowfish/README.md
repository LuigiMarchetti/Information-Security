# Exercise List 7

In this list, we will practice using a cryptography algorithm.

We will use the "Blowfish" algorithm. This algorithm uses 64-bit block encryption. In these exercises, use the "PKCS#5" block padding scheme for all cases in this list. Also use the byte sequence [65, 66, 67, 68, 69] as the key.

Create a program for the questions below. Submit the program you built to the AVA, as well as the answers to the questions.

## Case 1
Encrypt the text "FURB" using the "ECB" operation mode.

1.1. What is the content of the ciphertext (in hexadecimal)?
1.2. What is the length (number of characters) of the ciphertext?

## Case 2
Encrypt "COMPUTADOR" and use the "ECB" operation mode.

2.1. What is the content of the ciphertext (in hexadecimal)?
2.2. What is the length of the ciphertext?
2.3. Why does the ciphertext have such a size?

## Case 3
Encrypt "SABONETE" and use the "ECB" operation mode.

3.1. What is the content of the ciphertext (in hexadecimal)?
3.2. What is the length of the ciphertext?
3.3. Why does the ciphertext have such a size?

## Case 4
Encrypt the byte sequence [8, 8, 8, 8, 8, 8, 8, 8] using the ECB operation mode.

4.1. What is the content of the ciphertext?
4.2. Compare the first 8 bytes of the ciphertext with the last encrypted block from the previous question. What conclusion can be drawn?

## Case 5
Encrypt the text "SABONETESABONETESABONETE" and use the "ECB" operation mode.

5.1. What is the content of the ciphertext (in hexadecimal)?
5.2. What is the length of the ciphertext?
5.3. Evaluate the content of the ciphertext. What conclusion can be drawn from the ciphertext and the plaintext?

## Case 6
Encrypt the text "FURB" and now use the "CBC" operation mode.

6.1. What is the content of the ciphertext (in hexadecimal)?
6.2. Try to decrypt the ciphertext to recover the plaintext. What happens?

## Case 7
Encrypt the text "FURB" using the "CBC" operation mode. Establish that the initialization vector consists of the bytes: 1, 1, 2, 2, 3, 3, 4, 4.

7.1. What is the content of the ciphertext?

## Case 8
Encrypt the text "SABONETESABONETESABONETE" and use the "CBC" operation mode. Define the initialization vector consisting of the bytes 1, 1, 2, 2, 3, 3, 4, 4.

8.1. What is the content of the ciphertext (in hexadecimal)?
8.2. Compare the ciphertext with that obtained in case 5 and present a conclusion of this comparison.

## Case 9
Encrypt the text "SABONETESABONETESABONETE" and use the "CBC" operation mode. Define the initialization vector consisting of the bytes 10, 20, 30, 40, 50, 60, 70, 80.

9.1. What is the content of the ciphertext?
9.2. Compare the ciphertext with what was obtained in case 8 and present a conclusion about the comparison.
9.3. From the result of 9.2, decrypt the message using the initialization vector consisting of the bytes 1, 1, 2, 2, 3, 3, 4, 4. What conclusion do you reach?

## Case 10
10.1. Encrypt the text "FURB" using the "ECB" operation mode. From the obtained ciphertext, try to decrypt it using the key "11111". Explain the result.

## Case 11
Using the key "ABCDE", encrypt the PDF file that was published for this exercise, saving it to disk with the name "output.bin". Use the ECB operation mode.

11.1. What is the size in bytes of the two files?

## Case 12
Decrypt the output.bin file that you generated previously. Use the key "ABCDE" and the ECB operation mode. Save the file with the name "decrypted.pdf". Try to open the file.