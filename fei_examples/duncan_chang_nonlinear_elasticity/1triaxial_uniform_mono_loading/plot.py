import numpy as np
import matplotlib.pyplot as plt  
import h5py 

def h52stressStrain(h5in_filename):
	h5in=h5py.File(h5in_filename,"r")
	outputs_all=h5in['/Model/Elements/Gauss_Outputs'][()]
	stress = outputs_all[13 , :]
	strain = outputs_all[1  , :]
	return [stress, strain]

[stress1,   strain1]   = h52stressStrain("DP_1Confine.h5.feioutput")
# [stress_load,   strain_load]   = h52stressStrain("DP_2shearing.h5.feioutput")
# [stress_unload, strain_unload] = h52stressStrain("DP_3unloading.h5.feioutput")
# [stress_reload, strain_reload] = h52stressStrain("DP_4reloading.h5.feioutput")


stress = [0]
stress  = - np.concatenate((stress,stress1))

strain = [0]
strain  = - np.concatenate((strain,strain1))

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