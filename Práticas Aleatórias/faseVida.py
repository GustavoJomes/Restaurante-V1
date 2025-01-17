idade = input('Digite sua idade para saber em qual fase da vida você está: ')
idade = int(idade)
if idade < 13 and idade >= 0:
    print('Você é uma criança')
elif idade > 12 and idade < 19:
    print('Você é um adolescente')
else:
    print('Você é um adulto')