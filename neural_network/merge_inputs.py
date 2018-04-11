import sys
path1 = sys.argv[1]
path2 = sys.argv[2]

# Merges i2b2 and mimic vectors into one file.
filenames = [path1, path2]
with open('input_to_nn.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)