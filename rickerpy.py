import numpy as np
import scipy.signal as ss
import matplotlib.pyplot as plt
import scipy.signal as ss

"""
script para generar ondiculas de ricker siguiendo: 
ricker(t) = [ 1 - 2*(pi*f0*t)^2 ] * exp [ - (pi*f0*t)^2 ]
con opcion de rotar la fase
f0: frecuencia central
leng: longitud en tiempo
dt: intervalo de muestreo en tiempo en ms
fase: fase de la ondicula

obs: si la fase no es llamada por defualt es cero 
"""

def rickerpy(leng,dt,f0,fase=0):

    M = round(leng/(2*dt)) 
    
    N = int(2*M+1)
    
    rick = np.zeros((N,1))
    for n in range(0,N):
        t = dt*(n-M-1)/1000 # para que este en ms
        aux = np.pi*f0*t
        rick[n]= (1-2*aux**2)*np.exp(-aux**2)

    angles = np.radians(fase)
    w_rot = np.zeros((len(rick),1))
    w_rot = np.cos(angles)*rick[:,0]-np.sin(angles)*np.imag(ss.hilbert(rick[:,0]))
    
    return w_rot


