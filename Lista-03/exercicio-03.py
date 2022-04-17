#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escreva um programa em Python que pergunte ao usuário um número entre 0 e 10, e diga se ele é ímpar ou par.

numero = int(input('Digite um número entre 0 e 10: '))

if (numero%2) == 0:
  print("Par")
else:
  print("Ímpar")
