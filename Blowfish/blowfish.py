from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import binascii
import os


def encrypt_ecb(text, key):
    """Criptografa usando modo ECB"""
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_text = pad(text, Blowfish.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext


def encrypt_cbc(text, key, iv):
    """Criptografa usando modo CBC com vetor de inicialização"""
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    padded_text = pad(text, Blowfish.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext


def decrypt_ecb(ciphertext, key):
    """Descriptografa usando modo ECB"""
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)
    return plaintext


def decrypt_cbc(ciphertext, key, iv):
    """Descriptografa usando modo CBC com vetor de inicialização"""
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)
    return plaintext


def encrypt_file(input_file, output_file, key):
    """Criptografa um arquivo usando modo ECB"""
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)

    with open(input_file, 'rb') as infile:
        data = infile.read()

    padded_data = pad(data, Blowfish.block_size)
    ciphertext = cipher.encrypt(padded_data)

    with open(output_file, 'wb') as outfile:
        outfile.write(ciphertext)

    return len(data), len(ciphertext)


def decrypt_file(input_file, output_file, key):
    """Descriptografa um arquivo usando modo ECB"""
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)

    with open(input_file, 'rb') as infile:
        ciphertext = infile.read()

    plaintext = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)

    with open(output_file, 'wb') as outfile:
        outfile.write(plaintext)


# Chave fornecida: [65, 66, 67, 68, 69] (corresponde a 'ABCDE')
key = bytes([65, 66, 67, 68, 69])

print("Resolução da Lista de Exercícios - Criptografia Blowfish\n")

# Caso 1
print("Caso 1:")
plaintext = b"FURB"
ciphertext = encrypt_ecb(plaintext, key)
hex_ciphertext = binascii.hexlify(ciphertext).decode().upper()
print(f"1.1. Texto cifrado (hex): {hex_ciphertext}")  # 7F4700AA6F5FE08B
print(f"1.2. Extensão do texto cifrado: {len(ciphertext)} bytes")  # 8 bytes
print()

# Caso 2
print("Caso 2:")
plaintext = b"COMPUTADOR"
ciphertext = encrypt_ecb(plaintext, key)
hex_ciphertext = binascii.hexlify(ciphertext).decode().upper()
print(f"2.1. Texto cifrado (hex): {hex_ciphertext}")  # F34739AB7634C4EFE50FF1B554856572
print(f"2.2. Extensão do texto cifrado: {len(ciphertext)} bytes")  # 16 bytes
print("2.3. O texto cifrado tem esse tamanho porque o algoritmo Blowfish opera em blocos de 8 bytes (64 bits).")
print("     Como 'COMPUTADOR' tem 10 bytes, é necessário um padding para completar o segundo bloco de 8 bytes,")
print("     resultando em um texto cifrado de 16 bytes (2 blocos).")
print()

# Caso 3
print("Caso 3:")
plaintext = b"SABONETE"
ciphertext = encrypt_ecb(plaintext, key)
hex_ciphertext = binascii.hexlify(ciphertext).decode().upper()
print(f"3.1. Texto cifrado (hex): {hex_ciphertext}")  # 841091472604B96ACDBC3E2FEFA73BDD
print(f"3.2. Extensão do texto cifrado: {len(ciphertext)} bytes")  # 16 bytes
print("3.3. O texto cifrado tem esse tamanho porque 'SABONETE' tem 8 bytes, exatamente o tamanho de um bloco.")
print("     Porém, devido ao padding PKCS#5, é adicionado um bloco completo de padding,")
print("     resultando em 16 bytes de texto cifrado (2 blocos).")
print()

# Caso 4
print("Caso 4:")
plaintext = bytes([8, 8, 8, 8, 8, 8, 8, 8])
ciphertext = encrypt_ecb(plaintext, key)
hex_ciphertext = binascii.hexlify(ciphertext).decode().upper()
print(f"4.1. Texto cifrado (hex): {hex_ciphertext}")  # CDBC3E2FEFA73BDDCDBC3E2FEFA73BDD
print("4.2. Comparando os primeiros 8 bytes do texto cifrado com o último bloco cifrado da questão anterior:")
print("     O último bloco da questão 3 contém o padding, que para uma mensagem que termina em um limite de bloco")
print(
    "     consiste em um bloco inteiro com o valor 08. Isso corresponde exatamente à nossa sequência [8,8,8,8,8,8,8,8].")
print("     A conclusão é que os padrões de padding são previsíveis e identificáveis no modo ECB.")
print()

# Caso 5
print("Caso 5:")
plaintext = b"SABONETESABONETESABONETE"
ciphertext = encrypt_ecb(plaintext, key)
hex_ciphertext = binascii.hexlify(ciphertext).decode().upper()
print(f"5.1. Texto cifrado (hex): {hex_ciphertext}")  # 841091472604B96A841091472604B96A841091472604B96ACDBC3E2FEFA73BDD
print(f"5.2. Extensão do texto cifrado: {len(ciphertext)} bytes")  # 32 bytes
print(
    "5.3. Analisando o texto cifrado e o texto simples, podemos observar que o texto 'SABONETE' se repete três vezes.")
print("     No modo ECB, blocos idênticos de texto plano produzem blocos idênticos de texto cifrado.")
print("     Isso revela um padrão que pode ser explorado por atacantes, demonstrando uma fraqueza do modo ECB.")
print()

