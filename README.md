# Udd Proyecto 7 - Técnicas avanzadas para ciencia de datos y empleabilidad

Este repositorio contiene toda la información respecto a el proyecto 7 del bootcamp de la UDD Data Science.

**Creador: Angel Araya Gonzalez.**

## Descripción

Este proyecto se creó en base al sigueinte dataset de kaggle:

*https://www.kaggle.com/datasets/lava18/google-play-store-apps*

Este dataset contiene información de Apps de la Google Store del año 2018, esto incluye:

- Nombres
- Categorías
- Calificaciones o Rating
- Cantidad de Reseñas o Reviews
- Tamaños en Mb, Kb y b
- Cantidad de Descargas o Instalaciones
- Si es gratuita o de pago
- Precios
- Tipo de contenido
- Últimas actualizaciones
- Versiones de las apps
- Versiones del sistema android

La idea de usar esta información de las apps es identificar que aplicaciones o qué rasgos de estas son mejores que otros, con el fin crear apps con esos rasgos y generar que sean competitivas en el mercado (Por supuesto sería deseable analizar información mas actualizada, pero es genial comenzar por algo).
Pero no es lo unico que se puede hacer con esta información, con la misma se planea buscar relaciones entre las variables para entrenar un modelo de machine learning que logre clasificar las apps según sus datos. Esta Clasificación en si, seria su valoración/calificación de 1 a 5 puntos.

Por lo que la siguiente información descrita tiene el objetivo de enseñar a usar el modelo empleado como tambien ver el análisis correspondiente.

## Archivos: 

- Análisis:

    - Presentación : Es una breve presentación que explica el análisis realizado junto con los objetivos del proyecto.
    - EDA&MODEL.ipynb : Este archivo jupiter, contiene el análisis del dataset de google y también el desarrollo del modelo creado.
    - requirementsforeda.txt: Contiene las librerías utilizadas para realizar el análisis y el modelo.

- Modelo:

    - modelo.pkl : Es el modelo de machine learning creado para la Api
    - encoder.pkl: Contiene la información del las variables categoricas codificadas para el modelo.
    - escalador.pkl: Contiene la informacion del escalador de los datos númericos del modelo
    - acc.pkl: Contiene la información de la exactitud del modelo creado.

- Api Web:

    - main.py: Contiene el programa principal del Api, en él se llama al modelo y se ingresan los datos para tener el resultado.
    - model.py: Contiene el programa que transforma los datos ingresados para poder ser procesados por el modelo y devuelve los resultados de las predicciones.
    - requirements.txt:  Contiene las librerías necesarias para tanto main.py y model.py puedan ser ejecutadas por el servicio web.
    - Procfile: Indica al servicio Web cuál es el archivo principal, de esta manera se ejecuta el servicio.
    - runtime.txt: Indica la versión de python que debe instalar el servicio web para lograr ejecutar el modelo.
    - .slugignore: Indica los tipos de archivos innecesarios para ejecutar el Api, de esta manera el servicio web optimiza el espacio.

## Como usar el Api del servicio Web.

1. Se debe tener intalado o a su disponibilidad un cliente HTTP de línea de commandos como puede ser HTTPie.
2. Luego en la sección del URL debe ingresar el siguiente link *"https://califiacionapp-8a45adf76c94.herokuapp.com/home_page"* con el método "GET" para revisar si funciona correctamente el Api.
3. Una vez comprobado el funcionamiento, en el link *"https://califiacionapp-8a45adf76c94.herokuapp.com/predict"* con el método "POST" debe ingresar los valores de las variables necesarias para que el modelo devuelva la prediccion de los datos.

    - Los datos deben tener el sigueinte formato:

        {"Category": "FAMILY",
        "Reviews": 92010,
        "Installs": 1000000,
        "Type": "Free",
        "Price_usd": 0.0,
        "Content Rating": "Everyone",
        "Size_Mb": 5.9,
        "Updated Mes": 9,
        "Updated Año": 2018}

    Puedes usar estos mismos datos si lo prefieres. Debes considerar que si cambias los valores deben ser del mismo tipo de dato que los del ejemplo.

4. Con ello el Api devolvera la calificación entregada por el modelo junto con la exactitud del mismo.
