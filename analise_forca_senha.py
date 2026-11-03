requisitos_categoria = {
    "Redes sociais": 4,
    "Banco": 5, 
    "E-mail": 4, 
    "Lojas virtuais": 3,
    "Plataformas de estudo": 3,
    "Streaming": 3,
    "Jogos": 2,
    "Outros": 3
}

def carregar_senhas_comuns():
    arquivo = open("senhas_comuns.txt", "r")
    senhas_comuns = []
    for linha in arquivo: 
        senha = linha.strip()
        senhas_comuns.append(senha)
    arquivo.close()
    return senhas_comuns

def verificar_senha_comum(senha):
    senhas_comuns = []
    senhas_comuns = carregar_senhas_comuns()

    if senha in senhas_comuns: 
        return True
    else: 
        return False

def analisar_senha(senha, categoria):
    pontos = 0
    motivos = []

    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_simbolo = False

    for letra in senha: 
        if letra in maiusculas:
            tem_maiuscula = True
        elif letra in minusculas:
            tem_minuscula = True
        elif letra in numeros: 
            tem_numero = True
        elif letra != "":
            tem_simbolo = True

    if len(senha) >= 8:
        pontos += 1
        motivos.append("A senha possui pelo menos 8 caracteres ")
    else: 
        motivos.append("A senha possui menos de 8 caracteres ")

    if tem_maiuscula == True: 
        pontos += 1
        motivos.append("A senha possui letras maiúsculas ")
    else:
        motivos.append("A senha não possui letras maiúsculas ")

    if tem_minuscula == True: 
        pontos += 1
        motivos.append("A senha possui letras minúsculas ")
    else: 
        motivos.append("A senha não possui letras minúsculas ")

    if tem_numero == True:
        pontos +=1
        motivos.append("A senha possui números ")
    else: 
        motivos.append("A senha não possui números ")

    if tem_simbolo == True: 
        pontos +=1
        motivos.append("A senha possui símbolos especiais ")
    else: 
        motivos.append("A senha não possui símbolos especiais ")

    if pontos <= 2: 
        classificacao = "Fraca"
    elif pontos <= 4: 
        classificacao = "Média"
    else: 
        classificacao = "Forte"

    categoria_encontrada = False
    for nome_categoria in requisitos_categoria:
        if categoria.lower().strip()==nome_categoria.lower().strip():
            categoria_encontrada = True

            if pontos < requisitos_categoria[nome_categoria]:
                classificacao = "Fraca"
                motivos.append("A senha não atingiu a pontuação mínima para essa categoria ")
                
    if categoria_encontrada == False: 
        classificacao = "Fraca"
        motivos.append("Categoria não cadastrada! ")    

    if verificar_senha_comum(senha) == True:
        motivos.append("Essa senha está na lista de senhas comuns ")
        classificacao = "Fraca"

    return classificacao, pontos, motivos

def exibir_analise_senha(senha, categoria):
    classificacao, pontos, motivos = analisar_senha(senha, categoria)
    
    print("\n ---------- ANÁLISE DA SENHA ---------- ")
    print("Categoria:", categoria)
    print("Pontuação:",pontos,"/5")
    print("Classificação:", classificacao)

    if len(motivos) > 0:
        print("\n Motivos da classificação: ")

        for motivo in motivos: 
            print("-", motivo)
    else: 
        print("A senha atende a todos os critérios! ")

senha = input("Digite uma senha para analisar: ")
print("\n Categorias disponiveis: ")

for categoria in requisitos_categoria: 
    print("-", categoria)

categoria_escolhida = input("\n Digite a categoria da senha: ")

exibir_analise_senha(senha, categoria_escolhida)
