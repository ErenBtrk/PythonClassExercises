'''
5. Write a Python class to find a pair of elements (indices of the two numbers)
from a given array whose sum equals a specific target number. 
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4

'''

class Pairs:
    def FindPairs(self,list,target):
        pairList = []
        for index in range(len(list)-1):
            if(list[index] + list[index+1] == target):
                pairList.append(index)
                pairList.append(index+1)
        return pairList

numbers= [10,20,10,40,50,60,70]
target=50

print(Pairs().FindPairs(numbers,target))

