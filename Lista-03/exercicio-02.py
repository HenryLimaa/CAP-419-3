#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escreva um programa em Python que leia o tamanho dos lados de um triângulo, 
#...avalie se esses valores realmente formam um triângulo, e em caso positivo, 
#...classifique o triângulo em isósceles, escaleno ou equilátero.

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

   # Testando se é triângulo
    if (a + b < c) or (a + c < b) or (b + c < a):
        print('Nao é um triangulo')
    elif (a == b) and (a == c) :
        print('Equilatero')
    elif (a==b) or (a==c) or (b==c):
        print('Isósceles')
    else:
        print('Escaleno')
