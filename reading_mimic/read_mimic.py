import pandas as pd
import numpy as np

rows=pd.read_csv("NOTEEVENTS.csv",nrows=10);
text_list=rows['TEXT'].tolist()
for i in range(0,len(text_list)):
	fp=open("trunc/clinical-"+str(i)+".txt","w+")
	fp.write(text_list[i])
	fp.close()
