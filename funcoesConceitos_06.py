# criando uma função de boas vindas

def minha_funcao(nome):
    frase = 'Este é um seja bem vindo! criado por: {}!'.format(nome)
    print(frase)
    return frase

minha_funcao('luciano')