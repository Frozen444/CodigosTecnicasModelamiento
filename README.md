# Modelo SEIR-SI para el Dengue
Códigos realizados para el proyecto final del curso de Técnicas de Modelamiento. 

Este repositorio contiene tres códigos Python relacionados con la modelización matemática de la dinámica del dengue, considerando tanto a la población humana como a los mosquitos. Los modelos utilizados están basados en el enfoque SEIR (Susceptible, Expuesto, Infectado, Recuperado) extendido para humanos y un modelo similar para los mosquitos. Los códigos están completamente comentados para facilitar su comprensión y análisis.

## Paquetes Utilizados

Los códigos de este repositorio hacen uso de los siguientes paquetes Python:

- **sympy**: Para la resolución simbólica de las ecuaciones y el cálculo de la matriz Jacobiana y los puntos críticos.
- **scipy**: Para la integración numérica de las ecuaciones diferenciales en el modelo dinámico del dengue.
- **dash**: Para la creación de una aplicación web interactiva que permite la visualización de los resultados y la modificación de parámetros del modelo.
- **plotly**: Para la creación de gráficos interactivos que visualizan las poblaciones humanas y de mosquitos en función del tiempo.

Los tres códigos tienen objetivos distintos:

1. **Cálculo de los Puntos Críticos**:
Este código se encarga de calcular los puntos críticos (o puntos de equilibrio) del modelo de la dinámica del dengue entre humanos y mosquitos. Los puntos críticos corresponden a los valores de las poblaciones de cada grupo (humanos y mosquitos) en los cuales las tasas de cambio de todas las poblaciones son iguales a cero. En términos simples, estos son los valores de las poblaciones donde el sistema alcanza un estado de equilibrio, y no hay más cambios en las cantidades de individuos de cada grupo (susceptibles, expuestos, infectados, etc.).

**Objetivo**: Verificar los resultados del calculo de los puntos críticos obtenidos de manera manual.

3. **Cálculo de la Matriz Jacobiana**:
Este código calcula la matriz Jacobiana del sistema de ecuaciones diferenciales, que es útil para analizar la estabilidad de los puntos críticos. Utiliza el paquete sympy para calcular la derivada de cada ecuación con respecto a cada variable, formando la matriz que describe la sensibilidad de las tasas de cambio de las poblaciones frente a cambios en los valores de las variables.

**Objetivo**: Verificar la estabilidad de los puntos críticos obtenidos, y verificar la matriz Jacobiana obtenida de manera manual.

5. **Simulación del Modelo SEIR-SI para el Dengue**:
Este código simula la evolución del sistema de ecuaciones diferenciales, resolviendo el modelo con diferentes parámetros y generando gráficas interactivas para visualizar las dinámicas de las poblaciones humanas y de mosquitos en el contexto de la transmisión del dengue. Utiliza la librería odeint de scipy para resolver las ecuaciones diferenciales del modelo y plotly para generar gráficas interactivas.**(Verificar si Dash está instalado antes de ejecutar el código del modelo para que el código no lance un error de importación)**

**Objetivo**: Simular el comportamiento del sistema para diferentes parámetros, visualizando cómo cambian las poblaciones de humanos y mosquitos a lo largo del tiempo.




