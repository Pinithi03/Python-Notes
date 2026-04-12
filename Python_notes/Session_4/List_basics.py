"""Part 2: Lists Basics
What is a List?
A list is an ordered collection that can store multiple values."""

# Creating lists
from doctest import Example


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

"""append() - Add Single Item
 # Add one item at a time
 scores = [85 , 92 , 78]
 scores . append (95)
 print ( scores ) # [85 , 92 , 78 , 95]

 scores . append (88)
 print ( scores ) # [85 , 92 , 78 , 95 , 88]"""
 
"""extend() - Add Multiple Items
# Add multiple items at once
scores = [85 , 92 , 78]
new_scores = [95 , 88 , 82]
scores . extend ( new_scores )
print ( scores ) # [85 , 92 , 78 , 95 , 88 , 82]"""

#Alternative: Using + operator
scores = [85 , 92]
more_scores = [78 , 95]
all_scores = scores + more_scores # Creates NEW list
print ( all_scores ) # [85 , 92 , 78 , 95]


"""Built-in List Functions"""
numbers = [5 , 2 , 8 , 1 , 9 , 3]

print ( len ( numbers ) ) # 6 ( length )
print ( sum ( numbers ) ) # 28 ( sum of all )
print ( min ( numbers ) ) # 1 ( smallest )
print ( max ( numbers ) ) # 9 ( largest )

#Heterogeneous Lists and Built-in Functions
#Warning: Mixed Types with sum(), min(), max()
#Lists can hold different types, but sum(), min(), and max() have restrictions!
#Example 1: Numbers and Strings - ERROR!
mixed = [1 , 2 , " hello " , 3]
# print ( sum ( mixed ) ) # TypeError !
# print ( max ( mixed ) ) # TypeError !

# Can ’t mix numbers and strings in these functions

#Example 2: Strings Only - Works!
words = [ " apple " , " zebra " , " banana " ]
print ( max ( words ) ) # " zebra " ( alphabetically last )
print ( min ( words ) ) # " apple " ( alphabetically first )
# print ( sum ( words ) ) # TypeError - can ’t sum strings

#Example 3: Numbers with Booleans - Surprising!
# Booleans are treated as numbers !
# True = 1 , False = 0
nums = [10 , True , 20 , False , 5]
print ( sum ( nums ) ) # 36 (10 + 1 + 20 + 0 + 5)
print ( max ( nums ) ) # 20
print ( min ( nums ) ) # False ( which is 0)

#Example 4: Mixed int and float - Works Fine!
numbers = [10 , 3.5 , 20 , 7.8]
print ( sum ( numbers ) ) # 41.3
print ( max ( numbers ) ) # 20
print ( min ( numbers ) ) # 3.5

"""Best Practice
Keep lists homogeneous for math operations:
• All integers: [85, 92, 78, 95]
• All floats: [10.5, 20.0, 15.75]
• All strings: ["Alice", "Bob", "Charlie"]
Key Takeaways:
• sum() only works with numbers (int/float)
• max()/min() work if all items are comparable
• Strings compare alphabetically
• Booleans behave as numbers (True=1, False=0)
• Can’t compare different types (string vs number)"""