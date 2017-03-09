from sys import argv

script, filename = argv
# open file
txt = open(filename)

print "Here's your file %r:" % filename
# read file
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

# open file

txt_again = open(file_again)

# read again file

print txt_again.read()

txt.close()
txt_again.close()
