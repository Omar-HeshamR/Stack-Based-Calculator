from Calculator import Calculator
from AdvancedCalculator import AdvancedCalculator

def main():
    while True:
        print("--- Welcome to my Stack Calculator APP ! ---")
        USER_WANT = input("What Calculator type would you like to use ? \n A) Normal Calculator \n B) Advanced Calculator \n C) Getting PostFix Expressions \n D) Exit\nEnter Letter: ")
        if USER_WANT in ("A","a","Normal","Normal Calculator", "1"):
            print("*** Currently using Normal Calculator, please add spaces after operands/operators ***")
            expression = input("Enter Expression: ")
            x = Calculator()
            x.setExpr(expression)
            print("---------------------------------------------------")
            print("--> Calculation:", x.calculate)
            print("---------------------------------------------------")
        elif USER_WANT in ("B","b","Advanced","Advanced Calculator", "2", ):
            print("*** Currently using Advanced Calculator, please follow examples below of how to use the Advanced varible Calcuator***")
            print("*** Example 1: x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return 2 * x1 + x2 ***")
            print("*** Example 2: pi = 3.1415926;r = 6 * ( 2 - ( 7 - 5 ) / 3 );return pi * r ^ 2 ***")
            expression = input("Enter Expression: ")
            x = AdvancedCalculator()
            x.setExpression(expression)
            print("---------------------------------------------------")
            print("--> Calculation:", x.calculateExpressions())
            print("---------------------------------------------------")
        elif USER_WANT in ("C","c","postfix","Getting PostFix Expressions", "3"):
            print("*** Currently Getting PostFix Expressions, please add spaces after operands/operators ***")
            expression = input("Enter Expression: ")
            x = Calculator()
            print("---------------------------------------------------")
            print("--> PostFix Form: ", x._getPostfix(expression))
            print("---------------------------------------------------")
        elif USER_WANT in ("Exit","exit","quit","Quit","D","d"):
            print("--- Bye, Hope we helped! ---")
            break
        else:
            print("ALERT: Command Not Recognized!")

if __name__ == '__main__':
    main()

main()