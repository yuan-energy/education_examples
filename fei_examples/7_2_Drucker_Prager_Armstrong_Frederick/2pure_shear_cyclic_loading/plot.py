import numpy as np
import matplotlib.pyplot as plt  


strain = np.loadtxt("strain.feioutput")
stress = np.loadtxt("stress.feioutput")


plt.plot(strain, stress)
plt.xlabel('Strain / (unitless)')
plt.ylabel('Stress / (Pa)')
plt.title('Material Behavior: Stress-Strain')
plt.grid()
plt.box()
plt.savefig('result.pdf', transparent=True, bbox_inches='tight')
plt.show()
