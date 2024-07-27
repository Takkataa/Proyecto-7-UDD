import joblib #Se importa para poder traer los modelos y demas archivos al codigo
import pandas as pd

model = joblib.load("modelo.pkl") # el nombre del archivo que contiene el modelo
scaler = joblib.load("escalador.pkl") #el nombre del archivo que tiene el escalador
acc = joblib.load("acc.pkl") # y la precision del modelo segun sus pruebas
encoders = joblib.load("encoder.pkl") #el nombre del archivo que tiene los encoders
#Funcion para tranformar las columnas categoricas a numericas con sus respectivos encoders
def transform_column(column_name, values):
    encoder = encoders[column_name]
    return encoder.transform(values)

#Funcion definida para generar la predicicon de los datos
def make_prediction(data):
     
     #Se define un formato de los datos
    model_input_data = [
        data["Category"],
        data["Reviews"],
        data["Installs"],
        data["Type"],
        data["Price_usd"],
        data["Content Rating"],
        data["Size_Mb"],
        data["Updated Mes"],
        data["Updated Año"]
    ]
    #Se definen las columnas del df para usar los datos de manera correcta
    columns = ['Category', 'Reviews', 'Installs',"Type","Price_usd","Content Rating","Size_Mb","Updated Mes","Updated Año"]
    
    #Se genera el df en base a los valores ingresados y las columnas anteriores nombradas
    model_input_data =pd.DataFrame([model_input_data], columns=columns)
    
    #Se genera un df para guardar los valores tranformados por los encoders
    transformed_data = model_input_data.copy()
    
    #For para procesar los datos con sus respectivos encoders y se guardan los datos segun su columna en el nuevo df
    for column in model_input_data.columns:
        try:
            transformed_data[column] = transform_column(column, model_input_data[column])
        except KeyError:
            print(f"LabelEncoder para la columna '{column}' no encontrado.") # para el caso de que no exista un encoder para las columnas numericas
        except Exception as e:
            print(f"Error al transformar la columna '{column}': {e}")# Para el caso de que encuentre otro problema en base a valores que no esten codificados
                  
    #Se escalan los datos y se guardan en una variable nueva
    new_data_scaled = scaler.transform(transformed_data)
    #Se realiza la prediccion
    output_data = model.predict(new_data_scaled)[0]
    #Se convierte en entero por si el caso
    calificacion = int(output_data)
    #Se trae la exatitud y se redondea su valor para luego calcular el porcentaje
    accuracy = int(round(acc , 2)*100)
    
    return calificacion, accuracy #Se devuelven los valores de la prediccion y la exactitud para ser mostradas.
