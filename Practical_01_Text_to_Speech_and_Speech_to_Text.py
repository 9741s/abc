"""Practical 1: Text-to-speech and speech-to-text. Optional: pip install pyttsx3 SpeechRecognition pyaudio"""
import importlib.util

def main():
    text="Welcome to the Natural Language Processing practical."
    print("PRACTICAL 1 - TEXT AND SPEECH")
    if importlib.util.find_spec("pyttsx3"):
        try:
            import pyttsx3
            engine=pyttsx3.init(); engine.say(text); engine.runAndWait()
            print("Text-to-speech completed.")
        except Exception as e: print("TTS unavailable:",e)
    else: print("TTS demo text:",text,"(optional: install pyttsx3)")
    if importlib.util.find_spec("speech_recognition"):
        try:
            import speech_recognition as sr
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak now..."); r.adjust_for_ambient_noise(source,duration=.4); audio=r.listen(source,timeout=5,phrase_time_limit=8)
            try: print("Recognized:",r.recognize_google(audio))
            except sr.UnknownValueError: print("Speech was unclear.")
            except sr.RequestError as e: print("Recognition service unavailable:",e)
        except Exception as e: print("Microphone unavailable:",e)
    else: print("Speech-to-text microphone demo skipped (optional: install SpeechRecognition and PyAudio).")
if __name__=="__main__": main()
