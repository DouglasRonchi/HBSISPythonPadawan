# First Challenge BLACKJACK 21

from random import randint
from exemplo.baralho import Baralho
from time import sleep


class BlackJack(Baralho):
    def __init__(self):
        super().__init__()
        self.jogador = []
        self.dealer = []
        self.resultado_jogador = 0
        self.resultado_dealer = 0
        self.jogada = False

    def exibir_resultado(self):
        print("DEALER")
        print(self.dealer, end=' Total: ')
        print(self.resultado_dealer)
        print("JOGADOR")
        print(self.jogador, end=' Total: ')
        print(self.resultado_jogador, end=' | Falta para 21: ')
        print(21 - self.resultado_jogador)

    def verificacao_blackjack(self):
        # Rules
        if self.resultado_dealer > 21:
            print("Dealer perdeu, voce ganhou!")
            return True

        if self.resultado_jogador > 21:
            print("Você perdeu!!")
            return True

        if self.resultado_jogador == 21:
            print("BLACKJACK!!!")

        if self.jogada == True and (self.resultado_jogador == self.resultado_dealer):
            print("Empate!")
            return True

        if self.jogada == True and (self.resultado_jogador > self.resultado_dealer):
            print("Jogador Venceu!")
            return True

        if self.jogada == True and (self.resultado_dealer > self.resultado_jogador):
            print("Dealer Venceu!")
            return True

    def pontuacao(self, tipo: str):
        resultado = 0
        if self.baralho[0] == "A":
            if tipo.upper() == "JOGADOR":
                carta_a = 1 if len(self.jogador) > 0 else 11
            elif tipo.upper() == "DEALER":
                carta_a = 1 if len(self.dealer) > 0 else 11
            resultado += carta_a
        elif self.baralho[0] == "J":
            resultado += 11
        elif self.baralho[0] == "Q":
            resultado += 12
        elif self.baralho[0] == "K":
            resultado += 13
        elif int(self.baralho[0]) <= 10:
            resultado += int(self.baralho[0])

        if tipo.upper() == "JOGADOR":
            self.resultado_jogador += resultado
        elif tipo.upper() == "DEALER":
            self.resultado_dealer += resultado
        self.baralho.pop(0)

    def jogar(self):
        print("{:^50}".format("\033[33mBlackjack\033[m"))
        # Primeira jogada, o jogador recebe 2 cartas e o dealer recebe 1 carta
        # Dando cartas para o Dealer
        print(f"Dealer virou a carta {self.baralho[0]}!")
        sleep(1)
        self.dealer.append(self.baralho[0])
        self.pontuacao("DEALER")

        # Dando Cartas para o Jogador
        for i in range(2):
            print(f"Você virou a carta {self.baralho[0]}!")
            sleep(1)
            self.jogador.append(self.baralho[0])
            self.pontuacao("JOGADOR")

        # Exibindo Resultados
        self.exibir_resultado()

        # Rodadas Seguintes
        while True:
            # DEBUG - Ver o Baralho...
            # print(f"Baralho {self.baralho}")
            if self.verificacao_blackjack():
                break

            try:
                escolha = int(input("""
                1 - Pega mais uma carta
                2 - Fica com as cartas que tem
                Escolha: """))
            except:
                print("Opcao invalida!")
            else:
                if escolha == 1:
                    # Pega mais uma carta
                    print(f"Você virou a carta {self.baralho[0]}!")
                    sleep(1)
                    self.jogador.append(self.baralho[0])
                    self.pontuacao("JOGADOR")
                elif escolha == 2:
                    self.jogada = True

                    # mantem e o dealer joga
                    contador = 0
                    while True:
                        if self.resultado_dealer > self.resultado_jogador:
                            break
                        if contador > 0:
                            self.jogada = False
                        contador += 1
                        sleep(1)
                        print(f"Dealer virou a carta {self.baralho[0]}!")
                        self.dealer.append(self.baralho[0])
                        self.pontuacao("DEALER")

                        if self.resultado_dealer > randint(10, 16):
                            print("Dealer Passou a Vez...")
                            self.jogada = False
                            sleep(1)
                            break

                self.exibir_resultado()


jogo = BlackJack()
jogo.jogar()