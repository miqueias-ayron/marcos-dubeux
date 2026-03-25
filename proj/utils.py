def exibir_menu():
    """Imprime as opções disponíveis no sistema."""
    print("\n" + "-"*30)
    print("1. Visualizar Estoque")
    print("2. Realizar Venda")
    print("3. Reposição de Estoque")
    print("4. Relatório de Faturamento")
    print("5. Sair")
    print("-"*30)

def visualizar_estoque(lista_produtos):
    """Percorre a lista de dicionários e exibe os itens formatados."""
    print(f"{'Produto':<20} | {'Preço':<10} | {'Qtd':<5}")
    print("-" * 40)
    for item in lista_produtos:
        nome = item["nome"]
        preco = item["preco"]
        qtd = item["quantidade"]
        print(f"{nome:<20} | R$ {preco:>7.2f} | {qtd:>5}")

def realizar_venda(lista_produtos, nome_item):
    """
    Busca o item, abate 1 unidade se houver estoque e retorna o preço.
    Retorna 0 se não encontrar ou não houver estoque.
    """
    for item in lista_produtos:
        # Comparação ignorando maiúsculas/minúsculas para melhor UX
        if item["nome"].lower() == nome_item.lower():
            if item["quantidade"] > 0:
                item["quantidade"] -= 1
                return item["preco"]
            else:
                print(f"Erro: O item '{item['nome']}' está esgotado!")
                return 0
    
    print(f"Erro: Produto '{nome_item}' não encontrado.")
    return 0

def adicionar_estoque(lista_produtos, nome_item, quantidade):
    """Localiza um item e soma a quantidade informada ao estoque atual."""
    if quantidade <= 0:
        print("Erro: A quantidade de reposição deve ser maior que zero.")
        return

    for item in lista_produtos:
        if item["nome"].lower() == nome_item.lower():
            item["quantidade"] += quantidade
            print(f"Sucesso! {quantidade} unidades adicionadas ao item '{item['nome']}'.")
            return
    
    print(f"Erro: Produto '{nome_item}' não encontrado para reposição.")