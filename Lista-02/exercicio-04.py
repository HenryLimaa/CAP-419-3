# Biblioteca
import math
from math import asin, cos, pi, radians, sin, sqrt

#Constantes
# São Bernardo do Campo
lat1 = -23.6944 #latitude
lon1 = -46.5654 #longitude
# São José dos Campos
lat2 = -23.1791 #latitude
lon2 = -45.8872 #longitude
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


print(E)
# 89.83574577076772
