class NumberHelper():
    def Zero(currentNumber): #Fix if equals 0
        return currentNumber + "0" if str(currentNumber) != "0" else "0"
    def One(currentNumber):
        return currentNumber + "1" if str(currentNumber) != "0" else "1"
    def Two(currentNumber):
        return currentNumber + "2" if str(currentNumber) != "0" else "2"
    def Three(currentNumber):
        return currentNumber + "3" if str(currentNumber) != "0" else "3"
    def Four(currentNumber):
        return currentNumber + "4" if str(currentNumber) != "0" else "4"
    def Five(currentNumber):
        return currentNumber + "5" if str(currentNumber) != "0" else "5"
    def Six(currentNumber):
        return currentNumber + "6" if str(currentNumber) != "0" else "6"
    def Seven(currentNumber):
        return currentNumber + "7" if str(currentNumber) != "0" else "7"
    def Eight(currentNumber):
        return currentNumber + "8" if str(currentNumber) != "0" else "8"
    def Nine(currentNumber):
        return currentNumber + "9" if str(currentNumber) != "0" else "9"
    def Decimal(currentNumber):
        currentNumber = str(currentNumber) + "."
        return currentNumber

