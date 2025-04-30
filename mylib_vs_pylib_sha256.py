import hashlib
from main_sha256 import sha256

def compare_hashes(message: str) -> None:
    my_hash = sha256(message)
    lib_hash = hashlib.sha256(message.encode()).hexdigest()

    print(f"Mensagem: {message}")
    print(f"Meu SHA256 : {my_hash}")
    print(f"SHA256 hashlib: {lib_hash}")
    print("Hashes conferem!" if my_hash == lib_hash else "Hashes diferentes!")

if __name__ == "__main__":
    compare_hashes("abc")
    compare_hashes("")
    compare_hashes("The quick brown fox jumps over the lazy dog")
    compare_hashes("The quick brown fox jumps over the lazy dog.")
