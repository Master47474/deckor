"""
    Marcus F
    This will be where Session logic is kept
"""


from console import Console
import modules.frequencyanalysis as fa

from text import text

def startSession(ciphertext):
    console = Console(ciphertext)
    while(True):
        console.awaitcommand()
