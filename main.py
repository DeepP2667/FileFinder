import os
from datetime import datetime
import PySimpleGUI as sg
import time


os.chdir('/Users/deepp/Desktop/')
print(os.getcwd())
print('Hello')
sg.theme('dark grey 9')

layout=[[sg.Text("Enter a file name or keyword")],
        [sg.Text("Please type in all lowercase")],
        [sg.Input(key='-INPUT-')],
        [sg.Text(size=(40,1), key='-OUTPUT-')],
        [sg.Button('Enter'),sg.Button('Quit')]]



def find_file(values):                          #Search through computer for files with that word
    user_filename=values
    files=[]
    for dirpath, dirnames, filenames in os.walk('/Users/deepp/Desktop/'):
        for i in filenames:
            i=i.lower()
            if user_filename in i:
                files.append(i)

    return files


def Upper_find_file(values):                          #To print out the file name without all lowercase
    user_filename=values
    files=[]
    for dirpath, dirnames, filenames in os.walk('/Users/deepp/Desktop/'):
        for x in range(len(filenames)):
            if(user_filename in filenames[x].lower()):
                files.append(filenames[x])

    return files


def update_window(files_found):                                     #New window to print all the files found
    layout2=[]
    for i in range(len(files_found)):
        layout2+=[[sg.Button(files_found[i],key=files_found[i],size=(150,1))]]

    return layout2

def Insert_Scroll(layout2):                                                         #Inserts a scroll
    layout3=layout2
    layout3=[[sg.Column(layout2,scrollable=True,size=(1500,1500))]]
    return layout3

def Open_File(events2):                                                             #Finds the path name to open the file
    for dirpath, dirnames, filenames in os.walk('/Users/deepp/Desktop/'):
        if(events2 in filenames):
            return dirpath
    return dirpath


window= sg.Window('File Finder',layout)

while True:

    events, values= window.read()
    if(events==sg.WINDOW_CLOSED or events=='Quit'):                   #Closes window when quit or x is clicked
        break

    values_found=values['-INPUT-']                                    #Gets the value of the input
    files_found=find_file(values_found)                               #Returns the list of files found
    Upper_files=Upper_find_file(values_found)                         #Returns the original file names

    if(files_found==[]):                                              #Tells if no file was found
        window['-OUTPUT-'].update("No files found with this word")



    if(files_found!=[]):                                              #When there are files with the name
        window['-OUTPUT-'].update("")                                 #Allows for re entering word without keeping text

        time.sleep(1)
        window2 = sg.Window('Files Found', Insert_Scroll(update_window(Upper_files))).Finalize()
        window2.Maximize()
        events2, values2 = window2.read()
        if(events2 in Upper_files):
            os.startfile('C:{}/{}'.format(Open_File(events2),events2))
            time.sleep(2)
            sg.popup("File Location C:{}/{}".format(Open_File(events2),events2))


