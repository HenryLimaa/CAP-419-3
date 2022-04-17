#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escreva um programa em Python que avalie se dois segmentos de reta se interceptam ou não.

# Solicitando ao usuário as informações dos pontos pertencentes às retas:

# 1° ponto da primeira reta (P1):
x1 = int(input("Digite o valor da coordenada x do primeiro ponto da primeira reta: "))
y1 = int(input("Digite o valor da coordenada y do primeiro ponto da primeira reta: "))

# 2° ponto da primeira reta (P2):
x2 = int(input("Digite o valor da coordenada x do segundo ponto da primeira reta: "))
y2 = int(input("Digite o valor da coordenada y do segundo ponto da primeira reta: "))

# 1° ponto da segunda reta (P3):
x3 = int(input("Digite o valor da coordenada x do primeiro ponto da segunda reta: "))
y3 = int(input("Digite o valor da coordenada y do primeiro ponto da segunda reta: "))

# 2° ponto da segunda reta (P4):
x4 = int(input("Digite o valor da coordenada x do segundo ponto da segunda reta: "))
y4 = int(input("Digite o valor da coordenada y do segundo ponto da segunda reta: "))

# Calculando h(P1), h(P2), h(P3) e h(P4):
# Importando a biblioteca math:

import math

h1 = ((y4 - y3) * (x1 - x3) - (x4 - x3) * (y1 - y3)) / (math.sqrt((x4 - x3)*2 + (y4 - y3)*2)) # Para h(P1)
h2 = ((y4 - y3) * (x2 - x3) - (x4 - x3) * (y2 - y3)) / (math.sqrt((x4 - x3)*2 + (y4 - y3)*2)) # Para h(P2)
h3 = ((y2 - y1) * (x3 - x1) - (x2 - x1) * (y3 - y1)) / (math.sqrt((x2 - x1)*2 + (y2 - y1)*2)) # Para h(p3)
h4 = ((y2 - y1) * (x4 - x1) - (x2 - x1) * (y4 - y1)) / (math.sqrt((x2 - x1)*2 + (y2 - y1)*2)) # Para h(p4)

# Realizando o produto:
H1 = (h1 * h2)
H2 = (h3 * h4)

if (H1) < 0:
    print("Os dois segmentos de reta se interceptam!")
elif (H2) < 0:
    print("Os dois segmentos de reta se interceptam!")
elif (h1 == 0) or (h2 == 0):
    print("Os dois segmentos de reta se interceptam!")
elif (h1 == 0) and (h2 == 0):
    print("Os dois segmentos de reta se interceptam!")
else:
    print("Os dois segmentos de reta não se interceptam!")
