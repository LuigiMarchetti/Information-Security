from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def load_public_key(key_path):
    with open(key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

def verify_signature(message_path, signature_path, public_key):
    # Read the original message
    with open(message_path, "rb") as file:
        message = file.read()
    
    # Read the signature
    with open(signature_path, "rb") as sig_file:
        signature = sig_file.read()
    
    try:
        # Verify the signature
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

def main():
    print("Write the path of the file to verify: ")
    document_path = input().strip()
    signature_path = document_path + ".sig"
    
    try:
        # Load public key B (this should fail since the document was signed with key A)
        public_key = load_public_key("pair_b/public_key.pem")
        
        # Verify the signature
        if verify_signature(document_path, signature_path, public_key):
            print("Unexpected result: Signature is valid with key B!")
            print("This should not happen since the document was signed with key A.")
        else:
            print("As expected: Invalid signature when verifying with key B!")
            print("This is correct because the document was signed with key A.")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 