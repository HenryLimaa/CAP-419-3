#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escreva um programa em Python que pergunte ao usuário um número entre 0 e 10, e diga se ele é ímpar ou par.

n = -1

while n < 0 or n > 10:
  n = int(input('Digite um número entre 0 e 10: '))

if (n%2) == 0:
  print("Par")
else:
  print("Ímpar")
