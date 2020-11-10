from tkinter import *;
from OperatorHelper import OperatorHelper
from NumberHelper import NumberHelper
import keyboard

total = "0"
currentNum = "0"
runningTotal = "0"
lastOpUsed = "0"
opUsed = "0"
decimalUsed = 0

def main():
    root = Tk();
    root.title('Calculator in Python');
    root.geometry("300x300");

    numberBox = Entry(root)
    numberBox.grid(row=0,column=3)
    numberBox.insert(0,total)
    numberBox.configure(state='disabled')

    def EntryUpdater(numToEnter):
        numberBox.configure(state='normal')
        numberBox.delete(0,"end")
        numberBox.insert(0,numToEnter)
        numberBox.configure(state='disabled')
    def ClearEverything():
        global total
        global currentNum
        global decimalUsed
        total = OperatorHelper.Clear()
        currentNum = OperatorHelper.Clear()
        decimalUsed = 0
        EntryUpdater(total)
    def ClearScreen():
        global currentNum
        EntryUpdater("0")
        currentNum = "0"
        decimalUsed = 0
    def SignFlip():
        global currentNum
        currentNum = OperatorHelper.SignFlip(currentNum)
        EntryUpdater(currentNum)
    def Mod():
        OpFunc("%")
    def Division():
        OpFunc("/")
    def Multi():
        OpFunc("*")
    def Add():
        OpFunc("+")
    def Sub():
        OpFunc("-")
    def Equals():
        global total
        global currentNum
        global lastOpUsed
        global opUsed
        total = OperatorHelper.Equals(lastOpUsed, total, currentNum)
        currentNum = total
        lastOpUsed = "0"
        opUsed = "0"
        EntryUpdater(total)
    def OpFunc(operator):
        global total
        global currentNum
        global lastOpUsed
        global opUsed
        if str(opUsed) != "1" and lastOpUsed != operator:
            lastOpUsed = operator
            total = currentNum
            currentNum = "0"
            opUsed = "1"
        elif str(opUsed) == "1" and lastOpUsed != operator:
            if str(total) == "0" or str(currentNum) == "0":
                lastOpUsed = operator
            else:
                totalToAdd = OpConditional(lastOpUsed)
                lastOpUsed = operator
                total = str(totalToAdd)
                currentNum = "0"
                EntryUpdater(total)
        elif str(opUsed) == "1" and lastOpUsed == operator:
            if str(currentNum) != "0":
                lastOpUsed = operator
                totalToAdd = OpConditional(operator)
                total = str(totalToAdd)
                currentNum = "0"
                EntryUpdater(total)
    def OpConditional(operator):
        global total
        global currentNum
        totalToAdd = 0
        if operator == "+":
            totalToAdd = int(total) + int(currentNum)
        elif operator == "-":
            totalToAdd = int(total) - int(currentNum)
        elif operator == "/":
            totalToAdd = int(total) / int(currentNum)
        elif operator == "*":
            totalToAdd = int(total) * int(currentNum)
        elif operator == "%":
            totalToAdd = int(total) % int(currentNum)
        return totalToAdd

    def Zero():
        global currentNum
        currentNum = NumberHelper.Zero(currentNum)
        EntryUpdater(currentNum)
    def One():
        global currentNum
        currentNum = NumberHelper.One(currentNum)
        EntryUpdater(currentNum)
    def Two():
        global currentNum
        currentNum = NumberHelper.Two(currentNum)
        EntryUpdater(currentNum)
    def Three():
        global currentNum
        currentNum = NumberHelper.Three(currentNum)
        EntryUpdater(currentNum)
    def Four():
        global currentNum
        currentNum = NumberHelper.Four(currentNum)
        EntryUpdater(currentNum)
    def Five():
        global currentNum
        if keyboard.is_pressed("shift") == False:
            currentNum = NumberHelper.Five(currentNum)
            EntryUpdater(currentNum)
    def Six():
        global currentNum
        currentNum = NumberHelper.Six(currentNum)
        EntryUpdater(currentNum)
    def Seven():
        global currentNum
        currentNum = NumberHelper.Seven(currentNum)
        EntryUpdater(currentNum)
    def Eight():
        global currentNum
        currentNum = NumberHelper.Eight(currentNum)
        EntryUpdater(currentNum)
    def Nine():
        global currentNum
        global total
        currentNum = NumberHelper.Nine(currentNum)
        EntryUpdater(currentNum)
    def Decimal():
        global decimalUsed
        if decimalUsed == 0:
            global currentNum
            currentNum = NumberHelper.Decimal(currentNum)
            EntryUpdater(currentNum)
            decimalUsed = 1

    # Buttons With Their Commands
    clearEverythingButton = Button(root, text="CE", command= lambda: ClearEverything() , font=20).grid(row=1,column=0)
    clearScreenButton = Button(root, text="C", command= ClearScreen, font=20).grid(row=1,column=1)
    signButton = Button(root, text="+/-", command= lambda: SignFlip(), font=20).grid(row=1,column=2)
    modButton = Button(root, text="%", command= lambda: Mod(), font=20).grid(row=1,column=3)

    sevenButton = Button(root, text="7", command= lambda: Seven(), font=20).grid(row=2,column=0)
    eightButton = Button(root, text="8", command= lambda: Eight(), font=20).grid(row=2,column=1)
    nineButton = Button(root, text="9", command= lambda: Nine(), font=20).grid(row=2,column=2)
    divButton = Button(root, text="/", command= lambda: Division(), font=20).grid(row=2,column=3)

    fourButton = Button(root, text="4", command= lambda: Four(), font=20).grid(row=3,column=0)
    fiveButton = Button(root, text="5", command= lambda: Five(), font=20).grid(row=3,column=1)
    sixButton = Button(root, text="6", command= lambda: Six(), font=20).grid(row=3,column=2)
    multiButton = Button(root, text="X", command= lambda: Multi(), font=20).grid(row=3,column=3)

    oneButton = Button(root, text="1", command= lambda: One(), font=20).grid(row=4,column=0)
    twoButton = Button(root, text="2", command= lambda: Two(), font=20).grid(row=4,column=1)
    threeButton = Button(root, text="3", command= lambda: Three(), font=20).grid(row=4,column=2)
    multiButton = Button(root, text="-", command= lambda: Sub(), font=20).grid(row=4,column=3)


    zeroButton = Button(root, text="0", command= lambda: Zero(), font=20).grid(row=5,column=0)
    decimalButton = Button(root, text=".", command= lambda: Decimal(), font=20).grid(row=5,column=1)
    equalsButton = Button(root, text="=", command= lambda: Equals(), font=20).grid(row=5,column=2)
    addButton = Button(root, text="+", command= lambda: Add(), font=20).grid(row=5,column=3)

    #If a number, decimal, or operator char is pressed then call the relevant function
    keyboard.on_press_key("0", lambda _: Zero())
    keyboard.on_press_key("1", lambda _: One())
    keyboard.on_press_key("2", lambda _: Two())
    keyboard.on_press_key("3", lambda _: Three())
    keyboard.on_press_key("4", lambda _: Four())   
    keyboard.on_press_key("5", lambda _: Five())
    keyboard.on_press_key("6", lambda _: Six())
    keyboard.on_press_key("7", lambda _: Seven())
    keyboard.on_press_key("8", lambda _: Eight())
    keyboard.on_press_key("9", lambda _: Nine())
    keyboard.on_press_key(".", lambda _: Decimal())

    keyboard.on_press_key("+", lambda _: Add())
    keyboard.on_press_key("-", lambda _: Sub())
    keyboard.on_press_key("*", lambda _: Multi())
    keyboard.on_press_key("/", lambda _: Division())
    keyboard.add_hotkey("shift+5", lambda : Mod())
    keyboard.on_press_key("return", lambda _: Equals())

    root.mainloop()


if __name__ == "__main__":
    main();
