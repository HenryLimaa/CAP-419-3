#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escreva um programa em Python que simule uma calculadora com as 04 funções básicas (, , , ). 
#O programa deve pedir ao usuário para entrar com os operandos (números reais) e o tipo de operação (+, -, /, *) e, a seguir, deverá escrever o resultado.

#entrada de valores
n1 = float(input('>>> Digite o Primeiro valor: '))
n2 = float(input('>>> Digite o Segundo valor: '))

opcao = 0
while opcao != 4:
  
  print ('''  [1] Soma
  [2] Subtração
  [3] Multipicação
  [4] Divisão ''') #exibindo as opções
  
  opcao = int(input('>>> Informe a sua opção! '))
  if opcao == 1:
    soma = n1 + n2
    print ('A soma entre os valores {} e {} = {}'.format(n1, n2, soma))
  
  elif opcao == 2:
    subtracao = n1 - n2
    print ('A subtração entre os vlores {} e {} = {}'.format(n1, n2, subtracao))
  
  elif opcao == 3:
    produto = n1 * n2
    print ('O produto entre os vlores {} e {} = {}'.format(n1, n2, produto))
  
  elif opcao == 4:
    divisao = n1 / n2
    print ('A divisão entre os vlores {} e {} = {}'.format(n1, n2, divisao))

  else:
    print ('Opção inválida. Tente Novamente!')
  
  print ('Fim')
