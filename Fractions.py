# Date: December 12, 2017
# Author: Edward Tang
# Purpose: This program is designed to create a re-executable game with questions based on the validity of fraction equations, keeping score throughout.
# Input: Mouse and/or Keyboard
# Output: Screen, Console and/or GUI
# =======================================================================================================================================================

from tkinter import *
from tkinter import messagebox
import random

# Date: December 12, 2017
# Author: Edward Tang
# Purpose: This class is intended to be used to edit (through randomization or programmer/user input)
#          Fraction values, and create equation questions using them through text or a GUI interface. 
# Field Data:
#   intNumerator - Correlates to the numerator of a fraction value
#   intDenominator - Correlates to the denominator of a fraction value
# Methods:
#   calcGCD() - This method is designed to return the Greatest Common Divisor of 2 positive integers (m and n).
#   reduce() - This method is designed to set invalid Fraction object values to 0 and simplify valid Fraction object values.
#   setValue() - This method is designed to set inputted values for the Fraction object's numerator and denominator
#                (ensuring they are integers), then validate and simplify the Fraction object by calling reduce().
#   randomize() - This method is designed to set random values for the Fraction object's numerator and denominator,
#                 then validate and simplify the Fraction object by calling reduce().
#   __str__() - This method is designed to convert the Fraction object into mixed number form (if possible) and
#               return a string to represent the Fraction object's value.
#   calcInverse() - This method is designed to return the Fraction object with its numerator and denominator swapped.
#   __eq__() - This method is designed to return True or False based on whether or not the Fraction object and a second are equal.
#   __add__() - This method is designed to return the sum of two fractions, ensuring they are being added with a common denominator.
#   __sub__() - This method is designed to return the difference of two fractions, ensuring they are being subtracted with a common denominator.
#   __mul__() - This method is designed to return the product of two fractions.
#   __truediv__() - This method is designed to return the quotient of two fractions.
# ==============================================================================================================================================

