import PySimpleGUI as sg
from datetime import datetime

data_hora = datetime.today()


class Extrato:
    def __init__(self):
        self._movimentacao = []

    def imprime_mov(self):
        print('Movimentaçãoes:')
        for m in self._movimentacao:
            print('-', m)

    @property
    def movimentacao(self):
        return self._movimentacao


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def cpf(self):
        return self.cpf


class Conta:
    def __init__(self, num, senha, saldo, cliente):
        self._numero = num
        self._senha = senha
        self._cliente = cliente
        self._saldo = saldo
        self._extrato = Extrato()
        self.sal = float(self._saldo)
        self.descricao = ''

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    def deposito(self, arquivo, valor, numeroD='', contaDestino=False):
        valor = str(valor).replace(',', '.')
        v = float(valor)

        try:
            a = open(arquivo, 'rt')
        except:
            sg.popup('Houve um ERRO ao abrir o arquivo!', font=("arial", 13), title='Depósito')
        else:
            try:
                c = 0
                linhas = []
                for linha in a:
                    linhas.append(linha)

                for dados in linhas:
                    dado = dados.split(',')

                    if contaDestino:
                        if dado[0] in numeroD:
                            self.descricao = f'{dado[3]} {dado[4]}'
                            tot = float(dado[2]) + v
                            dado[2] = f'{tot:.2f}'
                            linha_atualizada = f'{dado[0]},{dado[1]},{dado[2]},{dado[3]},{dado[4]},{dado[5]}'
                            linhas[c] = linha_atualizada
                        c += 1
                    else:
                        if dado[0] in self._numero:
                            self.descricao = f'{dado[3]} {dado[4]}'
                            self.sal += v
                            dado[2] = f'{self.sal:.2f}'
                            linha_atualizada = f'{dado[0]},{dado[1]},{dado[2]},{dado[3]},{dado[4]},{dado[5]}'
                            linhas[c] = linha_atualizada
                        c += 1

                try:
                    a = open(arquivo, 'wt')
                    for valor in linhas:
                        a.write(f'{valor}')
                    a.close()
                    sg.popup('Depósito feito com sucesso!', font=("arial", 13), title='Depósito')

                except:
                    sg.Popup('ERRO ao arquivar dados!', font=("arial", 13), title='Depósito')
            except:
                sg.popup('Houve um ERRO ao ler o aquivo!', font=("arial", 13), title='Depósito')
        finally:
            a.close()

        self._extrato.movimentacao.append(f'Depósito de R$:{v:.2f} - {datetime.strftime(data_hora, "%d/%m/%y - %H:%Mh")}\n'
                                          f'Destino >> {self.descricao}\n')

    def saca(self, arquivo, valor, senha):
        valor = str(valor).replace(',', '.')
        v = float(valor)

        try:
            a = open(arquivo, 'rt')
        except:
            sg.popup('Houve um ERRO ao abrir o arquivo!', font=("arial", 13), title='Saque')
        else:
            try:
                c = 0
                linhas = []
                valid = ''

                for linha in a:
                    linhas.append(linha)

                for dados in linhas:
                    dado = dados.split(',')

                    if senha == self._senha:
                        self.sal = float(dado[2]) - v
                        if self.sal < 0:
                            sg.popup('Você não tem saldo suficiente!', font=("arial", 13), title='Saque')
                            self.sal = 0
                            valid = True
                            return valid
                        else:
                            dado[2] = f'{self.sal:.2f}'
                            linha_atualizada = f'{dado[0]},{dado[1]},{dado[2]},{dado[3]},{dado[4]},{dado[5]}'
                            linhas[c] = linha_atualizada
                            valid = True
                            break
                    c += 1

                    if c == len(linhas):
                        sg.popup('  Senha inválida!  ', font=("arial", 13), title='Saque')
                        valid = False

                if valid:
                    try:
                        a = open(arquivo, 'wt')
                        for valor in linhas:
                            a.write(f'{valor}')
                        a.close()
                        sg.popup(f'Saque de R$:{v:.2f}\nRetire suas cédulas! '.replace('.', ','),
                                 font=("arial", 13), title='Saque')
                        self._extrato.movimentacao.append(f'Saque de {v:.2f} - '
                                                          f'{datetime.strftime(data_hora, "%d/%m/%y - %H:%Mh")}\n')
                        return valid

                    except:
                        sg.Popup('ERRO na gravação dos dados!', font=("arial", 13), title='Saque')


            except:
                sg.popup('Houve um ERRO ao ler o aquivo!', font=("arial", 13), title='Saque')
        finally:
            a.close()

    def pagtos(self, arquivo, valor, senha, descricao):

        valor = str(valor).replace(',', '.')
        v = float(valor)

        try:
            a = open(arquivo, 'rt')
        except:
            sg.popup('Houve um ERRO ao abrir o arquivo!', font=("arial", 13), title='Pagamentos')
        else:
            try:
                c = 0
                linhas = []
                valid = ''

                for linha in a:
                    linhas.append(linha)

                for dados in linhas:
                    dado = dados.split(',')

                    if senha == self._senha:
                        self.sal = float(dado[2]) - v
                        if self.sal < 0:
                            sg.popup('Você não tem saldo suficiente!', font=("arial", 13), title='Pagamentos')
                            self.sal = 0
                            valid = True
                            return valid

                        else:
                            dado[2] = f'{self.sal:.2f}'
                            linha_atualizada = f'{dado[0]},{dado[1]},{dado[2]},{dado[3]},{dado[4]},{dado[5]}'
                            linhas[c] = linha_atualizada
                            valid = True
                            break
                    c += 1

                    if c == len(linhas):
                        sg.popup('  Senha inválida!  ', font=("arial", 13), title='Pagamentos')
                        valid = False

                if valid:
                    try:
                        a = open(arquivo, 'wt')
                        for valor in linhas:
                            a.write(f'{valor}')
                        a.close()
                        sg.popup(f'Pagamento Realizado com sucesso!\n'
                                 f'{"valor R$:":>25}{v:.2f}'.replace('.', ','),
                                 font=("arial", 13), title='Pagamentos')
                        self._extrato.movimentacao.append(f'Fatura de {v:.2f} - '
                                                          f'{datetime.strftime(data_hora, "%d/%m/%y - %H:%Mh")}\n'
                                                          f'Descrição >> {descricao}\n')
                        return valid

                    except:
                        sg.Popup('ERRO na gravação dos dados!', font=("arial", 13), title='Pagamentos')

            except:
                sg.popup('Houve um ERRO ao ler o aquivo!', font=("arial", 13), title='Pagamentos')
        finally:
            a.close()

    def transfer(self, arquivo, valor, numD):
        valor = str(valor).replace(',', '.')
        v = float(valor)
        try:
            a = open(arquivo, 'rt')
        except:
            sg.popup('Houve um ERRO ao abrir o arquivo!', font=("arial", 13), title='Transferência')
        else:
            try:
                valid = False
                linhas = []
                for linha in a:
                    linhas.append(linha)
                conta_dep = 0
                conta_des = 0
                for dados in linhas:
                    dado = dados.split(',')
                    if dado[0] in self._numero:
                        self.sal = float(dado[2]) - v
                        if self.sal < 0:
                            sg.popup('Você não tem saldo suficiente!', font=("arial", 13), title='Transferência')
                            self.sal = 0
                            return valid
                        else:
                            dado[2] = f'{self.sal:.2f}'
                            linha_atual = f'{dado[0]},{dado[1]},{dado[2]},{dado[3]},{dado[4]},{dado[5]}'
                            linhas[conta_des] = linha_atual
                    conta_des += 1

                for dados in linhas:
                    dado = dados.split(',')
                    if dado[0] in numD:
                        self.descricao = f'{dado[3]} {dado[4]}'
                        dep = float(dado[2]) + float(valor)
                        dado[2] = f'{dep:.2f}'
                        linha_atual = f'{dado[0]},{dado[1]},{dado[2]},{dado[3]},{dado[4]},{dado[5]}'
                        linhas[conta_dep] = linha_atual
                    conta_dep += 1

                try:
                    a = open(arquivo, 'wt')
                    for valor in linhas:
                        a.write(f'{valor}')
                    a.close()
                    sg.popup('Trasferência feita com sucesso!', font=("arial", 13), title='Transferência')

                except:
                    sg.Popup('ERRO na gravação dos dados!', font=("arial", 13), title='Transferêcia')
            except:
                sg.popup('Houve um AQUI ao ler o aquivo!', font=("arial", 13), title='Transferência')
        finally:
            a.close()
        self._extrato.movimentacao.append(f'Trasferência de {v:.2f} - {datetime.strftime(data_hora, "%d/%m/%y - %H:%Mh")}\n'
                                          f'Destino >> {self.descricao}\n')

    def consulta(self, arquivo, contaD):
        try:
            a = open(arquivo, 'rt')
        except:
            sg.Popup('ERRO na consulta!', font=("arial", 13), title='Consulta')
        else:
            try:
                conta = list()
                for valor in a:
                    dados = valor.split(',')
                    if dados[0] == contaD:
                        dados[5] = dados[5].replace('\n', '')
                        for c in range(0, len(dados)):
                            conta.append(dados[c])
                        return conta
                return False

            except:
                sg.Popup('ERRO na consulta!', font=("arial", 13), title='Consulta')

        finally:
            a.close()

    def print_mov(self):
        print(f'Conta: {self._numero}\n'
              f'Nome: {self._cliente.nome} {self._cliente.sobrenome}')
        print()
        self._extrato.imprime_mov()
        print(f'Saldo: R$ {self.sal:.2f}')
