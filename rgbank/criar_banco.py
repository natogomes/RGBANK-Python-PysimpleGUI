import PySimpleGUI as sg


def verif_arq(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        sg.popup('Houve um ERRO ao criar os dados!', font=("arial", 15), title='Criar Arquivos')