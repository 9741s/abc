"""Practical 4: Tokenization using Python, regex, NLTK, spaCy, Keras and Gensim. Optional packages are skipped safely."""
import re,importlib.util
TEXT="NLP is useful. Tokenization divides text into words and sentences!"
def main():
    print("PRACTICAL 4 - TOKENIZATION")
    print("Python split:",TEXT.split()); print("Regex words:",re.findall(r"\b[\w'-]+\b",TEXT)); print("Regex sentences:",re.split(r"(?<=[.!?])\s+",TEXT))
    if importlib.util.find_spec("nltk"):
        import nltk
        try: print("NLTK:",nltk.word_tokenize(TEXT))
        except LookupError: print("NLTK tokenizer data missing; optional download punkt_tab.")
    else: print("NLTK not installed; skipped.")
    if importlib.util.find_spec("spacy"):
        try:
            import spacy; print("spaCy:",[t.text for t in spacy.blank("en")(TEXT)])
        except Exception as e: print("spaCy skipped:",e)
    else: print("spaCy not installed; skipped.")
    if importlib.util.find_spec("tensorflow"):
        try:
            from tensorflow.keras.preprocessing.text import Tokenizer
            t=Tokenizer(); t.fit_on_texts([TEXT]); print("Keras word index:",t.word_index)
        except Exception as e: print("Keras skipped:",e)
    else: print("TensorFlow/Keras not installed; skipped.")
    if importlib.util.find_spec("gensim"):
        try: from gensim.utils import simple_preprocess; print("Gensim:",simple_preprocess(TEXT))
        except Exception as e: print("Gensim skipped:",e)
    else: print("Gensim not installed; skipped.")
if __name__=="__main__": main()
