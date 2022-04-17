#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escreva um programa que calcule a menor distância entre um ponto e uma reta, 
#...possibilitando que o usuário entre com as informações de dois pontos pertencentes à reta, 
#...bem como o ponto para o qual deva ser avaliada a distância.

import math
 
# função que permite calcular a distância entre dois pontos no plano (R2)
def distancia2d(x1, y1, x2, y2):
  a = x2 - x1
  b = y2 - y1
  c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
  return c

# função principal do programa
def main():
  # ler os dados do primeiro ponto
  x1 = float(input("Informe o x do primeiro ponto: "))
  y1 = float(input("Informe o y do primeiro ponto: "))
     
  # ler os dados do segundo ponto
  x2 = float(input("Informe o x do segundo ponto: "))
  y2 = float(input("Informe o y do segundo ponto: "))
     
  # obter a distância entre eles
  distancia = distancia2d(x1, y1, x2, y2)
  print("Distância entre os dois pontos: %0.2f" % distancia);
  
  if __name__== "__main__":
  main()
  
  import math

# calculando a menor distância entre um ponto e uma reta.
# 1° ponto da reta:
x1 = int(input("Digite o valor da coordenada x do primeiro ponto da sua reta: "))
y1 = int(input("Digite o valor da coordenada y do primeiro ponto da sua reta: "))

# 2° ponto da reta:
x2 = int(input("Digite o valor da coordenada x do segundo ponto da sua reta: "))
y2 = int(input("Digite o valor da coordenada y do segundo ponto da sua reta: "))

# Perguntando o ponto para o qual deva ser avaliada a distância:
x = int(input("Digite o valor da coordenada x do ponto para o qual deva ser avaliada a distância: "))
y = int(input("Digite o valor da coordenada y do ponto para o qual deva ser avaliada a distância: "))

# Calculando o h(x,y):
n = (y2 - y1) * (x - x1) - (x2 - x1) * (y - y1)
d = math.sqrt((x2 - x1)*2 + (y2 - y1)*2)

if (d <= 0):
    print("Denominador menor que zero, temos uma indeterminação!")
else:
   h = abs(n/d)

print("A menor distância entre o ponto e a reta é", h,".")
