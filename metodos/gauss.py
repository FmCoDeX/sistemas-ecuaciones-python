# Programa: Eliminación de Gauss
# Propósito: Resolver un sistema de ecuaciones lineales usando
#            eliminación hacia adelante y sustitución regresiva.
# Autor: FmCoDeX
# Fecha: 07/10/2026


# Función que resuelve un sistema mediante Eliminación de Gauss.
# Parámetro:
# matriz: matriz aumentada del sistema, tipo list[list[float]].
# Retorna:
# solucion: lista con los valores de las incógnitas.
# pasos: lista de matrices resultantes durante el procedimiento.
def eliminacion_gauss(matriz):
    a = [fila[:] for fila in matriz]
    n = len(a)
    pasos = []

    for columna in range(n):
        pivote = max(range(columna, n), key=lambda fila: abs(a[fila][columna]))

        if abs(a[pivote][columna]) < 1e-12:
            raise ValueError(
                "El sistema no tiene solución única o la matriz es singular."
            )

        if pivote != columna:
            a[columna], a[pivote] = a[pivote], a[columna]
            pasos.append([fila[:] for fila in a])

        for fila in range(columna + 1, n):
            factor = a[fila][columna] / a[columna][columna]

            for j in range(columna, n + 1):
                a[fila][j] -= factor * a[columna][j]

            pasos.append([f[:] for f in a])

    solucion = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = sum(a[i][j] * solucion[j] for j in range(i + 1, n))
        solucion[i] = (a[i][n] - suma) / a[i][i]

    return solucion, pasos
