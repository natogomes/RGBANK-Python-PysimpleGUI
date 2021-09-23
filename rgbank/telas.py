import PySimpleGUI as sg


def tela_login():
    sg.theme('DarkBlue16')
    login_frame = [
        [sg.Text('Conta', font='arial 15')],
        [sg.Input(font='arial 15', size=(15, 1), key='conta', do_not_clear=False),
         sg.Text('-'),
         sg.Input(size=(1, 1), font='arial 15', key='digito', do_not_clear=False)],
        [sg.Text('Senha', font='arial 15')],
        [sg.Input(font='arial 15', size=(20, 1), key='senha', password_char='*', do_not_clear=False)],
        [sg.Button('Login', font='arial 13', size=(8, 1))]
    ]
    layout = [
        [sg.Text('RGBANK', pad=((0, 450), 0), font=('Arial', 22, 'bold'))],
        [sg.Text('Seja bem vindo!', font='arial 20')],
        [sg.Frame(layout=login_frame, title='Login', pad=(0, 20))],
        [sg.Text('Não possui conta?', font='arial 13'), sg.Button('Abrir Conta',
                                                                  size=(12, 1), font='arial 13')],
        [sg.CloseButton('Sair', font='arial 13', size=(10, 1), pad=(0, 20))]
    ]
    telalog = sg.Window('Login', layout=layout, size=(600, 500), element_justification='center', finalize=True)


def tela_abrir_conta():
    sg.theme('DarkBlue16')

    dados_frame = [
        [sg.Text('Nome', font='arial 13', pad=(5, 0))],
        [sg.Input(font='arial 13', size=(25, 1), pad=(5, (0, 17)), key='nome', do_not_clear=False)],
        [sg.Text('Sobrenome', font='arial 13', pad=(5, 0))],
        [sg.Input(font='arial 13', size=(25, 1), pad=(5, (0, 17)), key='Snome', do_not_clear=False)],
        [sg.Text('CPF (Só números)', font='arial 13', pad=(5, 0))],
        [sg.Input(font='arial 13', size=(25, 1), pad=(5, (0, 17)), key='cpf', do_not_clear=False)],
        [sg.Text('Senha (6 dígitos)', font='arial 13', pad=(5, 0))],
        [sg.Input(font='arial 13', size=(25, 1), pad=(5, (0, 17)), key='senha1', do_not_clear=False)],
        [sg.Text('Confirmar Senha', font='arial 13', pad=(5, 0))],
        [sg.Input(font='arial 13', size=(25, 1), pad=(5, (0, 5)), key='senha2', do_not_clear=False)]
    ]

    layout = [
        [sg.Text('RGBANK', pad=((0, 450), 0), font=('Arial', 22, 'bold'))],
        [sg.Text('Abrir Conta', pad=(0, 0), font='arial 16')],
        [sg.Frame(layout=dados_frame, pad=(0, 0), title='Dados')],
        [sg.Button('Criar Conta', font='arial 13', size=(12, 1), pad=(10, 18)),
         sg.Button('Voltar', font='arial 13', size=(8, 1), pad=(10, 18))]
    ]
    tela_abrir_c = sg.Window('Abrir Conta', layout=layout, size=(600, 500), element_justification='center',
                             finalize=True, modal=True)


