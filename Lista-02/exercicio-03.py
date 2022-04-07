# Leitura dos valores
Xgreen = float(input("Informe o valor para o Xgreen: ")) # 2 (valor de teste aleatório sem considerar um exemplo real)
Xnir = float(input("Informe o valor para o Xnir: ")) # 4 (valor de teste aleatório sem considerar um exemplo real)
Xred = float(input("Informe o valor para o Xred: ")) # 6 (valor de teste aleatório sem considerar um exemplo real)
#Informe o valor para o Xgreen: 2
#Informe o valor para o Xnir: 4
#Informe o valor para o Xred: 6

# Fórmulas
ndwi = (Xgreen - Xnir) / (Xgreen + Xnir)
ndvi = (Xnir - Xred) / (Xnir + Xred)

# Resultado
print("NDWI:", ndwi, "\nNDVI:", ndvi)
# NDWI: -0.3333333333333333 
# NDVI: -0.2
