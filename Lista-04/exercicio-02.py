#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escrever um programa em Python que simule uma calculadora com as funções básicas (, , , )...
#...O programa deve pedir ao usuário para entrar com os operandos (números reais) e o tipo de operação, 
#...e a seguir escrever o resultado. Assim como uma calculadora, que ao final de uma operação pode ser utilizada novamente, 
#...você deve simular este comportamento perguntando ao usuário se ele quer realizar uma nova operação.

def calculate():
    operation = input('''
Por favor, informe a operação matemática que você gostaria de usar:
+ Soma
- Subtração
* Multipliação
/ Divisão
''')

    n1 = int(input('Informe o 1° Número: '))
    n2 = int(input('Informe o 2° Número: '))

    if operation == '+':
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)

    elif operation == '-':
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)

    elif operation == '*':
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)

    elif operation == '/':
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)

    else:
        print('Opção inválida. Tente Novamente!')

    # Adicionando a função again() à função calculate()
    again()

def again():
    calc_again = input('''
Deseja calcular novamente?
Digite S para SIM ou N para NÃO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Fim.')
    else:
        again()

calculate()
