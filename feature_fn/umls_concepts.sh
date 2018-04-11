#!/bin/sh

python lookup_concepts.py -k cad3998b-1467-4b98-96a9-05c511abbb76 -v 2017AB -s1 $1 -s2 $2
python word_lookup_concepts.py -k cad3998b-1467-4b98-96a9-05c511abbb76 -v 2017AB -s1 $1 -s2 $2
python leftTruncation_lookup_concepts.py -k cad3998b-1467-4b98-96a9-05c511abbb76 -v 2017AB -s1 $1 -s2 $2
python rightTruncation_lookup_concepts.py -k cad3998b-1467-4b98-96a9-05c511abbb76 -v 2017AB -s1 $1 -s2 $2
python approximate_lookup_concepts.py -k cad3998b-1467-4b98-96a9-05c511abbb76 -v 2017AB -s1 $1 -s2 $2
python normalizedString_lookup_concepts.py -k cad3998b-1467-4b98-96a9-05c511abbb76 -v 2017AB -s1 $1 -s2 $2
python calc_umls_features.py