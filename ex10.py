tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* %r Grass %r  %s %s
'''%(12,13,13,"test")

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


test = "My test"

print "%r" % test
print "%r" % "TEST \"My test\""

print "%s" % test
print "%s" % "TEST \"My test\""

