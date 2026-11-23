"""Practical 11: Multiword expressions, local Normalized Web Distance approximation, similarity and WSD."""
import re,math
DOCS=["bank river water shore fishing","bank money loan account finance","python programming language code","python snake reptile animal","natural language processing text"]
def words(s): return re.findall(r"[a-z]+",s.lower())
def hits(term):
    ts=words(term); return sum(all(t in words(d) for t in ts) for d in DOCS)
def nwd(x,y):
    n=len(DOCS); fx,fy,fxy=hits(x),hits(y),hits(x+" "+y)
    if not fx or not fy or not fxy or n<=max(fx,fy): return float("inf")
    return (max(math.log(fx),math.log(fy))-math.log(fxy))/(math.log(n)-min(math.log(fx),math.log(fy)))
def main():
    print("PRACTICAL 11 - MWE, NWD, SIMILARITY, WSD")
    print("Multiword expressions:",["natural language","machine learning","New York"])
    for a,b in [("bank","money"),("python","programming")]: print(a,b,"hits:",hits(a),hits(b),"local NWD:",round(nwd(a,b),3) if math.isfinite(nwd(a,b)) else "infinity")
    vec={"cat":{"animal","pet","fur"},"dog":{"animal","pet","bark"},"car":{"vehicle","road","engine"}}
    def jac(a,b): return len(vec[a]&vec[b])/len(vec[a]|vec[b])
    print("Jaccard similarity cat/dog:",round(jac("cat","dog"),3)); print("Jaccard similarity cat/car:",round(jac("cat","car"),3))
    context=set(words("She deposited money in the bank to earn interest.")); senses={"financial":{"money","deposit","interest","loan","account"},"river":{"water","river","shore","fishing"}}
    scores={k:len(context&v) for k,v in senses.items()}; print("WSD scores:",scores); print("Selected sense:",max(scores,key=scores.get))
if __name__=="__main__": main()
