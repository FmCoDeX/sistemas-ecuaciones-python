# Programa: Entrada de datos
# Propósito: Solicitar y validar los coeficientes de un sistema
#            de ecuaciones lineales.
# Autor: FmCoDeX
# Fecha: 07/10/2026


# Función que solicita al usuario el tamaño y los coeficientes
# del sistema de ecuaciones.
# No recibe parámetros.
# Retorna una matriz aumentada tipo list[list[float]].
def solicitar_sistema():
    try:
        n = int(input("\nNúmero de ecuaciones/incógnitas: "))
    except ValueError:
        raise ValueError("El número de ecuaciones debe ser un entero.")

    if n < 2:
        raise ValueError("El sistema debe tener al menos 2 ecuaciones.")

    matriz = []

    print("\nIngrese los coeficientes de cada ecuación.")
    print("Ejemplo para 2x + 3y = 7 → 2 3 7")

    for i in range(n):
        while True:
            entrada = input(f"Ecuación {i + 1}: ").strip().split()

            if len(entrada) != n + 1:
                print(
                    f"Debe ingresar exactamente {n + 1} números "
                    f"({n} coeficientes y el término independiente)."
                )
                continue

            try:
                fila = [float(valor) for valor in entrada]
                matriz.append(fila)
                break
            except ValueError:
                print("Todos los valores deben ser numéricos.")

    return matriz
