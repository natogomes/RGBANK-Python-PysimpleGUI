from random import randint
import PySimpleGUI as sg


def criar_conta(arquivo, nome, sobreN, cpf, senha1, senha2):

    num = randint(0000, 9999)
    dig = randint(1, 9)
    numero = f'{num}-{dig}'
    saldo = '0.00'
    nova_linha = f'{numero},{senha2},{saldo},{nome},{sobreN},{cpf}\n'

    try:
        a = open(arquivo, 'rt')
    except:
        sg.popup('Houve um ERRO ao abrir o arquivo!', font=("arial", 13), title='Criar Conta')
    else:
        try:
            linhas = []
            for linha in a:
                linhas.append(linha)
            linhas.append(nova_linha)

            try:
                a = open(arquivo, 'wt')
                for valor in linhas:
                    a.write(f'{valor}')
                a.close()
                sg.popup(f'{"Conta criada com sucesso!":^45}\n'
                         f'Faça LOGIN e comece a usar sua conta!', font=("arial", 13), title='Criar Conta')
            except:
                sg.popup('ERRO ao arquivar os dados!', font=("arial", 13), title='Criar Conta')

        except:
            sg.popup('ERRO ao ler dados!', font=("arial", 13), title='Criar Conta')

    finally:
        a.close()


def login(numero, senha, arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        sg.Popup('ERRO ao obter os dados!', font=("arial", 15), title='Login')
    else:
        try:
            conta = list()
            for valor in a:
                dados = valor.split(',')
                if dados[0] == numero and dados[1] == senha:
                    conta.append(dados[0])
                    conta.append(dados[1])
                    conta.append(dados[2])
                    conta.append(dados[3])
                    conta.append(dados[4])
                    conta.append(dados[5])
                    return conta
            return False

        except:
            sg.Popup('ERRO ao obter os dados!', font=("arial", 13), title='Login')

    finally:
        a.close()