def tela_prin(cliente, conta):
    sg.theme('DarkBlue16')

    colunaE = [
        [sg.Button('Transferência', size=(13, 2), font=('Arial', 13, 'bold'), pad=(5, 10))],
        [sg.Button('Depósito', size=(13, 2), font=('Arial', 13, 'bold'))]
    ]
    colDados = [

        [sg.Text(f'Olá, {cliente.nome}!', font='arial 14')],
        [sg.Text(f'Conta: {conta.numero}', font='arial 14', key='tpnum')],
        [sg.Text('O que deseja fazer?', font='arial 14', key='tpsaldo')]
    ]
    colunaD = [
        [sg.Button('Saque', size=(13, 2), font=('Arial', 13, 'bold'), pad=(5, 10))],
        [sg.Button('Pagamentos', size=(13, 2), font=('Arial', 13, 'bold'))]
    ]

    layout = [
        [sg.Text('RGBANK', pad=((0, 450), 0), font=('Arial', 22, 'bold'))],
        [sg.Column(colunaE),
         sg.Column(colDados, pad=(30, 30)),
         sg.Column(colunaD)],
        [sg.Button('Voltar', font='arial 13', size=(8, 1)),
         sg.CButton('Sair', font='arial 13', size=(8, 1))],
        [sg.Button('Exibir extrato', font='arial 13', size=(14, 1), pad=(0, (25, 5)))],
        [sg.Output(size=(45, 6), font='arial 14', text_color='Black')]
    ]
    telap = sg.Window('RGBANK', layout=layout, size=(600, 500), element_justification='center',
                      modal=True, finalize=True)


def tela_transf():
    sg.theme('DarkBlue16')

    dados_frame = [
        [sg.Text('Conta destino', font='arial 15')],
        [sg.Input(font='arial 15', size=(15, 1), key='contaD'),
         sg.Text('-'),
         sg.Input(size=(1, 1), font='arial 15', key='digitoD')],
        [sg.Text('Valor', font='arial 15')],
        [sg.Input(size=(12, 1), font='arial 15', key='valorTr')],
    ]

    dados_destino = [
        [sg.Text('Dados do destinatário', size=(26, 1), font='arial 14', justification='center')],
        [sg.Text('Nome:', font='arial 13'),
         sg.Input('*' * 35, size=(30, 1), background_color='white', font=('Arial', 13, 'bold'),
                  text_color='#000000', key='nomeD')],
        [sg.Text('Valor da transferência: R$', font='arial 13'),
         sg.Input('0,00', size=(14, 1), background_color='white', font=('Arial', 13, 'bold'),
                  text_color='#000000', key='valorD')]
    ]

    layout = [
        [sg.Text('RGBANK', pad=((0, 450), 0), font=('Arial', 22, 'bold'))],
        [sg.Text('Transferência RGB', font='arial, 12', pad=(0, 0))],
        [sg.Frame(layout=dados_frame, title='', pad=(0, (0, 30)))],
        [sg.Button('OK', font='arial 13', size=(8, 1)),
         sg.Button('Voltar', font='arial 13', size=(8, 1))],
        [sg.Frame(layout=dados_destino, title='', pad=(30, 30))],
        [sg.Button('Confirmar', size=(10, 1), font='arial 13'),
         sg.CButton('Sair', size=(8, 1), font='arial 13')]
    ]
    telaTr = sg.Window('Transferência', layout=layout, size=(600, 500),
                       element_justification='center', modal=True, finalize=True)


def tela_deposito():
    sg.theme('DarkBlue16')

    dados_frame = [
        [sg.Text('Valor', font='arial 15')],
        [sg.Input(size=(12, 1), font='arial 15', key='valorInp')],
        [sg.Text('Conta destino', font='arial 15')],
        [sg.Input(font='arial 15', size=(15, 1), key='contaDp'),
         sg.Text('-'),
         sg.Input(size=(1, 1), font='arial 15', key='digitoDp')],
        [sg.Button('Em minha conta', font='arial 13', size=(23, 1))],
    ]

    dados_destino = [
        [sg.Text('Dados do destinatário', size=(26, 1), font='arial 14', justification='center')],
        [sg.Text('Nome:', font='arial 13'),
         sg.Input('*' * 35, size=(30, 1), background_color='white', font=('Arial', 13, 'bold'),
                  text_color='#000000', key='nomeDp')],
        [sg.Text('Valor do Depósito: R$', font='arial 13'),
         sg.Input('0,00', size=(12, 1), background_color='white', font=('Arial', 13, 'bold'),
                  text_color='#000000', key='valorDp')]
    ]

    layout = [
        [sg.Text('RGBANK', pad=((0, 450), 0), font=('Arial', 22, 'bold'))],
        [sg.Text('Depósito RGB', font='arial, 12', pad=(0, 0))],
        [sg.Frame(layout=dados_frame, title='', pad=(0, (0, 20)))],
        [sg.Button('OK', font='arial 13', size=(8, 1)),
         sg.Button('Voltar', font='arial 13', size=(8, 1))],
        [sg.Frame(layout=dados_destino, title='', pad=(30, 20))],
        [sg.Button('Confirmar', size=(10, 1), font='arial 13'),
         sg.CButton('Sair', size=(8, 1), font='arial 13')]
    ]
    telaDp = sg.Window('Depósito', layout=layout, size=(600, 500),
                       element_justification='center', modal=True, finalize=True)


