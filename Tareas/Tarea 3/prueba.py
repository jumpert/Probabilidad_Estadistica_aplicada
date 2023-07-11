"""En una encuesta electoral para la intencion de voto a un candidato A se obttuvo la siguiente informacion:
Promedio de votar X: 0.48
una estimacion para la deviacion estandar S fue de 0.02
con un valor de muestra N de 10.000 personas"""

# Calcular la intencion de voto. utilizando la distribucion normal
#se conoce que alfa es 0.05

import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

#se define la media y la desviacion estandar
X = 0.48
S = 0.02
N = 10000 
alfa = 0.000000001
M = st.norm.ppf(1-alfa/2)*S/np.sqrt(N)
print(M)
