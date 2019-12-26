from random import shuffle


class Baralho:
    def __init__(self):
        self.baralho = []
        self.cartas_baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
        for c in range(4):
            for i in self.cartas_baralho:
                self.baralho.append(i)
        # Shuffling cards
        shuffle(self.baralho)
