x = input('Digite o eixo y ')
y = input('Digite o eixo X ')
x = float(x)
y = float(y)
if x > 0 and y > 0:
    print('Primeiro Quadrante!')
elif x < 0 and y > 0:
    print('Segundo Quadrante!')
elif x < 0 and y < 0:
    print('Terceiro Quadrante!')
elif x > 0 and y < 0:
    print('Quarto Quadrante!')
else:
    print('O ponto está localizado no eixo ou origem!')