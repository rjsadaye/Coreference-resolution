#Coreference resolution in clinical documents

##########################################################

TO RUN END TO END PIPELINE:

go the /end_to_end folder

Place the input file in the /input folder

Run the following command on terminal:

./run.sh <name of the file you want to run from input folder>

The output will be generated in the /output folder

You can check output for mention pairs, coreferent pairs, chains

TO RUN CEAF BASED EVALUATION ON THE OUTPUT:

go the /end_to_end folder

run the following command on terminal:

python evaluation.py <path to the chains file generated by system> <path to the gold mentions chain file>

##############################################################

##############################################################
PREREQUISITES:

CLAMP command line tool
Stanford CoreNLP toolkit
Stanford ner toolkit

python packages:
genderize
inflect
##############################################################







