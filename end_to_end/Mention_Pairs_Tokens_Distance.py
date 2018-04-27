# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 18:52:44 2018

@author: Rishi
"""
f3=open("Mention_Pairs_Tokens_Distance.txt","w+")
with open("test.txt","r+") as f2:
    words=[0]
    for line in f2:
        words.append(len(line.rstrip("\n\r").replace(",","").replace(".","").replace("'","").replace('"',"").replace(":","").replace("!","").split(" ")))
f2.close()
with open("Mention_Pairs.txt","r+") as f1:
    for line in f1:
        items = line.rstrip("\n\r").split("|")
        mention_1, start_1, end_1,mention_2,start_2,end_2,concept_type = items[0], items[1], items[2],items[3],items[4],items[5],items[6]
        e1=end_1.split(":")
        line_1,word_1=e1[0],e1[1]
        s2=start_2.split(":")
        line_2,word_2=s2[0],s2[1]
        if int(line_1)==int(line_2):
            if int(word_1)>int(word_2):
                tokens=int(word_1)-int(word_2)-1
            else:
                tokens= int(word_2)-int(word_1)-1
        elif int(line_1)>int(line_2):
                low,high=int(line_2),int(line_1)
                #print (low)
                #print (len(words))
                tokens=words[low]-int(word_2)
                low=low+1
                while low<high:
                    tokens=tokens+words[low]
                    low+=1
                tokens=tokens+int(word_1)-1
        else:
            low,high=int(line_1),int(line_2)
            
            tokens=words[low]-int(word_1)
        
            low=low+1
            while low<high:
                tokens=tokens+words[low]
                
                low+=1
            tokens=tokens+int(word_2)-1
        f3.write(mention_1+"|"+start_1+"|"+end_1+"|"+mention_2+"|"+start_2+"|"+end_2+"|"+concept_type+"|"+str(tokens)+"\n")
f1.close()
f2.close()
f3.close()        
        