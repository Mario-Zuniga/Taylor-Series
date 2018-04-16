#Importacion de paquetes
from scipy import *
from numpy import *
from sympy import *
from math import *

#Valor que tendra la serie de taylor
n = 3

#Declaramos simbolos para funciones
y = Symbol ('y')
x = Symbol ('x')

#Valores de X y Y
X = 10.0
Y = 15.0

#Datos para la funcion
A = 1
B = 1
w = (2*pi)/6.35

#Funcion
f = A*cos(w*(x/10)) + B*sin(w*(y/10))

#Valores de a y b
a = 5.0
b = 10.0

result = 0

#Comenzamos la serie de Taylor
for cont in range(0, n):
	if cont == 0:
		result = result + f.subs([(x, a), (y, b)])

	if cont == 1:
	dfx = f.diff((x, 1))
	dfy = f.diff((y, 1))
	result = result + (1/factorial(cont)) * ((x * dfx.subs([(x, a), (y, b)])) + (y * dfy.subs([(x, a), (y, b)])))

	if cont == 2:
		dfxy = dfx.diff(y, 1)
		dfx = dfx.diff(x, 1)
		dfy = dfy.diff(y, 1)
		result = result + (1/factorial(cont)) * ((x**cont * dfx.subs([(x, a), (y, b)])) + ((cont*x*y) * dfxy.subs([(x, a), (y, b)])) + (y**cont * dfy.subs([(x, a), (y, b)])))

	if cont >= 3:
	dfxy2 = dfxy
	dfxy = dfxy.diff(x, 1)
	dfxy2 = dfxy2.diff(y, 1)
	dfx = dfx.diff(x, 1)
	dfy = dfy.diff(y, 1)
	result = result + (1/factorial(cont)) * ((x**cont * dfx.subs([(x, a), (y, b)])) + ((cont*(x**cont-1)*y) * dfxy.subs([(x, a), (y, b)])) + ((cont*(y**cont-1)*x) * dfxy2.subs([(x, a), (y, b)])) + (y**cont * dfy.subs([(x, a), (y, b)])))

print(result)