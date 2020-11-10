
class OperatorHelper():
    def Addition():
        return "+";
    def Subtraction():
        return "-";
    def Multiply():
        return "*";
    def Division():
        return "/";
    def Modulo():
        return "%";
    def Equals(lastOpUsed,currentTotal, currentNum):
        if str(lastOpUsed) == 0:
            return currentTotal
        elif str(lastOpUsed) == "+":
            output = int(currentTotal)+int(currentNum)
            return output
        elif str(lastOpUsed) == "-":
            output = int(currentTotal)-int(currentNum)
            return output
        elif str(lastOpUsed) == "/":
            output = int(currentTotal)/int(currentNum)
            return output
        elif str(lastOpUsed) == "*":
            output = int(currentTotal)*int(currentNum)
            return output
        elif str(lastOpUsed) == "%":
            output = int(currentTotal)%int(currentNum)
            return output
        return currentTotal;
    def Clear():
        return 0;
    def SignFlip(numberToFlip):
        return int(numberToFlip) * -1