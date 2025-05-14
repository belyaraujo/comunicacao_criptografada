import streamlit as st
import time
from crypt import *

st.title("🔐 Comunicação Criptografada")


text = st.text_input("🔤 Digite o texto em claro:")
option = st.selectbox("🔑 Algoritmo", ["DES", "AES", "RSA", "Híbrido"])

if st.button("🚀 Processar"):
    start = time.time()

    if option == "DES":
        encrypted = des_encrypt(text); decrypted = des_decrypt(encrypted)
    elif option == "AES":
        encrypted = aes_encrypt(text); decrypted = aes_decrypt(encrypted)
    elif option == "RSA":
        pub, priv = generate_rsa_keys()
        encrypted = rsa_encrypt(text, pub); decrypted = rsa_decrypt(encrypted, priv)
    else:  # Híbrido
        pub, priv = generate_rsa_keys()
        encrypted, encrypted_key = hybrid_encrypt(text, pub)
        decrypted = hybrid_decrypt(encrypted, encrypted_key, priv)

    elapsed = time.time() - start

    st.subheader("🔐 Texto cifrado")
    if option == "Híbrido":
        st.code(f"Mensagem: {encrypted}\nChave : {encrypted_key}", language="text")
    else:
        st.code(encrypted, language="text")

    st.subheader("🛰️ Simulação de Recebimento → Decifrado")
    st.success(decrypted)

    st.info(f"⏱️ Tempo total: {elapsed:.4f}s")

    # Feedback de segurança
    if option == "DES":
        st.warning("⚠️ DES é considerado inseguro.")
    elif option == "AES":
        st.success("✅ AES é seguro e rápido.")
    elif option == "RSA":
        st.info("🔐 RSA é seguro, mas lento. Bom para troca de chaves.")
    else:
        st.success("✅ Híbrido: troca de chave + cifragem eficiente.")
