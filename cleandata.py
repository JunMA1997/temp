import re
def read_data(filename):
    with open(filename,"r",encoding="utf-8") as f:
        cn_word=f.read().split("\n")
    return cn_word
def clean_save(cn_word,filename):
    with open(filename,"w",encoding="utf-8") as f:
        for word in cn_word:
            if(re.match("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）1234567890“”\-\<>《》：；、ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz]+", word)):
                continue
            else:
                f.write(word+"\n")

        

cn_word = read_data("./1.txt")
cn_word = {}.fromkeys(cn_word).keys()
clean_save(cn_word,"./2.txt")