class Fraction:
    def __init__(self,numerator=0,denominator=1):
        self.intNumerator = numerator
        self.intDenominator = denominator
        self.reduce()
        
    # Date: October 11, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the Greatest Common Divisor of 2 positive integers (m and n).
    # Input: Two positive integers (m and n)
    # Output: The GCD of m and n
    # ===========================================================================================================
    
    def calcGCD(self,m=1,n=1):
        t = m % n
        while not t == 0:
            m = n
            n = t
            t = m % n
        return n
    
    # Date: December 13, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to set invalid Fraction object values to 0 and simplify valid Fraction object values.                    
    # Input: N/A
    # Output: N/A
    # =======================================================================================================================
    
    def reduce(self):
        if self.intDenominator == 0:
            self.intNumerator = 0
            self.intDenominator = 1
        else:
            divisor = self.calcGCD(self.intNumerator,self.intDenominator)
            self.intNumerator = int(self.intNumerator / divisor)
            self.intDenominator = int(self.intDenominator / divisor)
            if self.intDenominator < 0:
                self.intDenominator = self.intDenominator * -1
                if self.intNumerator > 0:
                    self.intNumerator = self.intNumerator * -1
                else:
                    self.intDenominator = abs(self.intDenominator)
                    self.intNumerator = abs(self.intNumerator)
                    
    # Date: December 13, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to set inputted values for the Fraction object's numerator and denominator
    #          (ensuring they are integers), then validate and simplify the Fraction object by calling reduce().
    # Input: Two numbers
    # Output: N/A
    # =============================================================================================================
    
    def setValue(self,numerator,denominator):
        numerator = numerator - numerator%1
        denominator = denominator - denominator%1
        self.intNumerator = numerator
        self.intDenominator = denominator
        self.reduce()
        
    # Date: December 13, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to set random values for the Fraction object's numerator and denominator,
    #          then validate and simplify the Fraction object by calling reduce().
    # Input: [INT] A number to set as the range for possible positive and negative numerator or denominator values
    # Output: N/A
    # Dependencies: [Class] random
    # =============================================================================================================
    
    def randomize(self,maxInt=10):
        self.intNumerator = random.randint(maxInt*-1,maxInt)
        self.intDenominator = random.randint(maxInt*-1,maxInt)
        self.reduce()
        
    # Date: December 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to convert the Fraction object into mixed number form (if possible) and
    #          return a string to represent the Fraction object's value.
    # Input: N/A
    # Output: [STRING] The Fraction object
    # =============================================================================================================
    
    def __str__(self):
        if self.intNumerator < 0:
            string = str(self.intNumerator) + "/" + str(self.intDenominator)
        elif self.intNumerator == 0:
            string = "0"
        else:
            string = str(self.intNumerator) + "/" + str(self.intDenominator)
        wholeNumber = abs(self.intNumerator) // self.intDenominator
        numeratorBackup = self.intNumerator
        if wholeNumber > 0:
            if self.intNumerator < 0:
                wholeNumber = wholeNumber * -1
                self.intNumerator = self.intNumerator * -1
            self.intNumerator = self.intNumerator - self.intDenominator * abs(wholeNumber)
            if wholeNumber < 0 and self.intNumerator > 0:
                string = str(wholeNumber) + " " + str(self.intNumerator) + "/" + str(self.intDenominator)
            elif wholeNumber < 0 or self.intNumerator == 0:
                string = str(wholeNumber)
            else:
                string = str(wholeNumber) + " " + str(self.intNumerator) + "/" + str(self.intDenominator)
            self.intNumerator = numeratorBackup
        return string
    
    # Date: December 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the Fraction object with its numerator and denominator swapped.
    # Input: N/A
    # Output: A Fraction object
    # =============================================================================================================
    
    def calcInverse(self):
        return Fraction(self.intDenominator,self.intNumerator)
    
    # Date: December 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return True or False based on whether or not the Fraction object and a second are equal.
    # Input: The name of a second Fraction object
    # Output: A Fraction object
    # ==============================================================================================================================
    
    def __eq__(self,secondObject):
        isEqual = False
        if self.intNumerator == secondObject.intNumerator and \
           self.intDenominator == secondObject.intDenominator:
            isEqual = True
        return isEqual
    
    # Date: December 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the sum of two fractions, ensuring they are being added with a common denominator.
    # Input: The name of a second Fraction object
    # Output: A Fraction object
    # ===============================================================================================================================
    
    def __add__(self,secondObject):
        fractionSum = Fraction()
        if self.intDenominator != secondObject.intDenominator:
            fractionSum.setValue(self.intNumerator * secondObject.intDenominator + secondObject.intNumerator * self.intDenominator,self.intDenominator * secondObject.intDenominator)
        else:
            fractionSum.setValue(self.intNumerator + secondObject.intNumerator,self.intDenominator)
        return fractionSum
    
    # Date: December 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the difference of two fractions, ensuring they are being subtracted with a common denominator.
    # Input: The name of a second Fraction object
    # Output: A Fraction object
    # ===========================================================================================================================================
    
    def __sub__(self,secondObject):
        fractionDiff = Fraction()
        if self.intDenominator != secondObject.intDenominator:
            fractionDiff.setValue(self.intNumerator * secondObject.intDenominator - secondObject.intNumerator * self.intDenominator,self.intDenominator * secondObject.intDenominator)
        else:
            fractionDiff.setValue(self.intNumerator - secondObject.intNumerator,self.intDenominator)
        return fractionDiff
    
    # Date: December 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the product of two fractions.
    # Input: The name of a second Fraction object
    # Output: A Fraction object
    # ==========================================================================
    
    def __mul__(self,secondObject):
        return Fraction(self.intNumerator*secondObject.intNumerator,self.intDenominator*secondObject.intDenominator)
    
    # Date: December 14, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the quotient of two fractions.
    # Input: The name of a second Fraction object
    # Output: A Fraction object
    # ===========================================================================
    
    def __truediv__(self,secondObject):
        return self*secondObject.calcInverse()

