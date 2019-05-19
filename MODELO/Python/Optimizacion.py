# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:15:26 2019

@author: Borja
"""
#Importamos libería Scipy
import scipy.optimize 
import numpy as np
import pandas as pd

from scipy.optimize import minimize

#t = tiempo
#a = batería que pierde en una hora un BOT
#b= mínima batería consentida
#d= demanda de BOT’s 
#i= número de BOT’s
#M = Constante definida para resolver la función= 3000
#X(it) = Estado de la batería
#Y(it) = (1: Si está trabajando, 0: si está cargando)
#Función objetivo: 
#Z = ∑t [ (∑i Y(it))-dt]
#Restricción
#X(it) – b >= M (Y(it) - 1)

 
#return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

def f_objetivo(x):
    #Z = ∑t [ (∑i Y(it))-dt]
    #tiempo en horas
    t = x0[0]
    #numero de bots disponibles
    i = x0[1]
    #número de bots trabjando
    
    
    
    return sum(x[1:]-x[:-1])

def rosen(x):
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

def restriccion(x):
    return 0
        

#definimos una situación inicial (robots trabjando) podemos tener 14
x0 = np.array([1, 0, 1, 0, 1])
print(x0[0])

x0 = np.array([1.0, 0.0, 0.0, 1.0, 1.1])

print(f_objetivo(x0))

solucion = minimize(f_objetivo, x0,  method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})

solucion2 = minimize(rosen, x0,  method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})

print(solucion.x)