"""Part 2: Lists Basics
What is a List?
A list is an ordered collection that can store multiple values."""

# Creating lists
scores = [85 , 92 , 78 , 95 , 88]
fruits = [ " apple " , " banana " , " cherry " ]
mixed = [42 , " hello " , 3.14 , True ] # Can mix types !

#Accessing List Elements
fruits = [ " apple " , " banana " , " cherry " , " date " ]

# Positive indexing ( starts at 0)
print ( fruits [0]) # apple
print ( fruits [1]) # banana
print ( fruits [2]) # cherry

# Negative indexing ( from the end )
print ( fruits [ -1]) # date ( last item )
print ( fruits [ -2]) # cherry ( second - to - last )


#Iterating Through Lists
scores = [85 , 92 , 78 , 95 , 88]
# Iterate through values
for score in scores :
 print ( score )

 # Calculate average
total = sum ( scores )
average = total / len ( scores )
print ( f" Average : { average } " )