# Date: December 16, 2017
# Author: Edward Tang
# Purpose: This subprogram is designed to create a random equation, ask the user whether the equation is right or not and score the user based on their response.
# Input: Keyboard, [INT] A score number
# Output: Screen/Console, [INT] A score, calculated based on the user's response to the equation question
# ================================================================================================================================================================

def setup(score):
    operator = random.choice(["+","-","×","÷"])
    operand1.randomize()
    operand2.randomize()
    if operator == "+":
        answer = operand1+operand2
    elif operator == "-":
        answer = operand1-operand2
    elif operator == "×":
        answer = operand1*operand2
    elif operator == "÷":
        answer = operand1/operand2
    guess = random.choice([answer,answer.calcInverse()])
    print(operand1,operator,operand2,"=",guess,"\n")
    choice = input("Enter 'right' or 'wrong' based on the validity of this equation: ")
    while choice != "right" and choice != "wrong":
        print("ERROR: You must enter either 'right' or 'wrong'!")
        choice = input("Enter 'right' or 'wrong' based on the validity of this equation: ")
    print()
    if (choice == "right" and answer == guess) or (choice == "wrong" and answer != guess):
        score = score + 1
        print("You're right! The real answer was "+str(answer)+". Your current score is " + str(score)+".")
    else:
        print("You're wrong! The real answer was "+str(answer)+". Your current score is " + str(score)+".")
    return score

# Date: December 16, 2017
# Author: Edward Tang
# Purpose: This subprogram is designed to run a re-executable game that asks the user about the validity of fraction
#          equations in an infinite or set number of questions. Score is kept throughout, and the game ends after a
#          set amount of questions (assuming the user did not select the inifite "marathon" mode or when the user
#          chooses to stop.
# Input: Keyboard
# Output: Screen/Console
# ====================================================================================================================

def mainConsole():
    score = 0
    count = 0
    operator = ""   
    restartFull = ""
    while restartFull != "stop":
        restart = ""
        playMethod = input("Enter any number of questions to answer, enter 'marathon' to receive an infinite amount of questions or enter 'stop' to stop: ")
        while not playMethod.isdigit() and playMethod != "marathon" and playMethod != "stop":
            print("ERROR: Invalid entry")
            playMethod = input("Enter any number of questions to answer, enter 'marathon' to receive an infinite amount of questions or enter 'stop' to stop: ")
        if playMethod != "stop":
            print()
            print("==========================================================================================================\n")
            if playMethod.isdigit():
                count = int(playMethod)
                questionNum = count
                while restart != "stop" or count > 0:
                    print("Score:",score,"/",questionNum,"\n")
                    score = setup(score)
                    count = count - 1
                    if count > 0:
                        restart = input("Enter anything to get the next equation, or enter 'stop' to stop: ")
                        if restart == "stop":
                            restartFull = input("There are no more questions! Enter anything to answer more or to play 'marathon', or enter 'stop' to stop: ")
                    else:
                        restart = "stop"
                        restartFull = input("There are no more questions! Enter anything to answer more or to play 'marathon', or enter 'stop' to stop: ")
                    print()
                    print("==========================================================================================================\n")
            elif playMethod == "marathon":
                while restart != "stop":
                    print("Score:",score,"\n")
                    score = setup(score)
                    restart = input("Enter anything to get the next equation, or enter 'stop' to stop: ")
                    print()
                    print("==========================================================================================================\n")
        else:
            restartFull = "stop"
            
