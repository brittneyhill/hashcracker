# How to use crack.py
## By: Brittney Hill

### Program rundown:
1. In terminal, user must go to folder the file crack.py is located in and pass the argument into the file

         exp: python crack.py ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
2. Then you run the file and it will find a match for your hash value if it a match with a hash value in my locally saved file

    * If you want to use another password list to sort through, you must go into the code and change the file name to your new password list
3. If your hash is a salted hash, the program will check through the hashed passwordList and return there is no match at first.
     
     * Then, the program will prompt you to say whether the hash is salted or unsalted. 
     
     * If you say the hash is salted (by responding with yes, Yes, or YES). It will concatenate the salt term that we already know with each hash value that is in the password list to make a new hash value that includes the salt term and original passwordlist
          *      exp: newhash = saltterm + originalpassword
4. Lastly, the program will tell you the password explicitly if found. If not found, it will print there is no match.

#### Other features
1. The program times how long it takes to find the hash
2. The program states how many attempts were made before finding the match, if there is a match.

 **Other Modules Used:**
* sys   
    * used to parse arguments in command line
* time
    * used to track time it takes to run program
##### Solutions:
**a**. I found the password! It's  letmein it took 16 tries to find your match in 0.0 seconds

**b**. I found the password! It's  vjhtrhsvdctcegth it took 999968 tries to find your match in 1.2208588123321533 seconds

**c**. I found the password! It's harib it took 546155 tries to find your match in 4.395314455032349 seconds.
