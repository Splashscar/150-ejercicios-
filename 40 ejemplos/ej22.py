def sumaria(a, b):
    resultad = a + b
    return resultad
def restaria(a, b):
    resultad = a - b
    return resultad
def multiplicacion(a, b):
    resultad = a * b
    return resultad
def division(a, b):
    resultad = a / b
    return resultad
num1 = 15
num2 = 3

print("CALCULADORA CON FUNCIONES")
print(f"Números a operar: {num1} y {num2}")
print("-" * 30)
print(f"{num1} + {num2} = {sumaria(num1, num2)}")
print(f"{num1} - {num2} = {restaria(num1, num2)}")
print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
print(f"{num1} / {num2} = {division(num1, num2)}")
print("-" * 30)
print("¡He terminado las operaciones!")