from datetime import datetime
#manipulação do arquivo 
def registrar_senha(nova_credencial):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    analisar_senha(nova_credencial['senha'], nova_credencial['categoria'])
    arquivo = open("cofre_dados.txt", "a", encoding="utf-8")
    arquivo.write(
        f"[Serviço: {nova_credencial['servico']} | Usuario: {nova_credencial['usuario']} | Senha: {nova_credencial['senha']} | Categoria: {nova_credencial['categoria']} | Observacoes: {nova_credencial['observacoes']} | Atualizado: {nova_credencial['data_atualizacao']}]\n"
    )
    arquivo.close()
  

# Registro no arquivo de auditoria
def registrar_log(operacao, servico):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    arquivo = open("auditoria.log", "a", encoding="utf-8")
    arquivo.write(
        f"{data_hora} | Operação: {operacao} | Serviço: {servico}\n"
    )
    arquivo.close()

# Consulta de logs:
def consultar_logs():
    try:
        arquivo = open("auditoria.log", "r", encoding="utf-8")

        print("\n---------- LOG DE AUDITORIA ----------")

        vazio = True
        for linha in arquivo:
            print(linha.strip())
            vazio = False

        if vazio:
            print("Nenhum registro encontrado.")

        arquivo.close()

    except FileNotFoundError:
        print("Nenhum log foi gerado ainda.")


credenciais = []
categorias = [
    "Rede Social", 
    "Banco",
    "E-mail",
    "Lojas virtuais",
    "Plataformas de estudo", 
    "Streaming", 
    "Jogos", 
    "Outros"
]

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
    motivos = []

    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbolos = "!@#$%&*()-_+=.;:?"
    
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
        elif letra in simbolos:
            tem_simbolo = True

    if len(senha) >= 8:
        motivos.append("A senha possui pelo menos 8 caracteres.")
    else:
        motivos.append("A senha possui menos de 8 caracteres.")

    if tem_maiuscula:
        motivos.append("A senha possui letras maiúsculas.")
    else:
        motivos.append("A senha não possui letras maiúsculas.")

    if tem_minuscula:
        motivos.append("A senha possui letras minúsculas.")
    else:
        motivos.append("A senha não possui letras minúsculas.")

    if tem_numero:
        motivos.append("A senha possui números.")
    else:
        motivos.append("A senha não possui números.")

    if tem_simbolo:
        motivos.append("A senha possui símbolos especiais.")
    else:
        motivos.append("A senha não possui símbolos especiais.")

    tipos_caracteres = 0

    if tem_maiuscula:
        tipos_caracteres +=1
    if tem_minuscula:
        tipos_caracteres +=1
    if tem_numero:
        tipos_caracteres +=1
    if tem_simbolo:
        tipos_caracteres +=1

    if len(senha) < 8 or tipos_caracteres <=1:
        classificacao = "Fraca"
        motivos.append("A senha não atende aos requisitos mínimos de segurança")
    elif (len(senha) > 8 and tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo):
        classificacao = "Forte"
        motivos.append("A senha atende a todos os critérios de uma senha forte.")
    else: 
        classificacao = "Média"
        motivos.append("A senha atende a alguns critérios de segurança, mas não a todos os requisitos de uma senha forte.")
    

    if verificar_senha_comum(senha):
        classificacao = "Fraca"
        motivos.append("Essa senha está na lista de senhas comuns e, por segurança, foi classificada como fraca")

    return classificacao, motivos

def exibir_analise_senha(senha, categoria):
    classificacao, motivos = analisar_senha(senha, categoria)
    print("\n---------- ANÁLISE DA SENHA ----------")
    print("Categoria:", categoria)
    print("Classificação:", classificacao)
    print("\nMotivos da classificação:")
    for motivo in motivos:
        print("-", motivo)

# Cadastro
def cadastrar_credenciais():
    servico = input("Digite o nome do serviço: ")
    usuario = input("Digite o nome do usuário: ")

    #subir motivos 
    print("sugerir senhas ")
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
    registrar_senha(nova_credencial)
    
    
    credenciais.append(nova_credencial)
# Registrar no log:
    registrar_log("Cadastro de credencial", servico)

    print("Cadastro confirmado!")
    exibir_analise_senha(senha, categoria)


# Visualização
def visualizar_credenciais():
    if len(credenciais) == 0:
        print("Não existem cadastros.")
    else:
        for credencial in credenciais:

# Registrar no log:
            registrar_log(
                "Visualização de credencial",
                credencial["servico"]
            )
            
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
            # Registrar no log:
            registrar_log("Revelação de senha", servico_revelar)
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
            # Registrar no log:
            registrar_log("Alteração de senha", servico_editar)
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
            # Registro no log:
            registrar_log("Exclusão de credencial", servico_excluir)
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

    for categoria in categorias:
        if categoria.lower() == nome.lower():
            print("Essa categoria já existe.")
            return

    categorias.append(nome)
    # Registro no log:
    registrar_log("Cadastro de categoria", nome)
    print("Categoria cadastrada com sucesso!")
    


# Consulta de categorias
def visualizar_categorias():
    print("\n---------- CATEGORIAS ----------")

    for categoria in categorias:
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
    print("9 - Consultar Log de Auditoria")

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

    elif opcao == "9":
        consultar_logs()

    else:
        print("Opção inválida!")
