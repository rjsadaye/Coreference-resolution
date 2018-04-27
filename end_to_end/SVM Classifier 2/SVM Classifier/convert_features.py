f1 = open("new_features.txt","w+")
file = open("all_features.txt","r")
for line in file:
    vect = []
    X = []
    if (line.strip() == ","):
        continue
    else:
        s=line.strip().split(",")
        
        
        for i in range(0,23):
            vect.append(float(s[i].strip()))
        X.append(','.join(str(v) for v in vect))
        X.append(','.join(str(v) for v in s[23:]))
        X = ','.join(str(v) for v in X)
        f1.write(X)
        f1.write("\n")