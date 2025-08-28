print('App para conversão de material de pintura!')
print('-'*40)
a = float(input('altura da parede:'))
l = float(input('largura da parede:'))
m2 = a * l
gl = m2 / 2
#print('Para pintar uma parede com essa medidas voce ira gastar {}l de tinta'.format(gl))
print(f'''Para pintar uma parede de {a}m de altura x {l}m de largura com a area de {m2} m2,
serão necessarios {gl} l de tinta!''')

print('~~'*15)
print('    Made by Andre Caliento')
print('~~'*15)

App para conversão de material de pintura!
----------------------------------------
altura da parede:10
largura da parede:30
Para pintar uma parede de 10.0m de altura x 30.0m de largura com a area de 300.0 m2,
serão necessarios 150.0 l de tinta!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Made by Andre Caliento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~