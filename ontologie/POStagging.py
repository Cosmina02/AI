from nltk import pos_tag
def file_splitter(text):
    sentences = list()
    for sentence in text:
        if sentence.find('.', 0, len(sentence)) != -1:
            chunk = sentence.split('.')
            for c in chunk:
                sentences.append(c)
    return sentences

def generate_file(sentences):
    sentences_in_file = 0
    for sentence in sentences:
        words = sentence.split()
        tokens_tag = pos_tag(words)
        poz = 0
        poz_s1 = -1
        poz_s2 = -1
        poz_v = -1
        k = 0
        for tuple in tokens_tag:
            # print(tuple)
            if poz_s1 == -1 and tuple[1].find('NN', 0, len(tuple[1])) != -1:
                poz_s1 = poz
            elif poz_s1 != -1 and poz_s2 == -1 and poz_v != -1 and tuple[1].find('NN', 0, len(tuple[1])) != -1:
                poz_s2 = poz
            elif poz_v == -1 and tuple[1].find('VB', 0, len(tuple[1])) != -1:
                poz_v = poz
                k += 1
            elif poz_s1 != -1 and poz_s2 == -1 and poz_s1 < poz and tuple[1].find('VB', 0, len(tuple[1])) != -1:
                k += 1
            poz += 1
            # print(poz_s1," ",poz_v," ",poz_s2, " ", k)
        if k == 1 and poz_s1 < poz_v < poz_s2:
            sentences_in_file += 1
            g.write(sentence)
            g.write("\n")
    return sentences_in_file
# nltk.download()
with open("computer-science.txt", 'r', encoding='utf-8') as f:
    g = open("result.txt", 'w', encoding='utf-8')
    text = f.read().split('\n')
    sentences = file_splitter(text)

    print("Number of sentances in input file :",len(sentences))

    print("Number of sentences in result file :",generate_file(sentences))