# python e list ekti **object, ei objects ti **Array ke re-presents kore.
# List indexing 0 theke shuru hoy
books = ['JavaScript', 'Python', 'Java']
javaScript = books[0]
java = books[-1]
# print(javaScript, java)
'''
 **in** ,**not in** diye array list e kuno property check kora hoy
 in, not in=> true/false return kore
 Example:
'''
yes = ('Python' in books)
dont = ('Kotlin' in books)
# print(yes, dont)

# true, false : karon list e python ace kintu Kotlin nei.

# add new property on Array list
# ze array te notun propety add korte hobe sei array er sathe + sign diye arekti array list jure dilei hobe.
books = books+['Kotlin', 'Flutter']
# print(books)

''''
python built in array function
array=['w','e','r','t','y','w','t']

length=array.len(),
array.append('a','d','h','j')
array.insert(3,'d') // duita argument dite hoy, index and propertyName
array.remove(propertyName) //argument hisabe propertyName dite hoy
array.revers() //list ke ulta sazay
array2=array.copy()
array.pop()
array.sort() // sort func list ke alphabatically sazay 
array.clear() // empty array 
array.index(propertyName)  //argu propertyName dite hoy, index return kore
array.count(propertyName) //proName dite hoy, sei property list ti te koybar exist kore sei songkha return kore.
'''
file = ['kt', 'js', 'py', 'jar', 'cc']
file.remove('cc')
# print(file) // ['kt', 'js', 'py', 'jar']

file.insert(3, 'php')
# print(file)
