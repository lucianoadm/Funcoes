# criando algumas funções básicas

def colocar_linha():  # criando uma função para gerar linhas de separação
    print('-' * 30)

colocar_linha()

print()
# exemplo:
print('Hello, World!')
colocar_linha()
print('Sejam bem vindos!')
colocar_linha()
print()

def titulo(txt):  # criando uma função que receberá textos como título de algo
    print(txt)

titulo(' Hello, World!')
colocar_linha()
titulo('duas funções uma para inserir linha continúas e outra que recebe texto')
colocar_linha()
