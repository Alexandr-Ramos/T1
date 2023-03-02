"""
Alexandr Ramos: Exercici 1, Tasca 1
"""
# Importem tots els moduls necessaris

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft

# Gnenerem la senyal
T= 2.5                                # Durada de T segons
fm=8000                               # Freqüència de mostratge en Hz
fx1=440                               # Freqüència de la sinusoide 1
fx2=4000                              # Freqüència de la sinusoide 2
fx3=220                               # Freqüència de la sinusoide 3
A=0.5                                 # Amplitud de les sinusoide
pi=np.pi                              # Valor del número pi
L = int(fm * T)                       # Nombre de mostres del senyal digital
Tm=1/fm                               # Període de mostratge
t=Tm*np.arange(L)                     # Vector amb els valors de la variable temporal, de 0 a T
x = A * ( np.cos(2*pi*fx1*t) + np.sin(2*pi*fx2*t) + np.cos(2*pi*fx3*t) ) # Creo la senyal i la gruardo    
sf.write('so_sinusoides.wav', x, fm)

# Representem la senyal
Tx=1/fx3                              # Període del senyal de mes baixa frequencia
Ls=int(fm*5*Tx)                       # Nombre de mostres corresponents a 5 períodes de la sinusoide de major amplitud 'fx3'

plt.figure(0)                         # Nova figura
plt.plot(t[0:Ls], x[0:Ls])            # Representació del senyal en funció del temps
plt.xlabel('t en segons')             # Etiqueta eix temporal
plt.title('5 periodes de 220Hz')      # Títol del gràfic
plt.show()                            # Visualització de l'objecte gràfic.

# Escoltem la senyal
sd.play(x, fm)

# Generem la transformada
N=5000                                # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)                   # Càlcul de la transformada de 5 períodes de la sinusoide

# Mostrem la transformada
k=np.arange(N)                        # Vector amb els valors 0 ≤ k < N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics