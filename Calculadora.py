# Definir funciones para operaciones matematicas

def suma(x, y) :
    return x + y

def resta(x, y) :
    return x - y

def multiplicacion(x, y) :
    return x * y

def division(x, y) :
    if y !=0 :
        return x / y
    else :
        return "Error: division por cero"
    
# Menu de la calculadora

print("Seleccione una operacion")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

# Solicitar al usuario que elija una operacion

opcion = input("Ingrese el numero de la operacion deseada: ")

# Solicitar al usuario q ingrese dos  numeros

num1= float(input("Ingrese el primer numero: "))
num2= float(input("Ingrese el segundo numero: "))
    
# Realizar la operacion segun la eleccion del usuario

if opcion == "1" :
    print(num1, "+", num2, "=" , suma(num1, num2))

elif opcion == "2" :
    print(num1, "-", num2, "=" , suma(num1, num2))

elif opcion == "3" :
    print(num1, "*", num2, "=" , suma(num1, num2))

elif opcion == "4" :
    print(num1, "/", num2, "=" , suma(num1, num2))
    
else:
    print("Operacion no valida")