print("Hello")
userInput='abc'

option=input("d or e?")
print("User input?",userInput)

incBy=input("key?")

key=int(incBy)

if option is 'e':
    encryptedOutput=''
    for ch in userInput:
        asc=ord(ch)
        asc=asc+key
        newCh=chr(asc)
        encryptedOutput= encryptedOutput+newCh
    
    print("Encrypted user input", encryptedOutput)

else:
    decryptedOutput=''
    for ch in userInput:
        asc=ord(ch)
        asc=asc-key
        newCh=chr(asc)   
        decryptedOutput=decryptedOutput +newCh
    print("Receiver Output:", decryptedOutput)