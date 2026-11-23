"""Practical 10: POS tagging, statistical transition estimates, probabilistic and dependency parsing demo."""
from collections import Counter,defaultdict
import re
CORPUS=[[('the','DET'),('cat','NOUN'),('sleeps','VERB')],[('a','DET'),('dog','NOUN'),('runs','VERB')],[('the','DET'),('dog','NOUN'),('eats','VERB'),('food','NOUN')]]
def tag(w,em):
    found=[(c[w],t) for t,c in em.items() if c[w]]
    if found: return max(found)[1]
    return "DET" if w in {"a","an","the"} else "VERB" if w.endswith("s") else "NOUN"
def main():
    print("PRACTICAL 10 - TAGGING AND PARSING"); em=defaultdict(Counter); trans=Counter(); totals=Counter()
    for sent in CORPUS:
        for w,t in sent: em[t][w]+=1
        seq=["START"]+[t for w,t in sent]+["END"]
        for a,b in zip(seq,seq[1:]): trans[a,b]+=1; totals[a]+=1
    s="the dog eats food"; ws=re.findall(r"[a-z]+",s); tags=[tag(w,em) for w in ws]
    print("Input:",s); print("POS tags:",list(zip(ws,tags)))
    print("P(VERB|NOUN):",round(trans["NOUN","VERB"]/max(1,totals["NOUN"]),3))
    root=next((i for i,t in enumerate(tags) if t=="VERB"),0); arcs=[]
    for i,(w,t) in enumerate(zip(ws,tags)):
        rel="ROOT" if i==root else "nsubj" if t=="NOUN" and i<root else "obj" if t=="NOUN" else "det" if t=="DET" else "dep"
        head="ROOT" if i==root else ws[root]
        arcs.append((w,rel,head))
    print("Dependency arcs (token, relation, head):",arcs)
if __name__=="__main__": main()
