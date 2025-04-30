# Alfabeto base64 padrão: 64 caracteres únicos usados para codificar os dados
BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# Caractere de preenchimento usado quando o tamanho dos dados não é múltiplo de 3
BASE64_PAD = "="


def encode(data: bytes) -> str:
    # Verifica se o dado de entrada é do tipo bytes; se não for, lança erro
    if not isinstance(data, bytes):
        raise TypeError("data não é bytes")
        
    result = []  # Lista para armazenar os caracteres codificados
    i = 0  # Índice para percorrer os bytes
    
    while i < len(data):
        # Lê um bloco de até 3 bytes
        block = data[i:i + 3]
        
        # Converte os bytes para um número inteiro (big endian)
        b = int.from_bytes(block, 'big')
        
        # Calcula quantos bytes faltaram (para aplicar o padding depois)
        pad_len = 3 - len(block)
        
        # Faz shift à esquerda para simular os bytes faltantes (preenchidos com zeros)
        b <<= 8 * pad_len

        # Extrai 4 grupos de 6 bits (total de 24 bits) e mapeia no alfabeto base64
        for j in range(18, -1, -6):
            idx = (b >> j) & 0x3F  # Pega 6 bits por vez
            result.append(BASE64_ALPHABET[idx])  # Adiciona o caractere correspondente

        # Se houve padding, substitui os últimos caracteres pelo símbolo "="
        if pad_len:
            result[-pad_len:] = BASE64_PAD * pad_len

        i += 3  # Avança 3 bytes
    
    # Retorna a string final codificada
    return ''.join(result)

def decode(encoded: str) -> bytes:
    # Verifica se o comprimento da string codificada é múltiplo de 4 (regra do base64)
    if len(encoded) % 4 != 0:
        raise ValueError("Invalid Base64 input length")
    
    # Remove os "=" do final da string para facilitar a decodificação
    encoded = encoded.rstrip(BASE64_PAD)

    buffer = 0  # Armazena os bits combinados dos caracteres base64
    bits = 0  # Quantidade de bits válidos no buffer
    output = bytearray()  # Lista de bytes resultante

    for char in encoded:
        # Verifica se o caractere está no alfabeto válido
        if char not in BASE64_ALPHABET:
            raise ValueError(f"Invalid character in input: {char}")
        
        # Converte o caractere base64 para índice numérico e adiciona ao buffer
        buffer = (buffer << 6) | BASE64_ALPHABET.index(char)
        bits += 6  # Adiciona 6 bits a cada novo caractere

        # Enquanto tiver pelo menos 8 bits, extrai 1 byte (8 bits)
        if bits >= 8:
            bits -= 8
            output.append((buffer >> bits) & 0xFF)

    # Retorna os bytes decodificados
    return bytes(output)

if __name__ == "__main__":
    test_strings = [b"Hello, Base64!!", b"any carnal pleasure.,.,", b"", b"A", b"AB", b"ABC", b"Testando Base64", b"123456"]

    for original in test_strings:
        encoded = encode(original)
        decoded = decode(encoded)

        print(f"Original: {original}")
        print(f"Encoded : {encoded}")
        print(f"Decoded : {decoded}")

        # 🚨 TESTE AUTOMÁTICO: se falhar, lança erro
        assert decoded == original, f"Falha no teste! {original} → {encoded} → {decoded}"

        print("✅ Teste passou!\n" + "-" * 40)