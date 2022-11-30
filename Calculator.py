import re

class Calculator:
    
    #initial the operator when start calling class
    def __init__(self) -> None:               
        self.OPERATORS = {    '+',    '-',    '*',    '/',    '^'}

    #function checking  can string change into float : yes -> true No -> false
    def isfloat(self,element: any) -> bool:
        #If you expect None to be passed:
        if element is None: 
            return False
        try:
            float(element)
            return True
        except ValueError:
            return False

    #function calculate things in brackets without any variable
    def nonvar_without_brackets(self,expr) -> float:
        
        #split string in to list "expression list"
        exprlist = expr.split(" ")

        #stack keep value to calculate result    
        result_stack = []
        #print(exprlist)   

        #initial for loop
        i = 1
        num = 0
        result_stack.append(float(exprlist[0]))

        #loop to append into result_stack 
        while i < len(exprlist):
            c = exprlist[i]
            #print(c)
            #print(result_stack)        

            #check next index can cast into float or not : yes -> assign to num 
            if i + 1 < len(exprlist):
                if self.isfloat(exprlist[i+1]):            
                    num = float(exprlist[i+1])

            #check c in OPERATORS dict or not 
            if c in self.OPERATORS:

                #if it is + or - add in result_stack
                if c == '+':
                    result_stack.append(num)                  
                elif c == '-':
                    result_stack.append(-1*num)

                #if it is * or / or ^ calculate before add in stack 
                elif c == '*':
                    result_stack[-1] = (lambda x,y : x * y)(result_stack[-1],num)                    
                    #result_stack[-1] = result_stack[-1]*num
                elif c == '/':
                    result_stack[-1] = (lambda x,y : x / y)(result_stack[-1],num)                    
                    #result_stack[-1] = result_stack[-1]/num
                elif c == '^':
                    result_stack[-1] = (lambda x,y : x ** y)(result_stack[-1],num)
                    #result_stack[-1] = result_stack[-1]**num

            #next index
            i += 1           
        
        return sum(result_stack)

    #expression with variable
    def var_expression(self,expr) -> str:

        #initial        
        value = 0
        variables = re.findall(r'[a-zA-Z]',expr)

        #loop element in variable list to replace number instead of variable
        for x in variables:
            value = input(f"Enter a value of variable {x} : ")

            expr = expr.replace(x,str(value))

        return expr

    #start program
    def starting(self)-> None:

        #telling choice and asking user what they want to do
        print("c: Calculate Arithmetic Expression")
        print("q: Quit")

        choice = input("Please Enter Your Choice: ")

        #looping for ask expression and calculating
        while choice != 'q':
            inner_brackets_found = True

            if choice == 'c':
                exp = input("Enter an arithmetic expression: ")              
            
                while inner_brackets_found:
                    
                    #check the brackets
                    m = re.search('\([^\(\)]+\)', exp)           
                    
                    #if it have open and close brackets -> search for variable -> calculate it
                    if m != None:
                        #fetch a resolvable expression, and immediately drop its outer brackets
                        expr_with_brackets = exp[m.start():m.end()]
                        #print(expr_with_brackets)

                        expr = expr_with_brackets[1:-1]
                        #print(expr)

                        if re.search('[a-zA-Z]',exp):
                            result = self.var_expression(expr)
                            print("Arithmetic Expression to Evaluate : ",result)
                            total_result = self.nonvar_without_brackets(result)
                        else:
                            total_result = self.nonvar_without_brackets(expr)
                        #print(result)

                        exp = exp.replace(expr_with_brackets, str(total_result))
                        #print expression for demonstrative purposes
                        #print(exp)

                    else:
                        inner_brackets_found = False
                        
                        if re.search('[a-zA-Z]',exp):
                            result = self.var_expression(exp)
                            print("Arithmetic Expression to Evaluate : ",result)
                            total_result = self.nonvar_without_brackets(result)
                        else:
                            total_result = self.nonvar_without_brackets(exp)
                        
                        print("result = {:e}".format(total_result))
                
                choice = input("Please Enter Your Choice: ")

            elif choice == 'q':        
                break;

        print("\n<End of Program>")

#command to start program  
calbot = Calculator()
calbot.starting()
