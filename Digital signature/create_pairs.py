from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def create_and_save_two_key_pairs():
    create_and_save_key_pair("pair_a/private_key.pem", "pair_a/public_key.pem")
    create_and_save_key_pair("pair_b/private_key.pem", "pair_b/public_key.pem")

def create_and_save_key_pair(private_key_dir, public_key_dir):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(private_key_dir, "wb") as f:
        f.write(pem_private_key)

    # Retorna a chave pública em formato PEM
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1,
    )
    with open(public_key_dir, "wb") as f:
        f.write(public_pem)

create_and_save_two_key_pairs()