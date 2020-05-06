import math

def suma(a,b):
    return a + b

def resta (a,b):
    return a - b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def potencia(x,y):
    return pow(x, y)

def raiz(x):
    return math.sqrt(x)

def logarit(x):
    return math.log10(x)

def menu():
    print("CALCULADORA")
    print()
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Logaritmos base 10")

    operacion = input("Elige una operación: ")
    return operacion
    
x= float(input("Introduzca el primer número: "))

while True:
    try:
        print("Primer número: "+ str(x))
        print()
        opera= menu()
        

        if opera == "1":
            y= float(input("Introduzca el segundo número: "))
            resultado = suma(x,y)
        elif opera=="2":
            y= float(input("Introduzca el segundo número: "))
            resultado = resta(x,y)
        elif opera =="3":
            y= float(input("Introduzca el segundo número: "))
            resultado = multiplicacion(x,y)
        elif opera == "4":
            y= float(input("Introduzca el segundo número: "))
            resultado = division(x,y)
        elif opera == "5":
            y= float(input("Introduzca el segundo número: "))
            resultado = potencia(x,y)
        elif opera =="6":
            resultado = raiz(x)
        elif opera =="7":
            resultado = logarit(x)
        
        else:
            print("Opción incorrecta, reinicie el programa")
            break

    
        print("El resultado es: ", resultado)

        x= resultado


        continuar = input("Introduzca (n) si no quiere continuar, y cualquier tecla para sí: ")
        

        if continuar == "n":
            print("Has parado el programa")
            break
        
        print()
         
        
        

    except KeyboardInterrupt:
        print("Has cerrado el programa")
        break