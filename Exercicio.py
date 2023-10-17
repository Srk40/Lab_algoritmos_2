class CaixaEletronico:
    def __init__(self):
        self.saldo = 0
        self.transaction_limit = 1000
        self.movimentacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.movimentacoes.append(f'Depósito de R$ {valor:.2f}')
        else:
            raise Exception("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.transaction_limit:
            if self.saldo >= valor:
                self.saldo -= valor
                self.movimentacoes.append(f'Saque de R$ {valor:.2f}')
            else:
                raise Exception("Saldo insuficiente.")
        else:
            raise Exception("Valor de saque inválido.")

    def verificar_saldo(self):
        return self.saldo

    def historico_movimentacoes(self):
        return self.movimentacoes

def main():
    caixa = CaixaEletronico()

    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar dinheiro")
        print("2. Sacar dinheiro")
        print("3. Verificar saldo bancário")
        print("4. Histórico de movimentações")
        print("5. Sair")

        opcao = input("Digite o número da opção desejada: ")

        try:
            if opcao == '1':
                valor = float(input("Digite o valor a ser depositado: "))
                caixa.depositar(valor)
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

            elif opcao == '2':
                valor = float(input("Digite o valor a ser sacado: "))
                caixa.sacar(valor)
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

            elif opcao == '3':
                saldo = caixa.verificar_saldo()
                print(f"Saldo atual: R$ {saldo:.2f}")

            elif opcao == '4':
                movimentacoes = caixa.historico_movimentacoes()
                print("Histórico de movimentações:")
                for movimentacao in movimentacoes:
                    print(movimentacao)

            elif opcao == '5':
                print("Saindo do sistema.")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
