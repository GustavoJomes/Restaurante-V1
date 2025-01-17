import os
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nomes = ['Ciri', 'Triss', 'Yenneffer', 'Gerald']
lista_anos = [2002, 2025]

def main():
    os.system('cls')
    imprimir_menu()

def imprimir_menu():
    os.system('cls')
    print('Qual lista você deseja imprimir?\n')
    print('1. lista de números')
    print('2. lista de nomes')
    print('3. lista de anos')
    print('4. sair\n')

    selecao = int(input('Digite a lista aqui: '))
    

    if selecao == 1:
        imprimir_lista_numeros()
    elif selecao == 2:
        imprimir_lista_nomes()
    elif selecao == 3:
        imprimir_lista_anos()
    elif selecao == 4:
        os.system('cls')
        print('Programa finalizado!\n')
    else:
        print('Número inválido!')
        voltar_ao_menu()


def voltar_ao_menu():
    input('\nClique qualquer tecla para voltar ao menu')
    os.system('cls')
    imprimir_menu()


def imprimir_lista_numeros():
    try:
        for numeros in lista_numeros:
            print(int(numeros))

    except ValueError:
        print('Erro na exibição da lista')
    voltar_ao_menu()

def imprimir_lista_nomes():
    try:
        for nomes in lista_nomes:
            print(nomes)

    except ValueError:
        print('Erro na exibição da lista')
    voltar_ao_menu()

def imprimir_lista_anos():
    try:
        for anos in lista_anos:
            print(anos)
            
    except ValueError:
        print('Erro na exibição da lista')
    voltar_ao_menu()

if __name__ == '__main__':
    main()