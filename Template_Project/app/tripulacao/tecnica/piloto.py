from app.tripulacao.tripulante import Tripulante


class Piloto(Tripulante):
    def __init__(self, nome: str):
        super().__init__(nome)
