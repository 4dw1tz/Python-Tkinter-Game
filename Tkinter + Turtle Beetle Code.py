#Beetle Code
from random import *
from turtle import *
Beetle=Screen()
Beetle.setup(width=900, height=900)
penup()
setpos(0,0)
speed(11)
from tkinter import *
Yes = ["y", "yes", "yh"]
No = ["n", "no", "nope"]

def P2Eye2():
    setpos(180,250)
    pendown()
    fillcolor("black")
    begin_fill()
    circle(5)
    end_fill()
    penup()

def P2Eye1():
    setpos(220,250)
    pendown()
    fillcolor("black")
    begin_fill()
    circle(5)
    end_fill()
    penup()

def P1Eye2():
    setpos(-180,250)
    pendown()
    fillcolor("black")
    begin_fill()
    circle(5)
    end_fill()
    penup()

def P1Eye1():
    setpos(-220,250)
    pendown()
    fillcolor("black")
    begin_fill()
    circle(5)
    end_fill()
    penup()

def P2Ant2():
    setpos(175,265)
    width(15)
    color("blue")
    pendown()
    left(120)
    forward(25)
    right(30)
    forward(50)
    right(90)
    width(1)
    penup()

def P1Ant2():
    setpos(-225,265)
    width(15)
    color("red")
    pendown()
    left(120)
    forward(25)
    right(30)
    forward(50)
    right(90)
    width(1)
    penup()

def P2Ant1():
    setpos(225,265)
    width(15)
    color("blue")
    pendown()
    left(60)
    forward(25)
    left(30)
    forward(50)
    right(90)
    width(1)
    penup()

def P1Ant1():
    setpos(-175,265)
    width(15)
    color("red")
    pendown()
    left(60)
    forward(25)
    left(30)
    forward(50)
    right(90)
    width(1)
    penup()

def P2Leg4():
    color("blue")
    width(30)
    setpos(250, 50)
    pendown()
    left(45)
    forward(70)
    right(90)
    forward(70)
    width(1)
    left(45)
    penup()

def P1Leg4():
    color("red")
    width(30)
    setpos(-150, 50)
    pendown()
    left(45)
    forward(70)
    right(90)
    forward(70)
    width(1)
    left(45)
    penup()

def P2Leg3():
    setpos(150,50)
    color("blue")
    width(30)
    pendown()
    left(135)
    forward(70)
    left(90)
    forward(70)
    width(1)
    left(135)
    penup()

def P1Leg3():
    setpos(-250,50)
    color("red")
    width(30)
    pendown()
    left(135)
    forward(70)
    left(90)
    forward(70)
    width(1)
    left(135)
    penup()

def P2Leg1():
    setpos(150,150)
    color("blue")
    width(30)
    pendown()
    left(135)
    forward(70)
    left(90)
    forward(70)
    width(1)
    left(135)
    penup()

def P1Leg1():
    setpos(-250,150)
    color("red")
    width(30)
    pendown()
    left(135)
    forward(70)
    left(90)
    forward(70)
    width(1)
    left(135)
    penup()

def P2Leg2():
    color("blue")
    width(30)
    setpos(250, 150)
    pendown()
    left(45)
    forward(70)
    right(90)
    forward(70)
    width(1)
    left(45)
    penup()

def P1Leg2():
    color("red")
    width(30)
    setpos(-150, 150)
    pendown()
    left(45)
    forward(70)
    right(90)
    forward(70)
    width(1)
    left(45)
    penup()

def P2Tail():
    setpos(250,-50)
    color("blue")
    width(15)
    pendown()
    left(135)
    forward(70)
    left(90)
    forward(70)
    width(1)
    left(135)
    penup()

def P1Tail():
    setpos(-150,-50)
    color("red")
    width(15)
    pendown()
    left(135)
    forward(70)
    left(90)
    forward(70)
    width(1)
    left(135)
    penup()

def P2Head():
    setpos(200, 190)
    pendown()
    color("blue")
    fillcolor("light blue")
    begin_fill()
    circle(50)
    end_fill()
    penup()

def P1Head():
    setpos(-200, 190)
    pendown()
    color("red")
    fillcolor("beige")
    begin_fill()
    circle(50)
    end_fill()
    penup()

def P2Body():
    setpos(200,0)
    pendown()
    fillcolor("blue")
    begin_fill()
    circle(100)
    end_fill()
    penup()

def P1Body():
    setpos(-200,0)
    pendown()
    fillcolor("red")
    begin_fill()
    circle(100)
    end_fill()
    penup()

Turn=1
DL1=[]
DL2=[]
def Hum():
    global Comp
    Comp="yes"
    Human.config(bg="grey")
    Roller.pack()
    Header2.config(text="Press 'Roll' to start!")
    Computer.pack_forget()
def Com():
    global Comp
    Comp="no"
    Computer.config(bg="grey")
    Roller.pack()
    Header2.config(text="Press 'Roll' to start!")
    Human.pack_forget()
Human=Button(text="Play with Human", font="ArielBold 30", command=Hum)
Human.pack()
Computer=Button(text="Play with Computer", font="ArielBold 30", command=Com)
Computer.pack()

