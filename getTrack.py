import random
import json
import keyboard

if __name__ == '__main__':
    j = json.load(open("f1.json", 'r'))
    while True:
        number = random.randint(1, 26)
        track = j[str(number)]
        if "Kurz" in track:
            continue
        else:
            print(track)
        keyboard.wait('o')