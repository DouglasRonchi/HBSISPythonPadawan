import unittest
from unittest.mock import Mock

import pytest

from app.smart_fortwo.smart_fortwo import SmartForTwo


class TestSmartForTwo(unittest.TestCase):
    def test_smart_fortwo_deveria_ter_dois_tripulantes(self):
        smart_fortwo = SmartForTwo()
        tripulante_1_mock = Mock()
        tripulante_2_mock = Mock()
        smart_fortwo.adicionar(tripulante_1_mock)
        smart_fortwo.adicionar(tripulante_2_mock)
        self.assertEqual(len(smart_fortwo.get_tripulantes()), 2)

    def test_smart_fortwo_deveria_ter_somente_dois_tripulantes(self):
        smart_fortwo = SmartForTwo()
        tripulante_1_mock = Mock()
        tripulante_2_mock = Mock()
        tripulante_3_mock = Mock()
        with pytest.raises(Exception) as ex:
            smart_fortwo.adicionar(tripulante_1_mock)
            smart_fortwo.adicionar(tripulante_2_mock)
            smart_fortwo.adicionar(tripulante_3_mock)
        self.assertEqual(len(smart_fortwo.get_tripulantes()), 2)
        self.assertEqual(str(ex.value), 'Capacidade Máxima do smart fortwo Excedida!')
