from datetime import datetime, date, time, timedelta
from prettytable import PrettyTable
import os
import random


DIFFICULTY_OPTIONS = {
    1: "EASY",
    2: "MEDIUM",
    3: "HARD"
}

# Used for linux
sfile = "/tmp/highscores.txt"

# Used for Windows
#sfile = "C:\\temp\\highscores.txt"

def get_highscores():
    # This method handles grabbing the current high scores before each game

    # Creates a prettytable object for sorting and displaying highscores
    table = PrettyTable()
    table.field_names = ["Name","Difficulty","Correct","Total","Duration"]

    # If the highscore file doesn't exist, create it
    if os.path.exists(sfile):
        f = open(sfile, "r")
    else:
        f = open(sfile,"w+")

    print("\n")

    # Grab the current highscores if any
    contents = f.read()
    for line in contents.splitlines():
        table.add_row([line.split(",")[0],line.split(",")[1],line.split(",")[2],line.split(",")[3],line.split(",")[4]])
    f.close()

    table.sortby = "Duration"
    table.reversesort = False
    print(table.get_string(title="Highscores",start=0,end=9))  

    print("\n\n")


def update_highscores(player, difficulty, correct_answers, number_of_questions, duration):
    """ This method handles updating the high score of each player """

    # Grab the total seconds for the duration and format it to 2 decimal places
    total_seconds = duration.total_seconds()
    total_seconds_dec = float("%.2f" % total_seconds)

    # Grab the english corresponding value for difficulty
    difficulty = DIFFICULTY_OPTIONS[difficulty]

    # Open the highscore file for appending so we can add our new values
    target = open(sfile,'a')
    target.write("{},{},{},{},{}".format(player, difficulty, correct_answers, number_of_questions, total_seconds_dec))
    target.write("\n")

    target.close()

def get_format(anumber):
    chkformat = random.randint(1,4)
    if chkformat == 1:
        #decimal
        newnbr = anumber
        fmtstring = 'Decimal'
    elif chkformat == 2:
        #hex
        newnbr = hex(anumber)
        fmtstring = 'Hex'
    else:
        #octal
        newnbr = oct(anumber)
        fmtstring = 'Octal'

    return newnbr, fmtstring

def get_mathfunc():
    mthfunc = random.randint(1,3)
    if mthfunc ==1:
        return "ADD"
    else:
        return "SUBTRACT"

def play_game():

    # Show the highscores
    get_highscores()

    # Grab the begin time of the game
    start_time = datetime.now()

    # Grab the player name to keep track of highscores
    player = input("Name of player: ")
    player = str(player)

    # Grab the number of questions to ask
    number_of_questions = input("How many questions?: ")
    number_of_questions = int(number_of_questions)

    # Grab the difficulty of the questions
    difficulty =  input("Press 1 for easy, 2 for medium, and 3 for hard:")
    difficulty = int(difficulty)
    
    # Placeholder for number of correct answers
    correct_answers = 0

    # Ask N # of questions
    for nbr1 in range(number_of_questions):
        if difficulty == 1:
            nbr1 = random.randint(1,33)
            nbr2 = random.randint(1,33)
        elif difficulty == 2:
            nbr1 = random.randint(1,101)
            nbr2 = random.randint(1,101)
        else:
            nbr1 = random.randint(1,1001)
            nbr2 = random.randint(1,1001)

        domath = get_mathfunc()
        if domath == "ADD":
            answer = nbr1 + nbr2
        else:
            answer = nbr1 - nbr2

        nbr1,nbr1fmat = get_format(nbr1)
        nbr2,nbr2fmat = get_format(nbr2)
       

        question = nbr1fmat + " " + str(nbr1) 
        question = question + " " + domath + " "
        question = question + nbr2fmat + " " + str(nbr2) + " = "
        print('\n')
        print(question)

        myanswer = input("What is the answer to the question in decimal?  ")
        myanswer = int(myanswer)

        if myanswer == answer:
            print("Correct\n\n")
            correct_answers += 1
        else:
            print("Wrong!!!")
            print("Your answer was {} and the correct answer is {}.\n \n".format(myanswer, answer))

    # Game has finished, so grab the end time
    end_time = datetime.now()

    # Get the duration it took
    date_diff = end_time - start_time
    print("You completed the game in {} with {} of {} correct".format(date_diff, correct_answers, number_of_questions))

    # Update the highscores
    update_highscores(player, difficulty, correct_answers, number_of_questions, date_diff)

play_game()
