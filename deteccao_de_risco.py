# Detecção de risco (senha repetida)
def verificar_senha_repetida(credencial_atual):
    servicos_repetidos = []

    for credencial in credenciais:
        if credencial is not credencial_atual and credencial["senha"] == credencial_atual["senha"]:
            servicos_repetidos.append(credencial["servico"])

    if len(servicos_repetidos) > 0:
        print("\n! ALERTA DE RISCO !")
        print("Essa senha também é usada em outros serviços:")
        for servico in servicos_repetidos:
            print("-", servico)
        print("Se um deles vazar, todos os outros ficam expostos. Troque as senhas!")

        # Registrar no log:
        registrar_log("Alerta de senha repetida", credencial_atual["servico"])


# Detecção de risco (todas as senhas repetidas)
def verificar_todas_senhas_repetidas():
    grupos = {}

    for credencial in credenciais:
        senha = credencial["senha"]
        if senha in grupos:
            grupos[senha].append(credencial["servico"])
        else:
            grupos[senha] = [credencial["servico"]]

    print("\n---------- DETECÇÃO DE RISCO ----------")
    encontrou_risco = False

    for senha in grupos:
        if len(grupos[senha]) > 1:
            encontrou_risco = True
            print("\nSenha repetida em", len(grupos[senha]), "serviços:")
            for servico in grupos[senha]:
                print("-", servico)

    if encontrou_risco == False:
        print("Nenhuma senha repetida encontrada.")
    else:
        # Registrar no log:
        registrar_log("Verificação de risco", "! Senhas repetidas encontradas !")
