#!/usr/bin/env python
# -*- coding: utf-8 -*-

#screva um programa em Python que pergunte ao usuário um número qualquer (> 0), 
#...e diga se ele é divisível apenas por 2, apenas por 3, por 2 e por 3, 
#...ou se não é divisível nem por 2 nem por 3.

n = 0

while n<1:
  n = int(input('>>> Digite o valor desejado (>0): ')) # entrada de dados
  if (n <= 0):
    print('>>> Digite um número diferente de zero!!!')

div = [2,3]
vefif = [0,0]
for i, d in enumerate(div):
  if n%d == 0
  verif[i] = 1

if sum(verif) == 0:
  print("O valor informado é: ",n , "não é divisivel por 2 ou 3!")
else:
  print("O valor informado: ", n , "É divisível por: ", \
        [value for i, value in enumerate(div if verif[i] == 1)])
