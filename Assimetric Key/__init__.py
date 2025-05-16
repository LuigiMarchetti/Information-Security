from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def create_and_save_keys():
    # Gera um par de chaves RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open("private_key.pem", "wb") as f:
        f.write(pem_private_key)
    
    # Retorna a chave pública em formato PEM
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1,
    )
    with open("public_key.pem", "wb") as f:
        f.write(public_pem)

#create_and_save_keys()

def create_and_save_message():
    message = b"Hey my friend!"
    with open("martin_public_key.pem", "rb") as file:
        martin_public_key = serialization.load_pem_public_key(
            file.read(),
            backend=default_backend()
        )
        encrypted = martin_public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            ))
        with open("file_to_martin.bin", "wb") as f:
            f.write(encrypted)


#create_and_save_message()

def read_and_show_message():
    with open("file_from_martin.bin", "rb") as f:
        file_from_martin = f.read()

        with open("private_key.pem", "rb") as file:
            my_private_key = serialization.load_pem_private_key(
                file.read(),
                password=None,
                backend=default_backend()
            )
        message_decrypted = my_private_key.decrypt(
            file_from_martin,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    print("Decrypted message:", message_decrypted.decode('utf-8'))

read_and_show_message()