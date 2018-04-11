#!/bin/bash



cur_dir=$(pwd)
# Input is the directory of the concepts file
# Output is the input to be fed to the neural network

python ${cur_dir%/}/gen_in_out.py "$1" "$2"

python ${cur_dir%/}/out_vec_nn.py "${cur_dir%/}/output.txt"

python ${cur_dir%/}/class_dict_gen.py "${cur_dir%/}/input.txt" "${cur_dir%/}/output_vector.txt" 

parentdir="$(dirname "$(pwd)")"
#echo $parentdir
python ${cur_dir%/}/nn_input.py "${parentdir%/}/glove_module/path.glove" "${cur_dir%/}/phrase_class_dict.txt"