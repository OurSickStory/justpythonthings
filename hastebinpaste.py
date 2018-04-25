import os
import requests
import pathlib

def filesearch(string):
    '''searches for a file in the current dir based on the user request'''
    stringsearch = string
    lockFile = False
    filesFound = []
    extFound = []
    for file in os.listdir("."):
        ext = os.path.splitext(file)[-1].lower()
        filename = os.path.splitext(file)[0].lower()
        findfile = stringsearch + ext
        if stringsearch not in filename:
            pass

        else:
            filesFound.append(findfile)
            extFound.append(ext)
            lockFile = True

    if lockFile == False:
        print("We didn\'t Find Anything matching '{}'.".format(stringsearch))

    if lockFile == True:
        stringtohaste = filesFound[0]
        ext = extFound[0]
        if len(filesFound) == 1:
            hastebinpaste(stringtohaste, ext)
        else:
            print("we found these files that match your query {}".format(filesFound))
            userresponse(extFound, stringsearch)


def userresponse(ext,filename):
    '''**extension, *filename - if more then one file found with that name it will ask which file you want to upload'''
    user_input = ''
    stringsearch = filename
    myList = ext
    while user_input != "!quit":
        user_input = input('Type the extension of the file you\'d like to upload:')
        if user_input in myList:
            send_to_paste = stringsearch + user_input
            hastebinpaste(send_to_paste, user_input)
        else:
            print('that doesnt seem to be a file we found...')


def hastebinpaste(filename, ext):
    '''just a double check to see if that exact file name + ext you provided exists again'''
    filepath = pathlib.Path(__file__)
    try:
        if filepath.is_file():
            f = open(filename, "r")
            string = f.read()
            post(string, ext)
    except OSError:
        print('can\'t find that file')


def post(content, ext):
    '''sends the file to hastebin'''
    ext = ext
    post1 = requests.post("https://hastebin.com/documents", data=content.encode('utf-8'))
    response = "https://hastebin.com/" + post1.json()["key"] + ext
    print('Successfully uploaded your file to {}'.format(response))
