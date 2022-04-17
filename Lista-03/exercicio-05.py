#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Faça um programa em Python que pergunte ao usuário qual a série que ele deseja calcular e em seguida imprima o nome da série escolhida. 
#Veja o exemplo do que deve ser escrito na tela:

opcao = 0

while opcao != 5:
  print ('''  [0] Lucas
  [1] Pell
  [2] Triangular
  [3] Square
  [4] Pentagonal ''') #disponibilizando as opções
  
  opcao = int(input(">>> Qual série você deseja computar? "))
  if opcao == 0:
    print ('Você escolheu computar a série "Lucas" ')

  elif opcao == 1:
    print ('Você escolheu computar a série "Pell" ')

  elif opcao == 2:
   print ('Você escolheu computar a série "Triangular"')

  elif opcao == 3:
    print ('Você escolheu computar a série "Square"')

  elif opcao == 4:
   print ('Você escolheu computar a série "Pentagonal"')

  else:
    print ('Fim. Tente Novamente!')
