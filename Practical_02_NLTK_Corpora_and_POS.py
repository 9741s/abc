"""Practical 2: Corpus, conditional frequency, POS tagging and word segmentation."""
import re
from collections import Counter,defaultdict
CORPUS=["Natural language processing helps computers understand language.","Students study language, words, grammar and meaning.","Computers process text using useful language tools."]
def tokenize(s): return re.findall(r"[A-Za-z]+|[0-9]+|[^\w\s]",s.lower())
def tag(w):
    if w in {"a","an","the"}: return "DET"
    if w in {"and","or","but"}: return "CONJ"
    if w.endswith("ly"): return "ADV"
    if w.endswith(("ing","ed")): return "VERB"
    if w.endswith(("ous","ful","ive","al")): return "ADJ"
    return "NOUN"
def main():
    print("PRACTICAL 2 - CORPORA, FREQUENCY, POS")
    cfd=defaultdict(Counter)
    for i,s in enumerate(CORPUS,1):
        ts=tokenize(s); print("Sentence",i,"tokens:",ts)
        for w in ts:
            if w.isalpha(): cfd[f"Text {i}"][w]+=1
    print("Conditional frequency distribution:")
    for k,v in cfd.items(): print(k,dict(v))
    sample="Students are learning language processing."
    print("Fallback POS:",[(w,tag(w)) for w in tokenize(sample) if w.isalpha()])
    try:
        import nltk
        print("NLTK:",nltk.__version__)
        try: print("NLTK POS:",nltk.pos_tag(nltk.word_tokenize(sample)))
        except LookupError: print("NLTK data missing; fallback results above. Optional: python -m nltk.downloader punkt punkt_tab averaged_perceptron_tagger_eng")
    except ImportError: print("NLTK not installed; standard Python fallback used.")
if __name__=="__main__": main()
