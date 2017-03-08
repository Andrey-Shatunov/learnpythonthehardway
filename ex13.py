from sys import argv

script, first, second, third,fifth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fifth variable is:", fifth

old = raw_input("How old are you?")

print """The script is called: %s/n
Your first variable is: %s 
Your second variable is: %s 
Your third variable is: %s 
Your fifth variable is: %s 
Your old is %s """ % (script,first,second,third,fifth,old)

