import os

if __name__ == '__main__':
    print('Welcome to RoboSpeaker 1.1. Created by Anu')
    while True:
        x = input("Enter what you want me to speak (or type 'q' to quit): ")
        if x.lower() == "q":
            command = 'powershell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Bye bye, rude girl\')"'
            os.system(command)
            break
        else:
            command = f'powershell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
            os.system(command)