# Date: December 20, 2017
# Author: Edward Tang
# Purpose: This subprogram is designed to, assuming its "proceed" variable is True, reset the score and round global
#          variables, place widgets that are part of the fraction game's selection screen and hide widgets that are
#          part of the fraction gameplay itself.
# Input: [BOOLEAN] "Proceed" to be used with an "OK or Cancel" window to allow a user choice in executing the
#        subprogram.
# Output: Screen/Console
# References: [Tk() Window] main, [Buttons] manual,marathon,rightButton,wrongButton, [Scale] manualSlider,
#             [Labels] currentRoundText,equationText,scoreText,previousAnswer [Global Variables] roundScore, currentRound
# Dependencies: [Class] tkinter
# =========================================================================================================================

def returnToStart(proceed=True):
    if proceed == True:
        roundScore.set(0)
        currentRound.set(0)
        roundCount.set(25)
        marathon.place(x=22.5,y=20)
        manual.place(x=22.5,y=60)
        manualSlider.place(x=22.5,y=100)
        manualSlider.config(variable=roundCount)
        currentRoundText.place_forget()
        equationText.place_forget()
        scoreText.place_forget()
        rightButton.place_forget()
        wrongButton.place_forget()
        previousAnswer.place_forget()
    main.unbind("<r>")
    main.unbind("<w>")
    main.unbind("<BackSpace>")
    
# Date: December 20, 2017
# Author: Edward Tang
# Purpose: This subprogram is designed to create a new round of the fraction game by randomizing the equation.
#          It also returns the program to the game's selection screen if the user has opted to receive a set amount
#          of questions and that set amount has been reached.
# Input: N/A
# Output: Screen/Console
# References: [Global Variables] gameMode, currentRound, roundCount, strcurrentRound, strScore, strEquation
#             [Objects] operand1, operand1, answer, guess Fraction objects
# Dependencies: [Classes] tkinter,tkinter messagebox,random
# ==================================================================================================================

def setupGUI():
    if gameMode.get() == "marathon":
        roundCount.set(currentRound.get())
    strScore.set(("Score:",roundScore.get(),"/",roundCount.get()))
    if gameMode.get() == "manual" and currentRound.get() == roundCount.get():
        messagebox.showinfo(title="Game Over!",message=("There are no more questions to answer! You scored a total of "+str(roundScore.get())+" out of "+str(roundCount.get())+" questions."))
        returnToStart(True)
    else:
        currentRound.set(currentRound.get() + 1)
        strCurrentRound.set(("Round",currentRound.get()))
        operator = random.choice(["+","-","×","÷"])
        operand1.randomize()
        operand2.randomize()
        if operator == "+":
            answerValues = operand1+operand2
        elif operator == "-":
            answerValues = operand1-operand2
        elif operator == "×":
            answerValues = operand1*operand2
        elif operator == "÷":
            answerValues = operand1/operand2
        answer.setValue(answerValues.intNumerator,answerValues.intDenominator)
        guessValues = random.choice([answer,answer.calcInverse()])
        guess.setValue(guessValues.intNumerator,guessValues.intDenominator)
        strEquation.set((str(operand1)+"  "+str(operator)+"  "+str(operand2)+"  =  "+str(guess)))
        
# Date: December 20, 2017
# Author: Edward Tang
# Purpose: This subprogram is designed to hide the fraction game's selection screen and place the widgets needed
#          for the displaying of questions. It also calls setupGUI() to initiate the questions. 
# Input: N/A
# Output: Screen/Console
# References: [Tk() Window] main, [Global Variable] gameMode, [Buttons] marathon,manual,rightButton,wrongButton,
#             [Scale] manualSlider, [Labels] currentRoundText,equationText,scoreText,previousAnswer
# Dependencies: [Classes] tkinter,tkinter messagebox, [Subprograms] checkAnswer(),returnToStart(),setupGUI()
# =======================================================================================================================

