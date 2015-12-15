"""
Brittany Mazza
CST 205 Multimedia Design and Programming

Mini-lab: Adding on to the HTML Lab

This lab relies on two files. The first is titled "eggs.txt" and contains the
words that comprises "Green Eggs and Ham" by Dr. Suess. The second is titled
"otter-realm.html" and it contains the HTML that makes up 
http://otterrealm.com/category/news/ as of December 5, 2015.
"""


# Problem 1
def greenEggsAndHam(eggsFilePath, htmlFilePath):
    """
    Based on the text from the Dr. Suess book, "Green Eggs and Ham", display
    the amount of times each word was used, the total number of words, and the
    word that appeared the most in the book (and how many times that
    appearance was).

    params:
        eggsFilePath -> The path to eggs.txt (can use pickAFile in JES)
        htmlFilePath -> The path for the HTML page to write the output to.
    return: (nothing)
    """
    # Open file and split words into an array.
    eggsFile = open(eggsFilePath, "rt")
    eggsContents = eggsFile.read()
    eggsFile.close()
    words = eggsContents.split()
    # Count how many times each word appears.
    wordAppearance = {}
    for word in words:
        lowercasedWord = word.lower()
        if lowercasedWord in wordAppearance:
          wordAppearance[lowercasedWord] += 1
        else:
          wordAppearance[lowercasedWord] = 1
    # Create HTML output string.
    colors = ['00ff00','00cc00','009900','006600','003300']
    output = ""
    for word in wordAppearance:
        wordValue = wordAppearance[word] % 5
        output += "<p style=\"color:#" + colors[wordValue] + \
             "; font-size:" + str(wordValue*10) + "px;"
        if wordValue == 4: # Maximum value.
          output += " font-weight:bold" 
        output += "\">" + word + "</p>"
    # Create the Green Eggs and Ham HTML page
    htmlFile = open(htmlFilePath, "wt")
    htmlFile.write(output)
    htmlFile.close()
