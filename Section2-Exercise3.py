'''
3. Write a Python class to find validity of a string of parentheses, 
'(', ')', '{', '}', '[' and ']. These brackets must be close in the
correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

'''
class Parentheses:
    def validityOfParentheses(self,string):
        bracket1 = ('{','}')
        bracket2 = ('(',')')
        bracket3 = ('[',']')
        flag = True
        for index in range(len(string)):
            if(string[index] == bracket1[0]):
                if(string[index+1] != bracket1[1]):
                    flag = False
                    break
            elif(string[index] == bracket2[0]):
                if(string[index+1] != bracket2[1]):
                    flag = False
                    break
            elif(string[index] == bracket3[0]):
                if(string[index+1] != bracket3[1]):
                    flag = False  
                    break
        return flag



print(Parentheses().validityOfParentheses("[](){)}"))


#########################################################################################

class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))