def startGame():
    marathon.place_forget()
    manual.place_forget()
    manualSlider.place_forget()
    if gameMode.get() == "marathon":
        manualSlider.config(variable=answer)
    currentRoundText.place(x=60,y=10)
    equationText.place(x=20,y=40)
    scoreText.place(x=50,y=70)
    rightButton.place(x=15,y=100)
    wrongButton.place(x=120,y=100)
    previousAnswer.config(text="")
    previousAnswer.place(x=55,y=135)
    main.bind("<r>",lambda _:checkAnswer("right"))
    main.bind("<w>",lambda _:checkAnswer("wrong"))
    main.bind("<BackSpace>",lambda _:returnToStart(messagebox.askokcancel(title="Restart",message="Are you sure you want to restart? You will lose your current progress.")))
    setupGUI()
    
# Date: December 20, 2017
# Author: Edward Tang
# Purpose: This subprogram is designed to increase the user's score if they were correct in determining the
#          validity of a previous Fraction object equation. It also calls setupGUI() to initiate a new question. 
# Input: [STRING] The selected option from the user (right or wrong)
# Output: Screen/Console
# References: [Global Variable] roundScore, [Objects] answer,guess, [Label] previousAnswer
# Dependencies: [Class] tkinter, [Subprogram] setupGUI()
# ==================================================================================================================

def checkAnswer(selection="right"):
    if selection == "right":
        if answer == guess:
            roundScore.set(roundScore.get() + 1)
            previousAnswer.config(text="Previous Answer: ✓",fg="chartreuse3")
        else:
            previousAnswer.config(text="Previous Answer: ✗",fg="tomato2")
    else:
        if not answer == guess:
            roundScore.set(roundScore.get() + 1)
            previousAnswer.config(text="Previous Answer: ✓",fg="chartreuse3")
        else:
            previousAnswer.config(text="Previous Answer: ✗",fg="tomato2")
    setupGUI()

# Date: November 17, 2017
# Author: Edward Tang
# Purpose: This program is designed to create a window with a header label, five lines of smaller labels and a close button.
# Input: [STRING] Title name, six string values, desired window colour, desired window Text colour and [INTEGER] the width and height of the window
# Output: Screen
# References: [Tk() Window] main
# Dependencies: [Class] tkinter
# ==================================================================================================================================================

def window6Labels(title,text1,text2,text3,text4,text5,text6,width,height,textBg="#fcfcfc",textColour="black"):
    window = Toplevel(main)
    window.title(title)
    window.resizable(False,False)
    window.config(width=width,height=height,bg=textBg)
    ws = main.winfo_screenwidth()
    hs = main.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.grab_set()
    Label(window,text=text1,font=("Arial",12,"bold"),bg=textBg,fg=textColour).place(x=5,y=5)
    Label(window,text=text2,font=("Arial",10,"normal"),bg=textBg,fg=textColour).place(x=5,y=30)
    Label(window,text=text3,font=("Arial",10,"normal"),bg=textBg,fg=textColour).place(x=5,y=55)   
    Label(window,text=text4,font=("Arial",10,"normal"),bg=textBg,fg=textColour).place(x=5,y=80)
    Label(window,text=text5,font=("Arial",10,"normal"),bg=textBg,fg=textColour).place(x=5,y=105)
    Label(window,text=text6,font=("Arial",10,"normal"),bg=textBg,fg=textColour).place(x=5,y=130)
    Button(window,text="Close",font=("Arial",10,"bold"),relief=FLAT,cursor="hand2",command=lambda:window.destroy(),bg="tomato2").place(x=width-60,y=height-40)

# Date: November 17, 2017
# Author: Edward Tang
# Purpose: This program is designed to create a window to display a text box and 
# Input: [STRING] Title name, text, desired window colour, desired window text colour and [INTEGER] the width and height of the window 
# Output: Screen
# References: [Tk() Window] main
# Dependencies: [Class] tkinter
# =================================================================================================================================

