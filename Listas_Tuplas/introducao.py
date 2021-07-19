' Objetos próprios'

class ContaCorrente:

    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>> Código: {} --- Saldo: {} <<]".format(self.codigo,self.saldo)



conta_do_gui = ContaCorrente(15)
conta_da_dani = ContaCorrente(47685)

conta_do_gui.deposita(500)
conta_da_dani.deposita(1000)

contas = [ conta_do_gui, conta_da_dani]

for conta in contas:
    print('')
    print(conta)

print('''
***********************''')

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

deposita_para_todas(contas)
print('')
print(contas[0],contas[1])

contas.insert(0,76)
print('')
print(contas[0],contas[1], contas[2])


'''Herança e Polimorfismo'''
from abc import ABCMeta, abstractmethod
class Conta(metaclass=ABCMeta):

    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod # caso a classe não tenha definido, ela não ira funcionar
    def passa_o_mes(self):
        pass
    def __str__(self):
        return "[>> Código: {} --- Saldo: {} <<]".format(self._codigo,self._saldo)

class ContaCorrente (Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca (Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass

print('''
HERANÇA:''')
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)


#Polimorfismo
print('''
POLIMORFISMO:''')
contas=[conta16,conta17]
for conta in contas:
    conta.passa_o_mes()
    print(f'''
{conta}''')


# Igualdade de valores contidos no Obj

print('''
Igualdade de valores: 
Conta 1 = Conta 2 ?''')

from functools import total_ordering

@total_ordering
class ContaSalario:

    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self.codigo == outro.codigo

    def __lt__(self, outro):
        return self.saldo < outro.saldo

    def __str__(self):
        return "[>> Código: {} --- Saldo: {} <<]".format(self.codigo,self.saldo)

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

print(conta1 == conta2)

# Ordenando obj apartir de um unico valor interno

print('''
Ordenando lista de obj''')
from operator import attrgetter

for conta in sorted(contas, key= attrgetter("_saldo")):
    print(conta)

# usando less than (__lt__)
conta_do_gui = ContaSalario(15)
conta_da_dani = ContaSalario(47685)

conta_do_gui.deposita(500)
conta_da_dani.deposita(1000)

# agora podemos usar a comparação entre as contas e tambem sorted


''' Ordenando com mais de um criterio '''
# usando total ordering podemos fazer comparação de >= ou <= outro obj

# tb podemos usar o attrgetter passando mais de um parametro de comparação, na ordem a ser comparada