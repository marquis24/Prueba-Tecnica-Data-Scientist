
# Prueba Técnica - Data Scientist

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un script en Python para procesar datos numéricos contenidos en un archivo Excel, realizar cálculos estadísticos y generar visualizaciones automáticas.

Se busca demostrar habilidades en la limpieza y preparación de datos, consultas optimizadas, análisis exploratorio y presentación clara de resultados.

---

## Datasets

* **datos.xlsx**: Archivo Excel con datos numéricos que se utilizarán como entrada para el script.

---

## Archivos Incluidos

| Archivo            | Descripción                                      |
| ------------------ | ------------------------------------------------ |
| `main.py`          | Script principal que ejecuta el procesamiento.   |
| `datos.xlsx`       | Archivo Excel con los datos numéricos.           |
| `requirements.txt` | Dependencias necesarias para ejecutar el script. |
| `.venv`            | Entorno virtual para el proyecto.                |

---

## Funcionalidades Principales

* Lectura del archivo Excel y extracción de datos en arrays numéricos.
* Multiplicación elemento a elemento de los dos arrays y almacenamiento en un tercer array.
* Cálculo de la media y desviación estándar del array resultante.
* Escritura de los resultados en un nuevo archivo Excel.
* Generación automática de un gráfico de los valores del array resultante, directamente desde Python.

---

## Tecnologías Utilizadas

* **Python** con librerías: `pandas`, `numpy`, `matplotlib`
* Manipulación de archivos Excel con `openpyxl`
* Análisis exploratorio realizado mediante Jupyter Notebook (opcional para visualización y desarrollo)

---

## Objetivos 

El proyecto busca validar la capacidad para:

* Procesar datos estructurados eficientemente.
* Realizar cálculos estadísticos básicos.
* Presentar resultados de forma clara y visual.
* Desarrollar un flujo de trabajo reproducible y modular.

---

## Preguntas de Evaluación

### ¿Cómo diseñarías una interfaz frontend para interactuar con el script Python?

Para facilitar la interacción del usuario con el procesamiento Python, propondría desarrollar una aplicación web con las siguientes características:

* **Carga de archivos:** Permitir al usuario subir el archivo Excel desde la interfaz.
* **Visualización de resultados:** Mostrar la media, desviación estándar y gráficos generados tras el procesamiento.
* **Tecnologías backend:** Usar Django para la gestión de la lógica de negocio y/o FastAPI para exponer una API REST que maneje la ejecución del script.
* **Tecnologías frontend:** Crear una interfaz interactiva con React, apoyada en HTML, CSS y JavaScript para una experiencia fluida y responsiva.

Esta arquitectura permitiría separar claramente la lógica de procesamiento de datos (backend) y la experiencia de usuario (frontend), facilitando mantenimiento y escalabilidad.

---

## Recomendaciones para mejorar el proyecto

* Incluir manejo de excepciones para casos donde el archivo Excel no tenga el formato esperado o datos erróneos.
* Añadir validaciones de entrada y mensajes claros para el usuario.
* Documentar con más detalle cada función en el script `main.py` para facilitar su mantenimiento.
* Automatizar la generación de informes en formato PDF o HTML que incluyan resultados y gráficos.
* Considerar la integración de tests unitarios para asegurar la robustez del código.
