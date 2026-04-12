"""Part 3: Lambda Functions
What is a Lambda?
A lambda is a small anonymous function written in a single line."""

# Regular function
def square ( x ) :
 return x ** 2
# Lambda version
square = lambda x : x ** 2
# Both work the same !
print ( square (5) ) # 25

"""Lambda Syntax

lambda parameters: expression

Key Points:
• No def keyword
• No return statement (implicit)
• Single expression only
• Usually used inline with other functions"""

# Single parameter
square = lambda x : x ** 2
# Multiple parameters
add = lambda a , b : a + b
multiply = lambda x , y , z : x * y * z
# With conditional
is_even = lambda n : n % 2 == 0

"""When to Use Lambda

Use Lambda                       Use Regular Function
Quick, one-line operations       Complex logic
With map, filter, sorted         Multiple lines needed
One-time use                     Needs documentation"""