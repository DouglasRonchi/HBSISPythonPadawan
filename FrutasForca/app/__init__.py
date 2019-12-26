from app.forca import Forca
from app.frutas import Frutas


def start():
    frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
    forca = Forca(frutas)
    forca.sortear_fruta()
    forca.jogar()
