import PySimpleGUI as sg


def validacao_valor(valor):
    """
    -> Faz uma validação se o valor passado está no formato correto (float).
    :param valor: Passa o valor da transação.
    :return: Retorna o valor do parâmetro passado.
    """
    valor_form = str(valor).strip().replace(',', '.')
    try:
        valor_flt = float(valor_form)
    except (ValueError, TypeError):
        sg.popup('Informe um (VALOR) válido!', font='arial 13', title='Valor inválido')
    else:
        return valor


def validacao_num(num, dig=''):
    """
    -> Faz uma validação se o valor passado está no formato correto (int).
    :param num: Passa o valor do número da conta.
    :param dig: Passa o valor do dígito do número da conta.
    :return: Retorna o número e o dígito da conta.
    """
    num = str(num).strip()
    dig = str(dig).strip()

    if dig == '':
        try:
            num_int = str(num)

        except (ValueError, TypeError):
            sg.popup('Informe um (NÚMERO) válido!', font='arial 13', title='Número inválido')

        else:
            return f'{num}'
    else:
        if dig[0]:
            try:
                num_int = int(num)
                num_dig = int(dig)

            except (ValueError, TypeError):
                sg.popup('Informe um (DÍGITO) válido!', font='arial 13', title='Validação Número')

            else:
                return f'{num}-{dig}'


def validacao_dest(nome, valor):
    """
    -> Faz um print mostrando o nome e o valor caso o destino esteja válido.
    :param nome: Passa um valor em (***) no local onde vai ser printado o nome do destinatário.
    :param valor: Passa o valor (0,00) no local onde vai ser printado o valor da transação.
    :return: True, se caso os valores de entrada não foram alterados e False, se os valores foram
    atualizados para o destinatário.
    """

    if nome == '*' * 35 and valor == '0,00':
        sg.Popup('Clique (OK) para enviar os dados', font='arial 13', title='Conta Destino')
        return False
    else:
        return True


def validacao_cpf(cpf):
    """
    -> Faz a validação do valor do cpf para saber se será no formato (int).
    :param cpf: Passa o valor cpf.
    :return: False, caso o número não esteja no fomato correto (int) e True, se tiver tudo OK.
    """

    while True:
        try:
            cpf = int(cpf)
        except:
            sg.Popup('Informe um CPF válido!', font=("arial", 13), title='CPF inválido')
            return False
        else:
            return True


def valid_criar_senha(senha1, senha2):
    """
    -> Validação feita para criação de senha na janela de abrir conta
    :param senha1: Passa a primeira senha digitada.
    :param senha2: passa a segunda senha digitada.
    :return: False, caso as senhas estajam diferentes, e True, se tiverem iguais.
    """
    if senha1 == senha2:
        return True
    else:
        sg.Popup('As senha não correspondem!', font=("arial", 13), title='Senha inválida')
        return False


