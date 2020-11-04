# Python Functions
- What are they and why are they useful
- How to create a function
- Best practices involving functions

**Why?**
- Used to repeat a block of code
- DRY = "Don't repeat yourself" -- functions allow us to follow this

**How?**
```python
    # This is how to create a function
    def <function name>(<parameters>):
        <code>

    # When you call a function, one must input the necessary arguements it needs to run
```

**Return**
- Return is useful when one is using several functions. If a function uses another function then it needs to return an actual value, not just a print statement.

**Task 1**
```python
##task##
# 1) multiplication function
# Multiplies all the numbers in the arguement
def mult(*args):
    val = 1
    for number in args:
        val *= number
    return val
print(mult(1,2,3,4,5,6,7,8,9))

# 2) division function
# This will return the value of n1 divided by n2
# Of course, if n2 is 0 then it is undefined so we output an error message
def div(n1, n2):
    if n2 == 0:
        return "Can't divide by 0"
    else:
        return n1/n2

print(div(9,0))

# 3) modulo function
# Returns n1 modulo n2 
def mod(n1, n2):
    return n1%n2
print(mod(56,3))
```

**Best practices**
- Small blocks of code for any function that does only one thing
- Pseudo coding: limit to one line
- Create hints in simple bullet points or pointers
- Write a comment maybe explaining function results
