from playsound import playsound
from gtts import gTTS
import os

ids = [1, 2, 3, 4]
language = ['', 'English', 'French', 'Spanish', 'Portuguese']
lang = ['', 'en', 'fr', 'es', 'pt']

while True:
    while True:
        try:
            print("Please Select Your Language:")
            for i in range(1, len(lang)):
                print(f"\t{i}: {language[i]}")
            m = input("->").strip()
            m = int(m)
            if m in ids:
                break
            else:
                input("Please input a Number in Range!!!")
        except:
            input("Please input a Number!!!")
    print("You Have Selected", language[m])
    print("Please Enter Your Text:")
    text = input("->").strip()

    tts = gTTS(text=text, lang=lang[m], slow=False)
    tts.save("t.mp3")
    playsound("t.mp3")
    os.remove("t.mp3")

    print("Would you like to Continue (Y/N):")
    c = input("->").strip()
    if c != "Y" or c != "y":
        break
