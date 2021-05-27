'''
4. Write a Python class to get all possible unique subsets from a set
 of distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

'''

# class py_solution:
#     def sub_sets(self, sset):
#         return self.subsetsRecur([], sorted(sset))
    
#     def subsetsRecur(self, current, sset):
#         if sset:
#             return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
#         return [current]

# print(py_solution().sub_sets([4,5,6]))


#####################################################################################################

from itertools import combinations

class py_solution2:
    def sub_sets(self,listArg):
        resultList = []
        i = 0
        while i <= len(listArg):
            comb = combinations(listArg,i)
            for item in comb:
                resultList.append(item)
            i += 1
        return resultList
        
    

list1 = [4, 5, 6]

print(py_solution2().sub_sets(list1))