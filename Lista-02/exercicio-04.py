# Biblioteca
import math
from math import asin, cos, pi, radians, sin, sqrt

#Perguta ao usuário lat1/lon1          # São Bernardo do Campo
lat1 = float(input("Latitude 1: "))    #lat1 = -23.6944 #latitude
lon1 = float(input("Longitude 1: "))   #lon1 = -46.5654 #longitude

#Perguta ao usuário lat2/lon2          # São José dos Campos
lat2 = float(input("Latitude 2: "))    #lat2 = -23.1791 #latitude
lon2 = float(input("Longitude 2: "))   #lon2 = -45.8872 #longitude

#Constantes
# Raio Médio da Terra
R = 6371

#Conversão para radianos
#Função
lat1 = radians(lat1)
lat2 = radians(lat2)
lon1 = radians(lon1)
lon2 = radians(lon2)

# Fórmula
# lat1 = lat1 * pi / 180
# lat2 = lat2 * pi / 180
# lon1 = lon1 * pi / 180
# lon2 = lon2 * pi / 180

#Delta
dLat = lat2 - lat1
dLon = lon2 - lon1

#formula de Haversine
A = pow(sin(dLat/2), 2)
B = cos(lat1) * cos(lat2)
C = pow(sin(dLon/2), 2)
D = sqrt(A + B * C)
E = 2 * R * asin(D)

print(E)
# 89.83574577076772
