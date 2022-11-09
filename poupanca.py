#Fazer um sistema de calculo de juros simples = poupança 
#Fazer um sistema de calculo de juros compostos = CDB
#VARIAVEL
#Valor, Meses e taxa de juros
taxa = 0.69
saldo = int(input("Digite quanto quer deixar:"))
meses = int(input("Digite por quantos meses quer deixar:"))

for i in range(meses):
    saldo += saldo * (taxa/100)

print("Seu saldo no final de {} é de R$ {:2f}".format(meses, saldo))