# Caso 6
print("Caso 6:")
plaintext = b"FURB"
# No modo CBC sem especificar IV, um IV de zeros é usado por padrão
iv = bytes([0] * 8)  # IV de zeros com 8 bytes
ciphertext = encrypt_cbc(plaintext, key, iv)
hex_ciphertext = binascii.hexlify(ciphertext).decode().upper()
print(f"6.1. Texto cifrado (hex): {hex_ciphertext}")  # 7F4700AA6F5FE08B
print("6.2. Ao decifrar o texto cifrado com o mesmo IV, conseguimos recuperar o texto original.")
try:
    decrypted = decrypt_cbc(ciphertext, key, iv)
    print(f"     Texto decifrado: {decrypted.decode()}")  # FURB
except Exception as e:
    print(f"     Erro ao decifrar: {e}")
print()

# Caso 7
print("Caso 7:")
plaintext = b"FURB"
iv = bytes([1, 1, 2, 2, 3, 3, 4, 4])
ciphertext = encrypt_cbc(plaintext, key, iv)
hex_ciphertext = binascii.hexlify(ciphertext).decode().upper()
print(f"7.1. Texto cifrado (hex): {hex_ciphertext}")  # CF0A75A354FB624C
print()

# Caso 8
print("Caso 8:")
plaintext = b"SABONETESABONETESABONETE"
iv = bytes([1, 1, 2, 2, 3, 3, 4, 4])
ciphertext = encrypt_cbc(plaintext, key, iv)
hex_ciphertext = binascii.hexlify(ciphertext).decode().upper()
print(f"8.1. Texto cifrado (hex): {hex_ciphertext}")  # 9B1813DACAF2D6509D10C55C33F36B0918D49BF6CD0C1241E1AB6D1D3119EAB6
print("8.2. Comparando com o caso 5 (modo ECB):")
print("     No modo ECB, padrões no texto original são visíveis no texto cifrado.")
print("     No modo CBC, mesmo com texto repetitivo, o texto cifrado não revela esses padrões")
print("     devido ao encadeamento de blocos e uso do IV, oferecendo maior segurança.")
print()

# Caso 9
print("Caso 9:")
plaintext = b"SABONETESABONETESABONETE"
iv_caso9 = bytes([10, 20, 30, 40, 50, 60, 70, 80])
ciphertext_caso9 = encrypt_cbc(plaintext, key, iv_caso9)
hex_ciphertext_caso9 = binascii.hexlify(ciphertext_caso9).decode().upper()
print(
    f"9.1. Texto cifrado (hex): {hex_ciphertext_caso9}")  # 10981FE3009F1FE0AB7592179C361CC7AF8EB390B79EBC8ED6A1F71D43E1C0C4
print("9.2. Comparando com o caso 8:")
print("     Mesmo com o mesmo texto e chave, o texto cifrado é completamente diferente")
print("     porque o IV foi alterado. Isso demonstra como o IV influencia todo o resultado do processo de cifragem.")
print("9.3. Ao tentar descriptografar com um IV diferente do usado na cifragem:")
iv_caso8 = bytes([1, 1, 2, 2, 3, 3, 4, 4])
try:
    decrypted = decrypt_cbc(ciphertext_caso9, key, iv_caso8)
    print(f"     Resultado: A descriptografia falha ou produz texto ininteligível")
except Exception as e:
    print(f"     Erro ao decifrar: {e}")
print("     Conclusão: O IV é essencial para a descriptografia correta no modo CBC.")
print("     Usar um IV incorreto resulta em falha ou texto incompreensível.")
print()

# Caso 10
print("Caso 10:")
plaintext = b"FURB"
ciphertext = encrypt_ecb(plaintext, key)
chave_errada = b"11111"
print("10.1. Tentando decifrar o texto cifrado com uma chave diferente:")
try:
    decrypted = decrypt_ecb(ciphertext, chave_errada)
    print(f"     Resultado: {decrypted}")
except Exception as e:
    print(f"     Erro: {e}")
print("     Explicação: Ao usar uma chave diferente da original na descriptografia,")
print("     o resultado é um texto incompreensível ou ocorre um erro durante o processo.")
print("     Isso demonstra a importância da chave no processo criptográfico.")
print()


def processar_arquivo_pdf():
    """Criptografa e descriptografa o arquivo PDF da lista de exercícios"""
    # Chave 'ABCDE'
    key = b"ABCDE"

    input_file = "file.pdf"
    encrypted_file = "saida.bin"
    decrypted_file = "descriptografado.pdf"

    # Caso 11: Criptografar o arquivo PDF
    print("Caso 11:")
    try:
        original_size, encrypted_size = encrypt_file(input_file, encrypted_file, key)
        print(f"11.1. Tamanho do arquivo original: {original_size} bytes")
        print(f"      Tamanho do arquivo cifrado: {encrypted_size} bytes")
    except FileNotFoundError:
        print(f"Arquivo {input_file} não encontrado. Verifique se o arquivo está no diretório correto.")
    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")
    print()

    # Caso 12: Descriptografar o arquivo
    print("Caso 12:")
    try:
        if os.path.exists(encrypted_file):
            decrypt_file(encrypted_file, decrypted_file, key)
            print(f"Arquivo descriptografado com sucesso!")
        else:
            print(f"Arquivo {encrypted_file} não encontrado. Execute o caso 11 primeiro.")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")


print("\nProcessando o arquivo PDF...\n")
processar_arquivo_pdf()
