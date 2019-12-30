class CapacidadeMaximaDoFortwoExcedidaExeption(Exception):
    def __init__(self, msg: str = 'Capacidade Máxima do smart fortwo Excedida'):
        super().__init__(msg)