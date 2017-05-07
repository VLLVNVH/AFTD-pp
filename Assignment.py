# 2807ICT Assignment written by Allanah French (s5013563) and Tessa Donaldson (s5014499)
# Trimester 1 2017

#--------------INITIAL GAME SETUP----------------
#Open and read the dictionary file
dictionaryFile = open('dictionary.txt') #v2 - allow to use different dictionary file?
dictionaryData = dictionaryFile.read()

#Prompt for word length [calculated from additional code in Appendix A]
while True:
    try:
        wordLength = int(input('How long do you want the word to be? (Between 2 and 29 letters long): '))
        if wordLength >= 2 and wordLength <= 29: #parameters of word length between 2 & 29
            break
        else:
            print('Please insert a valid input')
            continue
    except:
        print('Please insert a valid input')
        continue
    else:
        break

#Prompt for number of guesses
while True:
    try:
        numGuesses = int(input('How many guesses do you want to have? (Must be more than 0): '))
        if numGuesses > 0:
            break
        else:
            print('Please try again')
            continue
    except:
        print('Please try again')
        continue
    else:
        break
            
#Prompt user for if they want a running total of words remaining in word list
while True:
    try:
        showWordList = str(input('Would you like to see the total number of words remaining in the word list? ')) #True/False?
        if showWordList[0] == 'y' or showWordList[0] == 'Y': #possible to use a .upper or .lower thing?
            showWordList = 'Yes' #Should Set to True??
            break
        elif showWordList[0] == 'n' or showWordList[0] == 'N':
            showWordList = 'No' #Should be set to False??
            break
        else:
            print('Please try again')
    except:
        print('Please try again')
        continue
    else:
        break

#---------------GAME PLAY-----------------
#Construct list of words matching wordLength
for line in dictionaryData:#seriously not working?!
    word = line.split()
    letters = list(word)

'''
Try/Except Example - NOT RELATED TO THE ASSIGNMENT
while True:
    try:
        a = int(input('Insert an integer '))
        if a < 5:
            print('please insert a valid input')
            continue
    except:
        print('please insert a valid input')
        continue
    else:
        break
'''
