"""
Brittany Mazza
CST 205 Multimedia Design and Programming

Lab #14: Files in Python

This lab relies on two file. The first is titled "eggs.txt" and contains the
words that comprises "Green Eggs and Ham" by Dr. Suess. The second is titled
"otter-realm.html" and it contains the HTML that makes up 
http://otterrealm.com/category/news/ as of December 5, 2015.
"""


# Problem 1
def greenEggsAndHam(eggsFilePath):
    """
    Based on the text from the Dr. Suess book, "Green Eggs and Ham", display
    the amount of times each word was used, the total number of words, and the
    word that appeared the most in the book (and how many times that
    appearance was).

    params:
        eggsFilePath -> The path to eggs.txt (can use pickAFile in JES)
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
    # Get the word with the highest count and print the word count for each word
    # at the same time.
    mostCommonWord = ""
    highestCount = 0
    print " Word Counts:",
    for word in wordAppearance:
        if wordAppearance[word] > highestCount:
          mostCommonWord = word
          highestCount = wordAppearance[word]
        print " %s: %s," % (word, wordAppearance[word]),
    print "\n Total Word Count: %s" % (sum(wordAppearance.values()))
    print (" \"%s\" appeared in the text the most at %s total times." % 
        (mostCommonWord, highestCount))


# Problem 2
def showBreakingNews(htmlFilePath):
    """
    Displays the headlines from the html file passed in and returns them as an
    array.

    params:
        htmlFilePath -> The path to otter-realm.html (can use pickAFile in
                        JES)
    """
    # Open file and split it into smaller section by line.
    htmlFile = open(htmlFilePath, "rt")
    htmlContents = htmlFile.readlines()
    htmlFile.close()
    # There's a headline if the line contains "<h3>". If that's the case,
    # split the line on "<h3>". Get the title by splitting the string again,
    # but on "</h3>". The first element in the array is the headline.
    headlines = []
    for line in htmlContents:
        if "<h3>" in line:
            splitAtTitleBegin = line.split("<h3>")
            # Remove first section if it wasn't a headline.
            if not line[:3] == "<h3>":
                del splitAtTitleBegin[0]
            for titleLine in splitAtTitleBegin:
                headlines.append(titleLine.split("</h3>")[0])
        
    print "\n*** Otter Realm Breaking News! ***"
    for headline in headlines:
        print " > %s" % headline
    return headlines