Header=Label(text="Welcome!", font="ArielBold 20", bg="beige")
Header.pack()
Header2=Label(text="Player", font="ArielBold 20", bg="beige")
Header2.pack()
Header3=Label(font="ArielBond 10", bg="beige")
Header3.pack()
def Roll():
    Human.destroy()
    Computer.destroy()
    global Dice
    global Turn
    Drawn=False
    while Drawn==False:
        if "Eyes" in DL1 and "Antennai" in DL1 and "Legs" in DL1 and 4 in DL1 and 5 in DL1 and 6 in DL1:
            End=True
            Header2.config(text="PLAYER 1 WINS!")
            break
        elif "Eyes" in DL2 and "Antennai" in DL2 and "Legs" in DL2 and 4 in DL2 and 5 in DL2 and 6 in DL2:
            End=True
            if Comp in Yes:
                Header2.config(text="PLAYER 2 WINS!")
            else:
                Header2.config(text="The Computer won.")
            break
        else:
            End=False
            Drawn=True
        if Turn%2==1:
            Turn+=1
            Header3.config(text="")
            Header.config(text="Player 1's Turn")
            Dice= randint(1,6)
            if Dice==1:
                Header2.config(text=("You got "+str(Dice)+" which is an EYE"))
                if 5 in DL1 and 6 in DL1:
                    if 1 in DL1:
                        DL1.append("Eyes")
                        P1Eye2()
                    else:
                        DL1.append(1)
                        P1Eye1()
                else:
                    Header3.config(text="You need to have the head drawn before the eyes!")
            elif Dice==2:
                Header2.config(text=("You got "+str(Dice)+" which is an ANTENA"))
                if 5 in DL1 and 6 in DL1:
                    if 2 in DL1:
                        DL1.append("Antennai")
                        P1Ant2()
                    else:
                        DL1.append(2)
                        P1Ant1()
                else:
                    Header3.config(text="You need to have the head drawn before the antennai!")
            elif Dice==3:
                Header2.config(text=("You got "+str(Dice)+" which is a LEG"))
                if 6 in DL1:
                    Count=0
                    for i in DL1:
                        if i == 3:
                            Count+=1
                    if Count==0:
                        DL1.append(3)
                        P1Leg1()
                    elif Count==1:
                        DL1.append(3)
                        P1Leg2()
                    elif Count==2:
                        DL1.append(3)
                        P1Leg3()
                    else:
                        DL1.append("Legs")
                        P1Leg4()
                else:
                    Header3.config(text="You need to have the body drawn before the legs!")
            elif Dice==4:
                Header2.config(text=("You got "+str(Dice)+" which is the TAIL"))
                if 6 in DL1:
                    DL1.append(4)
                    P1Tail()
                else:
                    Header3.config(text="You need to have the body drawn before the tail!")
            elif Dice==5:
                Header2.config(text=("You got "+str(Dice)+" which is the HEAD"))
                if 6 in DL1:
                    if 5 in DL1:
                        pass
                    else:
                        DL1.append(5)
                        P1Head()
                else:
                    Header3.config(text="You need to have the body drawn before the head!")
            else:
                Header2.config(text=("You got "+str(Dice)+" which is the BODY"))
                DL1.append(6)
                P1Body()

        #For the AI or Player 2
        else:
            Turn+=1
            Header3.config(text="")
            if Comp in Yes:
                Header.config(text="PLAYER 2's TURN!")
                Dice= randint(1,6)
            else:
                Header.config(text="The Computer is rolling")
                Dice= randint(1,6)
                sleep(1)
            if Dice==1:
                Header2.config(text=("You got "+str(Dice)+" which is an EYE"))
                if 5 in DL2 and 6 in DL2:
                    if 1 in DL2:
                        DL2.append("Eyes")
                        P2Eye2()
                    else:
                        DL2.append(1)
                        P2Eye1()
                else:
                    Header3.config(text="You need to have the head drawn before the eyes!")
            elif Dice==2:
                Header2.config(text=("You got "+str(Dice)+" which is an ANTENA"))
                if 5 in DL2 and 6 in DL2:
                    if 2 in DL2:
                        DL2.append("Antennai")
                        P2Ant2()
                    else:
                        DL2.append(2)
                        P2Ant1()
                else:
                    Header3.config(text="You need to have the head drawn before the antennai!")
            elif Dice==3:
                Header2.config(text=("You got "+str(Dice)+" which is a LEG"))
                if 6 in DL2:
                    Count=0
                    for i in DL2:
                        if i == 3:
                            Count+=1
                    if Count==0:
                        DL2.append(3)
                        P2Leg1()
                    elif Count==1:
                        DL2.append(3)
                        P2Leg2()
                    elif Count==2:
                        DL2.append(3)
                        P2Leg3()
                    else:
                        DL2.append("Legs")
                        P2Leg4()
                else:
                    Header3.config(text="You need to have the body drawn before the legs!")
            elif Dice==4:
                Header2.config(text=("You got "+str(Dice)+" which is the TAIL"))
                if 6 in DL2:
                    DL2.append(4)
                    P2Tail()
                else:
                    Header3.config(text="You need to have the body drawn before the tail!")
            elif Dice==5:
                Header2.config(text=("You got "+str(Dice)+" which is the HEAD"))
                if 6 in DL2:
                    if 5 in DL2:
                        pass
                    else:
                        DL2.append(5)
                        P2Head()
                else:
                    Header3.config(text="You need to have the body drawn before the head!")
            else:
                Header2.config(text=("You got "+str(Dice)+" which is the BODY"))
                DL2.append(6)
                P2Body()
    if End==False:
        Beetle.mainloop()
    else:
        def Out():
            exit()
        Header.config(text="GAME OVER!")
        Header3.config(text="Thanks for playing!")
        Roller.config(text="EXIT", command=Out)
Roller=Button(text="Roll / Next Turn", font="ArielBold 20", activebackground="grey", command=Roll)
Beetle.mainloop()
