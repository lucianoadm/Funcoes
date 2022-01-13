from aulas_funcoes.funcoes_00 import *

minha_lista = []
print('Preenchendo')
preencher_inventario(minha_lista)
print('Exibindo')
exibir_inventario(minha_lista)

print('Pesquisando')
pesquisar_inventario(minha_lista)
print('Alterando')
depreciar_equipamento(minha_lista, 15)

print('Excluindo')
print(excluir_serial(minha_lista))
exibir_inventario(minha_lista)

print('Resumindo')
resumir_valores(minha_lista)
