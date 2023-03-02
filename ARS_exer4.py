"""
Alexandr Ramos: Exercici 4, Tasca 1
"""

# Importem tots els moduls necessaris

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft

# Llegim la senyal
x, fm = sf.read('german-ambulance.wav')

# Agafem a partir del segon 6 fins el segon 8
dif_mostra = fm * 2                   # calculem quantes mostres son 2 segons
init_mostra = fm * 6                  # calculem la mostra inicial
fin_mostra = init_mostra + dif_mostra + 1  # Mostra post-final

x = x[init_mostra : fin_mostra : 1]   # reduim la senyal al que ens interesa

print('La freqüència de mostratge es de', fm, 'Hz')

print('La senyal te', len(x), 'mostres')

L = int(len(x))                       # Nombre de mostres del senyal digital
Tm=1/fm                               # Període de mostratge
t=Tm*np.arange(L)                     # Vector amb els valors de la variable temporal, de 0 a T

Ls=int(fm*0.025)                      # Mostres corresponents a 25ms

# Representació temporal
plt.figure(5)                         # Nova figura
plt.plot(t[0:Ls], x[0:Ls])            # Representació del senyal en funció del temps
plt.xlabel('t en segons')             # Etiqueta eix temporal
plt.title('25ms de la senyal')        # Títol del gràfic
plt.show()                            # Visualització de l'objecte gràfic.

N = 5000                              # Dimensio de la transformada discreta
X=fft(x[0 : Ls], N)                   # Càlcul de la transformada

# Ens quedem amb la meitat de la transformada per tindre el segment 0 < f < fm/2
X = X[0 : int(N/2)]

# Fem cambis d'escala
Xmax=float(max(abs(X)))               # Busquem valor maxim del modul de la transformada
Xabs=20*np.log10((abs(X)/Xmax))       # Generem modul en dB de la transformada

k=np.arange(int(N/2))                 # Vector amb els valors 0 ≤ k < N/2
freq=(k/N)*fm                         # Apliquem formula per pasar de k a Hz

# Mostrem la transformada
plt.figure(6)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(freq,Xabs)                   # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|dB')                # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(freq,np.unwrap(np.angle(X))) # Representació de la fase de la transformad, desenroscada
plt.xlabel('Hz')                      # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics 