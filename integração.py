from datetime import datetime

credenciais = []

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


# Cadastro
def cadastrar_credenciais():
    servico = input("Digite o nome do serviço: ")
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    print("\nCategorias disponíveis:")
    visualizar_categorias()

    categoria = input("Digite a categoria: ")
    observacoes = input("Digite as observações: ")

    data_atualizacao = datetime.now().strftime("%d/%m/%Y %H:%M")

    nova_credencial = {
        "servico": servico,
        "usuario": usuario,
        "senha": senha,
        "categoria": categoria,
        "observacoes": observacoes,
        "data_atualizacao": data_atualizacao
    }

    credenciais.append(nova_credencial)

    print("Cadastro confirmado!")
    exibir_analise_senha(senha, categoria)


# Visualização
def visualizar_credenciais():
    if len(credenciais) == 0:
        print("Não existem cadastros.")
    else:
        for credencial in credenciais:
            senha_oculta = credencial["senha"][:2] + "*" * max(0, len(credencial["senha"]) - 2)

            print("\n---------- CREDENCIAL ----------")
            print(f"Serviço: {credencial['servico']}")
            print(f"Usuário: {credencial['usuario']}")
            print(f"Senha: {senha_oculta}")
            print(f"Categoria: {credencial['categoria']}")
            print(f"Observações: {credencial['observacoes']}")
            print(f"Último cadastro/alteração: {credencial['data_atualizacao']}")


# Revelar senha
def revelar_senha():
    servico_revelar = input("Digite o nome do serviço: ")
    encontrado = False

    for credencial in credenciais:
        if credencial["servico"] == servico_revelar:
            print("Senha:", credencial["senha"])
            encontrado = True
            break

    if encontrado == False:
        print("Serviço não encontrado.")


# Edição
def editar_credenciais():
    servico_editar = input("Qual serviço deseja editar? ")
    encontrado = False

    for credencial in credenciais:
        if credencial["servico"] == servico_editar:
            nova_senha = input("Qual será a senha nova? ")

            credencial["senha"] = nova_senha
            credencial["data_atualizacao"] = datetime.now().strftime("%d/%m/%Y %H:%M")

            encontrado = True
            print("Senha alterada!")

            exibir_analise_senha(
                nova_senha,
                credencial["categoria"]
            )
            break

    if encontrado == False:
        print("Serviço não encontrado.")


# Exclusão
def excluir_credenciais():
    servico_excluir = input("Qual serviço deseja excluir? ")
    encontrado = False

    for credencial in credenciais:
        if credencial["servico"] == servico_excluir:
            credenciais.remove(credencial)
            encontrado = True
            print("Credencial excluída!")
            break

    if encontrado == False:
        print("Serviço não encontrado.")


# Cadastro de categorias
def cadastrar_categoria():
    nome = input("Digite o nome da categoria: ").strip()

    if nome == "":
        print("Nome inválido.")
        return

    for categoria in requisitos_categoria:
        if categoria.lower() == nome.lower():
            print("Essa categoria já existe.")
            return

    try:
        pontos = int(input("Digite a pontuação mínima (1 a 5): "))

        if pontos < 1 or pontos > 5:
            print("Pontuação inválida.")
        else:
            requisitos_categoria[nome] = pontos
            print("Categoria cadastrada com sucesso!")

    except ValueError:
        print("Digite um número válido.")


# Consulta de categorias
def visualizar_categorias():
    print("\n---------- CATEGORIAS ----------")

    for categoria in requisitos_categoria:
        print(f"{categoria}")


# Menu
while True:
    print("\n--------- COFRESEGURO ---------")
    print("1 - Cadastrar Credencial")
    print("2 - Visualizar Credenciais")
    print("3 - Editar Credencial")
    print("4 - Excluir Credencial")
    print("5 - Sair")
    print("6 - Revelar Senha")
    print("7 - Cadastrar Categoria")
    print("8 - Consultar Categorias")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        cadastrar_credenciais()

    elif opcao == "2":
        visualizar_credenciais()

    elif opcao == "3":
        editar_credenciais()

    elif opcao == "4":
        excluir_credenciais()

    elif opcao == "5":
        print("Encerrando o CofreSeguro...")
        break

    elif opcao == "6":
        revelar_senha()

    elif opcao == "7":
        cadastrar_categoria()

    elif opcao == "8":
        visualizar_categorias()

    else:
        print("Opção inválida!")

