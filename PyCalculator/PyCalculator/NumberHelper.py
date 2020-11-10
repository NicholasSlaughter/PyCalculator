class NumberHelper():
    def Zero(self,currentNumber): #Fix if equals 0
        numAsStr = str(currentNumber)
        return numAsStr + "0" if str(currentNumber) != "0" else "0"
    def One(self,currentNumber):
        numAsStr = str(currentNumber)
        return numAsStr + "1" if str(currentNumber) != "0" else "1"
    def Two(self,currentNumber):
        numAsStr = str(currentNumber)
        return numAsStr + "2" if str(currentNumber) != "0" else "2"
    def Three(self,currentNumber):
        numAsStr = str(currentNumber)
        return numAsStr + "3" if str(currentNumber) != "0" else "3"
    def Four(self,currentNumber):
        numAsStr = str(currentNumber)
        return numAsStr + "4" if str(currentNumber) != "0" else "4"
    def Five(self,currentNumber):
        numAsStr = str(currentNumber)
        return numAsStr + "5" if str(currentNumber) != "0" else "5"
    def Six(self,currentNumber):
        numAsStr = str(currentNumber)
        return numAsStr + "6" if str(currentNumber) != "0" else "6"
    def Seven(self,currentNumber):
        numAsStr = str(currentNumber)
        return numAsStr + "7" if str(currentNumber) != "0" else "7"
    def Eight(self,currentNumber):
        numAsStr = str(currentNumber)
        return numAsStr + "8" if str(currentNumber) != "0" else "8"
    def Nine(self,currentNumber):
        numAsStr = str(currentNumber)
        return numAsStr + "9" if str(currentNumber) != "0" else "9"
    def Decimal(self,currentNumber):
        currentNumber = str(currentNumber) + "."
        return currentNumber

