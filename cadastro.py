credenciais=[]

def cadastrar_credenciais():
    servico=input("Digite o nome do serviço: ")
    usuario=input("Digite o nome do usuario: ")
    senha=input("Digite a senha: ")
    categoria=input("Digite a categoria: ")

    nova_credencial = {
        "servico": servico,
        "usuario": usuario,
        "senha": senha,
        "categoria": categoria
    }
    credenciais.append(nova_credencial)
    print(f"Cadastro confirmado\n ----------Credencial------------\nServiço:{servico}\nUsuário:{usuario}\nSenha:{senha}\nCategoria:{categoria}")


def visualizar_credenciais():
    if len(credenciais)==0:
        print("Não existem cadastros")
    else:
        for credencial in credenciais:
            print("\n---------- CREDENCIAL ----------")
            print(f"Serviço: {credencial['servico']}")
            print(f"Usuário: {credencial['usuario']}")
            print(f"Senha: {credencial['senha']}")
            print(f"Categoria: {credencial['categoria']}")


def editar_credenciais():
    servico_editar=input("Qual serviço deseja editar? ")
    encontrado = False
    for credencial in credenciais:
        if credencial["servico"] == servico_editar:
            nova_senha= input("Qual será a senha nova? ")
            credencial["senha"] = nova_senha
            encontrado = True
            print("Senha alterada")
    if encontrado == False:
        print("Serviço não encontrado")


def excluir_credenciais():
    servico_excluir=input("Qual serviço deseja excluir? ")
    encontrado=False
    for credencial in credenciais:
        if credencial["servico"]==servico_excluir:
            credenciais.remove(credencial)
            encontrado=True
            break
    if encontrado==False:
        print("Serviço não encontrado")

while True:
    print("\n---------Credencial---------")
    print("1- Cadastrar Credencial")
    print("2-Visualizar Credenciais")
    print("3- Editar Credencial")
    print("4- Excluir Credencial")
    print("5- Sair")
    opcao=int(input("Digite a opção: "))
    if opcao==1:
        cadastrar_credenciais()
    elif opcao==2:
        visualizar_credenciais()
    elif opcao==3:
        editar_credenciais()
    elif  opcao==4:
        excluir_credenciais()
    else: 
        break




