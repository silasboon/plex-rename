from distutils import extension
import os
import re
import requests


# TODO: add thetvdb api functionality
# TODO: allow recursive sub-folder access
# TODO: automatically create directories for shows and seasons
# TODO: differentiate between shows and movies
# TODO: allow access to server to move files into respective directories or create new directory if not exists



#convert list to string
def listToString(s):
    string1 = '' 
    return (string1.join(s))

#clean up show name
def cleanUpName(showName, showEpisdode):
    #only capitalize first letter
    showName = showName.title()
    #concatinate show info and season info
    fullName = showName + ' ' + showEpisdode
    #replace '.' with a space 
    fullName = fullName.replace('.', ' ')
    #remove anything within parentheses
    fullName = re.sub("[\(\[].*?[\)\]]", "", fullName)
    #remove special characters
    fullName = re.sub("-", '', fullName)
    #remove extra spaces
    fullName = " ".join(fullName.split())
    return(fullName)

#Get show season and episode and convert to upper case if not already 
def showInfo(file):
    showInfo = ''
    #get SXXEXX information
    upperCase = re.findall('S[0-9][0-9]E[0-9][0-9]', file)
    lowerCase = re.findall('s[0-9][0-9]e[0-9][0-9]', file)
    #convert to string
    upperCase = listToString(upperCase)
    lowerCase = listToString(lowerCase)
    #if string is None then pass (uppercase)
    if len(upperCase) == 0:
        pass
    #else return uppercase (no changes made)
    else:
        return(upperCase)
    #if string is none then pass (lowercase)
    if len(lowerCase) == 0:
        pass
    #else convert showInfo to string and then convert to uppercase and return showInfo 
    else: 
        showInfo = listToString(lowerCase)
        showInfo = showInfo.upper()
        return(showInfo)

#Get show name information
def getShowName(file):
    #convert entire string to uppercase
    tempShowName = file.upper()
    #Split season info from the rest of the text
    showName = re.split('S[0-9][0-9]E[0-9][0-9]', tempShowName)
    #convert text to string
    #showName = listToString(showName)
    #Capitalize first letter of every word 

    return showName

def renameFile():
    # Path to files
    path = '/Users/silas/Torrents/Complete/'
    files = os.listdir(path)
    #loop through all files
    for file in files:
        #assign original name to variable 
        original = file
        #seperate extension from name
        name, extension = os.path.splitext(file)
        seasonEpisode = showInfo(file)
        #get show name 
        showName = getShowName(file)
        #assign to new variables and remove extra words
        SE = seasonEpisode
        SN = listToString(showName[0])
        #error check if SE does not exist (not a show file i.e a DS_Store file or script)
        if SE == None:
            pass 
        else:  
            #clean up and concat showName and seasonEpisode
            finalName = cleanUpName(SN, SE)
            #rename files 
            os.rename(path + '/' + original, path + '/' + finalName + extension)

renameFile()