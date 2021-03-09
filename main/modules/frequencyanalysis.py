"""
    Marcus F
    This will be where frequency analysis logic is kept
"""

# only lowercase for now
freqFromTexts = [8.2,1.5,2.8,4.3,13,2.2,2,6.1,7,0.15,0.77,4,2.4,6.7,7.5,1.9,0.095,6,9.3,9.1,2.8,0.98,2.4,0.15,2,0.074]
freqFromDict =  [7.8,2,4,3.8,11,1.4,3,2.3,8.6,0.21,0.97,5.3,2.7,7.2,6.1,2.8,0.19,7.3,9.7,6.7,3.3,1,0.91,0.27,1.6,0.44]


def frequencyanalysis(ciphertext):


    #Data from wiki/letter_frequency (alot of rounding so sum >=~~ 100 )

    freqFromCiphertext = [0] * 26
    totalchars = 0

    for c in ciphertext:
        if(c == " "):
            continue
        if(ord(c) < 97 or ord(c) > 123):
            print("This Ciphertext is not avaliable for frequency analysis")
            return
        #print(f"{c} is ord({ord(c)})-97 = {ord(c)-97}")
        freqFromCiphertext[ord(c)-97] += 1
        totalchars += 1

    for i in range(26):
        freqFromCiphertext[i] = freqFromCiphertext[i]/totalchars * 100

    print("\tDONE")

    if( input("Would you Like to print the results [y/n] : ").lower() == 'y'):
        printResults(freqFromCiphertext)
    else:
        pass


def printResults(freqtable):
    print("Results")
    for i in range(26):
        print(f"{chr(97 + i)} is {freqtable[i]}%")

    #for i in range(26):
    #    print(f"{chr(97 + i)} : {freqFromTexts[i]}% and {freqFromDict[i]}%")
