import lightrdf

parser = lightrdf.Parser()

word = input("Please enter a word: ")



def parse_ontology(word):
    with open("ontology.owl", "rb") as f:
        for triple in parser.parse(f, format="owl", base_iri=None):
            if triple[0].find(word, 0, len(triple[0])) != -1:
                if triple[1].find("superTopicOf", 0, len(triple[1])) != -1:
                    print(triple)


parse_ontology(word)