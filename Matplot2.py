import matplotlib.pyplot as plt
import pandas as pd

hbUK = pd.read_csv('headbrainUK.csv',delimiter=',',header=None)
plt.plot(hbUK[0], hbUK[1], color = 'b')

hbUS = pd.read_csv('headbrainUS.csv',delimiter=',',header=None)
plt.plot(hbUS[0], hbUS[1], color = 'r')

plt.xlabel('Head Size (cm^3)')
plt.ylabel('Brain Weight (grams)')
plt.title('Head Size & Brain Weight')
plt.xlim((2500),(5000))
plt.ylim((800),(1700))
plt.tight_layout()
plt.show()
