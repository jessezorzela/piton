porcentagem = 11.60/12
saldo = int( input('Digite o valor que deseja aplicar no SDB:') )
meses = int( input('Meses que vai deixar rendendo: ') )

nmeses = meses * 30
nporcentagem = porcentagem/30

for i in range(nmeses):
   saldo += saldo * (nporcentagem/100)

print("Saldo depois de {} meses é de R${:.2f}".format(meses,saldo))