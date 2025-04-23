import pyttsx3
import os
import datetime
import subprocess
import sys
import pywhatkit
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Ask user input mode
def choose_input_mode():
    mode = input("Choose input mode - 'voice' or 'type': ").lower()
    return mode

# Wake word detector
def listen_for_wake_word(mode, show_message_once=False):
    if mode == 'type':
        if show_message_once:
            print("Type or say 'jarvis' to wake me up...")
        while True:
            text = input().lower()
            if 'jarvis' in text:
                print("Wake word detected...!!")
                speak('Hi Sir, How can I help you?')
                return True
    elif mode == 'voice':
        if show_message_once:
            print("Type or say 'jarvis' to wake me up...")
        with sr.Microphone() as source:
            while True:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio).lower()
                    if 'jarvis' in text:
                        print("Wake word detected...!!")
                        speak('Hi Sir, How can I help you?')
                        return True
                except:
                    pass

# Command processor
def cmd(mode):
    if mode == 'type':
        text = input("Type your command: ").lower()
    else:
        with sr.Microphone() as source:
            print("Listening for your command...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio).lower()
                print("You said:", text)
            except:
                print("Sorry, I didn't get that.")
                return False

    print("Your Message:", text)

    if 'stop' in text or 'bye' in text:
        speak('Stopping the program. Goodbye!!')
        print("Stopping the program. Goodbye!!")
        return True

    elif 'how are you' in text:
        speak('I am doing great, thanks for asking. How about you?')
        print("I am doing great, thanks for asking. How about you?")

    elif 'good' in text or 'fine' in text:
        speak('Glad to hear that!')
        print("Glad to hear that!")

    elif 'open' in text:
        software_name = text.replace('open', '').strip()
        open_software(software_name)

    elif 'close' in text:
        software_name = text.replace('close', '').strip()
        close_software(software_name)

    elif 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print("Current time is:", current_time)
        speak(f"The time is {current_time}")

    elif 'date' in text:
        today_date = datetime.datetime.now().strftime('%B %d, %Y')
        print("Today's date is:", today_date)
        speak(f"Today's date is {today_date}")

    elif 'who is god' in text:
        speak('Ajitheyyy Kaduvaleyy')
        print("Ajitheyyy Kaduvaleyy")

    elif 'what is your name' in text:
        speak('My name is Jarvis and I am your Artificial Intelligence')
        print("My name is Jarvis and I am your Artificial Intelligence")

    else:
        speak("I didn't understand that command.")
        print("Unknown command.")

    return False


# Open software
def open_software(name):
    if 'chrome' in name:
        speak('Okay Opening Chrome...')
        print("Okay Opening Chrome...")
        subprocess.Popen([r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"])
    elif 'microsoft edge' in name:
        speak('Okay Opening Microsoft Edge...')
        print("Okay Opening Microsoft Edge...")
        subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"])
    elif 'notepad' in name:
        speak('Okay Opening Notepad...')
        print("Okay Opening Notepad...")
        subprocess.Popen(['notepad.exe'])
    elif 'calculator' in name:
        speak('Okay Opening Calculator...')
        print("Okay Opening Calculator...")
        subprocess.Popen(['calc.exe'])
    elif 'play' in name:
        speak('Okay Opening YouTube...')
        print("Okay Opening YouTube...")
        pywhatkit.playonyt(name)
    else:
        speak(f"I couldn't find the software {name}")
        print(f"I couldn't find the software {name}")

# Close software
def close_software(name):
    if 'chrome' in name:
        speak(' Okay Closing Chrome...')
        print("Okay Closing Chrome...")
        os.system("taskkill /f /im chrome.exe")
    elif 'microsoft edge' in name:
        speak('Okay Closing Microsoft Edge...')
        print("Okay Closing Microsoft Edge...")
        os.system("taskkill /f /im msedge.exe")
    elif 'notepad' in name:
        speak('Okay Closing Notepad...')
        print("Okay Closing Notepad...")
        os.system("taskkill /f /im notepad.exe")
    elif 'calculator' in name:
        speak('Okay Closing Calculator...')
        print("Okay Closing Calculator...")
        os.system("taskkill /f /im calc.exe")
    else:
        speak(f"I couldn't find any open software {name}")
        print(f"I couldn't find any open software {name}")

# Main
mode = choose_input_mode()  # You should define this to return 'type' or 'voice'
speak('Tell me pass code')
print("Tell me pass code : ")

while True:
    if listen_for_wake_word(mode):
        while True:
            should_exit = cmd(mode)
            if should_exit:
                sys.exit()



