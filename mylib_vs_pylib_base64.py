import base64
from main_sha256 import encode, decode

def test_vs_builtin():
    test_cases = [b"A", b"AB", b"ABC", b"Hello, Base64!", b"123"]

    for original in test_cases:
        # Sua função
        my_encoded = encode(original)
        my_decoded = decode(my_encoded)

        # Função do Python
        py_encoded = base64.b64encode(original).decode()
        py_decoded = base64.b64decode(py_encoded)

        assert my_encoded == py_encoded, f"Erro no encode: {original} → {my_encoded} (esperado: {py_encoded})"
        assert my_decoded == py_decoded, f"Erro no decode: {my_encoded} → {my_decoded} (esperado: {py_decoded})"
        print(f"✅ Bateu com base64 oficial: {original}")

if __name__ == "__main__":
    test_vs_builtin()