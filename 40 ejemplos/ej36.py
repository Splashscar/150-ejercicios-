import math

def menu():
    print("\n=== Calculadora Científica ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia (x^y)")
    print("6. Raíz cuadrada")
    print("7. Raíz n-ésima")
    print("8. Factorial")
    print("9. Salir")

def calculadora():
    while True:
        menu()
        opcion = input("Elige una opción (1-9): ")

        try:
            if opcion == '1':
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                print("Resultado:", a + b)

            elif opcion == '2':
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                print("Resultado:", a - b)

            elif opcion == '3':
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                print("Resultado:", a * b)

            elif opcion == '4':
                a = float(input("Ingresa el dividendo: "))
                b = float(input("Ingresa el divisor: "))
                if b == 0:
                    print("Error: División entre cero.")
                else:
                    print("Resultado:", a / b)

            elif opcion == '5':
                a = float(input("Ingresa la base: "))
                b = float(input("Ingresa el exponente: "))
                print("Resultado:", math.pow(a, b))

            elif opcion == '6':
                a = float(input("Ingresa el número: "))
                if a < 0:
                    print("Error: No se puede sacar raíz cuadrada de un número negativo.")
                else:
                    print("Resultado:", math.sqrt(a))

            elif opcion == '7':
                a = float(input("Ingresa el número: "))
                n = float(input("Ingresa el índice de la raíz: "))
                if n == 0:
                    print("Error: Índice no puede ser cero.")
                else:
                    print("Resultado:", a ** (1/n))

            elif opcion == '8':
                a = int(input("Ingresa un número entero: "))
                if a < 0:
                    print("Error: No se puede calcular el factorial de un número negativo.")
                else:
                    print("Resultado:", math.factorial(a))

            elif opcion == '9':
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida. Intenta de nuevo.")

        except ValueError:
            print("Entrada no válida. Asegúrate de ingresar números correctos.")
        except Exception as e:
            print("Error:", e)

calculadora()
