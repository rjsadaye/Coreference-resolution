# Coreference-resolution
Coreference resolution in clinical documents

#For generating phrases from .txt files:

python npchunking.py <Path the the folder containing the .txt files>

#For generating glove representation:

python glove.py <Path to the corpus pickle file> <Path to the file containing phrases> 

#For generating input and output:

python gen_in_out.py <Path to folder containing concept files>

python nn_input.py <Path to path.glove> # path to glove representation of phrases