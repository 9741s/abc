"""Practical 8: Rule-based stemming and dictionary lemmatization, with optional NLTK."""
WORDS=["playing","played","studies","cars","running","better","mice"]
LEMMAS={"better":"good","mice":"mouse","studies":"study","running":"run","played":"play","playing":"play","cars":"car"}
def stem(w):
    for suf in ("ingly","edly","ing","ed","ies","s"):
        if w.endswith(suf) and len(w)>len(suf)+2: return w[:-len(suf)]+("y" if suf=="ies" else "")
    return w
def main():
    print("PRACTICAL 8 - STEMMING AND LEMMATIZATION"); print(f"{'Word':<14}{'Stem':<14}Lemma")
    for w in WORDS: print(f"{w:<14}{stem(w):<14}{LEMMAS.get(w,w)}")
    try:
        from nltk.stem import PorterStemmer
        p=PorterStemmer(); print("NLTK Porter stems:",[(w,p.stem(w)) for w in WORDS])
    except ImportError: print("NLTK not installed; offline methods used.")
if __name__=="__main__": main()
