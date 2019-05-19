# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:15:26 2019

@author: Borja
"""
import pandas as pd
import numpy as np
import matplotlib.pylab as plt 
import seaborn as sns

 
#Obtenemos el fichero CSV para el análisis de  Bots activos y operaciones
df = pd.read_csv (r'C:\Users\Borja\Desktop\TR ASTI\EDA\Ficheros\Carga_Trabajo_Bots.csv', sep = ';')
df.head()

df.describe()

#Análisis de Bots activos y operaciones por hora
Oper_group_by_hora = df.filter(items=['Operaciones', 'hora']).groupby(by=['hora']).Operaciones.sum().plot(kind='bar',subplots='true')
Oper_group_by_hora = df.filter(items=['Operaciones', 'hora']).groupby(by=['hora']).Operaciones.mean().plot(kind='bar',subplots='true')

Bots_group_by_hora = df.filter(items=['BOTS', 'hora']).groupby(by=['hora']).BOTS.mean().plot(kind='bar',subplots='true')

#Análisis de Bots activos y operaciones por dia de la semana
Oper_group_by_dia = df.filter(items=['Operaciones', 'dia_semana']).groupby(by=['dia_semana']).Operaciones.sum().plot(kind='bar',subplots='true')

Bots_group_by_hora = df.filter(items=['BOTS', 'dia_semana']).groupby(by=['dia_semana']).BOTS.mean().plot(kind='bar',subplots='true')

#Análisis de Bots activos y operaciones por mes
Oper_group_by_mes = df.filter(items=['Operaciones', 'Mes']).groupby(by=['Mes']).Operaciones.sum().plot(kind='bar',subplots='true')

Bots_group_by_mes = df.filter(items=['BOTS', 'Mes']).groupby(by=['Mes']).BOTS.mean().plot(kind='bar',subplots='true')

# Correlación entre variables BOTS y Operaciones
sns.jointplot(x= 'BOTS' , y = 'Operaciones', data = df, kind="reg");

#Obtenemos el fichero CSV para el análisis de  Bots activos y operaciones
Bib_E = pd.read_csv (r'C:\Users\Borja\Desktop\TR ASTI\EDA\Ficheros\SISTEMA_BMS_BIBERON_ENTRAR.csv', sep = ';')
Bib_E.head()
Bib_E.describe()

Bib_E.VEHICULO.nunique()
Bib_E.ESTACION.nunique()

#Obtenemos el fichero CSV para el análisis de tiempos de cargas
Cargas = pd.read_csv (r'C:\Users\Borja\Desktop\TR ASTI\EDA\Ficheros\Tiempos_cargas.csv', sep = ';')

#Observamos relación lineal entre 
sns.lmplot(x="DIF_SOC", y="MINUTOS", data=Cargas,
           order=2, ci=None, scatter_kws={"s": 80});

#Observamos histogramas de porcentajes de bateria al entrar al biberon
sns.distplot(Cargas['SOC_ENTRADA'])

sns.distplot(Cargas['SOC_ENTRADA'], kde=False, color='red', bins=100)

#Obtenemos el fichero CSV para el análisis de tiempos de cargas
Cargas = pd.read_csv (r'C:\Users\Borja\Desktop\TR ASTI\EDA\Ficheros\Tiempos_cargas_30MIN.csv', sep = ';')

#Observamos relación lineal entre 
sns.lmplot(x="DIF_SOC", y="MINUTOS", data=Cargas,
           order=2, ci=None, scatter_kws={"s": 80});



#Analizamos descarga de baterias
Descargas = pd.read_csv (r'C:\Users\Borja\Desktop\TR ASTI\EDA\Ficheros\Tiempos_Descarga.csv', sep = ';')

#Consideramos solo las descargas en el que el número de órdenes realizadas es superior a 5
Descargas2 = Descargas[(Descargas['N_Ordenes'] > 10) & (Descargas['DISTANCIA_TOTAL'] > 50)] 
Descargas2.head()

# Correlación entre variables DIF_SOC y Órdes
sns.jointplot(x="DIF_SOC", y="DISTANCIA_TOTAL", data=Descargas2, kind="reg");
# Correlación entre variables DIF_SOC y Órdes
sns.jointplot(x="DIF_SOC", y="consumo_TOTAL", data=Descargas2, kind="reg");
# Correlación entre variables DIF_SOC y Órdes
sns.jointplot(x="DIF_SOC", y="N_Ordenes", data=Descargas2, kind="reg");

           

