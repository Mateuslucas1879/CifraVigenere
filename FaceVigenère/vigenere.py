import string


def tabela_vigenere():
    alfabeto = string.ascii_uppercase
    tabela = []

    for i in range(len(alfabeto)):
        linha = alfabeto[i:] + alfabeto[:i]
        tabela.append(linha)
    return tabela

def tabela_criptografica(mensagem, chave, tabela):
    mensagem = mensagem.upper().replace(" ", "")
    chave = chave.upper().replace(" ", "")
    mensagem_criptografada = []

    for i in range(len(mensagem)):
        letra_mensagem = mensagem[i]
        letra_chave = chave[i % len(chave)]

        linha_chave = string.ascii_uppercase.index(letra_chave)
        coluna_mensagem = string.ascii_uppercase.index(letra_mensagem)

        letra_criptografada = tabela[linha_chave][coluna_mensagem]
        mensagem_criptografada.append(letra_criptografada)

    return ''.join(mensagem_criptografada)

def descriptografar(mensagem_criptografada,chave,tabela):
    mensagem_criptografada = mensagem_criptografada.upper().replace(" ","")
    chave = chave.upper().replace(" ","")
    mensagem_original = []

    for i in range(len(mensagem_criptografada)):
        letra_criptografada = mensagem_criptografada[i]
        letra_chave = chave[i % len(chave)]

        linha_Chave = string.ascii_uppercase.index(letra_chave)
        coluna_mensagem = tabela[linha_Chave].index(letra_criptografada)
        mensagem_original.append(string.ascii_uppercase[coluna_mensagem])

    return ''.join(mensagem_original)
