import PySimpleGUI as sg


def validacao_valor(valor):
    valor_form = str(valor).strip().replace(',', '.')
    try:
        valor_flt = float(valor_form)
    except (ValueError, TypeError):
        sg.popup('Informe um (VALOR) válido!', font='arial 12')
    else:
        return valor


def validacao_num(num, dig=''):
    num = str(num).strip()
    dig = str(dig).strip()

    if dig == '':
        try:
            num_int = str(num)

        except (ValueError, TypeError):
            sg.popup('Informe um (NÚMERO) válido!', font='arial 12')

        else:
            return f'{num}'
    else:
        if dig[0]:
            try:
                num_int = int(num)
                num_dig = int(dig)

            except (ValueError, TypeError):
                sg.popup('Informe um (NÚMERO2) válido!', font='arial 12')

            else:
                return f'{num}-{dig}'


def validacao_dest(nome, valor):

    if nome == '*' * 35 and valor == '0,00':
        sg.Popup('Clique (OK) para enviar os dados', font='arial 12')
        return False
    else:
        return True


def validacao_cpf(cpf):
    valid = ''
    while True:
        try:
            cpf = int(cpf)
        except:
            sg.popup('Informe um CPF válido!', font='arial 12')
            valid = False
            return valid
        else:
            valid = True
            return valid