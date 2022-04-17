#!/usr/bin/env python
# -*- coding: utf-8 -*-

#screva um programa em Python que pergunte ao usuário um número qualquer (> 0), 
#...e diga se ele é divisível apenas por 2, apenas por 3, por 2 e por 3, 
#...ou se não é divisível nem por 2 nem por 3.

#entrada de dados

n = int(input('>>> Digite o valor desejado: '))
if (n <= 0):
  print('>>> Digite um número diferente de zero!!!')
