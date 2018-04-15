#################################################################################
# usage of the script
# usage: python search-terms.py -k APIKEY -v VERSION -s1 STRING1 -s2 STRING2
# see https://documentation.uts.nlm.nih.gov/rest/search/index.html for full docs
# on the /search endpoint
#################################################################################


#SEARCH TYPE = exact
from __future__ import print_function
from Authentication import *
import requests
import json
import argparse
import pickle

parser = argparse.ArgumentParser(description='process user given parameters')
#parser.add_argument("-u", "--username", required =  True, dest="username", help = "enter username")
#parser.add_argument("-p", "--password", required =  True, dest="password", help = "enter passowrd")
parser.add_argument("-k", "--apikey", required = True, dest = "apikey", help = "enter api key from your UTS Profile")
parser.add_argument("-v", "--version", required =  False, dest="version", default = "current", help = "enter version example-2015AA")
parser.add_argument("-s1", "--string1", required =  True, dest="string1", help = "enter a search term, like 'diabetic foot'")
parser.add_argument("-s2", "--string2", required =  True, dest="string2", help = "enter a search term, like 'diabetic foot'")

#name_l1=[]
#name_l2=[]

args = parser.parse_args()
#username = args.username
#password = args.password
apikey = args.apikey
version = args.version
string1 = args.string1
string2=args.string2

def concept_lookup(apikey,version,string):
  name_l=[]
  uri = "https://uts-ws.nlm.nih.gov"
  content_endpoint = "/rest/search/"+version
  ##get at ticket granting ticket for the session
  AuthClient = Authentication(apikey)
  tgt = AuthClient.gettgt()
  pageNumber=0

  while True:
      ##generate a new service ticket for each page if needed
      ticket = AuthClient.getst(tgt)
      pageNumber += 1
      query = {'string':string,'ticket':ticket, 'pageNumber':pageNumber}
      #query['includeObsolete'] = 'true'
      #query['includeSuppressible'] = 'true'
      #query['returnIdType'] = "sourceConcept"
      #query['sabs'] = "SNOMEDCT_US"
      query['searchType']='leftTruncation'
      r = requests.get(uri+content_endpoint,params=query)
      r.encoding = 'utf-8'
      items  = json.loads(r.text)
      jsonData = items["result"]
      #print (json.dumps(items, indent = 4))

      print("Results for page " + str(pageNumber)+"\n")
      
      for result in jsonData["results"]:
          
        try:
          print("ui: " + result["ui"])
        except:
          NameError
        try:
          print("uri: " + result["uri"])
        except:
          NameError
        try:
          print("name: " + result["name"])
          name_l.append(result["name"])
        except:
          NameError
        try:
          print("Source Vocabulary: " + result["rootSource"])
        except:
          NameError
        
        print("\n")
      
      
      ##Either our search returned nothing, or we're at the end
      if jsonData["results"][0]["ui"] == "NONE":
          break
      print("*********")
  return name_l
      

name_l1=concept_lookup(apikey,version,string1)
name_l2=concept_lookup(apikey,version,string2)    
print(len(name_l1))
with open('leftTruncation_name_l1.pickle','wb') as p:
  pickle.dump(name_l1,p,protocol=2)
with open('leftTruncation_name_l2.pickle','wb') as p:
  pickle.dump(name_l2,p,protocol=2)
print(len(name_l2))

    

