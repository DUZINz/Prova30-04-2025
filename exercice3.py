from main_sha256 import sha256
'''exercicio 3 eu faria multiplas interações a mais na lib do sha256'''
# SHA-256 com múltiplas iterações (fortalecido)
def sha256_com_iteracoes(message, sal="", iteracoes=100000):
    valor = message + sal
    for _ in range(iteracoes):
        valor = sha256(valor)
    return valor

if __name__ == '__main__':
    senha1 = "minhaSenha123"
    senha2 = "senhaDiferente456"

    sal1 = "usuario1_salt"
    sal2 = "usuario2_salt"

    hash1 = sha256_com_iteracoes(senha1, sal=sal1, iteracoes=100000)
    hash2 = sha256_com_iteracoes(senha2, sal=sal2, iteracoes=100000)

    print("Hash 1 (fortalecido):", hash1)
    print("Hash 2 (fortalecido):", hash2)