i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

#---------------------------------------------------
def my_list(num,inc):
    my_numbers = []
    for i in range(0,num,inc):
        print "At the top i is %d" % i
        my_numbers.append(i)
    return my_numbers
    
numbers=my_list(16,2)
print numbers

