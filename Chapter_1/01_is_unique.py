
# Cracking the Coding Interview - Chapter 1

myList = {'a':True,'b':True,'c':True,'d':True,'e':True,'f':True,'g':True,'h':True,'i':True,'j':True,'k':True,
          'l':True,'m':True,'n':True,'o':True,'p':True,'q':True,'r':True,'s':True,'t':True,'u':True,'v':True,
          'w':True,'x':True,'y':True,'z':True,'A':True,'B':True,'C':True,'D':True,'E':True,'F':True,'G':True,
          'H':True,'I':True,'J':True,'K':True,'L':True,'M':True,'N':True,'O':True,'P':True,'Q':True,'R':True,
          'S':True,'T':True,'U':True,'V':True,'W':True,'X':True,'Y':True,'Z':True}

# This function uses a dictionary to store the STATE of each character.
# As we traverse the provided string, we will change the value of the key
# to False. If a character that has already been seen is found again, the
# program will terminate and thus, it is not a unique string. Otherwise,
# we do have a unique string.

# Cons: The downside to this solution is that we have to store all of the
# characters a-z and A-Z in memory.
def is_unique_0(myString):
    for index in myString:
        if myList[index]:
            myList[index] = False
        else:
            print("This is not a unique string.")
            return False


# Create an empty list. As we traverse the provided string, append each
# character to the list. Before appending the current character, we have to
# make sure that the character is not already in the list. If it is, then
# we do not have a unique string. Otherwise, we do have a unique string.

# Pros: The upside to this solution is that we don't have to store all the
# possible values beforehand.
def is_unique_1(myString):
    record = []

    for index in myString:
        if index not in record:
            record.append(index)
        else:
            print("This is not a unique string.")
            return False


if __name__ == '__main__':
    myString = "Hello"

    # Let's make sure that this is actually a string.
    assert myString.isalpha(), "Ooops, this is not a valid string."

    is_unique_0(myString)
    is_unique_1(myString)