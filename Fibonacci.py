# coding=utf-8
n = int(raw_input("Ingrese la cantidad de iteraciones: "))
cont = 0
a = 1L
b = 2L
while cont < n:
    cont = cont + 1
    print str(a) + ','
    a, b = b, a + b
