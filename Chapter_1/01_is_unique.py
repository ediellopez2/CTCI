
# Cracking the Coding Interview - Chapter 1

myList = {'a':True,'b':True,'c':True,'d':True,'e':True,'f':True,'g':True,'h':True,'i':True,'j':True,'k':True,
          'l':True,'m':True,'n':True,'o':True,'p':True,'q':True,'r':True,'s':True,'t':True,'u':True,'v':True,
          'w':True,'x':True,'y':True,'z':True,'A':True,'B':True,'C':True,'D':True,'E':True,'F':True,'G':True,
          'H':True,'I':True,'J':True,'K':True,'L':True,'M':True,'N':True,'O':True,'P':True,'Q':True,'R':True,
          'S':True,'T':True,'U':True,'V':True,'W':True,'X':True,'Y':True,'Z':True}

# This function uses a dictionary to store the STATE of each character.
# As we traverse the provided string, we will change the value of the key
# to False. If a character that has already been seen is found again, the
# program will terminate. It is not a unique string. Otherwise, we do have
# a unique string.
def is_unique(myString):
    for index in myString:
        if myList[index]:
            myList[index] = False
        else:
            print("This is not a unique string.")
            return False

if __name__ == '__main__':
    myString = "HelLo"

    # Let's make sure that this is actually a string.
    assert myString.isalpha(), "Ooops, this is not a valid string."

    is_unique(myString)