from Crypto.Cipher import AES, DES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

def pad(text, block_size):
    pad_len = block_size - len(text) % block_size
    return text + chr(pad_len) * pad_len

def unpad(text):
    pad_len = ord(text[-1])
    return text[:-pad_len]
    

# --------------------- DES ------------------------------
def des_encrypt(text):
    key = b'12345678'
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text, 8)
    encrypted = cipher.encrypt(padded_text.encode())
    return base64.b64encode(encrypted).decode()

def des_decrypt(encrypted):
    key = b'12345678'
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted))
    return unpad(decrypted.decode())


# --------------------- AES ------------------------------
def aes_encrypt(text):
    key = b'ThisIsASecretKey'
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(text, 16)
    encrypted = cipher.encrypt(padded_text.encode())
    return base64.b64encode(encrypted).decode()

def aes_decrypt(encrypted):
    key = b'ThisIsASecretKey'
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted))
    return unpad(decrypted.decode())


# --------------------- RSA ------------------------------
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

def rsa_encrypt(text, public_key_bytes):
    public_key = RSA.import_key(public_key_bytes)
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(text.encode())
    return base64.b64encode(encrypted).decode()

def rsa_decrypt(encrypted, private_key_bytes):
    private_key = RSA.import_key(private_key_bytes)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(base64.b64decode(encrypted))
    return decrypted.decode()


# --------------------- Hibrido ------------------------------
def hybrid_encrypt(text, public_key_bytes):
    # 1) Gera chave AES aleatória
    aes_key = get_random_bytes(16)
    # 2) Cifra o texto com AES
    cipher_aes = AES.new(aes_key, AES.MODE_ECB)
    padded = pad(text, 16).encode()
    encrypted_text = cipher_aes.encrypt(padded)
    b64_text = base64.b64encode(encrypted_text)

    # 3) Cifra a chave AES com RSA
    public_key = RSA.import_key(public_key_bytes)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_key = cipher_rsa.encrypt(aes_key)
    b64_key = base64.b64encode(encrypted_key)

    # Retorna dupla (texto, chave) em Base64
    return b64_text.decode(), b64_key.decode()

def hybrid_decrypt(b64_text, b64_key, private_key_bytes):
    # 1) Decifra a chave AES com RSA
    private_key = RSA.import_key(private_key_bytes)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(base64.b64decode(b64_key))

    # 2) Usa chave AES para decifrar o texto
    cipher_aes = AES.new(aes_key, AES.MODE_ECB)
    decrypted = cipher_aes.decrypt(base64.b64decode(b64_text))
    return unpad(decrypted.decode())