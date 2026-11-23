"""Practical 6: POS tagging, noun-phrase chunking and named entity recognition."""
import re
S="Riya works at Google in Pune on Monday."
def fallback(w):
    if w.lower() in {"at","in","on"}: return "IN"
    if w[0].isupper(): return "NNP"
    if w.endswith("s"): return "VBZ"
    return "NN"
def main():
    print("PRACTICAL 6 - POS, CHUNKING, NER"); ws=re.findall(r"[A-Za-z]+|[.,]",S)
    try:
        import nltk
        try:
            tagged=nltk.pos_tag(ws); print("NLTK tags:",tagged); print("NLTK NER:",nltk.ne_chunk(tagged))
        except LookupError: tagged=[(w,fallback(w)) for w in ws]; print("NLTK data missing; fallback tags:",tagged)
    except ImportError: tagged=[(w,fallback(w)) for w in ws]; print("Fallback tags:",tagged)
    chunks=[]; cur=[]
    for w,t in tagged:
        if t.startswith("NN"): cur.append(w)
        elif cur: chunks.append(" ".join(cur)); cur=[]
    if cur: chunks.append(" ".join(cur))
    print("Noun phrase chunks:",chunks)
    entities=[(w,k) for w,k in [("Riya","PERSON"),("Google","ORGANIZATION"),("Pune","LOCATION")] if w in ws]
    print("Rule-based entities:",entities)
if __name__=="__main__": main()
