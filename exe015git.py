#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('~~'*15)
print('Empresa de aluguel de carros')
print('~~'*15)
al = float(input('Dias alugados:'))
km = float(input('kilometros rodados:'))
pago= (al * 60) + (km * 0.15)
print(f'Voce rodou {km}km em {al} dias, sua conta ficou em R${pago}.')

print('~~'*15)
print('   Made by Andre Caliento')
print('~~'*15)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Empresa de aluguel de carros
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dias alugados:20
kilometros rodados:300
Voce rodou 300.0km em 20.0 dias, sua conta ficou em R$1245.0.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Made by Andre Caliento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
