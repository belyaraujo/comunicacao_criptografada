# 🔐 Comunicação Criptografada com Streamlit

Este projeto simula a **comunicação segura entre duas aplicações**, usando criptografia **simétrica (DES, AES)**, **assimétrica (RSA)** e um modo **híbrido (AES + RSA)** para troca segura de chaves.

A interface foi desenvolvida com [Streamlit](https://streamlit.io), permitindo fácil visualização de como os dados são cifrados, enviados e decifrados.

---

## 📌 Funcionalidades

✅ Criptografia e descriptografia de mensagens em texto plano  
✅ Escolha entre algoritmos: **DES**, **AES**, **RSA** e **HÍBRIDO (AES + RSA)**  
✅ Comparação de desempenho (tempo de execução)  
✅ Explicações sobre quando usar simétrica ou assimétrica  
✅ Interface web amigável com Streamlit

---

## 🧠 Conceitos

- **DES**: algoritmo simétrico antigo e inseguro.
- **AES**: algoritmo simétrico moderno, seguro e rápido.
- **RSA**: algoritmo assimétrico seguro, mas lento.
- **Híbrido**: combinação de RSA (para troca segura de chave AES) + AES (para cifrar dados).

---

## 🚀 Como rodar o projeto localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/criptografia-streamlit.git
cd criptografia-streamlit
```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**

```bash
streamlit run app.py
```

A aplicação abrirá no seu navegador em `http://localhost:8501`.

---

## ☁️ Como hospedar com Streamlit Cloud

1. Suba os arquivos para um repositório no GitHub
2. Vá para: [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Clique em **“New app”**
4. Escolha seu repositório, o branch (geralmente `main`) e o arquivo `app.py`
5. Clique em **Deploy**

---

## 📦 Requisitos

- Python 3.7+
- `streamlit`
- `pycryptodome`

Instalados via:

```bash
pip install streamlit pycryptodome
```
