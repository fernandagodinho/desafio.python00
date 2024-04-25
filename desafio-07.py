# faça um programa que leia o comprimento do cateto opsto e do cateto adjacente de um
# triangulo retangulo, calcule e mostre o comprimento da hipotenusa

import math
co = float (input('comprimento do cateto oposto :'))
ca = float (input('comprimento do cateto adjacente :'))
h1 = math.hypot (co, ca)
print("a hipotenusa vai medir {: .2f}".format (h1))