saldo_da_conta=1000.50

exibir_o_extrato_ou_nao="N"

quantidade_de_depositos_diarios=0

quantidade_de_saques_diarios=0

while exibir_o_extrato_ou_nao=="N":
    atividade=input("O que deseja fazer? D para deposito(pode fazer 3 diariamente de R$ 500,00) S para saque e E para extrato.")

    if atividade=="S":

        valor_do_saque=float(input("de quanto é o saque?"))

        if valor_do_saque<0:
            print("saque negativo não é permitido.")
            exibir_o_extrato_ou_nao="S"

        elif valor_do_saque>saldo_da_conta:
            print("o valor do saque ultrapassou o saldo da conta.")
            exibir_o_extrato_ou_nao="S" 

        quantidade_de_saques_diarios=quantidade_de_saques_diarios+1

        if valor_do_saque>0 and valor_do_saque<saldo_da_conta:
            saldo_da_conta=saldo_da_conta-valor_do_saque

        if valor_do_saque>0 and valor_do_saque<saldo_da_conta:
            print("sua conta contem R$",saldo_da_conta)

    elif atividade=="D":

        quantidade_do_deposito=float(input("informe a quantidade do deposito (não pode ultrapassar R$ 500,00)."))

        if quantidade_do_deposito<0:
            print("deposito negativo não é permitido.")
            exibir_o_extrato_ou_nao="S"

        elif quantidade_do_deposito>500.00:
            print("deposito passou R$500,00.")
            exibir_o_extrato_ou_nao="S"

        elif quantidade_de_depositos_diarios>=3:
            print("limite de depositos alcançado.")
            exibir_o_extrato_ou_nao="S"

        quantidade_de_depositos_diarios=quantidade_de_depositos_diarios+1

        if quantidade_do_deposito<500.00 and quantidade_do_deposito>0 and quantidade_de_depositos_diarios<=3:
            saldo_da_conta=saldo_da_conta+quantidade_do_deposito

        if quantidade_do_deposito<500.00 and quantidade_do_deposito>0 and quantidade_de_depositos_diarios<=3:
            print("sua conta contem R$",saldo_da_conta)

    elif atividade == "E":
        exibir_o_extrato_ou_nao="S"
else:
    print(F""".....................................
Quantidade de depositos:""",quantidade_de_depositos_diarios,F"""
.....................................
quantidade de saques:""",quantidade_de_saques_diarios,F"""
.....................................
saldo atual:""",saldo_da_conta)
    
