run:
	script -c "essi -f main.fei " log
look_confine:
	paraview_release DP_Confine.h5.feioutput
look_shear:
	paraview_release DP_shearing.h5.feioutput

plot:
	python plot.py
plot_unloading:
	python plot_unloading.py