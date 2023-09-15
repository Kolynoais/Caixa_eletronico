TIPO_E="E"

TIPO_N="N"

limite=0

print("informe qual e o tipo do cartão,N para normal e E para especial:",end=" ")

tipo_do_cartao=input("")

if tipo_do_cartao in TIPO_N:
    limite=5000.0
elif tipo_do_cartao in TIPO_E:
    limite=100000000.0

print("O limite é",limite,"informe o quanto deseja sacar:",end=" ")

saque=float(input(""))

if limite  >= saque:
    novo_limite=limite-saque
    print("Transação realizada! O novo limite e de",novo_limite)
else:
    print("A transação não foi realizado pois passou do limite definido")