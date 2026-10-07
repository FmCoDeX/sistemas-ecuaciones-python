# Programa: Utilidades de impresión
# Propósito: Mostrar matrices y soluciones de forma ordenada.
# Autor: FmCoDeX
# Fecha: 07/10/2026


# Función que muestra una matriz aumentada con formato.
# Parámetro:
# matriz: matriz aumentada tipo list[list[float]].
# No retorna valores.
def mostrar_matriz(matriz):
    for fila in matriz:
        izquierda = " ".join(f"{valor:10.4f}" for valor in fila[:-1])
        print(f"[ {izquierda} | {fila[-1]:10.4f} ]")


# Función que muestra la solución final del sistema.
# Parámetro:
# solucion: lista de valores numéricos.
# No retorna valores.
def mostrar_solucion(solucion):
    nombres = ["x", "y", "z", "w", "v", "u"]

    print("\n" + "-" * 30)
    print("SOLUCIÓN")
    print("-" * 30)

    for i, valor in enumerate(solucion):
        variable = nombres[i] if i < len(nombres) else f"x{i + 1}"
        print(f"{variable} = {valor:.6f}")
