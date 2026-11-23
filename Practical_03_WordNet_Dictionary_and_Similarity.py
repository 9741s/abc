"""Practical 3: WordNet synonyms, antonyms, lemmas, hypernyms, hyponyms and similarity."""
OFFLINE={"happy":{"synonyms":["glad","joyful"],"antonyms":["sad"],"hypernyms":["emotion"],"hyponyms":["cheerful"]}}
def main():
    print("PRACTICAL 3 - WORDNET")
    try:
        from nltk.corpus import wordnet as wn
        ss=wn.synsets("happy")
        if not ss: raise LookupError("No synsets")
        for s in ss[:3]:
            print("Synset:",s.name(),"Definition:",s.definition())
            print("Lemmas:",[l.name() for l in s.lemmas()])
            print("Hypernyms:",[x.name() for x in s.hypernyms()])
            print("Hyponyms:",[x.name() for x in s.hyponyms()[:5]])
            print("Antonyms:",[a.name() for l in s.lemmas() for a in l.antonyms()])
        if len(ss)>1: print("Path similarity:",ss[0].path_similarity(ss[1]))
    except (ImportError,LookupError) as e:
        print("WordNet corpus unavailable:",e)
        print("Offline example for 'happy':",OFFLINE["happy"])
        print("Lemma: happy")
if __name__=="__main__": main()
