from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def load_private_key(key_path):
    with open(key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def sign_document(document_path, private_key):
    with open(document_path, "rb") as file:
        message = file.read()
    
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def main():
    print("Write the path of the file you want to sign: ")
    document_path = input().strip()
    
    try:
        # Load private key A
        private_key = load_private_key("pair_a/private_key.pem")
        
        # Sign the document
        signature = sign_document(document_path, private_key)
        
        # Save the signature
        signature_path = document_path + ".sig"
        with open(signature_path, "wb") as sig_file:
            sig_file.write(signature)
            
        print(f"Document signed successfully! Signature saved to: {signature_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

