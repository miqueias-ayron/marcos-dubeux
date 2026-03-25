from utils import exibir_menu, visualizar_estoque, realizar_venda, adicionar_estoque

def main():
    # 1. Banco de Dados Inicial (Lista de Dicionários)
    estoque = [
        {"nome": "Espresso", "preco": 5.50, "quantidade": 15},
        {"nome": "Cappuccino", "preco": 8.00, "quantidade": 10},
        {"nome": "Pão de Queijo", "preco": 4.50, "quantidade": 20},
        {"nome": "Bolo de Cenoura", "preco": 6.00, "quantidade": 5}
    ]
    
    faturamento_total = 0.0

    print("="*30)
    print("SISTEMA COFFEESTACK V1.0")
    print("="*30)

    # 2. Loop Principal (Controle do Sistema)
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            # Visualizar estoque
            print("\n--- ESTOQUE ATUAL ---")
            visualizar_estoque(estoque)
        
        elif opcao == "2":
            # Realizar Venda
            nome_venda = input("Digite o nome do produto para venda: ")
            valor_venda = realizar_venda(estoque, nome_venda)
            
            if valor_venda:
                faturamento_total += valor_venda
                print(f"Venda realizada! R$ {valor_venda:.2f} adicionados ao caixa.")
        
        elif opcao == "3":
            # Reposição de Estoque
            nome_repo = input("Produto para repor: ")
            try:
                qtd_repo = int(input("Quantidade a adicionar: "))
                adicionar_estoque(estoque, nome_repo, qtd_repo)
            except ValueError:
                print("Erro: Digite um número inteiro para a quantidade.")

        elif opcao == "4":
            # Relatório de Faturamento
            print(f"\n--- RELATÓRIO DO DIA ---")
            print(f"Faturamento Total: R$ {faturamento_total:.2f}")
            print("-" * 25)

        elif opcao == "5":
            # Sair
            print("Encerrando o sistema... Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Garante que o programa só rode se for o arquivo principal
if __name__ == "__main__":
    main()