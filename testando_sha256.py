from main_sha256 import sha256

def run_tests():
    messages = [
        "",
        "abc",
        "The quick brown fox jumps over the lazy dog",
        "The quick brown fox jumps over the lazy dog.",
        "1234567890",
        "a" * 1000,
    ]

    for msg in messages:
        print(f"Mensagem: {repr(msg)}")
        print(f"Hash gerado: {sha256(msg)}")
        print("-" * 60)

if __name__ == "__main__":
    run_tests()
