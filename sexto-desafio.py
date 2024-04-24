# resolvendo o teorema de pitagoras

import math

def calcular_hipotenusa(cateto_a, cateto_b):
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    return hipotenusa

# Exemplo de uso da função
cateto_a = 3
cateto_b = 4
hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
print(f"A hipotenusa é: {hipotenusa}")
