from tokenize import Double


class conta_corrente:
    def __init__(self) -> None:
        self.agencia = ''
        self.conta = ''
        self.senha = ''
        self.saldo = 0.00
        self.autenticado = False


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
                pass
            if comando == 3:
                self.agencia = input("informe o valor do deposito> ")
                pass
            if comando == 4:
                self.agencia = input("informe o valor do deposito> ")
                pass
            if comando == 5:
                print("Seu saldo é de" self.saldo)
                pass
            
    def get_saldo(self):
        return self.saldo

    def deposita(self,valor: float):
        if valor > 0:
            self.saldo += valor
        else:
            print('Valor para deposito tem que ser maior que zero')


    def get_agencia(self):
        return self.agencia

    def ag(self,valor: float):
        return self.agencia

    def get_conta(self):
        return self.conta

    def con(self,valor: float):
        return self.conta

    def get_senha(self):
        return self.senha

    def sen(self,valor: float):
        return self.senha


    def get_saldo(self):
        return self.saldo

    def deposita(self,valor: float):
        if valor > 0:
            self.saldo += valor
        else:
            print('Valor para deposito tem que ser maior que zero')
        

    def saca(self,valor: float):
        if valor <= self.saldo and valor > 0:
            self.saldo = self.saldo - valor 
        elif valor == 0:
            print('O valor a ser sacado tem que ser maior que zero!')  
        else:
            print('O valor a ser sacado não pode ser menor ou igual o saldo')        

conta = conta_corrente()


