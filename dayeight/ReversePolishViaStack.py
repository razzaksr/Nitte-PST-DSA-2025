def evaluateExpression(expression):
    stack = []
    for char in expression:
        if char in "+-*/":
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == "+": stack.append(operand1+operand2)
            elif char == "-": stack.append(operand1-operand2)
            elif char == "*": stack.append(operand1*operand2)
            elif char == "/": stack.append(int(operand1/operand2))
        else: stack.append(int(char))
    return stack[0]
print(evaluateExpression(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(evaluateExpression(["2","1","+","3","*"]))
print(evaluateExpression(["4","13","5","/","+"]))