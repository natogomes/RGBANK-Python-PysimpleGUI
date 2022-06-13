from rgbank.janelas import *
from rgbank.validacao import *
from rgbank.criar_banco import *
from rgbank.conta_login import *
from rgbank.classes import *
import PySimpleGUI as sg


# CRIA UM ARQUIVO DE TEXTO QUE AQUI USAMOS COMO BANCO DE DADOS
banco_dados = 'dados.txt'
if not verif_arq(banco_dados):
    criar_arq(banco_dados)

# ABRE A JANELA DE ENTRADA (LOGIN)
tela_login()
while True:
    window, event, values = sg.read_all_windows()
    conta_num = f'{values["conta"].strip()}-{values["digito"].strip()}'
    senha = values['senha'].strip()

    if event == sg.WIN_CLOSED:
        break

# FAZ LOGIN E ABRE A JANELA PRINCIPAL DO PROGRAMA
    elif event == 'Login':
        log = login(conta_num, senha, banco_dados)
        if log:
            dados_log = []
            for i in log:
                dados_log.append(i)
            cliente = Cliente(dados_log[3], dados_log[4], dados_log[5])
            cliente_conta = Conta(dados_log[0], dados_log[1], dados_log[2], cliente)

            tela_p = tela_prin(cliente, cliente_conta)
            window.close()
            while True:
                window, event, values = sg.read_all_windows()

                if event == sg.WIN_CLOSED:
                    exit()

                elif event == 'Voltar':
                    tela_login()
                    window.close()
                    break

                elif event == 'Transferência':
                    tela_transf()
                    window.close()
                    while True:
                        window, event, values = sg.read_all_windows()
                        num_dest = f'{values["contaD".strip()]}-{values["digitoD".strip()]}'

                        if event == sg.WIN_CLOSED:
                            exit()

                        elif event == 'OK':

                            if validacao_valor(values['valorTr']):
                                dados = cliente_conta.consulta(banco_dados, num_dest)
                                if dados:
                                    cliente_transf = Cliente(dados[3], dados[4], dados[5])
                                    cliente_conta_transf = Conta(dados[0], dados[1], dados[2], cliente_transf)

                                    window['nomeD'].update(f'{cliente_transf.nome} {cliente_transf.sobrenome}')
                                    window['valorD'].update(values['valorTr'.strip()])
                                else:
                                    sg.popup('Informe um número válido!', font='arial 13', title='Erro')
                                    window['contaD'].update('')
                                    window['digitoD'].update('')
                            else:
                                window['valorTr'].update('')

                        elif event == 'Confirmar':
                            if validacao_dest(values['nomeD'], values['valorD']):

                                if validacao_valor(values['valorTr']) and validacao_num(values["contaD"],
                                                                                         values["digitoD"]):
                                    num_dest = validacao_num(values["contaD"], values["digitoD"])
                                    cliente_conta.transfer(banco_dados, values['valorTr'].strip(),
                                                           num_dest)
                                    window.close()
                                    tela_prin(cliente, cliente_conta)
                                    break
                                else:
                                    window['valorTr'].update('')
                                    window['contaD'].update('')
                                    window['digitoD'].update('')

                        elif event == 'Voltar':
                            window.close()
                            tela_prin(cliente, cliente_conta)
                            break

                elif event == 'Depósito':
                    tela_deposito()
                    window.close()
                    while True:
                        window, event, values = sg.read_all_windows()

                        if event == sg.WIN_CLOSED:
                            exit()

                        elif event == 'Voltar':
                            window.close()
                            tela_prin(cliente, cliente_conta)
                            break

                        elif event == 'Em minha conta':

                            if validacao_valor(values['valorInp']):
                                window['contaDp'].update(cliente_conta.numero.strip())
                                window['nomeDp'].update(f'{cliente.nome.strip()} {cliente.sobrenome.strip()}')
                                window['valorDp'].update(validacao_valor(values['valorInp'].strip()))
                                sg.Popup('Verifique os dados e (CONFIRMAR)', font='arial 13', title='Confirmar')
                            else:
                                window['valorInp'].update('')

                        elif event == 'OK':

                            if validacao_valor(values['valorInp']):
                                num_dest = f'{values["contaDp"].strip()}-{values["digitoDp"].strip()}'
                                dados = cliente_conta.consulta(banco_dados, num_dest)
                                if dados:
                                    cliente_dep = Cliente(dados[3], dados[4], dados[5])
                                    cliente_conta_dep = Conta(dados[0], dados[1], dados[2], cliente_dep)

                                    window['nomeDp'].update(f'{cliente_dep.nome} {cliente_dep.sobrenome}')
                                    window['valorDp'].update(values['valorInp'].strip())
                                else:
                                    sg.popup('Informe um número válido!', font='arial 13', title='Erro')
                                    window['contaDp'].update('')
                                    window['digitoDp'].update('')
                            else:
                                window['valorInp'].update('')

                        elif event == 'Confirmar':

                            if validacao_dest(values['nomeDp'], values['valorDp']):

                                if validacao_valor(values['valorInp']) and\
                                        validacao_num(values["contaDp"], values["digitoDp"]):
                                    num_dest = validacao_num(values["contaDp"], values["digitoDp"])

                                    if values['digitoDp'] == '':
                                        cliente_conta.deposito(banco_dados, values['valorInp'].strip(),
                                                               num_dest, contaDestino=False)
                                    else:
                                        cliente_conta.deposito(banco_dados, values['valorInp'].strip(),
                                                               num_dest, contaDestino=True)

                                    window.close()
                                    tela_prin(cliente, cliente_conta)
                                    break
                                else:
                                    window['valorInp'].update('')
                                    window['contaDp'].update('')
                                    window['digitoDp'].update('')

                elif event == 'Saque':
                    tela_saque()
                    window.close()
                    while True:
                        window, event, values = sg.read_all_windows()

                        if event == sg.WIN_CLOSED:
                            exit()

                        elif event == 'Voltar':
                            window.close()
                            tela_prin(cliente, cliente_conta)
                            break

                        elif event == 'OK':
                            if validacao_valor(values['valorSq']):
                                if values['senhaSq'] == '':
                                    sg.popup('Informe sua senha!', font='arial 13', title='Saque')
                                else:
                                    window['valorS'].update(values['valorSq'])
                            else:
                                window['valorSq'].update('')

                        elif event == 'Confirmar':
                            if values['valorS'] == '0,00':
                                sg.popup('Clique (OK) para confirmar o valor', font='arial 13', title='Saque')
                                continue

                            if cliente_conta.saca(banco_dados, values['valorSq'], values['senhaSq']):
                                window.close()
                                tela_prin(cliente, cliente_conta)
                                break
                            else:
                                window['senhaSq'].update('')
                                continue

                elif event == 'Pagamentos':
                    tela_pagtos()
                    window.close()
                    while True:
                        window, event, values = sg.read_all_windows()

                        if event == sg.WIN_CLOSED:
                            exit()

                        elif event == 'Voltar':
                            window.close()
                            tela_prin(cliente, cliente_conta)
                            break

                        elif event == 'Confirmar':
                            if validacao_valor(values['valorPg']):
                                if values['senhaPg'] == '':
                                    sg.popup('Informe sua senha!', font='arial 13', title='Pagamentos')
                                    continue

                                else:
                                    if cliente_conta.pagtos(banco_dados, values['valorPg'], values['senhaPg'],
                                                            values['descricao']):
                                        window.close()
                                        tela_prin(cliente, cliente_conta)
                                        break
                                    else:
                                        window['senhaPg'].update('')
                                        continue

                            else:
                                window['valorPg'].update('')

                elif event == 'Exibir extrato':
                    cliente_conta.print_mov()

        elif not log:
            sg.popup('Número ou senha inválido!', font='arial 13', title='Login')
            window['conta'].update('')
            window['digito'].update('')
            window['senha'].update('')

# ABRE UMA JANELA PARA CRIAR CONTA
    elif event == 'Abrir Conta':
        window.close()
        tela_abrir_conta()
        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED:
                exit()

            elif event == 'Voltar':
                window.close()
                tela_login()
                break

            elif event == 'Criar Conta':

                nome = values['nome'].strip().title()
                sobreN = values['Snome'].strip().title()
                cpf = values['cpf'].strip()
                senha1 = values['senha1'].strip()
                senha2 = values['senha2'].strip()

                if nome == '' or sobreN == '' or cpf == '' or senha1 == '' or senha2 == '':
                    sg.Popup('Verifique se todos os campos estão preenchidos.', font='arial 13', title='Erro')

                elif validacao_cpf(cpf):
                    if valid_criar_senha(senha1, senha2):
                        criar_conta(banco_dados, nome, sobreN, cpf, senha2)
                        window.close()
                        tela_login()
                        break

                window['nome'].update(values['nome'])
                window['Snome'].update(values['Snome'])
                window['cpf'].update(values['cpf'])










