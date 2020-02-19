import re
from dic import dic
def read_data(filename):
    with open(filename,"r",encoding="utf-8") as f:
        cn_word=f.read().split("\n")
    return cn_word
def translate(cn_word,en_word,dic,bowdictionary=None,mode=0):
    for word in cn_word:
        print(word)
        if(re.match("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）1234567890“”\-\<>《》：；、ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz]+", word)):
            if(re.match("[1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz]+", word)):
                en_word.append(cn_word)
                continue
            if word.startswith("。"):
                en_word.append(".")
                continue
            if word.startswith( '，'):
                en_word.append(",")
                continue
            if word.startswith( '：'):
                en_word.append(":")
                continue
            if word.startswith( '“'):
                en_word.append("\"")
                continue
            if word.startswith( '”'):
                en_word.append("\"")
                continue
            if word.startswith( '‘'):
                en_word.append("\'")
                continue
            if word.startswith( '’'):
                en_word.append("\'")
                continue
            if word.startswith( '【'):
                en_word.append("[")
                continue
            if word.startswith( '】'):
                en_word.append("]")
                continue
            if word.startswith( '{'):
                en_word.append("{")
                continue
            if word.startswith( '}'):
                en_word.append("}")
                continue
            if word.startswith( '《'):
                en_word.append("<")
                continue
            if word.startswith( '》'):
                en_word.append(">")
                continue
            if word.startswith( '/'):
                en_word.append("/")
                continue
            if word.startswith( '？'):
                en_word.append("?")
                continue
            if word.startswith( '、'):
                en_word.append(",")
                continue
        
            continue
            ## todo 处理标点
        else:
            en_word.append(dic(word,mode=mode,dictionary=bowdictionary))
    return en_word



en_word=[]
cn_word=read_data("./1.txt")
bowdictionary={
    "他":"he",
    "还":"repay",
    "把":"control",
    "宣扬":"publicity",
    "自己":"oneself",
    "思想":"thought",
    "的":"of",
    "所谓":"same",
    "绿皮书":"Green Book",
    "称作":"be called",
    "新":"new",
    "福音书":"evangel"
}
en_word=translate(cn_word,en_word,dic,mode=1,bowdictionary=bowdictionary)
print(en_word)
print(cn_word)