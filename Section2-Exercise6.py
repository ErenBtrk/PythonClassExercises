'''
6. Write a Python class to find the three elements that sum to zero
 from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]

Click me to see the solution

'''

from itertools import combinations

def factorial(number):
    if(number == 1):
        return 1
    else:
        return number * factorial(number-1)

class SumZero:
    def findSumZero(self,listArg):
        resultList = []
        comb = list(combinations(listArg,3))
        
        for item in comb:
            sum = 0
            for item2 in item:
                sum += item2
            if(sum == 0):
                resultList.append(item)
        return resultList


list1 = [-25, -10, -7, -3, 2, 4, 8, 10]

result = SumZero().findSumZero(list1)

print(result)





