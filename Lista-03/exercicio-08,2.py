#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escreva um programa que calcule a menor distância entre um ponto e uma reta, 
#...possibilitando que o usuário entre com as informações de dois pontos pertencentes à reta, 
#...bem como o ponto para o qual deva ser avaliada a distância.

# 1° ponto da reta:

x1 = int(input("Digite o valor da coordenada x do primeiro ponto da sua reta: "))
y1 = int(input("Digite o valor da coordenada y do primeiro ponto da sua reta: "))

# 2° ponto da reta:

x2 = int(input("Digite o valor da coordenada x do segundo ponto da sua reta: "))
y2 = int(input("Digite o valor da coordenada y do segundo ponto da sua reta: "))

# Solicitando ao usuário o ponto para o qual deva ser avaliada a distância:

x = int(input("Digite o valor da coordenada x do ponto para o qual deva ser avaliada a distância: "))
y = int(input("Digite o valor da coordenada y do ponto para o qual deva ser avaliada a distância: "))

# Calculando o h(x,y):

import math

numerador = (y2 - y1) * (x - x1) - (x2 - x1) * (y - y1)

denominador = math.sqrt((x2 - x1)*2 + (y2 - y1)*2)

if (denominador <= 0):
    print("Denominador menor que zero, temos uma indeterminação!")
else:
   h = abs(numerador/denominador)

print("A menor distância entre o ponto e a reta é", h,".")
