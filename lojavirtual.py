from random import randint
produtos = {}
cadastro = {}
listaprodutos = []
try:
    with open("produtos.txt", "r") as arquivo:
        for linha in arquivo:
            nome, preco = linha.strip().split(",")
            listaprodutos.append({"PRODUTO": nome, "VALOR": float(preco)})
except FileNotFoundError:
    pass
listacadastro = []


def l ():
    print("="*40)


def e():
    print()


def area_vendedor():
    while True:
                    l()
                    print(" "*11,"ÁREA DO VENDEDOR")
                    l()
                    print("PARA:")
                    print("[1] ADICIONAR PRODUTOS")
                    print("[2] CONSULTAR PRODUTOS")
                    print("[3] ALTERAR PRODUTOS")
                    print("[4] EXCLUIR PRODUTOS")
                    print("[5] CADASTRO DE CLIENTES")
                    print("[6] VOLTAR AO MENU PRINCIPAL")
                    l()
                    menu2 = str(input("Digite a opção escolhida: "))
                    l()
                    if menu2 == "1":
                        while True:
                            produtos = {}
                            produtos["PRODUTO"] = str(input("Produto: "))
                            produtos["VALOR"] = float(input("Valor R$: "))
                            listaprodutos.append(produtos.copy())
                            with open("produtos.txt","a") as arquivo:
                                 arquivo.write(f"{produtos['PRODUTO']},{produtos['VALOR']}\n")
                                 
                            print("PRODUTO ADICIONADO COM SUCESSO!")
                            l()
                            menu3 = str(input("[1] ADICIONAR NOVO PRODUTO [2] VOLTAR AO MENU: "))
                            if menu3 == "1":
                                continue
                            if menu3 == "2":
                                break
                    elif menu2 == "2":
                        while True:
                            for k in listaprodutos:
                                for i,v in k.items():
                                    print(f"{i} -> {v}")
                                l()
                            menu4 = int(input("[1] VOLTAR AO MENU [2] ENCERRAR: "))
                            if menu4 == 1:
                                break
                            elif menu4 == 2:
                                print("ENCERRANDO...")
                                exit()

                    elif menu2 == "3":
                        for i,v in enumerate(listaprodutos):
                            print(f"{i}-> {v['PRODUTO']} - {v['VALOR' \
                            '']}")
                        l()
                        menu7 = int(input("Qual a numeração do produto que deseja alterar?"))
                        if menu7 >= 0 and menu7 < len(listaprodutos):
                            produtoalterado = listaprodutos[menu7]
                            print(f"Produto selecionado -> {produtoalterado}")
                            menu8 = str(input(f"Qual informação você deseja alterar {produtoalterado.keys()} (Digite tudo em MAIÚSCULO): ")).strip()
                            if menu8 in produtoalterado:
                                if menu8.lower() == "valor":
                                    novovalor = float(input("Novo valor: "))
                                else:
                                    novovalor = input("Novo nome:")
                            produtoalterado[menu8] = novovalor
                            print(f"PRODUTO ALTERADO COM SUCESSO! - {produtoalterado}")

                        else:
                            print("Campo inválido!")

                    elif menu2 == "4":
                        l()
                        print("LISTA DE PRODUTOS")
                        l()
                        
                        for i , v in enumerate(listaprodutos):
                            print(f"{i} - {v}")
                        menu9 = int(input("Código do produto que será excluído: "))
                        del listaprodutos[menu9]
                        print("PRODUTO REMOVIDO!")
                        for i , v in enumerate(listaprodutos):
                            print(f"{i} - {v}")

                    
                    elif menu2 == "5":
                         l()
                         print("LISTA DE CLIENTES CADASTRADOS")
                         l()
                         for i,v in enumerate(listacadastro):
                              print(f"{i} -> ID({v['ID']}) - Cliente: {v['Nome']}")
                            
                        
                    elif menu2 == "6":
                        break


def loja_virtual():
        l()
        print(f" "*3,"BEM VINDO(A) A NOSSA LOJA VIRTUAL")
        l()
        print("Confira nossos produtos:")
        for i, v in enumerate(listaprodutos):
            print(f"{i+1} - > {v['PRODUTO']}  | {v['VALOR']}")
            l()
        while True:
            menu5 = str(input("RETORNAR AO MENU PRINCIPAL [1]SIM [2]NÃO :" ))
            if menu5 == "1":
                break
            elif menu5 == "2":
                print("Obrigado! Encerrando....")
                exit()
            else:
                print("ERRO! Digite novamente!")
                continue


def area_cliente():
    while True:
            cadastro = {}
            l()
            print(" "*8,"ÁREA DO CLIENTE")
            print(" "*7,"Seja bem vindo(a)")
            l()
            print("[1] Já sou cliente. \n[2] Quero me cadastrar \n[3] Voltar ao Menu Principal")
            menu10 = str(input("Qual a opção desejada: "))
            if menu10 == "1":
                l()
                print(" "*6,"ÁREA DE LOGIN")
                l()
                login = int(input("NÚMERO DE CADASTRO: "))
                senha = str(input("SENHA: "))
                if login and senha not in listacadastro:
                     print("ERRO!")
                if login and senha in listacadastro:
                    print("ACESSO LIBERADO")

            if menu10 == "2":
                    l()
                    print(" "*10,"ÁREA DE CADASTRO ")
                    l()
                    cadastro['Nome'] = str(input("Nome completo: ")).strip()
                    cadastro['Nascimento'] = str(input('Data de nascimento(00/00/00): ')).strip()
                    cadastro['Celular'] = str(input("Digite seu celular (00)00000-0000: ")).strip()
                    cadastro['E-mail'] = str(input("E-mail: ")).strip()
                    while True:
                        cadastro['Senha'] = str(input("Senha(Até 8 caracteres): "))
                        cadastro['SenhaConf'] = str(input("Digite a Senha novamente: "))
                        if cadastro["Senha"] != cadastro["SenhaConf"]:
                             print("SENHAS DIVERGENTES, DIGITE NOVAMENTE!")
                             continue
                        elif len(cadastro["Senha"]) > 8:
                             print("ERRO! SENHA COM ATÉ 8 CARACTERES SOMENTE")
                             continue
                        else:                             
                            cadastro['ID'] = randint(10000,99999)
                            listacadastro.append(cadastro.copy())
                            print(f"CADASTRO REALIZADO COM SUCESSO!")
                            l()
                            print(f"O seu ID de acesso é {cadastro["ID"]}. \nUtilize o ID {cadastro['ID']} + Senha {cadastro['Senha']} para entrar.")
                            l()
                            break
                    while True:
                            menu11 = str(input("[1] ÁREA DO CLIENTE [2] LOJA VIRTUAL: "))
                            if menu11 == "1":
                                break
                            elif menu11 == "2":
                                loja_virtual()
                            else:
                                print("ERRO! Digite 1 ou 2.")             
            if menu10 == "3":
                break



while True:
    l()
    print(" "*13,"LELIS BEAUTY")
    l()
    print(" "*11,"Seja bem-vindo(a)")
    e()
    print("Para acessar:")
    print("[1] LOJA VIRTUAL")
    print("[2] ÁREA DO CLIENTE")
    print("[3] ÁREA DO VENDEDOR")
    l()
    menu1 = int(input("Digite a opção escolhida: "))

    if menu1 == 1:
        loja_virtual()
    
    if menu1 == 2:
         area_cliente()
            

    if menu1 == 3:
        area_vendedor()

                    