# python e list ekti **object, ei objects ti **Array ke re-presents kore.
# List indexing 0 theke shuru hoy
books = ['JavaScript', 'Python', 'Java']
javaScript = books[0]
java = books[-1]
print(javaScript, java)
'''
 **in** ,**not in** diye array list e kuno property check kora hoy
 in, not in=> true/false return kore
 Example:
'''
yes = ('Python' in books)
dont = ('Kotlin' in books)
print(yes, dont)

# true, false : karon list e python ace kintu Kotlin nei.

# add new property on Array list
# ze array te notun propety add korte hobe sei array er sathe + sign diye arekti array list jure dilei hobe.
books = (books+['Kotlin', 'Flutter'])
print(books)
