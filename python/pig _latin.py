"""
Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    return ' '.join([val[1:] + val[:1] + 'ay' if val.isalpha() else val for val in text.split(' ')])


if __name__ == '__main__':
    print(pig_it('Pig latin is cool ?'))
