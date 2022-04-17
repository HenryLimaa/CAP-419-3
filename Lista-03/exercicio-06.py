#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Faça um programa que pergunte ao usuário o seu conceito final em uma disciplina hipotética. 
#Dependendo do conceito digitado, diga o que ele significa (Excepcional, Bom, etc.). Utilize a tabela de conceitos abaixo:

opcao = 0
while opcao != 11:
  print ('''  [1]  A+
  [2]  A
  [3]  A-
  [4]  B+
  [5]  B
  [6]  B-
  [7]  C+
  [8]  C
  [9]  C-
  [10] D ''') #disponibilizando as opções
  
  opcao = int(input(">>> Qual série você deseja computar? "))
  if opcao == 1:
    print ('A+ Excepcional ')

  elif opcao == 2:
    print (' A  Excelente ')

  elif opcao == 3:
   print ('A- Excelente ')

  elif opcao == 4:
    print ('B+ Bom ')

  elif opcao == 5:
   print ('B  Bom ')

  elif opcao == 6:
    print ('B- Bom ')

  elif opcao == 7:
   print ('C+ Regular ')

  elif opcao == 8:
    print ('C  Regular ')

  elif opcao == 9:
    print ('C- Regular ')

  elif opcao == 10:
   print ('D  Reprovação ')

  else:
    print ('>>> Digite um valor entre 1 e 10!')
    break #encerra o programa para qualquer valor diferente entre 1 e 10
