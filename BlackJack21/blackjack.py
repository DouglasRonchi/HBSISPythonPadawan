#Desafio 1 BLACKJACK 21

from random import randint, shuffle
from baralho import Baralho

class BlackJack(Baralho):
    def __init__(self):
        self.baralho = Baralho()
        self.cartas_viradas = []
        self.resultado = 0
        self.jogadas = 0


    def verificacao_blackjack(self):
        if self.resultado == 21:
            print("Parabéns, você ganhou o jogo! Atingiu 21 pontos exatos!")
            print(f"Você conseguiu atingir 21 pontos com {self.jogadas} jogadas!")
            return True
        elif self.resultado > 21:
            print("Você perdeu!!")
            return True


    def jogar(self):
        print("{:^50}".format("\033[33mJogo das Cartas\033[m"))
        while True:
            if self.verificacao_blackjack():
                break

            carta = randint(0, len(self.baralho.baralho) - 1)


            self.jogadas += 1
            input("Aperte qualquer tecla para virar uma carta!")
            print(f"Você virou a carta {self.baralho.baralho[carta]}!")

            
            if self.baralho.baralho[carta] == "A":
                carta_a = 1 if len(self.baralho.baralho) < 52 else 11
                self.resultado += carta_a
            elif self.baralho.baralho[carta] == "J":
                self.resultado += 11
            elif self.baralho.baralho[carta] == "Q":
                self.resultado += 12
            elif self.baralho.baralho[carta] == "K":
                self.resultado += 13
            elif int(self.baralho.baralho[carta]) <= 10:
                self.resultado += int(self.baralho.baralho[carta])
            
            
            self.cartas_viradas.append(self.baralho.baralho[carta])
            self.baralho.baralho.pop(carta)
            print(self.cartas_viradas, end=' => ')
            print(self.resultado)



jogo = BlackJack()
jogo.jogar()