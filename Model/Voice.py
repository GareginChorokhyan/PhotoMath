from pygame import mixer
import speech_recognition
from word2number import w2n
import sympy as sp
import math
import re

mixer.init()

operations_key = {
    'ADD': lambda x, y: x + y,
    'ADDITION': lambda x, y: x + y,
    'SUBTRACTION': lambda x, y: x - y,
    'DIFFERENCE': lambda x, y: x - y,
    'SUBTRACT': lambda x, y: x - y,
    'MULTIPLY': lambda x, y: x * y,
    'PRODUCT': lambda x, y: x * y,
    'MULTIPLICATION': lambda x, y: x * y,
    'DIV': lambda x, y: x / y,
    'DIVISION': lambda x, y: x / y,
    'DIVIDE': lambda x, y: x / y,
    'MOD': lambda x, y: x % y,
    'MODULUS': lambda x, y: x % y,
    'ROOT': lambda x, y: sp.root(x, y),
    'FACTORIAL': lambda x: math.factorial(x),
    'POW': lambda x, y: x ** y,
    'POWER': lambda x, y: x ** y,
    'LCM': lambda x, y: math.lcm(x, y),  # Least common multiple
    'HCF': lambda x, y: math.gcd(x, y),  # Highest common factor
}


class Audio:
    def audio(self):
        mixer.music.load('data/music1.mp3')
        mixer.music.play()
        sr = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mikro:
            try:
                sr.adjust_for_ambient_noise(mikro, duration=0.2)
                voice = sr.listen(mikro)
                text = sr.recognize_google(voice)
                mixer.music.load('data/music2.mp3')
                mixer.music.play()
                text_list = text.split(' ')
                # print(text_list)
                for word in text_list:
                    if word.upper() in operations_key.keys():
                        l = self.findNumbers(text_list)
                        if len(l) == 1:
                            result = operations_key[word.upper()](l[0])
                            return result
                        else:
                            result = operations_key[word.upper()](l[0], l[1])
                            return result
            except:
                pass

    def findNumbers(self, text):
        numbers = []
        for word in text:
            try:
                num = w2n.word_to_num(word)
                numbers.append(num)
            except ValueError:
                # If the word is not a number, check if it's a numeric value
                if re.match(r'^-?\d+(?:\.\d+)?$', word):
                    numbers.append(float(word))  # Convert numeric string to float
        return numbers
