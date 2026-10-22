
def sumar(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


def restar(numeros):
    resultado = numeros[0]
    for numero in numeros[1:]:
        resultado -= numero
    return resultado


def multiplicar(numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


def dividir(numeros):
    resultado = numeros[0]
    for numero in numeros[1:]:
        if numero == 0:
            return "Error: no se puede dividir entre cero"
        resultado /= numero
    return resultado


print("=== CALCULADORA ===")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Selecciona una opción: ")

if opcion in ("1", "2", "3", "4"):
    entrada = input("Ingresa los números separados por comas: ")

    try:
        numeros = [float(n.strip()) for n in entrada.split(",")]

        if len(numeros) < 2:
            print("Debes ingresar al menos dos números.")
        elif opcion == "1":
            print("Resultado:", sumar(numeros))
        elif opcion == "2":
            print("Resultado:", restar(numeros))
        elif opcion == "3":
            print("Resultado:", multiplicar(numeros))
        else:
            print("Resultado:", dividir(numeros))

    except ValueError:
        print("Error: ingresa únicamente números separados por comas.")
else:
    print("Opción no válida.")
