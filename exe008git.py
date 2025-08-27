#Exercício Python 8: Escreva um programa que leia um valor 
#em metros e o exiba convertido em centímetros e milímetros.

d= float (input('Didite uma distancia em metros:'))
md1 = d/1000
md2 = d/100
md3 = d/10
md4 = d*10
md5 = d*100
md6 = d*1000
#print('A medida de',d,'corresponde\n{}km\n{}hm\n{}am\n{}dm\n{}cm\n{}mm'.format(md1,md2,md3,md4,md5,md6))
print(f'A medida {d}m corresponde a :')
print(f'{md1}km')
print(f'{md2}hm')
print(f'{md3}am')
print(f'{md4}dm')
print(f'{md5}cm')
print(f'{md6}mm')

print('Made by Andre Caliento')

Didite uma distancia em metros:5
A medida 5.0m corresponde a :
0.005km
0.05hm
0.5am
50.0dm
500.0cm
5000.0mm
Made by Andre Caliento
