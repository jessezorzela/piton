class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def idade(self,ano):
        return 2022-ano
    

maik = Pessoa("Michael", "Moreira")
print(maik.nome, maik.sobrenome, maik.idade(1999))

vitao = Pessoa("Vitor", "Custodio")
print(vitao.nome, vitao.sobrenome, vitao.idade(1998))