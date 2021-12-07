import lightrdf

parser = lightrdf.Parser()

def is_reapeating(words,text):
    for word in words:
        if word == text:
            return True
    return False

def ontology_parser():
    words = list()
    with open("ontology.owl", "rb") as f :
        for triple in parser.parse(f, format="owl", base_iri=None) :
            chunk = triple[0].split('/')
            if is_reapeating(words, chunk[len(chunk)-1]) is False:
                words.append(chunk[len(chunk)-1])

    return words

def modify_words(text):
    words = list()
    for t in text:
        word = t.replace("_"," ")
        words.append(word)
    return words

def find_words_in_file(words):
    with open("result.txt", 'r', encoding='utf-8') as f:
        g = open("output.txt", 'w', encoding='utf-8')
        text = f.read().split('\n')
        for line in text:
            r = True
            for word in words:
                if r is True and line.find(word, 0, len(line)) != -1:
                    print(line)
                    r = False
                    g.write(line)
                    g.write('\n')


words = ontology_parser()
words = modify_words(words)
ceva=['1960','computer']
find_words_in_file(words)
# print(modify_words(ceva))
