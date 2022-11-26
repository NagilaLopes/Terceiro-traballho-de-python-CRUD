i=1
while i<1000:
    opcao=int(input("=========MENU=========\n1-Cadastrar\n2-Ler\n3-Deletar\n4-Atualizar\n5-Sair\nDigite a opção: "))
    print("======================")
    if opcao==1:
        nome=input("\n======================\nDigite seu nome: ")
        cpf=input("Digite seu CPF: ")
        email=input("Digite seu email: ")
        senha=input("Digite seu senha: ")
        user=input("Digite seu usuário: ")
        conf=int(input("1-Sim\n2-Não\nConfirmar os dados? "))
        if conf==2:
            print("Refaça seus dados")
            i=i+1
        if conf!=1 and conf!=2:
            print("Digite um número válido")
        if conf==1:
            print("DADOS CONFIRMADOS!\n======================  \n")
            arquivo = open('Dados do usuário.txt', 'w')
            arquivo.write(" \n***DADOS DO USUÁRIO***\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s\n" %(nome,cpf,email,senha,user))
            arquivo.close()
            
    elif opcao==2:
        arquivo=open('Dados do usuário.txt', 'r')
        lerdados=arquivo.read()
        print(lerdados)
        arquivo.close()
#PARTE DE DELETAR *************************        
    elif opcao==3:
        arquivo=open('Dados do usuário.txt', 'r')
        lerdados=arquivo.read()
        print(lerdados)
        arquivo.close()
        
        delet=int(input("1-Sim\n2-Não\nDeseja deletar os dados? "))
        if delet==1:
            arquivo = open('Dados do usuário.txt', 'w')
            arquivo.close()
        else:
            print("Voltando ao menu...")
        

    elif opcao==4:
        atu=int(input("1-Sim\n2-Não\nDeseja atualizar seus dados? "))
        if atu==1:
            nome=input("\n======================\nDigite seu nome: ")
            cpf=input("Digite seu CPF: ")
            email=input("Digite seu email: ")
            senha=input("Digite seu senha: ")
            user=input("Digite seu usuário: ")
            print("DADOS CONFIRMADOS!\n======================  \n")
            arquivo = open('Dados do usuário.txt', 'w')
            arquivo.write(" \n***DADOS DO USUÁRIO***\nNome: %s\nCPF: %s\nEmail: %s\nSenha: %s\nUsuário: %s\n" %(nome,cpf,email,senha,user))
            arquivo.close()
        else:
            print("Voltando ao menu...")
            
    elif opcao==5:
        sair=int(input("1-Sim\n2-Não\nDeseja sair do programa? "))
        if sair==1:
            arquivo = open('Dados do usuário.txt', 'w')
            arquivo.write()
            arquivo.close()
        else:
            print("Voltando ao menu...")