
folder_nm='end_to_end'
coref_path="/home/raj/"+folder_nm+"/output/coreferent_pairs/output2.txt"
chains_path="/home/raj/"+folder_nm+"/output/chains/chains.txt"
f1=open(chains_path,"w+")
def linear_search(obj, item, start=0):
    for l in range(start, len(obj)):
        if obj[l] == item:
            return l
    return -1

with open(coref_path, 'r') as f6:
        i=0
        key=[]
        value=[]
        words,start,start_end,concept=[],[],[],[]
        for num,line in enumerate(f6,1):
            #from the coreferent pairs file separate the words and their positions in file
            items_nnp = line.rstrip("\n\r").split("|")
            word_1,start_1,end_1,word_2,start_2,end_2,concept_type = items_nnp[0], items_nnp[1],items_nnp[2],items_nnp[3],items_nnp[4],items_nnp[5],items_nnp[6]
            
            #get all words in a list and also their positions in another list at corresponding positions
            if linear_search(start,start_1)==-1:
                words.append(word_1)
                start.append(start_1)
                start_end.append(start_1+" "+end_1)
                concept.append(concept_type)
            if linear_search(start,start_2)==-1:
                words.append(word_2)
                start.append(start_2)
                start_end.append(start_2+" "+end_2)
                concept.append(concept_type)
            #1st row will be marked as 1st pair and so on
            key.append(num)
            value.append(start_1)
            key.append(num)
            value.append(start_2)




def formchain(i,Chains):
    #if the element is not present in the chain then add it
    if linear_search(Chains,value[i])==-1:
        Chains.append(value[i])
    #store the key and value temporarily
    temp_k=key[i]
    temp_v=value[i]
    #if there is only one element in the list delete it
    if i==(len(key)-1):
        key[len(key)-1]=""
        value[len(value)-1]=""
    else:
    #delete the element by shifting the following elements by 1 position to left    
        for j in range (i,len(key)-1):
            key[j]=key[j+1]
            value[j]=value[j+1]
        #mark the last position as ""
        key[len(key)-1]=""
        value[len(value)-1]=""
    # call the method again for the another mention of the pair which shares same key
    if linear_search(key,temp_k)!=-1:
        formchain(linear_search(key,temp_k),Chains)
    # call the method for another pair which has same mention which has already been included
    if linear_search(value,temp_v)!=-1:
        formchain(linear_search(value,temp_v),Chains)
   
#As positions are being shifted left, 0th element will never be zero unless the entire array is empty
while(key[0]!=""):
    Chains=[]
    #start with first element of the list
    formchain(0,Chains) 
    for i in range(len(Chains)-1):
       j=linear_search(start,Chains[i])
       f1.write(words[j]+"|"+start_end[j]+"|")
    j=linear_search(start,Chains[len(Chains)-1])
    f1.write(words[j]+"|"+start_end[j]+"|"+concept[j]+"\n")

f1.close()





