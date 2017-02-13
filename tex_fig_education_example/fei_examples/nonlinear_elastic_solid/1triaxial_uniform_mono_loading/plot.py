import numpy as np
import matplotlib.pyplot as plt  
import h5py 

def h52stressStrain(h5in_filename):
	h5in=h5py.File(h5in_filename,"r")
	outputs_all=h5in['/Model/Elements/Gauss_Outputs'][()]
	stress = outputs_all[16 , 1:-1]
	strain = outputs_all[4  , 1:-1]
	return [stress, strain]

[stress_load,   strain_load]   = h52stressStrain("DP_2shearing.h5.feioutput")
[stress_unload, strain_unload] = h52stressStrain("DP_3unloading.h5.feioutput")
[stress_reload, strain_reload] = h52stressStrain("DP_4reloading.h5.feioutput")

stress  = np.concatenate((stress_load,stress_unload,stress_reload))
strain  = np.concatenate((strain_load,strain_unload,strain_reload))

# plt.plot(strain, stress)
# plt.show()

plt.plot(strain, stress)
plt.xlabel('Strain / (unitless)')
plt.ylabel('Stress / (Pa)')
plt.title('Material Behavior: Stress-Strain')
plt.grid()
plt.box()
plt.savefig('result.pdf', transparent=True, bbox_inches='tight')
plt.show()