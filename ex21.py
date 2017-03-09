def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

def remainder_of_the_division(a,b):
    print "remainder_of_the_division %d and %d" % (a, b)
    return a-b*(a/b)


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
#-------------------------------------------------------------------------
# a*(a-b)
print "a*(a-b)"
print multiply(5,subtract(5,4))
# a%b
print remainder_of_the_division(10,4)
