'''
7. Write a Python class to implement pow(x, n).

'''

class Power:
    def pow(self,num,p):
        if(pow == 1):
            return 1
        else:
            return num* pow(num,p-1)


print(Power().pow(5,2))
print(Power().pow(1,10))
print(Power().pow(3,3))
print(Power().pow(10,2))
print(Power().pow(2,-3))
print(Power().pow(3,5))
print(Power().pow(100,0))