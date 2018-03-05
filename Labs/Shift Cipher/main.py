# The ord() method returns an integer representing 
#  Unicode code point for the given Unicode character.

# Equation : C = (M + P) mod 26 , 26 because 25 Alphabets Charaters
# C : Cipher Number
# M : Charater Value = ord(strValue)-65 , -65 because 'A' starts at 65
# P : Offset , this case 5
print("Shift Cipher Lab")
def shiftCipher(someString):
    print("going to Cipher: %s" % someString)
    cipherList = [ ] # Empty List
    newString = [ ]
    i = 0
    
    for i in range(len(someString)):
        intValue = ((ord(someString[i])-65) + 5) % 26
        cipherList.append(intValue)
    
    for j in range(len(cipherList)):
        cipherList[j] = cipherList[j] + 65
        newString.append(chr(cipherList[j]))
    
    value = ''.join(newString)
    return value

strValue = shiftCipher("Hello World")
print('Chiper Message: %s' % strValue)
