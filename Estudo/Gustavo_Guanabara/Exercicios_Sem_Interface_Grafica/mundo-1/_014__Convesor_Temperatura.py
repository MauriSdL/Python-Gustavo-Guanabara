import os
os.system("clear")

'''
Crie um programa que converta uma temperatura de Celsius para Fahrenheit.
Formulas:
1. Celsius e Fahrenheit
Celsius para Fahrenheit: --> F = (C * 1.8) + 32
Fahrenheit para Celsius: --> C = (F - 32) / 1.8

2. Celsius e Kelvin
Celsius para Kelvin: --> k = C + 273.15
Kelvin para Celsius: --> C = K - 273.15

3. Fahrenheit e Kelvin
Fahrenheit para Kelvin: --> K = (((F - 32) * 5) / 9) + 273.15
Kelvin para Fahrenheit: --> F = ((K - 273.15) * 1.8) + 32
'''
print()
print('x'*20, "Conversor de temperatura", 'x'*20)
print()

temperatura = float(input("Temperatura: "))

# Fahrenheit para Cesius
Fahrenheit = (temperatura - 32) / 1.8
celsius = (temperatura * 1.8) + 32
kelvin = temperatura + 273.15

print(f"{temperatura} Celsius para Fahrenheit = {celsius:.2f}")
print(f"{temperatura} Fahrenheit para Celsius = {Fahrenheit:.2f}")
print(f"{temperatura} Celsius para kelvin = {kelvin:.2f}")
print()