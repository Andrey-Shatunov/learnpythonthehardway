from sys import exit
import random

def str_to_int(b):
    while b.isdigit() is False:
        print "You enter not number"
        print "Try again"
        b=raw_input('Try again > :')
    return int(b)

def start():
    a=random.randint(0,10)
    #print a
    print "It the game - Guess number"
    b = raw_input('Enter number > :')
    b=str_to_int(b)
    if a==b:
        print "You guess"
    while a!=b:
        if a>b:
            print "My num is more"
            b=raw_input('Try again > :')
            b=str_to_int(b)
            if a==b:
                print "You guess"
        else:
            print "My num is less"
            b=raw_input('Try again > :')
            b=str_to_int(b)
            if a==b:
                print "You guess"

start()
