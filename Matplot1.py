import matplotlib.pyplot as plt
import pandas as pd

wktime1 = pd.read_csv('wktime.T001.his',delimiter=' ',header=None)
plt.plot(wktime1[0], wktime1[1], color = 'b', label = 'Time 001')

wktime4 = pd.read_csv('wktime.T004.his',delimiter=' ',header=None)
plt.plot(wktime4[0], wktime4[1], color = 'r', label = 'Time 004')

plt.xlabel('Wealth')
plt.ylabel('Probability')
plt.title('Distribution')
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.xlim((0.000001),(100))
plt.ylim((0.000001),(100000))
plt.tight_layout()
plt.show()
