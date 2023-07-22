# take a list input from user
# string = input('Enter your number list with space: ')
# numList = string.split()
# total = 0
# for x in numList:
#     total = total+int(x)
# print(total)

# find out total letter,number and word of an input sentence
letter = 0
number = 0
words = 0
sentence = input('Your sentence: ')
for x in sentence.lower():
    if x >= 'a' and x <= 'z':
        letter = letter+1
    elif x >= '0' and x <= '9':
        number = number+1
    elif x == ' ':
        words = words+1
print(words+1)
print(letter)
print(number)
