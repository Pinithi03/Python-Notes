"""Part 2: List Comprehensions - Elegant Python
What is a List Comprehension?
A concise way to create lists in a single line of code.
Basic Syntax: [expression for item in iterable]"""

# The verbose way
numbers = [1 , 2 , 3 , 4 , 5]
squared = []
for n in numbers :
 squared . append ( n ** 2)
print ( squared ) # [1 , 4 , 9 , 16 , 25]
# The elegant way - list comprehension
squared = [ n ** 2 for n in numbers ]
print ( squared ) # [1 , 4 , 9 , 16 , 25]
# Same result , one beautiful line !
 
 
"""Basic Comprehensions"""
numbers = [1 , 2 , 3 , 4 , 5]

# Square each number
squared = [ n ** 2 for n in numbers ]
# [1 , 4 , 9 , 16 , 25]

# Double each number
doubled = [ n * 2 for n in numbers ]
# [2 , 4 , 6 , 8 , 10]

# Uppercase each name
names = [ " alice " , " bob " , " charlie " ]
upper = [ name . upper () for name in names ]
# [ ’ ALICE ’, ’ BOB ’, ’ CHARLIE ’]

# String lengths
fruits = [ " apple " , " banana " , " kiwi " ]
lengths = [ len ( fruit ) for fruit in fruits ]
# [5 , 6 , 4]


"""Comprehensions with Conditions"""
#Syntax: [expression for item in iterable if condition]
numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]

# Only even numbers
evens = [ n for n in numbers if n % 2 == 0]
print ( evens ) # [2 , 4 , 6 , 8]

# Only odd numbers , squared
odd_squared = [ n ** 2 for n in numbers if n % 2 == 1]
print ( odd_squared ) # [1 , 9 , 25 , 49]

# Passing scores only
scores = [45 , 78 , 92 , 63 , 55 , 88]
passing = [ s for s in scores if s >= 60]
print ( passing ) # [78 , 92 , 63 , 88]


"""Transform AND Filter"""
#You can both transform and filter in one comprehension!
scores = [45 , 78 , 92 , 63 , 55 , 88]

# Double the passing scores
doubled_passing = [ s * 2 for s in scores if s >= 60]
print ( doubled_passing ) # [156 , 184 , 126 , 176]

# Convert to letter grades ( only passing )
def to_grade ( score ) :
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    else : return 'D'
    
passing_grades = [ to_grade ( s ) for s in scores if s >= 60]
print ( passing_grades ) # [ ' C ', 'A ', 'D ', 'B ']


"""Comprehensions vs map/filter"""
#List comprehensions are more readable than map/filter!
numbers = [1 , 2 , 3 , 4 , 5]

# Old way ( Session 04) - map / filter
squared_evens = list ( map (
lambda x : x ** 2 ,
filter ( lambda x : x % 2 == 0 , numbers )
) )

# New way - comprehension ( cleaner !)
squared_evens = [ n ** 2 for n in numbers if n % 2 == 0]
# Both give : [4 , 16]
# Comprehensions are more Pythonic !


"""Practical Comprehension Examples"""
# Extract email addresses
usernames = [ " alice@email . com " , " bob " , " charlie@email . com " ]
emails = [ u for u in usernames if " @ " in u ]
# [ ' alice@email . com ', ' charlie@email . com ']

# Temperature conversion ( Celsius to Fahrenheit )
celsius = [0 , 10 , 20 , 30 , 40]
fahrenheit = [( c * 9/5) + 32 for c in celsius ]
# [32.0 , 50.0 , 68.0 , 86.0 , 104.0]
# Extract first letters
words = [ " apple " , " banana " , " cherry " ]
first_letters = [ w [0] for w in words ]
# [ ' a ', 'b ', 'c ']

# Filter long words
words = [ " hi " , " hello " , " hey " , " goodbye " , " greetings " ]
long_words = [ w for w in words if len ( w ) >= 6]
# [ ' goodbye ', ' greetings ']


"""Nested Comprehensions"""
# Create multiplication table
table = [[ i * j for j in range (1 , 6) ] for i in range (1 , 6) ]
# [[1 , 2 , 3 , 4 , 5] ,
# [2 , 4 , 6 , 8 , 10] ,
# [3 , 6 , 9 , 12 , 15] ,
# [4 , 8 , 12 , 16 , 20] ,
# [5 , 10 , 15 , 20 , 25]]

# Flatten a 2 D list
matrix = [[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9]]
flat = [ item for row in matrix for item in row ]
print ( flat ) # [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

"""When to Use Comprehensions
Use comprehensions when:
• Transforming a list
• Filtering a list
• Logic is simple and clear
Avoid comprehensions when:
• Logic is complex
• Multiple operations needed
• Readability suffers
Rule: If it’s hard to read, use a regular loop!"""

