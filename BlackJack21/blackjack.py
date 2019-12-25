#Desafio 1 BLACKJACK 21

from random import randint, shuffle
from baralho import Baralho
from time import sleep

class BlackJack(Baralho):
    def __init__(self):
        self.baralho = Baralho()
        self.jogador = []
        self.dealer = []
        self.resultado_jogador = 0
        self.resultado_dealer = 0
        self.jogada = False


    def verificacao_blackjack(self):
        #Regras
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


    def pontuacao_jogador(self, carta:int):
        if self.baralho.baralho[carta] == "A":
            carta_a = 1 if len(self.baralho.baralho) < 52 else 11
            self.resultado_jogador += carta_a
        elif self.baralho.baralho[carta] == "J":
            self.resultado_jogador += 11
        elif self.baralho.baralho[carta] == "Q":
            self.resultado_jogador += 12
        elif self.baralho.baralho[carta] == "K":
            self.resultado_jogador += 13
        elif int(self.baralho.baralho[carta]) <= 10:
            self.resultado_jogador += int(self.baralho.baralho[carta])
        self.baralho.baralho.pop(carta)


    def pontuacao_dealer(self, carta:int):
        if self.baralho.baralho[carta] == "A":
            carta_a = 1 if len(self.baralho.baralho) < 52 else 11
            self.resultado_dealer += carta_a
        elif self.baralho.baralho[carta] == "J":
            self.resultado_dealer += 11
        elif self.baralho.baralho[carta] == "Q":
            self.resultado_dealer += 12
        elif self.baralho.baralho[carta] == "K":
            self.resultado_dealer += 13
        elif int(self.baralho.baralho[carta]) <= 10:
            self.resultado_dealer += int(self.baralho.baralho[carta])
        self.baralho.baralho.pop(carta)


    def jogar(self):
        print("{:^50}".format("\033[33mBlackjack\033[m"))
        #Primeira jogada, o jogador recebe 2 cartas e o dealer recebe 1 carta
        carta = randint(0, len(self.baralho.baralho) - 1)
        
        #Dando cartas para o Dealer
        print(f"Dealer virou a carta {self.baralho.baralho[carta]}!")
        self.dealer.append(self.baralho.baralho[carta])
        self.pontuacao_dealer(carta)

        #Dando Cartas para o Jogador
        for i in range(2):
            print(f"Você virou a carta {self.baralho.baralho[carta]}!")
            self.jogador.append(self.baralho.baralho[carta])
            self.pontuacao_jogador(carta)
        
        #Exibindo Resultados
        print("DEALER")
        print(self.dealer, end=' => ')
        print(self.resultado_dealer)
        print("JOGADOR")
        print(self.jogador, end=' => ')
        print(self.resultado_jogador)

        #Rodadas Seguintes
        while True:
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
                carta = randint(0, len(self.baralho.baralho) - 1)
                if escolha == 1:
                    #Pega mais uma carta
                    print(f"Você virou a carta {self.baralho.baralho[carta]}!")
                    sleep(1)
                    self.jogador.append(self.baralho.baralho[carta])
                    self.pontuacao_jogador(carta)
                elif escolha == 2:
                    self.jogada = True

                    #mantem e o dealer joga
                    contador = 0
                    while True:
                        if self.resultado_dealer > self.resultado_jogador:
                            break
                        if contador > 0:
                            self.jogada = False
                        contador += 1
                        sleep(1)
                        print(f"Dealer virou a carta {self.baralho.baralho[carta]}!")
                        self.dealer.append(self.baralho.baralho[carta])
                        self.pontuacao_dealer(carta)
                        
                        if self.resultado_dealer > randint(10,16):
                            print("Dealer Passou a Vez...")
                            self.jogada = False
                            sleep(1)
                            break
                        

                print("DEALER")
                print(self.dealer, end=' => ')
                print(self.resultado_dealer)
                print("JOGADOR")
                print(self.jogador, end=' => ')
                print(self.resultado_jogador)


jogo = BlackJack()
jogo.jogar()