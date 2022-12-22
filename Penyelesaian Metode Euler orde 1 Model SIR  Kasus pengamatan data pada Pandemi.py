import numpy as np              
import matplotlib.pyplot as plt

# Data yang diketahui pada pengamatan pandemi
t0 = 0  #sumbu awal X
tn = 200 # Sumbu akhir x
ndata = 1000 # Data di sumbu y
t = np.linspace(t0,tn,ndata)
h = t[2]-t[1]

# rumus pengamatan yang dilakukan

N = 1000 # Penduduk yang diamati
I0 = 1 # Yang terinfeksi
R0 = 0 # yang sembuh dari penyakit
S0 = N - I0 - R0 3 #  diduga kuat terjangkit infeksi

I = np.zeros(ndata)
S = np.zeros(ndata)
R = np.zeros(ndata)

I[0] = I0
S[0] = S0
R[0] = R0

beta = 0.2
gamma = 0.1

for v in range(0, ndata-1):
    S[v+1] = S[v] - h*beta/N*S[v]*I[v]
    I[v+1] = I[v] + h*beta/N*S[v]*I[v] - h*gamma*I[v]
    R[v+1] = R[v] + h*gamma*I[v]

plt.plot(t,S,label='S') # Pemisalan data yang diduga kuat terjangkit infeksi
plt.plot(t,I,label='I') # Pemisalan data yang Yang terinfeksi
plt.plot(t,R,label='R') # Pemisalan data yang yang sembuh dari penyakit

plt.legend()
plt.show()
