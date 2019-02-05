#!/usr/bin/python3

import sys
MAXMARGS=4
# sys.argv[0] es el nombre del programa
operando=sys.argv[1]
numero1=sys.argv[2]
numero2=sys.argv[3]

def sum(num1,num2):
    return float(num1)+float(num2)
def rest(num1,num2):
    return float(num1)-float(num2)
def multi(num1,num2):
    return float(num1)*float(num2)
def divi(num1,num2):
    return float(num1)/float(num2)

if __name__ == "__main__":
    if len(sys.argv) != MAXMARGS:
        sys.exit("Usage: python3 calculadora.py operacion operando1 operando2")

    if operando=="suma":
        try:
            print("El resultado es ",sum(numero1,numero2))
        except ValueError:
            print("Meter numeros para realizar la operacion")
    elif operando=="resta":
        try:
            print("El resultado es ",rest(numero1,numero2))
        except ValueError:
            print("Meter numeros para realizar la operacion")
    elif operando=="multiplicacion":
        try:
            print("El resultado es ",multi(numero1,numero2))
        except ValueError:
            print("Meter numeros para realizar la operacion")
    elif operando=="division":
        try:
            print("El resultado es ",divi(numero1,numero2))
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
        except ValueError:
            print("Meter numeros para realizar la operacion")    
    else:
        print("La operacion no es correcta")
