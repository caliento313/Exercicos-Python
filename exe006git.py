#Exercício Python 006: Crie um algoritmo que leia um número
# e mostre o seu dobro, triplo e raiz quadrada.

n = int (input('digite um numero: '))

#print('o dodro de {} e {}\no triplo de {} e {}\nraiz quadrada de {} e {:.2f}'.format(n,n*2,n,n*3,n,n**(1/2)))

n1 = n*2
n2 = n*3
n3 = n**(1/2)
print(f'O dobro de {n} é {n1}!')
print(f'O triplo de {n} é {n2}!')
print(f'A raiz quadrada de {n} é {n3:.2f}!')

# Resposta:

Digite um numero: 10
O dobro de 10 é 20!
O triplo de 10 é 30!
A raiz quadrada de 10 é 3.16!

# Made by Andre Caliento
