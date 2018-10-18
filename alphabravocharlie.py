from flask import Flask
from flask_ask import Ask, statement, question

from alphabet import *

app = Flask(__name__)
ask = Ask(app, "/")

def extractor(word):
    letters = []
    print(word)
    for letter in word.lower():
        try:
            print(eval(letter))
            letters.append(eval(letter))
        except:
            print(letter)
            letters.append(letter)
    print(letters)
    return '... '.join(str(x) for x in letters)

@ask.launch
def start_skill():
    welcome_message = 'HOOO RAH! I can help you spell things using the NATO phonetic alphabet.  For information, say' \
                      ' help or to try it out, ask me to spell a word.'
    return question(welcome_message)

@ask.intent("AMAZON.FallbackIntent")
def fallback():
    message = "Alpha Bravo Charlie didn't understand that. Try asking me to spell a word or phrase."
    return question(message)

@ask.intent("AMAZON.HelpIntent")
def help():
    message = "The NATO phonetic alphabet, officially denoted as the International Radiotelephony Spelling Alphabet, " \
              "and also commonly known as the ICAO phonetic alphabet, and in a variation also known officially as the I T U " \
              "phonetic alphabet and figure code, is the most widely used radiotelephone spelling alphabet. You can " \
              "ask me to spell a word or phrase by saying... Spell a word, or How do you spell?"
    return question(message)

@ask.intent("AMAZON.StopIntent")
def quit():
    message = "Thanks for using Alpha Bravo Charlie. Charlie Mike and have a great day!"
    return statement(message)

@ask.intent("AMAZON.CancelIntent")
def quit():
    message = "Thanks for using Alpha Bravo Charlie. Charlie Mike and have a great day!"
    return statement(message)

@ask.intent("spellIntent")
def spell(phrase):
    message = extractor(phrase)
    return statement(message)

if __name__ == '__main__':
    app.run(debug=False)