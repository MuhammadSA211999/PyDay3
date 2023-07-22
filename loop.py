# find out total from a list array

numbers = [1, 2, 3, 4, 5, 6]
sum = 0
length = len(numbers)
index = 0
while index < length:
    number = numbers[index]
    print(number)
    sum = sum+number
    index = index+1
print(sum)

# by for loop
total = 0
for x in numbers:
    total = total+x
print(total)
