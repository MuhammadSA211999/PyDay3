# find out total value of a series by While/For loop

''''
to find out the series value by loop
remember this 3 things:

1. loot at the starting number
2. difference between nearly two numbers
3. catch the last number of the  given series
'''
# 1+2+3+.....+n
n = int(input('Enter the didit: '))
total = 0
for x in list(range(1, n+1, 1)):
    total = total+x
print(total)

# 1*2+3*2+5*2+.....+n*2
n = int(input('Enter your number: '))
total = 0
for x in list(range(1, n+1, 2)):
    total = total+x**2
print(total)

# 2*3+4*3+6*3+.....+n*3
n = int(input('Enter the last digit: '))
total = 0
for x in list(range(2, n+1, 2)):
    # [2,4]
    total = total+x**3
print(total)
