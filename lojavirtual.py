def l ():
    print("="*40)

menu4 = 0
def e():
    print()

produtos = {}
listaprodutos = []
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
    if menu1 == 3:
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
                    menu2 = int(input("Digite a opção escolhida: "))
                    l()
                    if menu2 == 1:
                        while True:
                            produtos["Nome: "] = str(input("Produto: "))
                            produtos["Valor R$: "] = float(input("Valor R$: "))
                            listaprodutos.append(produtos.copy())
                            print("PRODUTO ADICIONADO COM SUCESSO!")
                            l()
                            menu3 = int(input("[1] ADICIONAR NOVO PRODUTO [2] VOLTAR AO MENU: "))
                            if menu3 == 1:
                                continue
                            if menu3 == 2:
                                break
                    elif menu2 == 2:
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
                    elif menu2 == 6:
                        break                      
                    