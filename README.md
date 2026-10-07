# 🧮 Sistemas de Ecuaciones Lineales en Python

Aplicación de consola desarrollada en **Python** para resolver sistemas de ecuaciones lineales mediante los métodos de **Eliminación de Gauss** y **Gauss-Jordan**.

## 👩‍💻 Autora

**FmCoDeX**

---

## ✨ Funcionalidades

- Resolver sistemas de 2 o más ecuaciones.
- Método de Eliminación de Gauss.
- Método de Gauss-Jordan.
- Pivoteo parcial.
- Visualización de la matriz aumentada.
- Visualización de los pasos intermedios.
- Cálculo de la solución final.
- Validación básica de los datos ingresados.
- Código organizado en módulos.

---

## 📁 Estructura del proyecto

```text
sistemas-ecuaciones-python/
│
├── main.py
│
├── README.md
│
├── metodos/
│   ├── __init__.py
│   ├── gauss.py
│   └── gauss_jordan.py
│
└── utilidades/
    ├── __init__.py
    ├── entrada.py
    └── impresion.py
```

---

## 🚀 Ejecución

Desde una terminal, dentro de la carpeta del proyecto:

```bash
python main.py
```

En Windows también puedes usar:

```bash
py main.py
```

---

## 🧪 Ejemplo

Sistema:

```text
2x + y - z = 8
-3x - y + 2z = -11
-2x + y + 2z = -3
```

En el programa se ingresa:

```text
Número de ecuaciones/incógnitas: 3

Ecuación 1: 2 1 -1 8
Ecuación 2: -3 -1 2 -11
Ecuación 3: -2 1 2 -3
```

La solución esperada es:

```text
x = 2
y = 3
z = -1
```

---

## 📚 Métodos implementados

### Eliminación de Gauss

Transforma la matriz aumentada en una matriz triangular superior y posteriormente aplica sustitución regresiva para encontrar las incógnitas.

### Gauss-Jordan

Transforma la matriz aumentada hasta obtener la matriz identidad en el lado izquierdo. Los términos independientes resultantes corresponden directamente a la solución.

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Programación modular
- Git
- GitHub

---

## 🎯 Objetivo

Aplicar métodos numéricos para resolver sistemas de ecuaciones lineales, organizando el código en módulos y mostrando el procedimiento de manera clara desde la consola.

---

<div align="center">

### 💙 FmCoDeX

**Código · Creatividad · Tecnología**

</div>
