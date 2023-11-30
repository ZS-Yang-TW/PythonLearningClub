import jieba
import numpy as np

# 斷詞處理
def tokenize(sentence):
    return list(jieba.cut(sentence, cut_all = False))

#詞袋模型
def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [w for w in tokenized_sentence]

    bag = np.zeros(len(all_words),dtype=np.float32)

    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag


# if __name__ == "__main__":
    