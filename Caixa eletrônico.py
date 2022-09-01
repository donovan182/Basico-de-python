saldo = 0
saque = 0
deposito = 0

while True:
    
    try:
        menu = float(input("Oque deseja fazer? (1)consultar saldo, (2)saque, (3)depósito e (4)sair."))
        if menu == 4:
            break
        
        elif menu == 1:
            print("Seu saldo é de:",round(saldo,2))
            
        elif menu == 2:
            saque = float(input("Quanto deseja sacar?:"))
            if saldo >= saque:
                saldo = saldo - saque
                print("Você Sacou R$:",saque)
            else:
                print("Você não tem dinheiro o suficiente para sacar este valor.")
            
        elif menu == 3:
            deposito = float(input("Quanto deseja depositar?:"))
            saldo = deposito + saldo
            print("Você depositou R$:",deposito)
            
        else:
            print("Digite um dos 4 números")
            
    except:
        print("Digite um dos 4 números")
        
        
        


            
        
        
        
                     
                     
    
