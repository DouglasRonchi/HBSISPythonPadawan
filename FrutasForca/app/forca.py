from .frutas import Frutas
from random import shuffle


class Forca(Frutas):
    def __init__(self, frutas: list):
        super().__init__(frutas)
        self.fruta_sorteada = ''
        self.palpites = []
        self.dica = []
        self.erro = True
        self.erros = 0

    def sortear_fruta(self):
        shuffle(self._frutas)
        self.fruta_sorteada = self._frutas[0]

    def montar_dica(self):
        for i in range(len(self.fruta_sorteada)):
            self.dica.append('__')
        print("Dica:")
        print(self.dica)
        return self.dica

    def jogar(self):
        self.montar_dica()
        while self.erros < 5:
            if "__" not in self.dica:
                self._winner()
                break
            palpite = input("Digite uma letra:")
            if palpite.upper() in self.palpites:
                print("Já escolheu esta letra")
                continue
            self.palpites.append(palpite.upper())
            c = 0
            for i in self.fruta_sorteada:
                if palpite == i:
                    self.dica[c] = i.upper()
                    self.erro = False
                c += 1
            if self.erro:
                self.erros += 1
                self._boneco()
            print(f"Erros: {self.erros}")
            print(self.dica)
            self.erro = True

    def _boneco(self):
        if self.erros == 1:
            print("""
            ___________
            |          O
            |         
            |           
            |        
            |                """)
        elif self.erros == 2:
            print("""
            ___________
            |          O
            |          | 
            |          
            |       
            |               """)
        elif self.erros == 3:
            print("""
            ___________
            |          O
            |          | 
            |          |
            |       
            |               """)
        elif self.erros == 4:
            print("""
            ___________
            |          O
            |        / | /
            |          |
            |       
            |               """)
        elif self.erros == 5:
            print(f"""
                    YOU LOSE
                    ERA {self.fruta_sorteada.upper()}
            ___________
            |          O
            |        / | /
            |          |
            |       _ / \ _
            |               """)

    def _winner(self):
        print(f"Você Ganhou! Erros: {self.erros}")
