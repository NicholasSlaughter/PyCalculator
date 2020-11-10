import math
class OperatorHelper():
    def Addition(self):
        return "+";
    def Subtraction(self):
        return "-";
    def Multiply(self):
        return "*";
    def Division(self):
        return "/";
    def Modulo(self):
        return "%";
    def Equals(self,lastOpUsed,currentTotal, currentNum):
        totalAsFloat = float(currentTotal)
        numAsFloat =  float(currentNum)
        if str(lastOpUsed) == 0:
            return currentTotal
        elif str(lastOpUsed) == "+":
            output = totalAsFloat+numAsFloat
            outputFloor = math.floor(output)
            if output - outputFloor != 0:
                formattedOutput = "{:.2f}".format(output)
                return formattedOutput
            else:
                return int(output)
        elif str(lastOpUsed) == "-":
            output = totalAsFloat-numAsFloat
            outputFloor = math.floor(output)
            if output - outputFloor != 0:
                formattedOutput = "{:.2f}".format(output)
                return formattedOutput
            else:
                return int(output)
        elif str(lastOpUsed) == "/":
            output = totalAsFloat/numAsFloat
            outputFloor = math.floor(output)
            if output - outputFloor != 0:
                formattedOutput = "{:.2f}".format(output)
                return formattedOutput
            else:
                return int(output)
        elif str(lastOpUsed) == "*":
            output = totalAsFloat*numAsFloat
            outputFloor = math.floor(output)
            if output - outputFloor != 0:
                formattedOutput = "{:.2f}".format(output)
                return formattedOutput
            else:
                return int(output)
        elif str(lastOpUsed) == "%":
            output = totalAsFloat%numAsFloat
            outputFloor = math.floor(output)
            if output - outputFloor != 0:
                formattedOutput = "{:.2f}".format(output)
                return formattedOutput
            else:
                return int(output)
        return currentTotal;
    def Clear(self):
        return 0;
    def SignFlip(self,numberToFlip):
        return float(numberToFlip) * -1