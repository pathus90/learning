"""
Convert String to camelcase
Complete the method/function so that it converts dash/underscore delimited
words into camel casing. The first word within the output should be capitalized
only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"""


def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


if __name__ == '__main__':
    print(to_camel_case('the_stealth_warrior'))
