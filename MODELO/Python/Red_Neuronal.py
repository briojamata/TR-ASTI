# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:15:26 2019

@author: Borja Rioja Mata
"""
#Importación de librerías
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.neural_network import MLPClassifier



#Obtenemos el fichero CSV para el análisis predictivo
df = pd.read_csv (r'C:\Users\Borja\Desktop\TR ASTI\MODELO\Ficheros\Fichero_Base.csv', sep = ';')
df.head()
df.describe()

#Limpieza de valores missing del dataset
df_clean = df.dropna()

#Observamos tipos de datos
df_clean.dtypes
#Principales estadísticos
df_clean.describe()

#Asigno variables predictoras 
v_pred = df_clean[['SOC', 'Carga_Trabajo','Bots_Activos','Mes','dia_semana','hora','CONSUMO_TOTAL','DISTANCIA_TOTAL']]

#Asigno variable objetivo
v_objetivo = df_clean.MCA_CARGAR


#Buscamos una red neuronal que nos acierte mas del 98 por ciento de los casos
i=0
while True:    
    pred_train, pred_test, tar_train, tar_test = train_test_split(v_pred, v_objetivo, test_size=.3)
    RedNeuronal=MLPClassifier()
    RedNeuronal=MLPClassifier()
    RedNeuronal=RedNeuronal.fit(pred_train,tar_train)
    print('Precision RN:'+ str(RedNeuronal.score(pred_train,tar_train)))
    i = i+1
    print('Numero de Redes creadas:'+ str(i))
    
    if (RedNeuronal.score(pred_train,tar_train) > 0.98) or i >30:
        break
         
        




