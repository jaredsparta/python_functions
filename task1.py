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
    