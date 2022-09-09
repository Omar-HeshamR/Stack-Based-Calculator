from StackClass import Stack
from NodeClass import Node

class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr = new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        try:
            txt = float(txt)
        except:
            return False
        return True

    def _getPostfix(self, txt):
        for i in txt: # check for invalid input
            if i == "@" or i == "#" or i == "!" or i == "$" or i == "&" or i == "`" or i == "~" or i == ">":
                return None
            if i == ";" or i == "<" or i == "|" or i == "%" or i.isalpha() == True:
                return None
        operator_counter = 0
        number_counter = 0
        for i in txt.split(): # check for correct number of operations
            if i == "*" or i == "^" or i == "+" or i == "-" or i =="/":
                operator_counter += 1
            if self._isNumber(i) == True:
                number_counter += 1
        if (number_counter) <= (operator_counter):
            return None
        infix_chceck = txt.split()
        for i in range(len(infix_chceck)-1): # to check for consecutive numbers
            if self._isNumber(infix_chceck[i]) == True and self._isNumber(infix_chceck[i+1]) == True:
                return None
        postfixStack = Stack()
        postfix = ""
        infix = txt.split()
        dict_of_power = {"^":3, "*":2, "/":2,"+":1,"-":1, "(":0,")":4}
        for ch in infix:
            if ch == "*" or ch == "^" or ch == "(" or ch == ")" or ch == "+" or ch == "-" or ch =="/":
                if postfixStack.isEmpty() == True or ch == "(":
                    postfixStack.push(ch)
                elif ch == ")":
                    temp = postfixStack.top
                    lst = []
                    while isinstance(temp, Node) == True and temp.value != "(":
                        lst.append(temp.value)
                        temp = temp.next
                        postfixStack.pop()
                    postfixStack.pop()
                    for i in range(0, len(lst)):
                        postfix = postfix + lst[i] + " "
                else:
                    op_power = dict_of_power[ch]
                    if op_power > dict_of_power[postfixStack.peek()] or (ch == '^' and postfixStack.peek() == "^"): # check if stack is empty
                        postfixStack.push(ch)
                    elif op_power <= dict_of_power[postfixStack.peek()]: # check how powerfull operator is
                        temp = postfixStack.top
                        lst = []
                        while isinstance(temp, Node) == True and dict_of_power[temp.value] >= op_power:
                            lst.append(temp.value)
                            temp = temp.next
                            postfixStack.pop()
                        postfixStack.push(ch)
                        for i in range(0,len(lst)):
                            postfix = postfix + lst[i] + " "
            else:
                postfix = postfix + str(float(ch)) + " "
        if postfixStack.top != None:
            temp = postfixStack.top
            while temp != None:
                postfix = postfix + temp.value + " "
                temp = temp.next
        postfix_check = postfix.split()
        for i in postfix_check:
            if i =='(' or i == ')':
                return None
        return postfix

    @property
    def calculate(self):
        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None
        calcStack = Stack()   # method must use calcStack to compute the  expression
        postfix = self._getPostfix(self.__expr)
        if postfix == None:
            return None
        postfix = postfix.split()
        for item in postfix:
            if item != "+" and item != "-" and item != "*" and item != "/" and item != "^": # item is a number
                calcStack.push(item)
            else:
                a = float(calcStack.top.value)
                b = float(calcStack.top.next.value)
                if item == "+":
                    s = b + a
                elif item == "-":
                    s = b - a
                elif item == "*":
                    s = b * a
                elif item == "/":
                    s = b / a
                else:
                    s = b ** a
                calcStack.pop()
                calcStack.pop()
                calcStack.push(s)
        return calcStack.peek()