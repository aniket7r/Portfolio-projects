import time
def morseEncode(x):
    if x == 'a':
        return "·-"
    elif x == 'b':
        return "-···"
    elif x == 'c':
        return "-·-·"
    elif x == 'd':
        return "-··"
    elif x == 'e':
        return "·"
    elif x == 'f':
        return "··-·"
    elif x == 'g':
        return "--·"
    elif x == 'h':
        return "····"
    elif x == 'i':
        return "··"
    elif x == 'j':
        return "·---"
    elif x == 'k':
        return "-·-"
    elif x == 'l':
        return "·-··"
    elif x == 'm':
        return "--"
    elif x == 'n':
        return "-·"
    elif x == 'o':
        return "---"
    elif x == 'p':
        return "·--·"
    elif x == 'q':
        return "--·-"
    elif x == 'r':
        return "·-·"
    elif x == 's':
        return "···"
    elif x == 't':
        return "-"
    elif x == 'u':
        return "··-"
    elif x == 'v':
        return "···-"
    elif x == 'w':
        return "·--"
    elif x == 'x':
        return "-··-"
    elif x == 'y':
        return "-·--"
    elif x == 'z':
        return "--··"
    elif x == '1':
        return "·----";
    elif x == '2':
        return "··---";
    elif x == '3':
        return "···--";
    elif x == '4':
        return "····-";
    elif x == '5':
        return "·····";
    elif x == '6':
        return "-····";
    elif x == '7':
        return "--···";
    elif x == '8':
        return "---··";
    elif x == '9':
        return "----·";
    elif x == '0':
        return "-----";
    elif x == " ":
        return "   "
 

def morseCode(signal):
    for character in signal:
        print(morseEncode(character), end = " ")
    time.sleep(10)
 

if __name__ == "__main__":
    signal = input("Enter the word:  ")
    morseCode(signal)
    
#  IMPORTANT TAKE AWAYS
# __name__= "__main__" indicate that the file is a script and it can be runned. when imported the script into another file it doesn't run script by its own.
# character or char is the characters of the string
# print(something, end = ""). print() prints the in the next line by deault but using end = "" we can litteraly put anything between two succesive prints.