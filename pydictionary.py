from difflib import get_close_matches
import json

x = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in x:
        return x[word]
    elif word.title() in x:
        return x[word.title()]
    elif word.upper() in x:
        return x[word.upper()]
    elif len(get_close_matches(word, x.keys())) > 0:
        print("Did you mean %s instead?" %get_close_matches(word, x.keys())[0])
        decide = input("Press y for yes or n for no ")
        if decide == "y":
            return x[get_close_matches(word, x.keys())[0]]
        elif decide == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        print("The word doesn't exist. Please double check it.")

word = input("Enter the word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)