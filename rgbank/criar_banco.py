import PySimpleGUI as sg


def verif_arq(nome):
    """
    -> Verifica toda vez que for iniciado, se ja existe um arquivo de texto criado
     (que usaremos como base de dados)
    :param nome: Passa o nome do arquivo.
    :return: Se False, o arquivo não existe. E se True, o arquivo ja foi criado.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arq(nome):
    """
    -> Cria um arquivo de texto (que aqui usaremos como banco de dados)
    :param nome: Passa o nome do arquivo a ser criado.
    :return: Sem retorno
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        sg.popup('Houve um ERRO ao criar os dados!', font=("arial", 13), title='Arquivar Dados')
