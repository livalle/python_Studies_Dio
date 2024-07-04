#Estrutura condicional aninhada
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal: #este é um if "primario"
    if saldo >= saque: #este é o if aninhado dentro do outro if
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque! Saldo insuficiente!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

        #Agora uma condição ternaria, ou seja escrita em uma unica linha:

status = "Sucesso" if saldo >= saque else "Falha" #o cod. check if true, e imprime oq está antes do if, caso contrario imprime a 3 parte que é pos if
print(f"{status} ao realizar o saque!")
