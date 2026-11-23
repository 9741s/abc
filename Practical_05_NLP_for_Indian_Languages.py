"""Practical 5: Hindi tokenization, similar sentence generation and script-based language identification."""
import re
SAMPLES=["भारत एक विविधताओं वाला देश है।","प्राकृतिक भाषा संसाधन भाषा को समझने में मदद करता है।","विद्यार्थी हिंदी भाषा का अध्ययन करते हैं।"]
def tokens(s): return re.findall(r"[\u0900-\u097F]+|[A-Za-z]+|[0-9]+|[^\w\s]",s)
def identify(s):
    d=sum("\u0900"<=c<="\u097F" for c in s); a=sum(c.isascii() and c.isalpha() for c in s)
    return "Likely Hindi/Devanagari" if d>a and d else "Likely English/Latin" if a else "Unknown"
def similar(s):
    for a,b in {"भारत":"मेरा देश","विद्यार्थी":"छात्र","अध्ययन":"अभ्यास","मदद":"सहायता"}.items(): s=s.replace(a,b)
    return s
def main():
    print("PRACTICAL 5 - INDIAN LANGUAGE NLP")
    for s in SAMPLES: print("\nText:",s,"\nTokens:",tokens(s),"\nSimilar:",similar(s),"\nLanguage:",identify(s))
if __name__=="__main__": main()