def windowOfText(title="INSERT TITLE HERE",text="INSERT TEXT HERE",width=500,height=500,textBg="#fcfcfc",textColour="black"):
    window = Toplevel(main)
    window.title(title)
    window.resizable(False,False)
    window.config(width=width,height=height,bg="#fcfcfc")
    ws = main.winfo_screenwidth()
    hs = main.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.grab_set()
    textBox = Text(window,font=("Arial",10,"normal"),width=width,height=height,bd=2,relief=GROOVE,bg=textBg,fg=textColour)
    textBox.place(x=0,y=0)
    textBox.insert(END,text)
    textBox.config(state=DISABLED)
    Button(window,text="Close",font=("Arial",10,"bold"),relief=FLAT,cursor="hand2",command=lambda:window.destroy(),bg="tomato2").place(x=width-60,y=height-40)

# MAIN CODE

main = Tk()
main.title("Fraction Test")

operand1 = Fraction()
operand2 = Fraction()
answer = Fraction()
guess = Fraction()

strEquation = StringVar()

roundCount = IntVar()
roundCount.set(25)

roundScore = IntVar()
roundScore.set(0)

currentRound = IntVar()
currentRound.set(0)

strCurrentRound = StringVar()
strCurrentRound.set("0")

strScore = StringVar()

gameMode = StringVar()
gameMode.set("manual")

answerState = StringVar()

currentRoundText = Label(main,textvariable=(strCurrentRound),font=("Arial",12,"bold"),bg="#fcfcfc",width=10)
equationText = Label(main,textvariable=strEquation,font=("Arial",12,"bold"),bg="#fcfcfc",width=18)
scoreText = Label(main,textvariable=strScore,font=("Arial",12,"normal"),bg="#fcfcfc",width=13)

rightButton = Button(main,command=lambda:checkAnswer("right"),text="Right (R)",bg="chartreuse3",relief=FLAT,font=("Arial",12,"bold"),width=8)
wrongButton = Button(main,command=lambda:checkAnswer("wrong"),text="Wrong (W)",bg="tomato2",relief=FLAT,font=("Arial",12,"bold"),width=8)

previousAnswer = Label(main,font=("Arial",10,"normal"),bg="#fcfcfc")

marathon = Button(main,text="Marathon (infinite)",bg="orange",width=17,relief=FLAT,font=("Arial",12,"bold"),command=lambda:(gameMode.set("marathon"),startGame()))
marathon.place(x=22.5,y=20)
manual = Button(main,text="Manual (adjust below)",bg="dark orange",relief=FLAT,font=("Arial",12,"bold"),command=lambda:(gameMode.set("manual"),startGame()))
manual.place(x=22.5,y=60)
manualSlider = Scale(main,variable=roundCount,font=("Arial",11,"bold"),orient="horizontal",cursor="hand2",bg="#30221b",fg="#fcfcfc",troughcolor="orange",length=177,sliderlength=30,from_=1,to=50)
manualSlider.place(x=22.5,y=100)

menu = Menu(main)

#"File" Menu
fileMenu = Menu(menu,tearoff=0)
fileMenu.add_command(label="Restart (BACKSPACE)",command=lambda:returnToStart(messagebox.askokcancel(title="Restart",message="Are you sure you want to restart? You will lose your current progress.")))
fileMenu.add_command(label="Exit (F4)",command=lambda:main.destroy())
menu.add_cascade(label="File", menu=fileMenu)

#"Help" Menu
helpMenu = Menu(menu,tearoff=0)
helpMenu.add_command(label="About",command=lambda:window6Labels("About","Fraction Game","Version: 2.0","Author: Edward Tang","E-Mail: 335433173@gapps.yrdsb.ca","","",300,110))
helpMenu.add_command(label="Hotkeys",command=lambda:windowOfText("Hotkeys","\n R = Right\n\n W = Wrong\n\n BACKSPACE = Restart\n\n F4 = Exit Program",250,150))
menu.add_cascade(label="Help", menu=helpMenu)

main.config(width=230,height=160,menu=menu,bg="#fcfcfc")

main.bind("<F4>",lambda _:main.destroy())

mainloop()
