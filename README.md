# 🎲 Simulación de la Máquina de Galton

Este proyecto implementa una **simulación de la máquina de Galton** usando Python.  
La **máquina de Galton**, ideada por Sir Francis Galton, muestra cómo **decisiones aleatorias binarias** (izquierda/derecha) pueden producir una **distribución aproximadamente normal**, similar a la famosa **campana de Gauss**.

---

## 📌 Descripción del Proyecto

En esta simulación:

- 🔵 Se lanzan **3,000 canicas**.
- 🟡 Cada canica atraviesa **12 niveles de obstáculos**.
- 🔴 Al finalizar, las canicas caen en **13 contenedores posibles** (de 0 a 12), según cuántas veces eligieron ir hacia la derecha.
- 📊 Se genera un **histograma gráfico** usando `matplotlib` para visualizar la distribución final.

---

## ⚙️ Funcionamiento del Programa

### 🧩 Estructura del Código

El código se organiza en dos funciones principales:

- `simulate_marbles(num_marbles, levels)`:  
  Simula el recorrido de cada canica, acumulando la cantidad que cae en cada contenedor dependiendo del número de veces que fue a la derecha.

- `plot_histogram(data, levels)`:  
  Muestra un gráfico de barras que representa la cantidad de canicas por contenedor usando la librería `matplotlib`.

### 🧪 Librerías Utilizadas

- `random`: Para simular la decisión binaria de cada canica en cada nivel (izquierda o derecha).
- `matplotlib.pyplot`: Para graficar el histograma final de forma visual y clara.

> Nota: **No se usa la función `normal()`** ni ninguna distribución estadística explícita. El comportamiento emerge naturalmente por la probabilidad acumulada.

---

## ▶️ Ejecución

### 📌 Requisitos previos

Instala la librería necesaria con:

```bash
pip install matplotlib
