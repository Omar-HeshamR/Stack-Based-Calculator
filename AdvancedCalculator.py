from Calculator import Calculator

class AdvancedCalculator:

    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        if isinstance(word, str) != True or len(word) == 0:
            return False
        elif word.isalnum() != True:
            return False
        elif word[0].isalpha() != True:
            return False
        else:
            return True

    def _replaceVariables(self, expr):
        output = expr.split()
        for var in range(0,len(output)):
            if self._isVariable(output[var]):
                if output[var] in self.states:
                    output[var] = str(self.states[output[var]])
                else:
                    return None
        return " ".join(output)

    def calculateExpressions(self):
        self.states = {}
        calcObj = Calculator()     # method must use calcObj to compute each expression
        saving_dict = {}
        expression = self.expressions.strip()
        expression = expression.split(";")
        for expr in expression[:-1]:
            unknown = expr.split("=")[0]
            unknown = unknown.strip()
            unkown_ans = self._replaceVariables(expr.split("=")[1])
            calcObj.setExpr(unkown_ans)
            if calcObj.calculate != None:
                self.states[unknown] = calcObj.calculate
            else:
                self.states ={}
                return None
            saving_dict[expr] = self.states.copy()
        rplc_w_calc = self._replaceVariables(expression[-1].split('return')[1])
        calcObj.setExpr(rplc_w_calc)
        saving_dict['_return_'] = float(calcObj.calculate)
        for value_dic in saving_dict.values():
            if isinstance(value_dic, float) == True:
                break
            for key in value_dic.keys():
               value_dic[key] = float(value_dic.get(key))
        return saving_dict