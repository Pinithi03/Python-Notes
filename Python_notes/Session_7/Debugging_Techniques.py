# Example traceback :
# Traceback ( most recent call last ) :
# File " app . py " , line 15 , in < module >
# result = calculate ( scores )
# File " app . py " , line 8 , in calculate
# average = total / count
# Z e r o D i v i s i o n E r r o r : division by zero
# How to read :
# 1. START AT THE BOTTOM - error type and message
# 2. READ UP - see where and how the error happened
# 3. LINE NUMBERS - tell you exactly where to look

# Add strategic print st at em ent s to find bugs
def process_data ( data ) :
 print ( f" DEBUG : data = { data } " ) # What went in ?
 print ( f" DEBUG : type = { type ( data ) } " ) # What type ?

 result = transform ( data )
 print ( f" DEBUG : result = { result } " ) # What came out ?

 return result
# REMOVE debug prints when done !

"""Common Bug Patterns
1. Off-by-one: range(1, 5) gives [1,2,3,4] not [1,2,3,4,5]
2. Reference vs copy: list2 = list1 doesn’t copy!
3. File data types: Everything from files is a string
4. Forgetting self: Most common OOP bug
5. Mutating while iterating: Don’t change a list while looping over it"""

