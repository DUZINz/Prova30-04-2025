'''
exercicio 01:
 implemente uma função que receba como entrada um texto de comunicação (string)
 e produza uma versão codificada que permita ao destinatario:
 a. reconstruir o conteudo original
 b. Verificar a autenticidade da mensagem
'''
from main_base64 import encode as base64_encode, decode as base64_decode
from main_sha256 import sha256

def encode_message(message, secret_key):
    # Primeiro codifica a mensagem em base64
    base64_msg = base64_encode(message.encode('utf-8'))
    # Depois aplica o hash com a chave secreta + base64
    combined = secret_key + base64_msg
    message_hash = sha256(combined)
    return f"{base64_msg}|{message_hash}"

def decode_message(encoded_message, secret_key):
    if '|' not in encoded_message:
        return None, False

    base64_msg, original_hash = encoded_message.rsplit("|", 1)
    recalculated_hash = sha256(secret_key + base64_msg)

    try:
        message = base64_decode(base64_msg).decode('utf-8')
    except Exception:
        return None, False

    return (message, recalculated_hash == original_hash)

def verificar_autenticidade(conteudo_recebido: str, chave: str):
    """
    Procedimento de verificação de autenticidade:
    1. Separa a parte base64 do hash.
    2. Recalcula o hash com chave + base64.
    3. Compara com o hash recebido.
    """
    if '|' not in conteudo_recebido:
        return False

    base64_msg, hash_recebido = conteudo_recebido.rsplit("|", 1)
    hash_calculado = sha256(chave + base64_msg)
    return hash_calculado == hash_recebido

# Demonstração sem interação
if __name__ == '__main__':
    secret_key = "my_secret_key"
    original_message = "Mensagem confidencial para validação."

    encoded = encode_message(original_message, secret_key)
    print(f"Mensagem codificada (base64 depois SHA-256): {encoded}")

    decoded_message, is_authentic = decode_message(encoded, secret_key)
    print(f"Mensagem decodificada: {decoded_message}")
    print(f"Autenticidade verificada: {is_authentic}")

    autenticado = verificar_autenticidade(encoded, secret_key)
    print(f"Resultado da verificação direta: {autenticado}")