from getpass import getpass
from random import randint


class ContaCorrente:
    def __init__(self, saldo):
        self.__numero = randint(1000, 9999)
        self.__saldo = saldo
        self.__senha = None

    def creditar(self, valor):
        self.__saldo += valor
        print(f'-> Conta Nº{self.__numero} creditada no valor de R${self.__saldo:.2f}\n')

    def debitar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f'-> Conta Nº{self.__numero} debitada no valor de R${self.__saldo:.2f}\n')
        else:
            print('Saldo insuficiente!')

    def transferir(self, conta_destino, valor):
        if (type(conta_destino) == object) and (valor <= self.__saldo):
            self.debitar(valor)
            conta_destino.creditar(valor)
            print(f"\nFoi realizada uma transferência de R${valor:.2f}\nConta de origem: Nº{self.__numero}\nConta de destino: Nº{conta_destino.numero}\n")
        else:
            print('Saldo insuficiente ou conta de destino inválida!')
        
    def criar_nova_senha(self):
        if self.__senha is None:
            senha = getpass("\nDigite a nova senha: ")
            self.__senha = senha
            print('Senha criada com sucesso!')
        else:
            print('Já possui uma senha criada!')

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero
    
    
    # Método para uso interno, não exige senha    
    def obter_saldo(self):
        return self.__saldo

    @property
    def saldo(self):
        senha = getpass('\nDigite a senha: ')
        if senha == self.__senha:
            return f'R${self.__saldo:.2f}'
        else:
            print('Senha inválida!')
            return None
    
    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha

    def __str__(self):
        return f'-> Número da conta: Nº{self.__numero}\n-> Saldo atual: R${self.__saldo:.2f}\n'


class ContaPoupanca(ContaCorrente):
    def __init__(self, saldo, taxa_juros):
        super().__init__(saldo)
        self.__taxa_juros = taxa_juros

    def render_juros(self):
        saldo_atual = self.obter_saldo()
        self.creditar(saldo_atual * self.__taxa_juros)
        print(f'Juros rendidos com sucesso!\nAgora seu saldo atual da conta Nº{self.numero} é R${self.obter_saldo():.2f}\n')

    @property
    def taxa_juros(self):
        return self.__taxa_juros
    
    @taxa_juros.setter
    def taxa_juros(self, nova_taxa_juros):
        self.__taxa_juros = nova_taxa_juros

    def __str__(self):
        return super().__str__() + f'-> Taxa de juros: {self.__taxa_juros}\n'


class ContaImposto(ContaCorrente):
    def __init__(self, saldo, percentual_imposto):
        super().__init__(saldo)
        self.__percentual_imposto = percentual_imposto

    def calcular_imposto(self):
        saldo_atual = self.obter_saldo()
        self.debitar(saldo_atual * self.__percentual_imposto)
        print(f'Imposto debitado com sucesso!\nAgora seu saldo atual da conta Nº{self.numero} é R${self.obter_saldo():.2f}\n')

    @property
    def percentual_imposto(self):
        return self.__percentual_imposto
    
    @percentual_imposto.setter
    def percentual_imposto(self, novo_percentual_imposto):
        self.__percentual_imposto = novo_percentual_imposto

    def __str__(self):
        return super().__str__() + f'-> Taxa de imposto: {self.__percentual_imposto}\n'
    
class ContaEspecial(ContaCorrente):
    def __init__(self, saldo, limite):
        super().__init__(saldo)
        self.__limite = limite
        
    def debitar(self, valor):
        saldo_atual = self.obter_saldo()
        if valor > saldo_atual + self.__limite:
            print('Saldo insuficiente!')
        else:
            self.saldo = saldo_atual - valor
            
    def __str__(self):
        return super().__str__() + f'-> Limite: R${self.__limite:.2f}\n-> Saldo disponível: R${self.obter_saldo() + self.__limite:.2f}'
    
class Banco:
    def __init__(self):
        self.total_valor_contas = 0
        self.contas = []
        
    def adicionar_conta(self, *contas):
        for conta in contas:
            if isinstance(conta, ContaCorrente):
                self.contas.append(conta)
                print(f'Conta Nº{conta.numero} adicionada ao banco com sucesso!\n')
            else:
                print('A conta não é uma instância de ContaCorrente!')
            
    def calcular_valor_total(self):
        self.total_valor_contas = 0
        for conta in self.contas:
            self.total_valor_contas += conta.obter_saldo()
        print(f'\nO valor total contido nas contas cadastradas: R${self.total_valor_contas:.2f}\n')
        
    def listar_contas(self):
        print(f'Total de contas no banco: {len(self.contas)}')
        for conta in self.contas:
            print(f'{conta}')

def main():
    cc = ContaCorrente(5000)
    cp = ContaPoupanca(3000, 0.05)
    ce = ContaEspecial(1000, 2000)
    
    banco = Banco()
    
    banco.adicionar_conta(cc, cp, ce)
    
    banco.listar_contas()
    banco.calcular_valor_total()

if __name__ == "__main__":
    main()
