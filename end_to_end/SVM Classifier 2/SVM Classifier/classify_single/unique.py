f3 = open("output.txt","r+")
uniqlines = f3.readlines()
f4 = open("output2.txt","w+")
f4.writelines(set(uniqlines))
