from main_sha256 import encode, decode
def test_encode_decode():
    test_cases = [
        b"",                     # vazio
        b"A",                   # 1 byte
        b"AB",                  # 2 bytes
        b"ABC",                 # 3 bytes
        b"Hello",              
        b"Hello, Base64!",      
        b"any carnal pleasure.",
        b"1234567890",
        b"Base64 eh legal!"
]

    for original in test_cases:
        encoded = encode(original)
        decoded = decode(encoded)
        assert decoded == original, f"Erro: {original} → {encoded} → {decoded}"
        print(f"✅ Teste passou: {original} → {encoded} /// {decoded}")


if __name__ == "__main__":
    test_encode_decode()