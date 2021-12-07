import nltk
from nltk import pos_tag
from nltk import RegexpParser

def remove_empty_string(text,index):
    text.pop(index)
    return text


with open("computer-science.txt", 'r', encoding = 'utf-8') as f:
    g = open("result.txt", 'w')
    text = f.read().split('\n')
    sentences = list()
    for sentence in text:
        if sentence.find('.', 0, len(sentence)) != -1:
            chunk = sentence.split('.')
            for c in chunk:
                sentences.append(c)
                # print(c)
    # print(sentences)

    for sentence in sentences:
        words = sentence.split()
        # print(words, "\n##########\n")
        tokens_tag = pos_tag(words)
        # print(tokens_tag,"\n##########\n")
        poz = 0
        poz_s1 = 0
        poz_s2 = 0
        poz_v = 0
        for tuple in tokens_tag:
            print(tuple)
            if tuple[1].find('NN', 0, len(tuple[1])) != -1:
                poz_s1 = poz

            ++poz

