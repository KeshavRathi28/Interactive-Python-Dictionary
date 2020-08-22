import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def dict(w):
    w = w.lower()
    list = get_close_matches(w, data.keys())
    if w in data.keys():
        return data[w]
    elif w.title() in data.keys():
        return data[w.title()]
    elif w.upper() in data.keys():
        return data[w.upper()]
    elif len(list) > 0:
        response = input("Did you mean '%s'? Enter Y if Yes, or N if No: " % list[0])
        if response == "Y" or response == "y":
            return data[list[0]]
        elif response == "N" or response == "n":
            return "Sorry, the word '%s' doesn't exist in the dictionary." % w
        else:
            return "We didn't understand your entry."
    else:
        return "Sorry, the word '%s' doesn't exist in the dictionary." %w

word = input("Enter a word: ")
output = dict(word)
if type(output) == list:
    i = 1
    for item in output:
        print("%s. %s" % (i, item))
        i += 1
else:
    print(output)