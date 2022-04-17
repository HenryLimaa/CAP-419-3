#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Faça um programa em Python que leia três números reais e escreva o valor do maior e do menor deles. Para resolver este exercício, não utilizar as funções min/max

lista = [] #lista vazia

#append adiciona um elemento ao final da lista. Prolonga a lista, adicionando no fim todos os elementos do argumento iterable passado como parâmetro
x = lista.append(int(input("1° Valor: ")))
y = lista.append(int(input("2° Valor: ")))
z = lista.append(int(input("3° Valor: ")))

lista_ord = sorted(lista) #chamando a função sorted() para ordenar as informações da lista

print("Maior valor: ", lista_ord [2])
print("Menor valor: ", lista_ord [0])
