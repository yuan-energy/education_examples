

current_dir=${PWD}
deepest_dir_array=( $(find . -type d -links 2 ) )
# deepest_dir_array=( $(find . -type d -links 3 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
	cd ${current_dir}/"${deepest_dir_array[$element]}"

	# cp ${current_dir}/plot.py .
	# python plot.py
	sed -i '/^\s*$/d' main.fei
	# sed -i 's/8NodeBrickLT/8NodeBrick/' *.fei
	# sed -i 's/20NodeBrickLT/20NodeBrick/' *.fei
	# sed -i 's/27NodeBrickLT/27NodeBrick/' *.fei
	# sed -i 's/linear_elastic_isotropic_3d_LT/linear_elastic_isotropic_3d/' main.fei
	# sed -i 's/linear_elastic_isotropic_3d/linear_elastic_isotropic_3d_LT/' main.fei

done