# Programa: Sistemas de ecuaciones lineales
# Propósito: Resolver sistemas de ecuaciones mediante Eliminación de Gauss
#            y Gauss-Jordan usando una interfaz por consola.
# Autor: FmCoDeX
# Fecha: 07/10/2026

from metodos.gauss import eliminacion_gauss
from metodos.gauss_jordan import gauss_jordan
from utilidades.entrada import solicitar_sistema
from utilidades.impresion import mostrar_matriz, mostrar_solucion


# Función que muestra el menú principal del programa.
# No recibe parámetros y no retorna valores.
def mostrar_menu():
    print("\n" + "=" * 58)
    print("        SISTEMAS DE ECUACIONES LINEALES")
    print("=" * 58)
    print("1. Eliminación de Gauss")
    print("2. Gauss-Jordan")
    print("3. Salir")
    print("=" * 58)


# Función principal que controla el flujo de la aplicación.
# No recibe parámetros y no retorna valores.
def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "3":
            print("\nPrograma finalizado.")
            print("Gracias por utilizar FmCoDeX 💙")
            break

        if opcion not in {"1", "2"}:
            print("\nOpción no válida.")
            continue

        try:
            matriz = solicitar_sistema()

            print("\nMatriz aumentada ingresada:")
            mostrar_matriz(matriz)

            if opcion == "1":
                solucion, pasos = eliminacion_gauss(matriz)
                nombre_metodo = "Eliminación de Gauss"
            else:
                solucion, pasos = gauss_jordan(matriz)
                nombre_metodo = "Gauss-Jordan"

            print(f"\n{'=' * 58}")
            print(f"RESULTADO - {nombre_metodo.upper()}")
            print("=" * 58)

            for i, paso in enumerate(pasos, start=1):
                print(f"\nPaso {i}:")
                mostrar_matriz(paso)

            mostrar_solucion(solucion)

        except ValueError as error:
            print(f"\nError: {error}")
        except Exception as error:
            print(f"\nOcurrió un error inesperado: {error}")


if __name__ == "__main__":
    main()
