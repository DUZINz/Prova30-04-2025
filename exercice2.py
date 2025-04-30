from main_base64 import encode, decode

# Função para codificar o conteúdo com um prefixo de comprimento
def encode_with_length(data: bytes) -> str:
    # Codificar o comprimento do conteúdo original em Base64
    length_prefix = len(data).to_bytes(4, 'big')  # Usa 4 bytes para armazenar o comprimento
    encoded_length = encode(length_prefix)  # Codifica o comprimento
    
    # Codificar o conteúdo original em Base64
    encoded_data = encode(data)
    
    # Concatenar o prefixo com o conteúdo codificado
    return f"{encoded_length}{encoded_data}"

# Função para verificar a autenticidade e integridade do conteúdo
def verify_integrity(encoded_with_length: str) -> bool:
    # Determina o comprimento do prefixo, que é a codificação do comprimento do conteúdo (4 bytes)
    # A codificação Base64 de 4 bytes resultará em 8 caracteres (já que cada grupo de 6 bits vira 1 caractere).
    encoded_length = encoded_with_length[:8]  # 8 caracteres Base64 para 4 bytes
    encoded_data = encoded_with_length[8:]  # O restante é o conteúdo codificado
    
    # Decodificar o comprimento original a partir do prefixo
    decoded_length = int.from_bytes(decode(encoded_length), 'big')
    
    # Decodificar o conteúdo Base64
    decoded_data = decode(encoded_data)
    
    # Verificar se o comprimento do conteúdo decodificado é igual ao comprimento original
    return len(decoded_data) == decoded_length

# Função de exemplo para demonstrar o uso
def test_with_authentication():
    test_strings = [b"Hello, Base64!!", b"any carnal pleasure.,.,", b"", b"A", b"AB", b"ABC", b"Testando Base64", b"123456"]
    
    for original in test_strings:
        # Codificar com prefixo de comprimento incluído
        encoded_with_length = encode_with_length(original)
        print(f"Original: {original}")
        print(f"Encoded with Length: {encoded_with_length}")
        
        # Verificar se o conteúdo é autêntico
        is_valid = verify_integrity(encoded_with_length)
        print(f"Autenticidade verificada: {'✅' if is_valid else '❌'}")
        
        # TESTE AUTOMÁTICO: se falhar, lança erro
        assert is_valid, f"Falha na verificação de autenticidade! {original} → {encoded_with_length}"
        
        print("✅ Teste passou!\n" + "-" * 40)

if __name__ == "__main__":
    test_with_authentication()

