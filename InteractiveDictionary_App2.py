import mysql.connector
from difflib import get_close_matches

conn = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
cursor = conn.cursor()

def dict(w):
    cursor.execute("SELECT Expression FROM Dictionary")
    words = cursor.fetchall()
    dictWordList = [word[0] for word in words]
    w = w.lower()
    possibleWordsList = get_close_matches(w, dictWordList)
    if w in dictWordList:
        queryStatement = "SELECT * FROM Dictionary WHERE Expression = '" + w + "'"
        query = cursor.execute(queryStatement)
        queryResults = cursor.fetchall()
        return(queryResults)
    elif w.title() in dictWordList:
        queryStatement = "SELECT * FROM Dictionary WHERE Expression = '" + w.title() + "'"
        query = cursor.execute(queryStatement)
        queryResults = cursor.fetchall()
        return(queryResults)
    elif w.upper() in dictWordList:
        queryStatement = "SELECT * FROM Dictionary WHERE Expression = '" + w.upper() + "'"
        query = cursor.execute(queryStatement)
        queryResults = cursor.fetchall()
        return(queryResults)
    elif len(possibleWordsList) > 0:
        response = input("Did you mean '{}'? Enter Y if Yes, or N if No: ".format(possibleWordsList[0]))
        if response == 'y' or response == 'Y':
            queryStatement = "SELECT * FROM Dictionary WHERE Expression = '" + possibleWordsList[0] + "'"
            query = cursor.execute(queryStatement)
            queryResults = cursor.fetchall()
            return(queryResults)
        elif response == 'n' or response == 'N':
            return("Sorry, the word '{}' doesn't exist in the dictionary.".format(word))
        else:
            return "We didn't understand your entry."
    else:
        return("Sorry, the word '{}' doesn't exist in the dictionary.".format(word))

word = input("Enter a word: ")
output = dict(word)
print()
if type(output) == list:
    i = 1
    for item in output:
        print("{}. {}".format(i, item[1]))
        i += 1
else:
    print(output)