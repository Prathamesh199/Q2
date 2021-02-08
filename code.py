n = int(input("Enter positive integer: "))
divisors = []
for i in range(1,n+1):
    if(n%i == 0):
        divisors.append(i)
output = sum(divisors)
print(output)

'''
Output of Test Data is given below
Input: 42 then Output: 96
Input: 147 then Output: 228
'''