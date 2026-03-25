from random import randint

def exercicio_1():
    senha_correta = "python123"
    senha_inserida = str(input("Informe a senha correta: "))

    while senha_inserida != senha_correta:
        print("Acesso negado")
        senha_inserida = str(input("Informe a senha correta: "))

    print("Acesso concedido!")

def exercicio_2():
    soma = 0
    usuario = int(input("Digite um número: "))

    while usuario != 0:
        soma += usuario
        usuario = int(input("Digite um número: "))

    print(f"O resultado da soma foi: {soma}")

def exercicio_3():
    sorteado = randint(1,20)
    escolhido = int(input("Informe o seu palpite: "))

    while escolhido != sorteado:
        if escolhido < sorteado:
            print("Um pouco mais!")
            escolhido = int(input("Informe um outro palpite: "))
        elif escolhido > sorteado:
            print("Um pouco menos!")
            escolhido = int(input("Informe um outro palpite: "))
    print("Parabéns, você acertou! ")

if __name__ == "__main__":
    quero = input("Escolha o que você quer rodar: [1], [2] ou [3]: ")
    if quero == "1":
        exercicio_1()
    elif quero == "2":
        exercicio_2()
    elif quero == "3":
        exercicio_3()