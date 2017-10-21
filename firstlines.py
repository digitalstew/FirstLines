################################################
#   firstlines.py  Python 3.6.2                                                                        #
#  1) read poetry first line files                                                                      #
#  2) turn each first line input file into a sorted frequency dictionary     #
#  >>>>  All code released as open source with no usage restrictions     #
################################################

# used to strip punctuation marks
import string

### ------ options ------ ###
RemoveCommon = True
# subset of most common words
CommonWords = ['the', 'to', 'of', 'and', 'a']
# optional freq limit, set to 0 to output all
optionalQty = 0
# optional output
GenerateScreenOutput = False
GenerateFileOutput = True

# input file names
f_rossetti = "225 First Lines from Christina Georgina Rossetti.txt"
f_dickinson = "225 First Lines from Emily Dickinson.txt"
f_longfellow = "225 First Lines from Henry Wadsworth Longfellow.txt"
f_emerson = "225 First Lines from Ralph Waldo Emerson.txt"
f_teasdale = "225 First Lines from Sara Teasdale.txt"
f_whitman = "225 First Lines from Walt Whitman.txt"


# strings for output display
rossetti = "Christina George Rossetti"
dickinson = "Emily Dickinson"
longfellow = "Henry Wadsworth Longfellow"
emerson = "Ralph Waldo Emerson"
teasdale = "Sara Teasdale"
whitman = "Walt Whitman"

########################################## 

# read a file, return the contents in a string    
def readInputFile(fileName):
    f = open(fileName , 'r')
    textInputString = f.read()
    f.close
    return textInputString

# takes a string, splits it and turns it into a list, returning the list
def stringToList(inputString):
    inList = inputString.split()
    return inList

#  takes a list of words and turns it into a frequency dictionary, returning the dictionary 
def listToFreqDict(inputList):
    wordFreq = [inputList.count(p) for p in inputList]
    return dict(zip(inputList,wordFreq))

# sorts a frequency dictionary in descending order
def sortFreqDict(inputFreqDict):
    result = [(inputFreqDict[key], key) for key in inputFreqDict]
    result.sort()
    result.reverse()
    return result
 
 # convert the input list into a sorted freq dictionary    
def getSortedFreqDict(inLst):
    tmpFreqDict = listToFreqDict(inLst)
    tmpSortedFreqDict = sortFreqDict(tmpFreqDict)
    return tmpSortedFreqDict   


# text processing is messy business, many times custom cleanup is required 
# clean up the string and return a list
def CleanupInput(inStr):
    # change strings to lower case    
    inStr = inStr.lower()
    #clean up some dashes and apostrophes
    inStr = inStr.replace("'", "")
    inStr = inStr.replace("-", "")
    # change string into a list
    words = inStr.split()
    #strip out punctuation    
    tempList = [w.strip( string.punctuation) for w in words]
    #remove all the common words 
    cleanList = []    
    if RemoveCommon:
        for item in tempList:
            if not(item in CommonWords):
                cleanList.append(item)       
        return cleanList
    else:
        return tempList
 
  
def generateScreenOutput(poetName, poetSortedDict):
    print(poetName)
    for item in poetSortedDict: 
        tmpstr = str(item)
        #remove all python dictionary characters
        tmpstr = tmpstr.replace("(", "")
        tmpstr = tmpstr.replace(")", "")   
        tmpstr = tmpstr.replace("'", "")
        tmpstr = tmpstr.replace('"', "")
        #optional freq output
        tmplst = tmpstr.split(',')
        if ( int(tmplst[0]) >= optionalQty):
            print (tmpstr)
    print()          
   
    
def generateFileOutput(poetName, poetSortedDict):
    filename = 'firstline_frequency_' + poetName + '.csv'
    f = open(filename, "w")
    f.write(poetName + '\r\n' )
    f.write('useage count' + ' , ' + 'word used' + '\r\n')
    for item in poetSortedDict: 
        tmpstr = str(item)
        #remove all python dictionary characters
        tmpstr = tmpstr.replace("(", "")
        tmpstr = tmpstr.replace(")", "")   
        tmpstr = tmpstr.replace("'", "")
        tmpstr = tmpstr.replace('"', "")
        #optional freq output
        tmplst = tmpstr.split(',')
        if ( int(tmplst[0]) >= optionalQty):
            f.write(tmpstr +'\r\n') 
    f.close()
    
############ main ##########################

## read the files
s_rossetti = readInputFile(f_rossetti)
s_dickinson = readInputFile(f_dickinson)
s_longfellow = readInputFile(f_longfellow)
s_emerson = readInputFile(f_emerson)
s_teasdale = readInputFile(f_teasdale)
s_whitman  = readInputFile(f_whitman )

##  clean up the input and turn it into a list
l_rossetti = CleanupInput(s_rossetti)
l_dickinson = CleanupInput(s_dickinson)
l_longfellow = CleanupInput(s_longfellow)
l_emerson = CleanupInput(s_emerson)
l_teasdale = CleanupInput(s_teasdale)
l_whitman  = CleanupInput(s_whitman)

## get the sorted freq dictionary for each poet
sfd_rossetti = getSortedFreqDict(l_rossetti)
sfd_dickinson = getSortedFreqDict(l_dickinson)
sfd_longfellow = getSortedFreqDict(l_longfellow)
sfd_emerson = getSortedFreqDict(l_emerson)
sfd_teasdale = getSortedFreqDict(l_teasdale)
sfd_whitman  = getSortedFreqDict(l_whitman )

## print out to the console
if (GenerateScreenOutput):
    generateScreenOutput( rossetti, sfd_rossetti)
    generateScreenOutput( dickinson, sfd_dickinson)
    generateScreenOutput( longfellow, sfd_longfellow)
    generateScreenOutput( emerson, sfd_emerson)
    generateScreenOutput( teasdale, sfd_teasdale)
    generateScreenOutput( whitman, sfd_whitman)

#print out to a text file
if (GenerateFileOutput):
    generateFileOutput( rossetti, sfd_rossetti)
    generateFileOutput( dickinson, sfd_dickinson)
    generateFileOutput( longfellow, sfd_longfellow)
    generateFileOutput( emerson, sfd_emerson)
    generateFileOutput( teasdale, sfd_teasdale)
    generateFileOutput( whitman, sfd_whitman)



