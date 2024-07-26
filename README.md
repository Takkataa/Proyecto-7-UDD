# Udd Proyecto 7 - Tecnicas avanzadas para ciencia de datos y empleabilidad

Este repositorio contiene toda la informacion respecto a el proyecto 7 del bootcamp de la UDD datacience.
creador: Angel Araya Gonzalez.

Archivos: 

.venv : Entorno virtual que contiene las librerias necesarias y utilizadas para generar el modelo

requierements.txt : Contiene los nombres de las librerias a instalar en el entorno virtual

EDA Y modelo.ipynb : contiene el analisis, liempieza y generacion de los modelos de machine learning para el Api

main.py : Es el archivo que genera el Api, entrega los datos ingresados y llama a la predeccion del modelo para muestra los datos deseados

model.py: Es el archivo que se encarga de generar la prediccion de los datos entregados por main.py, y devolver la prediccion al mismo, este hace el encoding y escala valores para ingresar los datos al modelo

acc.pkl: Este archivo contiene el valor de la precision del model.

modelo.pkl: Este archivo contiene el modelo entrenado.

escalador.pkl: Este archivo contiene el escalador entrenado para los datos del modelo

encoder.pkl: Este archivo contiene los codificadores de las variables categoricas del df, este se utiliza para tranformar los valores str a numeros y luego ser escalados.

## Pasos

1. Crear un entorno virtual (virtualenv)
2. Instalar las dependencias `pip install -r requirements.txt`
3. Ejecutar el servicio `python main.py`

## ¿Cómo probar el servicio?

Una vez realizados los pasos anteriores puede probar
el servicio a traves del navegador o cualquier cliente
rest como postman.

- Postman: debes realizar un post a http://127.0.0.1:5000/predict 
           enviando como body un JSON con la información que requiere 
           el modelo.
