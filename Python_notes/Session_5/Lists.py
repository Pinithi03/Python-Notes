"""Part 1: Advanced List Operations
List Slicing - The Power Tool
Slicing lets you extract parts of lists efficiently.
Basic Slicing Syntax: list[start:stop:step]"""

numbers = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
# Basic slicing [ start : stop ]
print ( numbers [1:4]) # [1 , 2 , 3] ( stop is exclusive !)
print ( numbers [:5]) # [0 , 1 , 2 , 3 , 4] ( from beginning )
print ( numbers [5:]) # [5 , 6 , 7 , 8 , 9] ( to end )
print ( numbers [:]) # [0 , 1 , 2 , ...] ( copy of entire list )

# With step [ start : stop : step ]
print ( numbers [::2]) # [0 , 2 , 4 , 6 , 8] ( every 2 nd item )
print ( numbers [1::2]) # [1 , 3 , 5 , 7 , 9] ( odd indices )

# Negative indices
print ( numbers [ -3:]) # [7 , 8 , 9] ( last 3)
print ( numbers [: -3]) # [0 , 1 , 2 , ... , 6] ( all but last 3)

# Reverse with negative step !
print ( numbers [:: -1]) # [9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 0]


#Ex2:
scores = [45 , 78 , 92 , 63 , 88 , 55 , 99 , 72]

# Get top 3 scores
top_3 = sorted ( scores , reverse = True ) [:3]
print ( top_3 ) # [99 , 92 , 88]

# Get every other score
alternate = scores [::2]
print ( alternate ) # [45 , 92 , 88 , 99]

# Reverse the list
reversed_scores = scores [:: -1]
print ( reversed_scores ) # [72 , 99 , 55 , 88 , 63 , 92 , 78 , 45]


"""List Methods"""
#Adding items:
fruits = [ " apple " , " banana " ]
fruits . append ( " orange " ) # Add to end
fruits . insert (1 , " mango " ) # Insert at index 1
fruits . extend ([ " kiwi " , " pear " ]) # Add multiple
print ( fruits )
# [ ' apple ', ' mango ', ' banana ', ' orange ', ' kiwi ', ' pear ' ]

#Removing items:
fruits = [ " apple " , " banana " , " orange " , " banana " ]
fruits . remove ( " banana " ) # Remove first occurrence
last = fruits . pop () # Remove and return last
first = fruits . pop (0) # Remove and return at index
print ( fruits )

#Searching and sorting:
numbers = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6]

# Search
print ( numbers . count (1) ) # 2 ( appears twice )
print ( numbers . index (5) ) # 4 ( index of first 5)
# Modify in place
numbers . reverse () # Reverse the list
numbers . sort () # Sort ascending
numbers . sort ( reverse = True ) # Sort descending


"""List Copying - CRITICAL!"""
#The Most Common List Bug!
#Assignment (=) does NOT create a copy!
#It creates a reference to the same list in memory.

# WRONG - Both variables point to same list !
list1 = [1 , 2 , 3]
list2 = list1 # Reference , not copy !
list2 . append (4)
print ( list1 ) # [1 , 2 , 3 , 4] - Changed ! ( Unexpected !)
print ( list2 ) # [1 , 2 , 3 , 4]

# CORRECT - Create an actual copy
list1 = [1 , 2 , 3]
list2 = list1 . copy () # Method 1: . copy ()
# list2 = list ( list1 ) # Method 2: list () constructor
# list2 = list1 [:]      # Method 3: slice notation
# All three create independent copies !

list2 . append (4)
print ( list1 ) # [1 , 2 , 3] - Unchanged ! ( Expected !)
print ( list2 ) # [1 , 2 , 3 , 4]


"""Nested Lists - Lists of Lists"""
#Ex1:
# 2 D list ( matrix )
matrix = [
[1 , 2 , 3] ,
[4 , 5 , 6] ,
[7 , 8 , 9]
]
# Access outer list
print ( matrix [0]) # [1 , 2 , 3]

# Access inner item
print ( matrix [1][2]) # 6

# Iterate through 2 D list
for row in matrix :
    for item in row :
        print ( item , end = " " )
    print () # New line after each row
    
#Ex2:
# Student records : [ name , age , grade ]
students = [
 [ " Alice " , 20 , 85] ,
 [ " Bob " , 21 , 92] ,
 [ " Charlie " , 19 , 78]
 ]
# Iterate and unpack
for student in students :
 name , age , grade = student # Unpacking !
 print ( f" { name } ( age { age }) : { grade } " )
 
 