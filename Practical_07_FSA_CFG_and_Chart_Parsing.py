"""Practical 7: DFA, context-free grammar and CKY chart parsing."""
def dfa(s):
    state=0
    for c in s:
        if c not in "01": return False
        if c=="1": state=1-state
    return state==0
def cky(words,lex,binary):
    n=len(words); chart=[[set() for _ in range(n+1)] for _ in range(n)]
    for i,w in enumerate(words): chart[i][i+1].update(lex.get(w,set()))
    for span in range(2,n+1):
        for i in range(n-span+1):
            j=i+span
            for k in range(i+1,j):
                for a in chart[i][k]:
                    for b in chart[k][j]: chart[i][j].update(binary.get((a,b),set()))
    return chart[0][n]
def main():
    print("PRACTICAL 7 - FSA, CFG, CHART PARSING")
    for s in ["","0","11","101","111"]: print(repr(s),"accepted:",dfa(s))
    lex={"the":{"Det"},"boy":{"N"},"apple":{"N"},"eats":{"V"}}
    binary={("Det","N"):{"NP"},("V","NP"):{"VP"},("NP","VP"):{"S"}}
    sent=["the","boy","eats","the","apple"]; print("Sentence:"," ".join(sent)); print("CKY top categories:",cky(sent,lex,binary)); print("CFG accepts:","S" in cky(sent,lex,binary))
if __name__=="__main__": main()
