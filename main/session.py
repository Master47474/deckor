"""
    Marcus F
    This will be where Session logic is kept
"""


from console import Console
import modules.frequencyanalysis as fa


def startSession(ciphertext):
    console = Console(ciphertext)
    while(True):
        console.awaitcommand()




"""

def deducecommand(args):
    print("Args : " , args)

    command = args[0]
    if(command == "help" or command == "HELP"):
        help()
    elif(command == "FREQA"):
        #look for flags
        for arg in args[1:]:
            pass
        ciphertext = args[1]
        print("No ciphertext provided using loaded ciphertext")
        fa.frequencyanalysis(ciphertext)



def help(args=None):
    if(args == None):
        print("\tFREQA\t\t : Use for Frequency Analysis")
"""
