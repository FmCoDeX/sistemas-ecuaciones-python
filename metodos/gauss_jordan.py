# Programa: Método de Gauss-Jordan
# Propósito: Resolver un sistema de ecuaciones lineales llevando
#            la matriz aumentada a su forma escalonada reducida.
# Autor: FmCoDeX
# Fecha: 07/10/2026


# Función que resuelve un sistema mediante Gauss-Jordan.
# Parámetro:
# matriz: matriz aumentada del sistema, tipo list[list[float]].
# Retorna:
# solucion: lista con los valores de las incógnitas.
# pasos: lista de matrices resultantes durante el procedimiento.
def gauss_jordan(matriz):
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

        valor_pivote = a[columna][columna]

        for j in range(n + 1):
            a[columna][j] /= valor_pivote

        pasos.append([fila[:] for fila in a])

        for fila in range(n):
            if fila == columna:
                continue

            factor = a[fila][columna]

            for j in range(n + 1):
                a[fila][j] -= factor * a[columna][j]

            pasos.append([f[:] for f in a])

    solucion = [a[i][n] for i in range(n)]

    return solucion, pasos
