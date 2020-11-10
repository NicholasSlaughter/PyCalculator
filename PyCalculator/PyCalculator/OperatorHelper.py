import math
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
    def Clear():
        return 0;
    def SignFlip(numberToFlip):
        return float(numberToFlip) * -1