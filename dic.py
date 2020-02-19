#return all English meanings
import re
import pandas as pd
def dic(word,mode=0,dictionary=None):
    if(mode == 0):
        #原始词典 origin
        dictionary = pd.read_csv('./results_1.txt',header = None)
        #print(dictionary)
        result=[]
        for row in dictionary.itertuples():
            if word == row[1]:
                #print(row[2])
                translations = re.findall(r"(?:\w|\s)*",row[2])
                for trans in translations:
                    if trans!="" and trans!=" ":
                        result.append(trans)
                
                #print(result)
                return result
    if(mode==1):        
        return dictionary[word]
    
