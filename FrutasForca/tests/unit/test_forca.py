import unittest
from random import randint
from string import ascii_letters
from unittest.mock import Mock, patch

from app import Forca


class TestForca(unittest.TestCase):
    def test_se_forca_e_uma_instancia_da_classe_forca(self):
        lista = Mock()
        forca = Forca(lista)
        self.assertIsInstance(forca, Forca)

    def test_sortear_fruta_esta_sorteando_apropriadamente(self):
        lista = [Mock(), Mock(), Mock(), Mock()]
        forca = Forca(lista)
        forca.sortear_fruta()
        sorteio = forca._frutas[0]
        self.assertEqual(sorteio, forca.fruta_sorteada)

    @patch('app.forca.print')
    def test_jogar_esta_funcionando(self, mock_print):
        lista = [Mock(), Mock(), Mock(), Mock()]
        forca = Forca(lista)
        forca.jogar()
        self.assertEqual(forca.erros, 0)

    @patch('app.forca.print')
    def test_boneco_finalizado_com_um_erro(self, mock_print):
        lista = [Mock(), Mock(), Mock(), Mock()]
        forca = Forca(lista)
        forca.erros = 1
        forca._boneco()

    @patch('app.forca.print')
    def test_boneco_finalizado_com_dois_erros(self, mock_print):
        lista = [Mock(), Mock(), Mock(), Mock()]
        forca = Forca(lista)
        forca.erros = 2
        forca._boneco()

    @patch('app.forca.print')
    def test_boneco_finalizado_com_tres_erros(self, mock_print):
        lista = [Mock(), Mock(), Mock(), Mock()]
        forca = Forca(lista)
        forca.erros = 3
        forca._boneco()

    @patch('app.forca.print')
    def test_boneco_finalizado_com_quatro_erros(self, mock_print):
        lista = [Mock(), Mock(), Mock(), Mock()]
        forca = Forca(lista)
        forca.erros = 4
        forca._boneco()

    @patch('app.forca.print')
    def test_boneco_finalizado_com_cinco_erros(self, mock_print):
        lista = [Mock(), Mock(), Mock(), Mock()]
        forca = Forca(lista)
        forca.erros = 5
        forca._boneco()

    @patch('app.forca.print')
    def test_se_a_montagem_da_dica_esta_criando_apropriadamente(self, mock_print):
        lista = ['morango']
        forca = Forca(lista)
        forca.sortear_fruta()
        forca.montar_dica()
        self.assertEqual(len(forca.dica), len(lista[0]))

    @patch('app.forca.print')
    @patch('app.forca.input',
           lambda letra: ascii_letters[randint(0, 5)])
    def test_se_jogar_esta_funcionando_quando_ganha(self, mock_print):
        lista = ['abcde']
        forca = Forca(lista)
        forca.sortear_fruta()
        forca.jogar()

    # @patch('app.forca.input')
    # def test_se_jogar_esta_funcionando_quando_ganha(self, mock_input):
    #     mock_input.side_effect = ('a', 'b', 'c', 'd', 'e')
    #     lista = ['abcde']
    #     forca = Forca(lista)
    #     forca.sortear_fruta()
    #     forca.jogar()

    @patch('app.forca.print')
    @patch('app.forca.input',
           lambda letra: ascii_letters[randint(5, 15)])
    def test_se_jogar_esta_funcionando_quando_perde(self, mock_print):
        lista = ['abcde']
        forca = Forca(lista)
        forca.sortear_fruta()
        forca.jogar()