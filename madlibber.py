'''
Description: Enter the name of the Mad lib template and this program will that 
    file,print out some specifics regarding the file, and lets the user input 
    the missing parts of speech, then it reads it out from a new file.
'''

def print_report(input_file): #prints out all the statistics for the madlib template
    sVowels = "aeiou"
    sConstants = "qwrtypsdfghjklzxcvbnm"
    iV = 0 #vowels
    iC = 0 #consonants
    iW = 0 #whitespace
    iP = 0 #punctuation
    
    sInput = ""
    with open (input_file, "r") as f:
        for s in f:
            for char in s:
                if char in sConstants:
                    iC = iC + 1
                    continue
                if char in sVowels:
                    iV = iV + 1
                    continue
                if char.isspace():
                    iW = iW + 1
                    continue
                else:
                    iP = iP + 1
    iT = iV + iC + iW + iP

    #print("----------"+ input_file + "---------\n")
    print("{:-^25}".format(input_file))
    print("Vowels:                  " + str(iV) + "\n")
    print("Consonants:              " + str(iC) + "\n")
    print("Whitespace:              " + str(iW) + "\n")
    print("Punctuation:             " + str(iP) + "\n")
    print("-------------------------\n")
    print("Total:                   " + str(iT) + "\n\n")
    
    print("Percent vowels:         " + str(round((iV/iT)*100, 1)) + "\n")
    print("Percent consonants:     " + str(round((iC/iT)*100, 1)) + "\n")
    print("Percent spaces:         " + str(round((iW/iT)*100, 1)) + "\n")
    print("Percent punctuation:    " + str(round((iP/iT)*100, 1)) + "\n")
    print("{:=^25}".format(''))


def replace_parts_of_speech(part, label): #Asks the user to enter the missing parts of speech
    iCount = part.count(label)
    for i in range(0,iCount):
        part = part.replace(label, input("Enter " + label.lower() + ": "), 1)
        
    return part
    
def complete_mad_lib(sFile): #Actually compiles the mad lib paragraph
    data = ""
    with open (sFile, "r") as file:
        data = file.read()
    sList = ["PLURAL NOUN", "VERB PAST", "VERB", "NOUN", "ADJECTIVE"]
    for s in sList:
        data = replace_parts_of_speech(data, s)
    print(data)
    
def main():
    '''
    Asks the user which template to use,
    prints out the report for that template,
    and then actually plays the Mad-Lib game,
    replaces the missing parts of speech, and then prints it out
    ''' 
    sFile = input("Enter Name of Mad-Lib Template File:")
    print_report(sFile)
    complete_mad_lib(sFile)

if __name__ == '__main__':
    main()
