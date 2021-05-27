'''
8. Write a Python class to reverse a string word by word.
Input string : 'hello .py'
Expected Output : '.py hello'

'''

import re

class ReverseString:
    def reverseWords(self,stringArg):
        listWords = stringArg.split()
        listWords.reverse()
        newString = ""
        for item in listWords:
            newString += "".join(item) + ' '
        return newString

print(ReverseString().reverseWords("hello .py"))
