# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:15:26 2019

@author: Borja Rioja Mata
"""
#Importación de librerías
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import sklearn.metrics
from IPython.display import Image as PImage
from subprocess import check_call
from PIL import Image, ImageDraw, ImageFont
from io import StringIO


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

#Creamos la muestra de entrenamiento y de test, tanto para predictores como para la variable objetivo, siendo test el 40%
pred_train, pred_test, tar_train, tar_test = train_test_split(v_pred, v_objetivo, test_size=.4)

#Comprobamos el tamaño de las diferentes muestras (pred=predictora; tar=target, objetivo). La salida en cada caso es una pareja de datos: el tamaño de la muestra y el número de variables
pred_train.shape
pred_test.shape
tar_train.shape
tar_test.shape

#Construimos árbol de decisión con datos de entrenamiento
arbol=DecisionTreeClassifier(class_weight={1:3.5})
arbol=arbol.fit(pred_train,tar_train)

RF=RandomForestClassifier(n_estimators=25,class_weight={1:3.5})
RF=RF.fit(pred_train,tar_train)

GB=GradientBoostingClassifier(n_estimators=100)
GB=RF.fit(pred_train,tar_train)

#Predecimos para los valores del grupo Test
predictions_A=arbol.predict(pred_test)
predictions_RF=RF.predict(pred_test)
predictions_GB=GB.predict(pred_test)

# Creamos matriz de confusión para cada uno de los algortimos
Matrix_Conf_A = sklearn.metrics.confusion_matrix(tar_test,predictions_A)
Matrix_Conf_RF = sklearn.metrics.confusion_matrix(tar_test,predictions_RF)
Matrix_Conf_GB = sklearn.metrics.confusion_matrix(tar_test,predictions_GB)

#Sacamos la tasa de aciertos para cada uno de los algoritmos
Pred_A = sklearn.metrics.accuracy_score(tar_test, predictions_A)
print('Precisión Arbol:'  + str(Pred_A))
Pred_RF = sklearn.metrics.accuracy_score(tar_test, predictions_RF)
print('Precisión Random_Forest:'  + str(Pred_RF))
Pred_GB = sklearn.metrics.accuracy_score(tar_test, predictions_GB)
print('Precisión Random_Forest:'  + str(Pred_GB))




#Pintamos el árbol
#out = StringIO()
#tree.export_graphviz(arbol, out_file='Arbol.dot')

# Convertimos el archivo .dot a png para poder visualizarlo
#check_call(['dot','-Tpng',r'Arbol.dot','-o',r'tree1.png'])
#PImage("tree1.png")

