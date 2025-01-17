import os
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, {'nome':'Pizza Suprema', 'categoria':'Italiana','ativo':True}, {'nome':'Cantina', 'categoria':'Italiano','ativo':False}]

def exibir_nome_do_programa():
    '''Exibe o título do programa utilizando print'''

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      """)

def exibir_opcoes():
    '''Exibe a lista de opções do usuário utilizando prints'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair')

def alterar_ativacao_restaurante():
    '''Altera a ativação do restaurante para o oposto da atual entre ativado-desativado'''
    exibir_subtitulo('Ativar/Desativar restaurante: ')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')
    voltar_ao_menu_principal()    

def finalizar_app():
    '''Limpa a tela do console e exibe uma mensagem de finalização do app'''
    os.system('cls')
    print('Finalizando o app\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu pincipal: ')
    main()

def exibir_subtitulo(texto):
    '''Limpa o console e exibe o subtítulo da opção selecionada no input'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)

def opcao_invalida():
    '''Acusa uma opção de ser inválida e ativa a função de retornar ao menu principal'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Lista os restaurantes que estão cadastrados até o momento no programa'''
    exibir_subtitulo('Lista de Restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''
    
    Inputs:
    - nome do restaurante
    - categoria
    
    Outputs:
    - Adciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de Novos Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    voltar_ao_menu_principal()

# receber imput em número inteiro
def escolher_opcao():
    '''Recebe um input, converte em número e ativa a opção escolhida dentre as apresentadas na função de listar as opções'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao_escolhida}')

        # lista de restaurantes
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_ativacao_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''inicia o programa, apresentantando o menu principal e apresentando as opções para que sejam escolhidas pelo usuário'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()