contato = []
while True:
    operacao = input("Oque você deseja fazer? \n(1)Adicionar contato \n(2)Ver seus contatos \n(3)Excluir contato \n(4)Modificar seus contatos \nOu digite \"sair\" para sair\n:")
    if operacao == 'sair' or operacao == 'SAIR':
        break
    if operacao == "1":
        contato.append(input("Digite o nome e o número do contato:"))
        print("Contato adicionado!\n")   
    if operacao == "2":
        for i in range(len(contato)):
            print(contato[i])
        print(".........................")
    if operacao == "3":
        try:
                remover = input(f"Qual contato deseja remover{contato}:")
                contato.remove(remover)
                print("Contato removido!\n")
        except:
                print("O valor de entrada está incorreto!\nDigite exatamente como está aparecendo na lista.\n")
    if operacao == "4":
            try:
                print(contato)
                modificar = int(input("Informe a posição do contato que dejesa modificar,começando pelo 0:"))
                novo = input("Digite qual será o novo contato:")
                contato[modificar] = novo
                print("O contato foi modificado!\n")
            except:
                print("A posição está incorreta!\nDigite a posição correta em números,exemplo:(João 934567869, Maria 958762001, José 976456002) \njoão está na posição 0, maria está na posição 1, josé na posição 2 e assim por diante...\n")
        
        

