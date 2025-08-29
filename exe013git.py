#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.
print('~~'*15)
print('Anuncio de aumento de salario.')
print('~~'*15)
s = float(input('Salario medio da empresa: R$'))
a = float(input('Aumento: '))
sa= s+(s*a/100)
#print('Todos os funcionarios que ganham R${:.2f} teram um aumento de {:.2f}% e o salario ficara em:R${:.2f}'.format(s,a,sa))
print(f'Todos os funcionarios que ganham R${s} teram o aumento de {a}%!')
print(f'Com o novo aumento o salario ficara com o valor de R${sa}!')
print('~~'*15)
print('     Made by Andre Caliento')
print('~~'*15)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Anuncio de aumento de salario.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Salario medio da empresa: R$2000
Aumento: 15
Todos os funcionarios que ganham R$2000.0 teram o aumento de 15.0%!
Com o novo aumento o salario ficara com o valor de R$2300.0!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Made by Andre Caliento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~