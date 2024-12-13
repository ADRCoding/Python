from cmu_graphics import *
import random as rand
import time

easterEgg = Label(0, -400, -400)
easterEggActivated = Label(False, -400, -400)
#Intro
app.background = "black"
time.sleep(1)
Label("Click on the target to increase your score", 200, 150, fill = "white")
time.sleep(2)
Label("If you click off the target, your incorrect value will increase", 200, 200, fill = "white")
time.sleep(2)
lives = app.getTextInput("How many lives do you want? ")
startingLives = lives
time.sleep(1)
Label("You only have room for " + lives + " error(s)", 200, 250, fill = "white")
time.sleep(2)
Rect(0, 0, 400, 400, fill = "lightCyan")

#color choices
colorChoices = ["white", "red", "yellow", "blue", "purple", "crimson", "navy", "grey"]

#Constant variables
target = Circle(rand.randint(20, 380), rand.randint(100, 380), 10, fill = rand.choice(colorChoices))
score = Label(0, 200, 60, size = 30, fill = "green")
incorrect = Label(0, 25, 60, size = 30, fill = "red")
title = Label("MouseClickyGame", 200, 25, size = 25)
Line(0, 80, 400, 80, lineWidth = 10)
Rect(0, 0, 400, 45, fill = None, border = "black")


#End Screen
def gameEnd():
    if easterEgg.value < 6:
        if target.radius == 0.25:
            Rect(0, 0, 400, 400, fill = "green")
            Label("You Beat The Game!", 200, 50, size = 40)
        else:
            Rect(0, 0, 400, 400, fill = "red")
            Label("Too many errors!", 200, 50, size = 50)
        Label("Score: " + str(score.value), 200, 150, size = 75)
        Label("Incorrect: " + str(incorrect.value), 200, 250, size = 60)
        time.sleep(5)
        Rect(0, 0, 400, 400)
        #End Credits
        credits = Label("Credits:", 200, 10, fill = "white")
        arush = Label("Arush Dinesh Raja", 200, 25, fill = "white")
        while arush.centerY <= 410:
            time.sleep(0.01)
            arush.centerY += 5
        credits.value = "Thanks for playing!"
        if easterEggActivated.value == False:
            Label("(Tap again to view stats)", 200, 350, fill = "red")
        credits.size = 40
        credits.centerY = 200
        pass

#Drawing the target
def drawCirc():
    target.centerX = rand.randint(20, 380)
    target.centerY = rand.randint(100, 380)
    target.fill = rand.choice(colorChoices)
    pass

#Moves the target arush shrinks it
def onMousePress(x, y):
    if x <= 6 and y <= 6:
        easterEgg.value += 1
        if easterEgg.value >= 6:
            easterEggBoss()
    if target.hits(x, y) == True and (target.fill == "crimson" or target.fill == "navy" or target.fill == "blue" or target.fill == "white" or target.fill == "yellow"):
        if score.value < 40 or incorrect.value < int(lives):
            score.value +=1
            drawCirc()
    elif target.hits(x, y) == False and (target.fill == "purple" or target.fill == "red" or target.fill == "grey"):
        if score.value < 40 or incorrect.value < int(lives):
            score.value +=1
            drawCirc()        
    elif target.hits(x, y) == True and (target.fill == "purple" or target.fill == "red" or target.fill == "grey"):
        if incorrect.value < int(lives):
            incorrect.value += 1
            target.radius += 0.25
            drawCirc()
    elif target.hits(x, y) == False and (target.fill == "crimson" or target.fill == "navy" or target.fill == "blue" or target.fill == "white" or target.fill == "yellow"):
        if incorrect.value < int(lives):
            incorrect.value += 1
            target.radius += 0.25
            drawCirc()    
    if target.radius > 0.25 or incorrect.value != int(lives):
        target.radius -= 0.25
    if incorrect.value == int(lives):
        gameEnd()
    if target.radius == 0.25:
        gameEnd()
    pass

        
def easterEggBoss():
    Rect(0, 0, 400, 400)
    guessTheNum = rand.randint(0, 10000)
    answer = Label("", 200, 200, fill = "white")
    numGuesses = Label(0, -400, -400)
    while True:
        guess = app.getTextInput("Guess a number between 0 and 10000")
        while int(guess) > 10000 or int(guess) < 0:
            answer.value = ("Guess has to be between 0 and 10000")
            time.sleep(1)
            guess = app.getTextInput("Guess a number between 0 and 10000")
        numGuesses.value += 1
        if int(guess) == guessTheNum:
            answer.value = "You were right"
            time.sleep(1)
            answer.value = "The number was " + str(guessTheNum)
            time.sleep(1)
            answer.value = "It took you " + str(numGuesses.value) + " guesses!"
            time.sleep(2)
            answer.value = "Thanks for playing!"
            time.sleep(2)
            easterEgg.value = 0
            easterEggActivated.value = True
            gameEnd()
            break
        elif int(guess) > guessTheNum:
            answer.value = "You need to guess lower"
        else:
            answer.value = "You need to guess higher"
        time.sleep(1)
        

cmu_graphics.run()


