# ☕ Projeto: CoffeeStack Control
Sistema de Gestão de Inventário e Vendas
Este projeto consiste no desenvolvimento de um sistema de terminal para gerenciar o estoque e as vendas de uma cafeteria, aplicando conceitos de modularização, estruturas de repetição e coleções.

## 📋 Enunciado do Problema
O software deve permitir que os atendentes da CoffeeStack gerenciem o dia a dia da loja. O desafio principal é manter a integridade dos dados (estoque) enquanto as operações de venda ocorrem.

## 🏗️ Estrutura de Arquivos
O projeto obrigatoriamente deve ser dividido em dois arquivos:

### 1. utils.py (Módulo de Funções)
Este arquivo deve conter toda a "inteligência" do sistema. Nenhuma interação direta de loop principal deve estar aqui, apenas as definições das funções:

``exibir_menu()``: Imprime as opções de 1 a 4 para o usuário.

``visualizar_estoque(lista_produtos)``: Recebe a lista de dicionários e exibe os dados (Nome, Preço e Qtd) de forma organizada.

``realizar_venda(lista_produtos, nome_item)``:

Busca o item na lista.

Se encontrar e houver estoque: subtrai 1 unidade e retorna o preço do item.

Se não encontrar ou não houver estoque: retorna 0 ou None e exibe uma mensagem de erro.

``adicionar_estoque(lista_produtos, nome_item, quantidade)``: Localiza o item e soma a nova quantidade ao valor já existente no dicionário.

## 2. main.py (Fluxo Principal)
Este arquivo deve importar as funções do utils.py (from utils import ...) e conter o loop while True.

Deve gerenciar a variável faturamento_total.

Deve conter a lista inicial de produtos (o banco de dados em memória).

Deve capturar os inputs do usuário e passar para as funções do utils.py.

## 🗂️ Modelo de Dados
Cada item dentro da sua lista de estoque deve ser um dicionário:

Python
{
    "nome": "Cappuccino",
    "preco": 12.50,
    "quantidade": 10
}
## 🚀 Requisitos e Regras
- **Modularização**: O código não será aceito se todas as funções estiverem dentro do ``main.py``.

- **Validação**: Se o usuário tentar vender um produto que não existe, o sistema deve avisar "Produto não cadastrado" sem encerrar o programa.

- **Persistência em Memória**: As alterações de estoque devem persistir enquanto o programa estiver rodando.

## 💡 Dica de Implementação
Para importar as funções corretamente no main.py, use:
```py
    from utils import exibir_menu, visualizar_estoque, realizar_venda
```