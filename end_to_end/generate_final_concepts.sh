#!/bin/bash



cur_dir=$(pwd)
# Input is the directory of the concepts file
# Output is the input to be fed to the neural network

python ${cur_dir%/}/gen_line_num1.py "${cur_dir%/}/input" "${cur_dir%/}/clamp_out" #Input.txt file path 

python ${cur_dir%/}/gen_line_num2.py "${cur_dir%/}/input/concepts" "${cur_dir%/}/input/final_concepts"
