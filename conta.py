class ContaBancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def exibir_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo R${self.saldo:.2f}")

# Teste simples
conta = ContaBancaria("Suzane Nunes", 10000)
conta.exibir_saldo()
