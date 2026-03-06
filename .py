import random
import time

print("=" * 40)
print("🎮 BEM-VINDO AO JOGO DE ADIVINHAÇÃO")
print("=" * 40)

numero_secreto = random.randint(1, 100)
tentativas = 0

time.sleep(1)
print("\nEstou pensando em um número entre 1 e 100...")
time.sleep(1)

while True:
    try:
        palpite = int(input("\nDigite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("📉 Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("📈 Muito alto! Tente novamente.")
        else:
            print("\n🎉 PARABÉNS!")
            print(f"Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break

    except ValueError:
        print("⚠️ Digite apenas números!")

print("\nObrigado por jogar! 🚀")