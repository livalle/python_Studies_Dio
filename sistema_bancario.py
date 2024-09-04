from datetime import datetime

class Conta:
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        self.transacoes = []
        self.limite_diario = 10
    
    def realizar_transacao(self, valor):
        hoje = datetime.now().date()
        transacoes_hoje = [t for t in self.transacoes if t['data'].date() == hoje]
        
        if len(transacoes_hoje) >= self.limite_diario:
            print("Você excedeu o número de transações permitidas para hoje.")
        else:
            transacao = {
                'valor': valor,
                'data': datetime.now()
            }
            self.transacoes.append(transacao)
            print(f"Transação de {valor} realizada com sucesso em {transacao['data']}.")

    def mostrar_extrato(self):
        print(f"Extrato da conta {self.numero_conta}:")
        for transacao in self.transacoes:
            print(f"Valor: {transacao['valor']} - Data e Hora: {transacao['data']}")

# Exemplo de uso
conta = Conta(1234)

# Simular algumas transações
for _ in range(12):  # Tenta fazer 12 transações
    conta.realizar_transacao(100)

# Mostrar extrato
conta.mostrar_extrato()
