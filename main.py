import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el fichero de entrada
data = pd.read_excel('datos.xlsx', header=None)

# Poner cada fila en un array numérico
array1 = data.iloc[0].values
array2 = data.iloc[1].values


# Multiplicar los dos arrays y ponemos los resultados en un tercer array
result_array = array1 * array2

# Calcular el valor medio y desviación estándar del tercer array
mean_value = np.mean(result_array, axis=0)
std_deviation = np.std(result_array)


# Crear un DataFrame con los resultados para escribir en el fichero Excel
results_df = pd.DataFrame({
    'Array 1': array1,
    'Array 2': array2,
    'Resultados': result_array,
    'Media': [mean_value] * len(result_array),
    'Desviación estándar': [std_deviation] * len(result_array)
})

# Escribir los resultados en un fichero Excel
results_df.to_excel('resultados.xlsx', index=False)

# Hacer un gráfico de los valores en el tercer array
plt.plot(result_array, marker='o', linestyle='-')
plt.title('Valores del tercer array')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.savefig('grafico.png')
plt.show()
