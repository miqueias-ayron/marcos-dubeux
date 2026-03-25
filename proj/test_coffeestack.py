import unittest
from utils import realizar_venda, adicionar_estoque

class TestCoffeeStack(unittest.TestCase):

    def setUp(self):
        """Prepara um cenário de teste antes de cada função de teste."""
        self.estoque_teste = [
            {"nome": "Cafe", "preco": 5.0, "quantidade": 2},
            {"nome": "Bolo", "preco": 10.0, "quantidade": 0}
        ]

    def test_venda_sucesso(self):
        """Testa se uma venda válida abate o estoque e retorna o preço correto."""
        preco = realizar_venda(self.estoque_teste, "Cafe")
        self.assertEqual(preco, 5.0)
        self.assertEqual(self.estoque_teste[0]["quantidade"], 1)

    def test_venda_sem_estoque(self):
        """Testa se o sistema impede a venda de algo com quantidade 0."""
        preco = realizar_venda(self.estoque_teste, "Bolo")
        self.assertEqual(preco, 0)
        self.assertEqual(self.estoque_teste[1]["quantidade"], 0)

    def test_venda_produto_inexistente(self):
        """Testa se o sistema lida corretamente com produtos fora da lista."""
        preco = realizar_venda(self.estoque_teste, "Suco")
        self.assertEqual(preco, 0)

    def test_adicionar_estoque(self):
        """Testa se a reposição de estoque soma corretamente os valores."""
        adicionar_estoque(self.estoque_teste, "Cafe", 5)
        self.assertEqual(self.estoque_teste[0]["quantidade"], 7)

    def test_venda_case_insensitive(self):
        """Testa se o sistema aceita 'CAFE' em vez de 'Cafe'."""
        preco = realizar_venda(self.estoque_teste, "CAFE")
        self.assertEqual(preco, 5.0)

if __name__ == "__main__":
    unittest.main()