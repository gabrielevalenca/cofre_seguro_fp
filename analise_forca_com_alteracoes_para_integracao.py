from datetime import datetime
requisitos_categoria = {
    "Rede Social": 4,
    "Banco": 5,
    "E-mail": 4,
    "Lojas virtuais": 3,
    "Plataformas de estudo": 3,
    "Streaming": 3,
    "Jogos": 2,
    "Outros": 3
}


# Análise de senha
def carregar_senhas_comuns():
    senhas_comuns = []

    try:
        arquivo = open("senhas_comuns.txt", "r")
        for linha in arquivo:
            senhas_comuns.append(linha.strip())
        arquivo.close()
    except:
        print("Arquivo de senhas comuns não encontrado.")
    return senhas_comuns

def verificar_senha_comum(senha):
    senhas_comuns = carregar_senhas_comuns()
    if senha in senhas_comuns:
        return True
    else:
        return False


def analisar_senha(senha, categoria):
    pontos = 0
    motivos = []
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_simbolo = False

    for letra in senha:
        if letra.isupper():
            tem_maiuscula = True
        elif letra.islower():
            tem_minuscula = True
        elif letra.isdigit():
            tem_numero = True
        elif not letra.isspace():
            tem_simbolo = True

    if len(senha) >= 8:
        pontos += 1
        motivos.append("A senha possui pelo menos 8 caracteres.")
    else:
        motivos.append("A senha possui menos de 8 caracteres.")

    if tem_maiuscula:
        pontos += 1
        motivos.append("A senha possui letras maiúsculas.")
    else:
        motivos.append("A senha não possui letras maiúsculas.")

    if tem_minuscula:
        pontos += 1
        motivos.append("A senha possui letras minúsculas.")
    else:
        motivos.append("A senha não possui letras minúsculas.")

    if tem_numero:
        pontos += 1
        motivos.append("A senha possui números.")
    else:
        motivos.append("A senha não possui números.")

    if tem_simbolo:
        pontos += 1
        motivos.append("A senha possui símbolos especiais.")
    else:
        motivos.append("A senha não possui símbolos especiais.")

    if pontos <= 2:
        classificacao = "Fraca"
    elif pontos <= 4:
        classificacao = "Média"
    else:
        classificacao = "Forte"

    categoria_encontrada = False

    for nome_categoria in requisitos_categoria:
        if categoria.lower().strip() == nome_categoria.lower().strip():
            categoria_encontrada = True

            if pontos < requisitos_categoria[nome_categoria]:
                classificacao = "Fraca"
                motivos.append(
                    "A senha não atingiu a pontuação mínima para essa categoria."
                )
            break

    if categoria_encontrada == False:
        classificacao = "Fraca"
        motivos.append("Categoria não cadastrada!")

    if verificar_senha_comum(senha):
        motivos.append("Essa senha está na lista de senhas comuns.")
        classificacao = "Fraca"

    return classificacao, pontos, motivos


def exibir_analise_senha(senha, categoria):
    classificacao, pontos, motivos = analisar_senha(senha, categoria)

    print("\n---------- ANÁLISE DA SENHA ----------")
    print("Categoria:", categoria)
    print("Pontuação:", pontos, "/5")
    print("Classificação:", classificacao)
    print("\nMotivos da classificação:")

    for motivo in motivos:
        print("-", motivo)
