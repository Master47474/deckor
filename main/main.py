"""
    Marcus F
    Entry Point for Deckor
"""

#Imports
import sys
import session

from text import text


def init():
    """
    Init Function for Deckor
    Called First on Startup
    """
    print("\nWelcome to Deckor")

    # arguments on load?
    n = len(sys.argv)
    if n > 1:
        print("\nLoaded ciphertext")
        print("Arguments passed:", end = " ")
        for i in range(1, n):
            print(sys.argv[i], end = ", ")
        print("\n")
        file = sys.argv[1]


        ciphertext = None
        with open(file, 'r') as file:
            ciphertext = file.read()
            print(f"Ciphertext Loaded from file: \n{ciphertext}\n")
        return text(ciphertext)

def main():
    ciphertext = init()
    session.startSession(ciphertext)



if __name__ == "__main__":
    main()
