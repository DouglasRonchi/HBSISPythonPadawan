from app.exeptions import CapacidadeMaximaDoFortwoExcedidaExeption
from app.tripulacao.tripulante import Tripulante

_CAPACIDADE_MAXIMA_NO_CARRO = 2


class SmartForTwo:
    def __init__(self):
        self._tripulantes = []

    def adicionar(self, tripulante: Tripulante) -> None:
        if self._get_quantidade_de_tripulantes() == _CAPACIDADE_MAXIMA_NO_CARRO:
            raise CapacidadeMaximaDoFortwoExcedidaExeption("Capacidade Máxima do smart fortwo Excedida!")
        self._tripulantes.append(tripulante)

    def get_tripulantes(self) -> list:
        return self._tripulantes.copy()

    def _get_quantidade_de_tripulantes(self):
        return len(self._tripulantes)
