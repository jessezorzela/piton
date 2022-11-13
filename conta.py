from tokenize import Double


class conta_corrente:
    def __init__(self) -> None:
        self.agencia = ''
        self.conta = ''
        self.senha = ''
        self.saldo = 0
        self.autenticado = False

    def depositar(self, valor):	
        self.saldo += valor
        self.extrato(valor)

    def sacar(self, valor):	
        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato(-valor)
        else:
            print('Saldo insuficiente.')
    
    def extrato(self, ultimo = 0):
        print()
        print('-' * 40)
        print(f'                EXTRATO           ')
        print('-' * 40)
        print('LANÇAMENTOS')
        if ultimo > 0:
            print(f' DEPÓSITO ATM |     CRÉDITO {ultimo:.2F} ')
        print('              |                |')
        print('              |                |')
        print('-' * 40)
        print(f'                        SALDO: R$ {self.saldo:.2F}')
        print('-' * 40)
        print('             FIM DO EXTRATO				  ')
        print('-' * 40)
        aperte = input('Aperte ENTER para retornar ao MENU\nou (X e ENTER) para sair: ')
        if aperte == 'X' or aperte == 'x': 
            exit()
        else:
            self.executa()
            
        executa = True
        while executa:
            print("Informe o que voce deseja fazer \n \
1 - Abrir uma nova conta\n \
2 - Acessar uma conta\n \
3 - Depositar \n \
4 - Sacar\n \
5 - Ver Saldo \n \
0 - Sair")
            comando = int(input())
            if comando == 0:
                executa = False
            if comando == 1:
                self.agencia = input("informe sua agência> ")
                self.conta = input("informe o numero da conta> ")
                self.senha = input("informe sua senha> ")
            if comando == 2:
                self.agencia = input("informe sua agência> ")
                self.conta = input("informe o numero da conta> ")
                self.senha = input("informe sua senha> ")
            if comando == 3:
                valor = float(input('Digite o valor a ser depositado: '))
                self.depositar(valor)
            if comando == 4:
                self.extrato(-valor)
            if comando == 5:
                self.extrato()
