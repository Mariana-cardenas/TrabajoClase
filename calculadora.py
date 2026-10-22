
def sumar(numeros):
    return sum(numeros)


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


while True:
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "5":
        print("Gracias por utilizar la calculadora.")
        break

    if opcion not in ("1", "2", "3", "4"):
        print("Opción no válida. Intenta nuevamente.")
        continue

    entrada = input("Ingresa los números separados por comas: ")

    try:
        numeros = [float(n.strip()) for n in entrada.split(",")]

        if len(numeros) < 2:
            print("Debes ingresar al menos dos números.")
            continue

        if opcion == "1":
            resultado = sumar(numeros)
        elif opcion == "2":
            resultado = restar(numeros)
        elif opcion == "3":
            resultado = multiplicar(numeros)
        else:
            resultado = dividir(numeros)

        print("Resultado:", resultado)

    except ValueError:
        print("Error: ingresa números válidos separados por comas.")
