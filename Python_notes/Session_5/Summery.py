"""Choosing the Right Data Structure
Decision Guide
LIST - [1, 2, 3]
• Ordered, mutable, allows duplicates
• Use: Sequential data, need order
TUPLE - (1, 2, 3)
• Ordered, immutable, allows duplicates
• Use: Fixed data, coordinates, return multiple values
SET - {1, 2, 3}
• Unordered, mutable, NO duplicates
• Use: Unique items, membership testing, set operations
DICTIONARY - {"a": 1, "b": 2}
• Key-based, mutable, keys unique
• Use: Fast lookups, key-value pairs, counting

Key Takeaways
Essential Concepts
• Slicing is powerful: list[::-1] reverses!
• Always .copy() lists if you want independent copies
• List comprehensions are more Pythonic than map/filter
• Dictionaries for lookups, lists for sequences
• Use .get() for safe dictionary access
• Tuples for fixed data, sets for unique items
• Choose the right data structure based on needs
• Set operations find common/unique items easily

Common Mistakes to Avoid
• list2 = list1 creates reference, not copy!
• Using [] instead of .get() causes KeyError
• Trying to modify tuples - they’re immutable!
• {} creates dict, not empty set - use set()

14

• Forgetting to convert set back to list when needed
• Using complex logic in comprehensions - use loops instead
• Accessing sets by index - they’re unordered!"""

# LISTS
nums = [1, 2, 3]
first_three = nums[:3]
reversed_nums = nums[::-1]
nums_copy = nums.copy()
doubled_nums = [x * 2 for x in nums]

# DICTIONARIES
d = {"key": "value"}
safe_value = d.get("key", "default")
d["key"] = "new"

for k, v in d.items():
    print(k, v)

# TUPLES
coord = (10, 20)
x, y = coord

# Can't modify tuples because they are immutable.

# SETS
s = {1, 2, 3}
s.add(4)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersection = set1 & set2
union = set1 | set2
difference = set1 - set2
symmetric_difference = set1 ^ set2
