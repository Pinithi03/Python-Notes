"""Part 4: Built-in Functions
map() - Transform All Items
map() applies a function to every item in a list."""

numbers = [1 , 2 , 3 , 4 , 5]

# The old way - manual loop
squared = []
for n in numbers:
    squared.append(n ** 2)
print(squared) # [1 , 4 , 9 , 16 , 25]

# With map () and lambda - elegant !
squared = list ( map ( lambda x : x ** 2 , numbers ) )
print ( squared ) # [1 , 4 , 9 , 16 , 25]

#Practical Example: Convert Strings to Numbers
prices_str = [ " 10.50 " , " 20.00 " , " 15.75 " ]
prices_float = list ( map ( float , prices_str ) )
print ( prices_float ) # [10.5 , 20.0 , 15.75]
total = sum ( prices_float ) # 46.25

#Practical Example: Uppercase All Names
names = [ "alice" , "bob" , "charlie" ]
uppercase_names = list ( map ( str.upper , names ) )
print ( uppercase_names ) # ["ALICE" , "BOB" , "CHARLIE"]

#filter() - Keep Matching Items
#filter() keeps only items that match a condition.
numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]

# The old way - manual loop
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens) # [2 , 4 , 6 , 8]
# With filter () and lambda - elegant !
evens = list ( filter ( lambda n : n % 2 == 0 , numbers ) )
print ( evens ) # [2 , 4 , 6 , 8]

#Practical Example: Passing Scores
scores = [45 , 78 , 92 , 63 , 55 , 88]
passing = list ( filter ( lambda s : s >= 60 , scores ) )
print ( passing ) # [78 , 92 , 63 , 88]


#zip() - Combine Lists
#zip() combines multiple lists element by element.
names = [ " Alice " , " Bob " , " Charlie " ]
scores = [85 , 92 , 78]
# Combine into pairs
combined = list ( zip ( names , scores ) )
print ( combined )
# [( ’ Alice ’, 85) , ( ’ Bob ’, 92) , ( ’ Charlie ’, 78) ]

# Common use : parallel iteration
for name , score in zip ( names , scores ) :
 print ( f" { name } scored { score } " )
 
#zip() stops at the SHORTEST list!
#Data will be lost if lists have different lengths!
names = [ " Alice " , " Bob " , " Charlie " , " Diana " ]
scores = [85 , 92 , 78]
# Validate before zipping
if len ( names ) != len ( scores ) :
  print ( " Warning : Length mismatch ! " )
  print ( f" Names : { len ( names ) } , Scores : { len ( scores ) } " )
  print ( " Some data will be lost ! " )
else :
 pairs = list ( zip ( names , scores ) )
print ( pairs )

"""enumerate() - Get Index + Value
enumerate() gives you both the index and value while iterating.
Why enumerate()?"""
# The old way - manual counter
fruits = [ " apple " , " banana " , " cherry " ]
index = 0
for fruit in fruits :
 print ( f" { index }: { fruit } " )
 index += 1

# The Python way - enumerate ()
for index , fruit in enumerate ( fruits ) :
 print ( f" { index }: { fruit } " )
 
#What enumerate() returns:
fruits = [ " apple " , " banana " , " cherry " ]
print ( list ( enumerate ( fruits ) ) )
# [(0 , ’ apple ’) , (1 , ’ banana ’) , (2 , ’ cherry ’) ]
# Each item is a tuple : ( index , value )

#Custom starting index:
# Start counting from 1 instead of 0
fruits = [ " apple " , " banana " , " cherry " ]

for index , fruit in enumerate ( fruits , start =1) :
 print ( f" #{ index }: { fruit } " )
# #1: apple
# #2: banana
# #3: cherry

#Practical Example: Numbered Menu
options = [ " New Game " , " Load Game " , " Settings " , " Quit " ]

print ( " === MENU === " )
for i , option in enumerate ( options , start =1) :
 print ( f" { i }. { option } " )
 
# Output :
# === MENU ===
# 1. New Game
# 2. Load Game
# 3. Settings
# 4. Quit

#Practical Example: Find Indices
students = [ " Alice " , " Bob " , " Charlie " , " Alice " , " Diana " ]

for i , name in enumerate ( students ) :
 if name == " Alice " :
   print ( f" Alice found at index { i } " )
 
# Output :
# Alice found at index 0
# Alice found at index 3

"""sorted() - Powerful Sorting
sorted() returns a new sorted list."""
numbers = [5 , 2 , 8 , 1 , 9]
sorted_nums = sorted ( numbers )
print ( sorted_nums ) # [1 , 2 , 5 , 8 , 9]
# Original unchanged !
print ( numbers ) # [5 , 2 , 8 , 1 , 9]

# Reverse order
descending = sorted ( numbers , reverse = True )
print ( descending ) # [9 , 8 , 5 , 2 , 1]

#sorted() vs .sort():
# sorted () - returns NEW list
numbers = [5 , 2 , 8 , 1 , 9]
result = sorted ( numbers )
print ( numbers ) # [5 , 2 , 8 , 1 , 9] - unchanged
print ( result ) # [1 , 2 , 5 , 8 , 9] - new sorted
# . sort () - modifies IN PLACE
numbers = [5 , 2 , 8 , 1 , 9]
numbers . sort ()
print ( numbers ) # [1 , 2 , 5 , 8 , 9] - modified !

#Sorting complex data:
# List of tuples
students = [
( " Alice " , 85) ,
( " Bob " , 92) ,
( " Charlie " , 78) ,
( " Diana " , 95)
]

# Sort by score ( second element )
by_score = sorted ( students , key = lambda x : x [1])
print ( by_score )
# [( ’ Charlie ’, 78) , ( ’ Alice ’, 85) , ( ’ Bob ’, 92) , ( ’ Diana ’, 95) ]

# Sort by score , highest first
top_students = sorted ( students ,
key = lambda x : x [1] ,
reverse = True )
print ( top_students )
# [( ’ Diana ’, 95) , ( ’ Bob ’, 92) , ( ’ Alice ’, 85) , ( ’ Charlie ’, 78) ]

#Sorting dictionaries:
students = [
{ " name " : " Alice " , " grade " : 85} ,
{ " name " : " Bob " , " grade " : 92} ,
{ " name " : " Charlie " , " grade " : 78} ,
]
# Sort by grade
by_grade = sorted ( students , key = lambda s : s [ " grade " ])
for student in by_grade :
 print ( f" { student [ ' name ']}: { student [ ' grade ']} " )
 


#Advanced sorting tricks:
# Sort by absolute value
numbers = [ -5 , 3 , -1 , 8 , -9 , 2]
by_magnitude = sorted ( numbers , key = abs )
print ( by_magnitude ) # [ -1 , 2 , 3 , -5 , 8 , -9]
# Case - insensitive sort
names = [ " alice " , " Bob " , " CHARLIE " , " diana " ]
sorted_names = sorted ( names , key = str . lower )
print ( sorted_names )
# [ ’ alice ’, ’ Bob ’, ’ CHARLIE ’, ’ diana ’]
# Sort by multiple criteria ( tuple comparison )
students = [
( " Alice " , 85) ,
( " Bob " , 85) , # Same score as Alice
( " Charlie " , 92) ,
]
# Sort by score DESC , then name ASC
sorted_students = sorted ( students ,
key = lambda x : ( - x [1] , x [0]) )
print ( sorted_students )
# [( ’ Charlie ’, 92) , ( ’ Alice ’, 85) , ( ’ Bob ’, 85) ]