# pattern printing by for loop
'''
*
**
***
****
'''
# lineNum = int(input('Enter the line number: '))
# for i in range(1, lineNum+1, 1):
#     pattern = i*'*'
#     print(pattern)

# print this:
'''
*
***
*****
*******
'''
# numLine = int(input('Enter the line number2: '))
# for i in list(range(1, numLine+1, 1)):
#     pattern = (i*2-1)*"*"
#     print(pattern)

# factorial pattern printing
n = int(input('Enter the factorial number: '))
for i in list(range(1, n+1, 1)):
    factPattern = (i*i)*'*'
    print(factPattern)