def tela_saque():
    sg.theme('DarkBlue16')

    dados_frame = [
        [sg.Text('Valor', font='arial 15')],
        [sg.Text('R$:', font='arial 15'),
         sg.Input(size=(12, 1), font='arial 15', key='valorSq')],
        [sg.Text('Senha', font='arial 15', pad=(0, (10, 0)))],
        [sg.Input(font='arial 15', size=(20, 1), password_char='*', key='senhaSq')],
    ]

    dados_destino = [

        [sg.Text('Valor do Saque: R$', font='arial 13'),
         sg.Input('0,00', size=(12, 1), background_color='white', font=('Arial', 13, 'bold'),
                  text_color='#000000', key='valorS')]
    ]

    layout = [
        [sg.Text('RGBANK', pad=((0, 450), (0, 20)), font=('Arial', 22, 'bold'))],
        [sg.Text('Saque RGB', font='arial, 12', pad=(0, 0))],
        [sg.Frame(layout=dados_frame, title='', pad=(0, (0, 20)))],
        [sg.Button('OK', font='arial 13', size=(8, 1)),
         sg.Button('Voltar', font='arial 13', size=(8, 1))],
        [sg.Frame(layout=dados_destino, title='', pad=(0, 20))],
        [sg.Button('Confirmar', size=(10, 1), font='arial 13'),
         sg.CButton('Sair', size=(8, 1), font='arial 13')]
    ]

    telaSq = sg.Window('Saque', layout=layout, size=(600, 500),
                       element_justification='center', modal=True, finalize=True)


def tela_pagtos():
    sg.theme('DarkBlue16')

    dadosPg = [
        [sg.Text('Valor', font='arial 15')],
        [sg.Text('R$:', font='arial 15'),
         sg.Input(size=(12, 1), font='arial 15', key='valorPg')],
        [sg.Text('Senha', font='arial 15', pad=(0, (10, 0)))],
        [sg.Input(font='arial 15', size=(20, 1), password_char='*', key='senhaPg')],
    ]
    descricao = [
        [sg.Text('Descrição:', font='arial 13'),
         sg.Input(size=(23, 1), background_color='white', font=('Arial', 13, 'bold'),
                  text_color='#000000', key='descricao')]
    ]

    layout = [
        [sg.Text('RGBANK', pad=((0, 450), (0, 20)), font=('Arial', 22, 'bold'))],
        [sg.Text('Pagamentos RGB', font='arial, 12', pad=(0, 0))],
        [sg.Frame(layout=dadosPg, title='', pad=(0, (0, 20)))],
        [sg.Button('Voltar', font='arial 13', size=(8, 1))],
        [sg.Frame(layout=descricao, title='', pad=(0, 20))],
        [sg.Button('Confirmar', size=(10, 1), font='arial 13'),
         sg.CButton('Sair', size=(8, 1), font='arial 13')]
    ]

    telaPgt = sg.Window('Pagamentos', layout=layout, size=(600, 500), element_justification='center', modal=True, finalize=True)

