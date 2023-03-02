"""
Alexandr Ramos: Exercici 3, Tasca 1
"""

# Importem tots els moduls necessaris

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft

# Llegim la senyal
x, fm = sf.read('so_sinusoides.wav')

L = int(len(x))                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T

# No hi ha necessetitat de rpresentar ni escoltar la Senyal, es el mateix proces que l'apartat anterior
Tx=1/220                             # Període del senyal de mes baixa frequencia
Ls=int(fm*5*Tx)                      # Nombre de mostres corresponents a 5 períodes de la sinusoide de major amplitud '220Hz'

# Generem la transformada
N=5000                               # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)                  # Càlcul de la transformada de 5 períodes de la sinusoide

# Fem cambis d'escala
Xmax=float(max(abs(X)))              # Busquem valor maxim del modul de la transformada
Xabs=20*np.log10((abs(X)/Xmax))      # Generem modul en dB de la transformada

k=np.arange(N)                       # Vector amb els valors 0 ≤ k < N
freq=(k/N)*fm

# Mostrem la transformada
plt.figure(4)                        # Nova figura
plt.subplot(211)                     # Espai per representar el mòdul
plt.plot(freq,Xabs)                  # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|dB')               # Etiqueta de mòdul
plt.subplot(212)                     # Espai per representar la fase
plt.plot(freq,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Hz')                     # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')            # Etiqueta de la fase en Latex
plt.show()                           # Per mostrar els grafics