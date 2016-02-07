# coding=utf-8
n = int(raw_input("Ingrese la cantidad de iteraciones: "))
cont = 0
a = 1L
b = 2L
while cont < n:
    print str(a) + ','
    a, b = b, a + b
    cont = cont + 1
