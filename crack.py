import hashlib
import sys
import time

passlist = open("C:/Users/bhill35/Documents/code/yeahcode/passwordList.txt")
list_of_pass = passlist.read().split("\n")
saltterm = "slayer"

def check(argument):
        start = time.time()
        tries = 0
        for item in list_of_pass:
            hashfromlib = hashlib.sha1(bytes(item, 'utf-8')).hexdigest()
            tries += 1
            if hashfromlib == argument:
                print("I found the password! It's ", str(item), "it took", tries, "tries to find your match in %s seconds" %(time.time() - start))
                quit()
        print("We tried ", tries, "times to find your match with no luck :(")
        userin = input("Is this a salted hash?")
        if userin == "yes" or "YES" or "Yes":
            tries = 0
            for item in list_of_pass:
                newhash = saltterm + item
                hashfromlib = hashlib.sha1(bytes(newhash, 'utf-8')).hexdigest()
                tries += 1
                if hashfromlib == argument:
                    print("I found the password! It's", str(item), "it took", tries,
                          "tries to find your match in %s seconds." % (time.time() - start))
                    quit()
        else:
            print("sorry no match")

check(sys.argv[1])
