# utilizando os dados do exerciocios de listas,
# vamos criar funções para cada módulo do exercicio


# transformando o módulo de recebimento de dados em uma função
def preencher_inventario(lista):
    resposta = 'C'
    while resposta == 'C':
        equipamentos = [input('Digite o equipamento: '),
                    float(input('Digite o valor: ')),
                    int(input('Digite o serial: ')),
                    input('Digite o setor: ')]
        lista.append(equipamentos)
        resposta = input('Digite \'C\' para continuar ou \'S\' para sair: ').upper()


# exibição dos dados do inventário
def exibir_inventario(lista):
    for dados in lista:
        print(f'Equipamento....: {dados[0]}')
        print(f'Valor..........: {dados[1]}')
        print(f'Serial.........: {dados[2]}')
        print(f'Setor..........: {dados[3]}')
        print()


# pesquisando um elemento do inventário
def pesquisar_inventario(lista):
    pesquisa = input('Digite o equipamento que deseja pesquisar: ')
    for dados in lista:
        if pesquisa == dados[0]:
            print(f'Valor......: {dados[1]}')
            print(f'Serial.....: {dados[2]}')

# depreciando um ítem
def depreciar_equipamento(lista, porc):
    depreciacao = input('Digite o nome do equipamento que deseja depreciar: ')
    for dados in lista:
        if depreciacao == dados[0]:
            print(f'Valor normal......: {dados[1]}')
            depreciado = dados[1] * (1-porc/100)
            print(f'Valor depreciado....: {depreciado}')

# eliminando um ítem do inventário
def excluir_serial(lista):
    excluir = int(input('Digite o serial que deseja excluir: '))
    for dados in lista:
        if excluir == dados[2]:
            lista.remove(dados)

# valores
def resumir_valores(lista):
    valores = []
    for dados in lista:
        valores.append(dados[1])
    if len(valores) > 0:
        print(f'Equipamento mais caro.....: {max(valores)}')
        print(f'Equipamento mais barato...: {min(valores)}')
        print(f'Total dos equipamentos...: {sum(valores)}')
