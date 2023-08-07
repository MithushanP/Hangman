#Hangman Project:
import csv
import random

#function

def blankconvert(text): #a function to convert the word into blanks
    text=text.lower()
    blanks=""
    for a in range(len(text)):
            if text[a].isalpha():
                blanks+="_"
            else:
                blanks+=" "
    return blanks

print("Welcome to hangman!: 10 strikes and you are out")

while True:
    mode = input("Select mode: 1.randomly generated word,  2.input your own word. Type either 1 or 2 to select a mode to begin: ")
    if mode == "1" or mode == "2":
        break 
    else:
        print("Please only type the character 1 or 2. ")

if mode== "2":
    while True:
        word = input("To start playing hangman choose a word: ")
        if all(x.isalpha() or x.isspace() for x in word ):
            break
        else:
            print("Invalid word. Contains invalid charectors which are not alphabetical or space")

else:
    with open("./wordlist.csv") as wordlist:
        csv_reader = csv.reader(wordlist)
        csvlist = list(csv_reader)
        word = str(random.choice(csvlist))
        word = word.strip()
    
#loop above only allows valid words go through. ie no punctuation etc

blanks = blankconvert(word) #note add function to convcer to to blanks

used=[]

i=0
while i<=10:

    print(" %s . You have %i strikes. All guessed letters: "%(blanks,i)) #where i is N.O strikes
    print(used)
    if i==10:
        print("GAME OVER! The word was %s" %(word))
        break
    if all( x.isalpha() or x.isspace() for x in blanks ):
        print("You Win!")
        break
    

    while True:
        guess=input("Please either guess a letter or the entire word:  ")
        if len(guess)==1:
            if guess in used:
                print("Already used that letter.")
            elif guess.isalpha():
                break
            else:
                print("Invalid Charector used.")
        if len(guess)>=2:
            if all(x.isalpha() or x.isspace() for x in guess): #perhaps could add some additional logic to so guess must contain atleas 2 alphabetical charectors
                break
            else:
                print("Invalid Charectors detected.")
#above part checks guesses use valid charectors
    if len(guess)==1:
        guess=guess.lower()
        if guess in word:
            for j in range(len(word)):
                if word[j]==guess:
                    blankslist=list(blanks)
                    blankslist[j]=guess
                    blanks="".join(blankslist)
                
            
         

        else:
            print("Sorry the letter is not in the word/s")
            used.append(guess)
            i+=1


    elif len(guess)>=2:
        guess=guess.lower()
        if guess==word:
            print("You Win!!!")
            break
        else:
            print("Guess Incorrect.")
            i+=1
       


            




    





     






















