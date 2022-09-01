def soma (num1,num2):
    totalsoma = num1 + num2
    return totalsoma
def subtracao (num1,num2):
    totalsub = num1 - num2
    return totalsub
def multiplicacao (num1,num2):
    totalmulti = num1 * num2
    return totalmulti
def divisao (num1,num2):
    totaldivi = num1 / num2
    return totaldivi
    
while True:
    try:
        operacao = input('Digite qual operação você quer fazer (+,-,*,/) ou digite 0 para sair:')
        if operacao == '0':
            break
        elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
            num1 = float(input('Digite o primeiro numero:'))
            num2 = float(input('Digite o segundo numero:'))
        else:
            print('Operacao invalida')
        if operacao == '+':
            print("O resultado da operação é:",soma(num1,num2))
        elif operacao == '-':
            print("O resultado da operação é:",subtracao(num1,num2))
        elif operacao == '*':
            print("O resultado da operação é:",multiplicacao(num1,num2))
        elif operacao == '/':
            if (num2 == 0):
                print("Não é possivel dividir por 0")
            else:
                print("O resultado da operação é:",divisao(num1,num2))
    except:
        print("O valor de entrada está incorreto!")
