'''
Dois navios de pesca navegam em mar aberto, ambos em uma missão conjunta de pesca.

Em altas apostas, alta expectativa de recompensa - os navios adotaram a estratégia de pendurar uma rede entre os dois navios.

A rede tem 64 km (milhas de comprimento) . Quando a distância em linha reta entre os navios for superior a 64 km, a rede
 rasgará e sua valiosa colheita no mar será perdida! Precisamos saber quanto tempo levará para que isso aconteça.

Dado o rumo de cada navio, encontre o tempo em minutos em que a distância em linha reta entre os dois navios atinge 64 km.
Ambos os navios viajam a 150 quilômetros por hora. No momento 0, suponha que os navios tenham o mesmo local.

Os rolamentos são definidos como graus do norte, contando no sentido horário . 
Eles serão passados ​​para sua função como números inteiros entre 0 e 359 graus. Arredonde seu resultado para 2 locais decimais.

Se a rede nunca quebrar, retorne float('inf')
'''

import math

# 1 grau = 60 min

# find_time_to_break(0, 90) => 18.86

pos_ship_one = 0
pos_ship_two = 0
distance = 0
fishing_net_breaks_at = 64
speed = 150


def find_time_to_break(bearing_a: int, bearing_b: int):
    





find_time_to_break(0, 90)
