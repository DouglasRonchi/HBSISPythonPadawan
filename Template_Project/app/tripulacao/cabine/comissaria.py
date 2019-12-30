from app.tripulacao.tripulante import Tripulante


class Comissaria(Tripulante):
    def __init__(self, nome: str):
        super().__init__(nome)
