import json
# seperate sentences into words
import jieba
l=0
cn=[]
en=[]
with open('D:\\download\\translation2019zh\\translation2019zh_train.json', encoding='utf-8') as f:
    for i in range(100000):
        line=f.readline()
        j=json.loads(line)
        # print(j["chinese"])
        cn.append(j["chinese"])
        en.append(j["english"])
        l+=1
    f.close()



cn_words=[]
for s in cn:
    words=[]
    w=jieba.cut(s)
    for word in w:
        words.append(word)
    cn_words.append(words)
print("save")
with open("1.txt","w",encoding="utf-8") as f:
    for words in cn_words:
        for word in words:
            f.write(word+"\n")