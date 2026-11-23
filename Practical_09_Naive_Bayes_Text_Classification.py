"""Practical 9: Multinomial Naive Bayes text classifier with Laplace smoothing."""
import re,math
from collections import Counter,defaultdict
DATA=[("I love this movie","positive"),("This film is wonderful","positive"),("Amazing story and great acting","positive"),("I hate this movie","negative"),("This film is boring","negative"),("Terrible story and poor acting","negative")]
def tok(s): return re.findall(r"[a-z]+",s.lower())
class NB:
    def fit(self,data):
        self.docs=Counter(); self.counts=defaultdict(Counter); self.vocab=set()
        for text,label in data:
            ws=tok(text); self.docs[label]+=1; self.counts[label].update(ws); self.vocab.update(ws)
        self.total=sum(self.docs.values())
    def predict(self,text):
        scores={}; ws=tok(text); V=max(1,len(self.vocab))
        for label,n in self.docs.items():
            total=sum(self.counts[label].values()); score=math.log(n/self.total)
            for w in ws: score+=math.log((self.counts[label][w]+1)/(total+V))
            scores[label]=score
        return max(scores,key=scores.get),scores
def main():
    print("PRACTICAL 9 - NAIVE BAYES"); m=NB(); m.fit(DATA)
    for s in ["The movie was wonderful","I hate this boring film","Amazing acting and great story"]:
        label,scores=m.predict(s); print("\nText:",s,"\nPrediction:",label,"\nScores:",{k:round(v,3) for k,v in scores.items()})
if __name__=="__main__": main()
