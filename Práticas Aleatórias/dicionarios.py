import os
os.system('cls')
pessoas = [{'nome':'Rodrigo', 'idade':15, 'cidade':'Blumenau'}, {'nome':'João', 'idade':30, 'cidade':'Itajai'}, {'nome':'Wender', 'idade':8, 'cidade':'Floripa'}]
numeros_quadrados = [{'numero':1, 'quadrado':1}, {'numero':2, 'quadrado':4}, {'numero':3, 'quadrado':9}, {'numero':4, 'quadrado':16}, {'numero':5, 'quadrado':25}]
pessoas[0]['idade'] = 20

def main():
    exibir_subtitulos('Menu')
    menu()

def menu():
    print('1. Dados cadastrais')
    print('2. Números quadrados')
    print('3. Sair\n')
    opcao_selecionada = int(input('Digite qual lista imprimir: '))
    if opcao_selecionada == 1:
        apresentar_nomes()
    elif opcao_selecionada == 2:
        apresentar_numeros_quadrados()

def apresentar_numeros_quadrados():
    exibir_subtitulos('Números quadrados')
    for numero in numeros_quadrados:
        
        print(f'{numero['numero']} --> {numero['quadrado']}')
    voltar_menu()

def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha+ '\n')

def voltar_menu():
    input('Clique qualquer tecla para voltar ao menu: ')
    os.system('cls')
    main()

def apresentar_nomes():
    exibir_subtitulos('Dados cadastrais')
    for pessoa in pessoas:
        nome_pessoa = pessoa['nome']
        idade_pessoa = pessoa['idade']
        cidade_pessoa = pessoa['cidade']
        print(f'Nome: {nome_pessoa}')
        print(f'Idade: {idade_pessoa}')
        print(f'Cidade: {cidade_pessoa}\n')
    voltar_menu()

if __name__ == '__main__':
    main()