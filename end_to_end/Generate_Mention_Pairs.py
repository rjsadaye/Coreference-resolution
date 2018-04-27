# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 21:48:16 2018

@author: Rishi


"""

import requests,json,inflect,sys
p=inflect.engine()

import gender_guesser.detector as gender
d = gender.Detector()


def Generate(input_file_name,folder_nm):
    print(input_file_name)
    pronoun_path="/home/raj/end_to_end/pronoun.txt"
    concepts_path="/home/raj/"+folder_nm+"/output/concepts.txt"
    mention_pairs_path="/home/raj/"+folder_nm+"/output/mention_pairs/mention_pairs_"+input_file_name
#ingesting the metadata knowledge for pronouns
    line_threshold=15
    with open(pronoun_path,"r") as f0:
        i=0
        pronoun_meta,gender_meta,is_plural_meta,is_personal_meta=[],[],[],[]
        for line_f0 in f0:
            items = line_f0.rstrip("\n\r").split("|")
            pronoun_meta.append(items[0])
            gender_meta.append(items[1])
            is_plural_meta.append(items[2])
            is_personal_meta.append(items[3])
            i+=1
    f0.close()
    #print (pronoun_meta)
    
    with open(concepts_path) as f2:
        pronoun_data,gender,is_plural,is_personal,start_pronoun,end_pronoun,end_line_list=[],[],[],[],[],[],[]
        for line in f2:
            
            items = line.rstrip("\n\r").split("|")
            #print(items)
            name, place, concept_type_pronouns = items[0], items[1], items[2]
            start_end= place.split(" ")
            start,end=start_end[0],start_end[1]
            end_array=end.split(":")
            end_line=end_array[0]
            end_word=end_array[1]
            if concept_type_pronouns=="0":
                x=0
                i=0
                #print(name)
                #labeling the pronouns fromt the input with the corresponding tags
                for x in range(len(pronoun_meta)):
                    if pronoun_meta[x].lower()==name.lower():
                        #print (pronoun_meta[x])
                        if is_personal_meta[x]=='1':
                            if gender_meta[x]=='Male':
                                if is_plural_meta[x]=='0':
                                    #print("Male Perosnal sing "+name)
                                    pronoun_data.append(name)
                                    gender.append('Male')
                                    is_plural.append('0')
                                    is_personal.append('1')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                                elif is_plural_meta[x]=='1':
                                    #print("Male Perosnal plur "+name)
                                    pronoun_data.append(name)
                                    gender.append('Male')
                                    is_plural.append('1')
                                    is_personal.append('1')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                                else:
                                    #print("Male Perosnal sing or plu "+name)
                                    pronoun_data.append(name)
                                    gender.append('Male')
                                    is_plural.append('')
                                    is_personal.append('1')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                            elif gender_meta[x]=='Female':
                                if is_plural_meta[x]=='0':
                                    #print("FeMale Perosnal sing "+name)
                                    pronoun_data.append(name)
                                    gender.append('Female')
                                    is_plural.append('0')
                                    is_personal.append('1')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                                elif is_plural_meta[x]=='1':
                                    #print("FeMale Perosnal plu "+name)
                                    pronoun_data.append(name)
                                    gender.append('Female')
                                    is_plural.append('1')
                                    is_personal.append('1')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                                else:
                                    #print("FeMale Perosnal sing or plu "+name)
                                    pronoun_data.append(name)
                                    gender.append('Female')
                                    is_plural.append('')
                                    is_personal.append('1')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                            else:
                                if is_plural_meta=='0':
                                    #print("FeMale or male Perosnal sing "+name)
                                    pronoun_data.append(name)
                                    gender.append('')
                                    is_plural.append('0')
                                    is_personal.append('1')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                                elif is_plural_meta[x]=='1':
                                    #print("FeMale or male Perosnal plu "+name)
                                    pronoun_data.append(name)
                                    gender.append('')
                                    is_plural.append('1')
                                    is_personal.append('1')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                                else:
                                    #print("FeMale or male Perosnal sing or plu "+name)
                                    pronoun_data.append(name)
                                    gender.append('')
                                    is_plural.append('')
                                    is_personal.append('1')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                        elif is_personal_meta[x]=='0':
                            if is_plural_meta[x]=='0':
                                    #print("NonPerosnal sing "+name)
                                    pronoun_data.append(name)
                                    gender.append('')
                                    is_plural.append('0')
                                    is_personal.append('0')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                            elif is_plural_meta[x]=='1':
                                    #print("NonPerosnal plu "+name)
                                    pronoun_data.append(name)
                                    gender.append('')
                                    is_plural.append('1')
                                    is_personal.append('0')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                            else:
                                    #print("NonPerosnal sing or plu "+name)
                                    pronoun_data.append(name)
                                    gender.append('')
                                    is_plural.append('')
                                    is_personal.append('0')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                        else:
                            if is_plural_meta[x]=='0':
                                    #print("NonPerosnal or personal sing "+name)
                                    pronoun_data.append(name)
                                    gender.append('')
                                    is_plural.append('0')
                                    is_personal.append('')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                            elif is_plural_meta[x]=='1':
                                    #print("NonPerosnal or personal plu "+name)
                                    pronoun_data.append(name)
                                    gender.append('')
                                    is_plural.append('1')
                                    is_personal.append('')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                            else:
                                    #print("NonPerosnal or personal sing or plu "+name)
                                    pronoun_data.append(name)
                                    gender.append('')
                                    is_plural.append('')
                                    is_personal.append('')
                                    start_pronoun.append(start)
                                    end_pronoun.append(end)
                                    end_line_list.append(end_line)
                        
                
    f2.close()
    
    
    f3=open(mention_pairs_path,"w+")
    #print (pronoun_data)
    #All the mentions with person type , Label them with corresponding gender, plurality using api.genderize.io and inflect library
    with open(concepts_path) as f10:
        person,gender_person,start_list,end_list,is_plural_person,end_line_list_1=[],[],[],[],[],[]
        for line in f10:
            items = line.rstrip("\n\r").split("|")
            name, place,concept_type_person = items[0], items[1], items[2]
            start_end= place.split(" ")
            start,end=start_end[0],start_end[1]
            end_array=end.split(":")
            end_line=end_array[0]
            end_word=end_array[1]
            if concept_type_person=="1":
                #print (name)
                flag=0
                for x in range(len(pronoun_meta)):
                    if pronoun_meta[x].lower()==name.lower():
                        flag=1
                        #print (pronoun_meta[x])
                        if is_personal_meta[x]=='1':
                            if gender_meta[x]=='Male':
                                if is_plural_meta[x]=='0':
                                    #print("Male Perosnal sing "+name)
                                    person.append(name)
                                    gender_person.append('Male')
                                    start_list.append(start)
                                    end_list.append(end)
                                    is_plural_person.append('0')
                                    end_line_list_1.append(end_line)
                                elif is_plural_meta[x]=='1':
                                    #print("Male Perosnal plur "+name)
                                    person.append(name)
                                    gender_person.append('Male')
                                    is_plural_person.append('1')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                                else:
                                    #print("Male Perosnal sing or plu "+name)
                                    person.append(name)
                                    gender_person.append('Male')
                                    is_plural_person.append('')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                            elif gender_meta[x]=='Female':
                                if is_plural_meta[x]=='0':
                                    #print("FeMale Perosnal sing "+name)
                                    person.append(name)
                                    gender_person.append('Female')
                                    is_plural_person.append('0')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                                elif is_plural_meta[x]=='1':
                                    #print("FeMale Perosnal plu "+name)
                                    person.append(name)
                                    gender_person.append('Female')
                                    is_plural_person.append('1')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                                else:
                                    #print("FeMale Perosnal sing or plu "+name)
                                    person.append(name)
                                    gender_person.append('Female')
                                    is_plural_person.append('')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                            else:
                                if is_plural_meta=='0':
                                    #print("FeMale or male Perosnal sing "+name)
                                    person.append(name)
                                    gender_person.append('')
                                    is_plural_person.append('0')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                                elif is_plural_meta[x]=='1':
                                    #print("FeMale or male Perosnal plu "+name)
                                    person.append(name)
                                    gender_person.append('')
                                    is_plural_person.append('1')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                                else:
                                    #print("FeMale or male Perosnal sing or plu "+name)
                                    person.append(name)
                                    gender_person.append('')
                                    is_plural_person.append('')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                        elif is_personal_meta[x]=='0':
                            if is_plural_meta[x]=='0':
                                    #print("NonPerosnal sing "+name)
                                    person.append(name)
                                    gender_person.append('')
                                    is_plural_person.append('0')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                            elif is_plural_meta[x]=='1':
                                    #print("NonPerosnal plu "+name)
                                    person.append(name)
                                    gender_person.append('')
                                    is_plural_person.append('1')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                            else:
                                    #print("NonPerosnal sing or plu "+name)
                                    person.append(name)
                                    gender_person.append('')
                                    is_plural_person.append('')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                        else:
                            if is_plural_meta[x]=='0':
                                    #print("NonPerosnal or personal sing "+name)
                                    person.append(name)
                                    gender_person.append('')
                                    is_plural_person.append('0')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                            elif is_plural_meta[x]=='1':
                                    #print("NonPerosnal or personal plu "+name)
                                    person.append(name)
                                    gender_person.append('')
                                    is_plural_person.append('1')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                            else:
                                    #print("NonPerosnal or personal sing or plu "+name)
                                    person.append(name)
                                    gender_person.append('')
                                    is_plural_person.append('')
                                    start_list.append(start)
                                    end_list.append(end)
                                    end_line_list_1.append(end_line)
                if flag==0:
                    #url = "https://api.genderize.io/?name="+name
                    #print(url)
                    #response = requests.get(url)
                    #data=json.loads(response.text)
                    gen=d.get_gender(name)
                    if gen==str("unknown") or gen==str("andy"):
                        gen=""
                    person.append(name)
                    gender_person.append(gen)
                    start_list.append(start)
                    end_list.append(end)
                    end_line_list_1.append(end_line)
                    if str(p.singular_noun(name))=='False' and p.plural_noun(name)!=name:
                        is_plural_person.append('0')
                    elif p.singular_noun(name)!=name and p.plural_noun(name)!=name:
                        is_plural_person.append('1')
                    else:
                        is_plural_person.append('-1')
    f10.close()
        #print(person)
        #print(gender_person)
        #print(is_plural_person)

        
        #p.singular_noun('they')

        
        
        
        #mapping persons with persons based on the gender and plurality
    x1,y1=0,0
    for x1 in range(len(person)):
        for y1 in range(len(person)):
            if y1>x1:
                dist=int(end_line_list_1[y1])-int(end_line_list_1[x1])
                if dist<0:
                    dist=dist*-1
                    
                #print(person[x1]+" "+gender_person[x1]+" "+is_plural_person[x1]+" "+person[y1]+" "+gender_person[y1]+" "+is_plural_person[y1])
                if dist<=line_threshold and ((gender_person[x1]==gender_person[y1]) or (gender_person[x1]=="" or gender_person[y1]=="")):
                    if (is_plural_person[x1]==is_plural_person[y1]) or (is_plural_person[x1]=='-1' or is_plural_person[y1]=='-1'):
                        #print (str(dist)+" "+end_line_list_1[y1]+" "+end_line_list_1[x1])        
                        f3.write(person[x1]+"|"+start_list[x1]+" "+end_list[x1]+"|"+person[y1]+"|"+start_list[y1]+" "+end_list[y1]+"|"+"1"+"\n")
    
    #mapping persons with pronoun based on the gender and plurality , considering only personal pronouns here
    for x1 in range(len(pronoun_data)):
        if is_personal[x1]=='1':
            for y1 in range(len(person)):
                if y1>x1:
                    dist=int(end_line_list_1[y1])-int(end_line_list[x1])
                    if dist<0:
                        dist=dist*-1
                    if dist<=line_threshold and ((gender[x1]==gender_person[y1]) or gender[x1]=="" or gender_person[y1]==""):
                        if (is_plural[x1]==is_plural_person[y1]) or (is_plural[x1]=='' or is_plural_person[y1]=='-1'):
                            f3.write(pronoun_data[x1]+"|"+start_pronoun[x1]+" "+end_pronoun[x1]+"|"+person[y1]+"|"+start_list[y1]+" "+end_list[y1]+"|"+"1"+"\n")
                            #print (dist)
    #mapping pronoun with pronoun based on the gender, plurality and the is_personal flag                       
    for x1 in range(len(pronoun_data)):
        for y1 in range(len(pronoun_data)):
            if y1>x1:
                dist=int(end_line_list[y1])-int(end_line_list[x1])
                if dist<0:
                    dist=dist*-1
                if dist<=line_threshold and ((gender[x1]==gender[y1]) or (gender[x1]=="" or gender[y1]=="")) :
                    if (is_plural[x1]==is_plural[y1]) or (is_plural[x1]=="" or is_plural[y1]==""):
                        if(is_personal[x1]==is_personal[y1]) or (is_personal[x1]=="" or is_personal[y1]==""):
                            f3.write(pronoun_data[x1]+"|"+start_pronoun[x1]+" "+end_pronoun[x1]+"|"+pronoun_data[y1]+"|"+start_pronoun[y1]+" "+end_pronoun[y1]+"|"+"0"+"\n")
                            #print (dist)
    
    #mapping all non personal pronons with others concepts except pronoun, personal
    with open(concepts_path) as f2:
        for line in f2:
            items = line.rstrip("\n\r").split("|")
            #print (items)
            name, place, concept_type_1 = items[0], items[1], items[2]
            start_end= place.split(" ")
            start,end=start_end[0],start_end[1]
            end_array=end.split(":")
            end_line=end_array[0]
            end_word=end_array[1]
            if concept_type_1!="0" and concept_type_1!="1" and concept_type_1!="6" :
                #print(name)
                for x1 in range(len(pronoun_data)):
                    dist=int(end_line)-int(end_line_list[x1])
                    if dist<0:
                        dist=dist*-1
                    if is_personal[x1]!='1' and dist<=line_threshold:
                        f3.write(pronoun_data[x1]+"|"+start_list[x1]+" "+end_list[x1]+"|"+name+"|"+start+" "+end+"|"+concept_type_1+"\n")
                        #print (dist)    
    f2.close()
    
    
    #Pairs of all mentions within same concept
    with open(concepts_path, 'r') as f6:
        for num, line in enumerate(f6,1):
            items_nnp = line.rstrip("\n\r").split("|")
            phrase, place,concept_type = items_nnp[0], items_nnp[1],items_nnp[2]
            start_end= place.split(" ")
            start,end=start_end[0],start_end[1]
            end_array=end.split(":")
            end_line=end_array[0]
            end_word=end_array[1]
            with open(concepts_path,'r') as f7:
                for num_1,line_1 in enumerate(f7,1):
                    items_ppn = line_1.rstrip("\n\r").split("|")
                    phrase_1, place_1,concept_type_2 = items_ppn[0], items_ppn[1],items_ppn[2]
                    start_end_1= place_1.split(" ")
                    start_1,end_1=start_end_1[0],start_end_1[1]
                    end_array_1=end_1.split(":")
                    end_line_1=end_array_1[0]
                    end_word_1=end_array_1[1]
                    dist=int(end_line_1)-int(end_line)
                    if dist<0:
                        dist=dist*-1
                    if dist<=line_threshold and concept_type==concept_type_2 and num_1>num and (concept_type_2!="0" and concept_type_2!="6" and concept_type_2!="1"):
                        f3.write(phrase+"|"+start+" "+end+"|"+phrase_1+"|"+start_1+" "+end_1+"|"+concept_type_2+"\n")
            
    f6.close()
    
    
    f3.close()

def count_concepts(input_file_name,folder_nm):
    concepts_path="/home/raj/"+folder_nm+"/output/concepts.txt"
    counts_path="/home/raj/"+folder_nm+"/output/metadata/concept_counts_"+input_file_name
    with open(concepts_path) as f11:
        person,gender_person,start_list,end_list,is_plural_person,end_line_list_1=[],[],[],[],[],[]
        pronoun_count,person_count,treatment_count,problem_count,test_count,temporal_count=0,0,0,0,0,0
        for line in f11:
            items = line.rstrip("\n\r").split("|")
            name, place,concept_type_person = items[0], items[1], items[2]
            if concept_type_person=="0":
                pronoun_count=pronoun_count+1
            elif concept_type_person=="1":
                person_count=person_count+1
            elif concept_type_person=="2":
                treatment_count=treatment_count+1
            elif concept_type_person=="3":
                problem_count=problem_count+1
            elif concept_type_person=="4":
                test_count=test_count+1
            elif concept_type_person=="5":
                temporal_count=temporal_count+1
    f11.close()
    f3=open(counts_path,"w+")
    f3.write("pronouns :"+str(pronoun_count)+"\n")
    f3.write("person :"+str(person_count)+"\n")
    f3.write("treatment :"+str(treatment_count)+"\n")
    f3.write("problem :"+str(problem_count)+"\n")
    f3.write("tests :"+str(test_count)+"\n")
    f3.write("temporal :"+str(temporal_count))
    f3.close()
    return[pronoun_count,person_count,treatment_count,problem_count,test_count,temporal_count]

                
    
import hashlib,os,ntpath

from pathlib import Path
folder_nm='end_to_end'
indir = '/home/raj/'+folder_nm+'/input/final_concepts/'
counts="/home/raj/"+folder_nm+"/output/metadata/concept_counts_all.txt"
#print (indir)
pathlist = Path(indir).glob('**/*.txt')
#print(pathlist)
no_pronouns,no_persons,no_treatments,no_problems,no_tests,no_temporals=0,0,0,0,0,0
for path in pathlist:
    # because path is object not string
    input_file_path = str(path)
    #print(input_file_path)
    
    output_file_path = "/home/raj/"+folder_nm+"/output/concepts.txt"
    completed_lines_hash = set()
    output_file = open(output_file_path, "w+")
    if ntpath.basename(input_file_path).startswith('clinical'):
        
        for line in open(input_file_path, "r"):
            #print(line)
            line=line.replace('|pronoun','|0')
            line=line.replace('|person','|1')
            line=line.replace('|test','|2')
            line=line.replace('|treatment','|3')
            line=line.replace('|problem','|4')
            line=line.replace('|temporal','|5')
            #print("e"+line)
            hashValue = hashlib.md5(line.rstrip().lower().encode('utf-8')).hexdigest()
            if hashValue not in completed_lines_hash:
                  output_file.write(line)
                  completed_lines_hash.add(hashValue)
    output_file.close()
    list_count=count_concepts(ntpath.basename(input_file_path),folder_nm)
    pronoun_count,person_count,treatment_count,problem_count,test_count,temporal_count=list_count[0],list_count[1],list_count[2],list_count[3],list_count[4],list_count[5]
    no_pronouns=no_pronouns+pronoun_count
    no_persons=no_persons+person_count
    no_treatments=no_treatments+treatment_count
    no_problmes=no_problems+problem_count
    no_tests=no_tests+test_count
    no_temporals=no_temporals+temporal_count
    Generate(ntpath.basename(input_file_path),folder_nm)
ff3=open(counts,"w+")
ff3.write("pronouns :"+str(no_pronouns)+"\n")
ff3.write("person :"+str(no_persons)+"\n")
ff3.write("treatment :"+str(no_treatments)+"\n")
ff3.write("problem :"+str(no_problmes)+"\n")
ff3.write("tests :"+str(no_tests)+"\n")
ff3.write("temporal :"+str(no_temporals))
ff3.close()
#Generate('clinical-802.txt','Beth')    
    
    
