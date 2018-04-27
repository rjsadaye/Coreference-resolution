# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 23:39:28 2018

@author: Rishi
"""

import hashlib,os,ntpath



def pair_compare(pairs_file,coref_file,folder_nm):
    print(coref_file)
    pairs_path="C:/Users/Rishi/Coreference-resolution/Pronoun Test/"+folder_nm+"/output/mention_pairs/"+pairs_file
    coref_path="C:/Users/Rishi/Coreference-resolution/Pronoun Test/"+folder_nm+"/pairs/"+coref_file
    output_path="C:/Users/Rishi/Coreference-resolution/Pronoun Test/"+folder_nm+"/output/compare/"
    f3=open(output_path+"compare_"+pairs_file,"w+")
    with open(pairs_path,"r") as f0:
        i=0
        word_1,place_1,word_2,place_2,concept_type_1,start_end_1,start_end_2,start_1,start_2,end_1,end_2="","","","","","","","","","",""
        for line_f0 in f0:
            line_f0=line_f0.rstrip("\n\r")
            items = line_f0.split("|")
            word_1=items[0]
            place_1=items[1]
            word_2=items[2]
            place_2=items[3]
            concept_type_1=items[4]
            start_end_1=place_1.split(" ")
            start_1=start_end_1[0]
            end_1=start_end_1[1]
            start_end_2=place_2.split(" ")
            start_2=start_end_2[0]
            end_2=start_end_2[1]
            flag=0
            with open(coref_path,"r") as f1:
                for line_f1 in f1:
                    if word_1.lower() in line_f1 and word_2.lower() in line_f1:
                        if end_1 in line_f1 and end_2 in line_f1:
                            
                            flag=1
                if flag==1:
                    f3.write(line_f0+"|1"+"\n")
                else:
                    f3.write(line_f0+"|0"+"\n")
                    
            f1.close()
    f0.close()
    f3.close()
    
def remove_pairs(file_name,line_threshold):
    output_path="C:/Users/Rishi/Coreference-resolution/Pronoun Test/"+folder_nm+"/output/compare/"
    to_be_deleted=[]
    with open(output_path+file_name,"r") as f4:
        i=0
        word_1,place_1,word_2,place_2,concept_type_1,start_end_1,start_end_2,start_1,start_2,end_1,end_2,match=[],[],[],[],[],[],[],[],[],[],[],[]
        lines=[]
        for num,line_f4 in enumerate(f4,1):
            line_f4=line_f4.rstrip("\n\r")
            items = line_f4.split("|")
            lines.append(line_f4)
            word_1.append(items[0])
            place_1.append(items[1])
            word_2.append(items[2])
            place_2.append(items[3])
            concept_type_1.append(items[4])
            match.append(items[5])
            start_end_1=items[1].split(" ")
            start_1.append(start_end_1[0])
            end_1.append(start_end_1[1])
            start_end_2=items[3].split(" ")
            start_2.append(start_end_2[0])
            end_2.append(start_end_2[1])
            flag=0
            line_words_1=start_end_1[1].split(":")
            line_end_1=line_words_1[0]
            line_words_2=start_end_2[1].split(":")
            line_end_2=line_words_2[0]
            distance_ends=int(line_end_1)-int(line_end_2)
            if distance_ends<0:
                distance_ends=distance_ends*-1
            if items[5]=='0' and distance_ends>line_threshold:
                to_be_deleted.append(num)
                
            
        for i in range(len(end_1)):
            if end_1[i]==end_2[i]:
                    #print(word_1[i]+" "+end_1[i]+" "+word_2[i]+" "+end_2[i])
                    to_be_deleted.append(i+1)
            for j in range(len(end_1)):
                if (end_1[i]==end_1[j] and end_2[i]==end_2[j]) and j>i:
                    #print(word_1[i]+" "+end_1[i]+" "+word_2[i]+" "+end_2[i])
                    #print(word_1[j]+" "+end_1[j]+" "+word_2[j]+" "+end_2[j])
                    if(len(lines[i])>=len(lines[j])):
                        to_be_deleted.append(j+1)
                        
                    else:
                        to_be_deleted.append(i+1)
                        
                elif (end_1[i]==end_2[j] and end_2[i]==end_1[j] and j>i):
                    if(len(lines[i])>=len(lines[j])):
                        to_be_deleted.append(j+1)
                    else:
                        to_be_deleted.append(i+1)
                        #print(i+1)
        to_be_deleted=set(to_be_deleted)
        to_be_deleted=list(to_be_deleted)
        to_be_deleted.sort()
        #print(to_be_deleted)            
        if end_1[len(end_1)-1]==end_2[len(end_1)-1]:
                    to_be_deleted.append(len(end_1))
        with open(output_path+"temp_"+file_name,"w+") as f5, open(output_path+file_name,"r") as f6 :
            i=0
            for num,line_1 in enumerate(f6,1):
                #print (str(num))
                #print(to_be_deleted)
                #print(i)
                if len(to_be_deleted)==0:
                    f5.write(line_1)
                elif num!=to_be_deleted[i]:
                    f5.write(line_1)
                elif i<len(to_be_deleted)-1:
                    #print(str(to_be_deleted[i])+"del")
                    i=i+1
        
        f6.close()
        f5.close()
    f4.close()    
               
    


from pathlib import Path
folder_nm='Partners'
indir = 'C:/Users/Rishi/Coreference-resolution/Pronoun Test/'+folder_nm+'/pairs/'
output_path="C:/Users/Rishi/Coreference-resolution/Pronoun Test/"+folder_nm+"/output/compare/"
#print (indir)
pathlist = Path(indir).glob('**/*.txt.pairs')
line_threshold=5
#print(pathlist)
for path in pathlist:
    # because path is object not string
    input_file_path = str(path)
    parts=ntpath.basename(input_file_path).split(".")
    coref_file=ntpath.basename(input_file_path)
    pairs_file="mention_pairs_"+parts[0]+".txt"
    pair_compare(pairs_file,coref_file,folder_nm)
    remove_pairs("compare_"+pairs_file,line_threshold)
    os.remove(output_path+"compare_"+pairs_file)
    os.rename(output_path+"temp_"+"compare_"+pairs_file,output_path+"compare_"+pairs_file)
'''pairs_file="mention_pairs_clinical-802.txt"
remove_pairs("compare_"+pairs_file,2)
os.remove(output_path+"compare_"+pairs_file)
os.rename(output_path+"temp_"+"compare_"+pairs_file,output_path+"compare_"+pairs_file)
pair_compare("mention_pairs_clinical-802.txt","clinical-802.txt.pairs","Beth")
'''    