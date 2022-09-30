# Write a method/function DISPLAYWORDS() in python to read lines from a text file STORY.TXT, and display those words, which are less than 4 characters.

def DISPLAYWORDS():
    file = open("Article.txt","r")
    dj = file.readlines()
    for words in dj:
        sfx = words.split()
        for word in sfx:
            if len(word)<4:
                print(word)
    file.close()
DISPLAYWORDS()
