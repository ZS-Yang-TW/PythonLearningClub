import json
import jieba
import numpy as np

# 引入資料集
with open('intents_chinese.json','r') as f:
    intents_box = json.load(f)

all_words = []  #儲存所有文字
tags =[]    #儲存標籤
xy = []     #儲存樣式與標籤

# 將json檔案中的資料存入變數
for intent in intents_box['intents_list']:
    tag = intent['tag']
    tags.append(tag)

    for sentence in intent['patterns']:
        w = list(jieba.cut(sentence, cut_all = False))
        all_words.extend(w)
        xy.append((w,tag))

# 停用詞
with open('stop_words.txt','r',encoding='utf-8') as f:
    stopwords = set(f.read().split('\n'))
ignore_symbols = {'；','，','。','！','：','「','」','…','、','？','【','】','.',':','?',';','!','~','`','+','-','<','>','/','[',']','{','}',"'",'"',' '}
ignore_set = stopwords.union(ignore_symbols)
all_words = [w for w in all_words if w not in ignore_set]
all_words = sorted(set(all_words))

# 建立詞袋向量與標籤序號
X_train = [] #輸入: BOW向量
y_train = [] #輸出: 儲存tag(分類)

for sentence, tag in xy:
    bag = [1 if w in sentence else 0 for w in all_words]
    X_train.append(bag)
    y_train.append(tags.index(tag))
    
# 利用 numpy 建立訓練資料
X_train = np.array(X_train, dtype=np.float32)
y_train = np.array(y_train, dtype=np.float32)