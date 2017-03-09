from sys import argv
from os.path import exists

script, from_file, to_file = argv

#in_file = open(from_file)
#indata = in_file.read()
#out_file = open(to_file, 'w')
open(to_file, 'w').write(open(from_file).read())


#out_file.close()
#in_file.close()
