import numpy as np
import matplotlib.pyplot as plt  
import h5py 
h5in_filename = "elastic_uniaxial.h5.feioutput"
h5in=h5py.File(h5in_filename,"r")
outputs_all=h5in['/Model/Elements/Gauss_Outputs'][()]
stress = outputs_all[14 , :-1]
strain = outputs_all[2  , :-1]
plt.plot(strain, stress)
plt.xlabel('strain')
plt.ylabel('stress/(Pa)')
plt.title('Material Behavior: Stress-Strain')
plt.grid()
plt.box()
plt.savefig('result.pdf', transparent=True, bbox_inches='tight')
plt.show()