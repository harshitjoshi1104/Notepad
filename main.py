# Importing all required modules as per  needed by this software/project by harshit joshi

import os
import tkinter
import time
# import tty
from PIL import Image,ImageTk
from tkinter import StringVar, Text, font
from tkinter.constants import ANCHOR, END, GROOVE, LEFT, RIGHT, SUNKEN 
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
# from typing import List, final


# Creating root window
root=tkinter.Tk()
root.geometry("800x600")
root.title("Untitled")

absoluteTheme="light"
#############################################################################################################################
#############################################################################################################################
# creating funtions for menubar
def colorLight():
    global absoluteTheme
    global imageULine
    global imageItalic
    global imageBold
    absoluteTheme="light"
    root.config(bg="white")
    file_menu.config(bg="white",fg="black")
    imageBold=tkinter.PhotoImage(file="images/Icon-bold.png")
    boldFont.config(image=imageBold)
    imageULine=tkinter.PhotoImage(file="images/Icon-underline.png")
    imageItalic=tkinter.PhotoImage(file="images/Icon-italic.png")
    italicFont.config(image=imageItalic)
    underlineFont.config(image=imageULine)
    textArea.config(bg="white",fg="black")

def colorDark():
    global absoluteTheme
    global imageBold
    global imageItalic
    global imageULine
    absoluteTheme="dark"
    root.config(bg="black")
    file_menu.config(bg="black",fg="white")
    edit_menu.config(bg="black",fg="white")
    color_theme_menu.config(bg="black",fg="white")
    file_menu.config(bg="black",fg="white")
    boldFont.config(bg="black",fg="white")
    italicFont.config(bg="black",fg="white")
    underlineFont.config(bg="black",fg="white")
    fontSelection.config(bg="black",fg="white")
    imageBold=tkinter.PhotoImage(file="images/Icon-bold-dark.png")
    boldFont.config(image=imageBold)
    imageItalic=tkinter.PhotoImage(file="images/Icon-italic-dark.png")
    italicFont.config(image=imageItalic)
    imageULine=tkinter.PhotoImage(file="images/Icon-underline-dark.png")
    underlineFont.config(image=imageULine)


    textArea.config(bg="black",fg="white",insertbackground="white")


def colorMODark():
    global absoluteTheme
    global imageItalic
    global imageBold
    global imageULine
    absoluteTheme="dark"
    root.config(bg="#11131C")
    file_menu.config(bg="#11131C",fg="white")
    edit_menu.config(bg="#11131C",fg="white")
    color_theme_menu.config(bg="#11131C",fg="white")
    fontSelection.config(bg="#11131C",fg="white")
    boldFont.config(bg="#11131C",fg="white")
    italicFont.config(bg="#11131C",fg="white")
    underlineFont.config(bg="#11131C",fg="white")
    imageBold=tkinter.PhotoImage(file="images/Icon-bold-dark.png")
    boldFont.config(image=imageBold)
    imageItalic=tkinter.PhotoImage(file="images/Icon-italic-dark.png")
    italicFont.config(image=imageItalic)
    imageULine=tkinter.PhotoImage(file="images/Icon-underline-dark.png")
    underlineFont.config(image=imageULine)
   
    textArea.config(bg="#11131C",fg="white",insertbackground="white")

def colorMoDeep():
    pass

def colorBlue():
    pass

file=None

def newFileCreate():
    global file
    root.title("Untitled     - JusT@Notepad")
    file=None
    textArea.delete(1.0,END)

def openFile():
    global file

    file=askopenfilename(defaultextension='.txt',filetypes=[("All files","*.*"),("Text Document","*.txt")])

    if file=="":
        file=None
    else:
        textArea.delete(1.0,END)
        root.title(os.path.basename(file)+ ' - JusT@Notepad')
        f=open(file,'r')
        textArea.insert(1.0,f.read())
        f.close()


def saveFileSome():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[("All files","*.*"),("Text Document","*.txt")])

        if file=="":
            file=None

        else:
            f=open(file,"w")
            f.write(textArea.get(1.0,END))
            root.title(os.path.basename(file)+" - JusT@Notepad")
            f.close()
    
    else:
        f=open(file,"w")
        f.write(textArea.get(1.0,END))
        f.close()


# Creating menubar
my_menu=tkinter.Menu(root)
root.config(menu=my_menu)


    # file menu added
file_menu=tkinter.Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="📁 New",command=newFileCreate,font="Garamond 10 bold")
file_menu.add_command(label="📁 Open",command=openFile,font="Garamond 10 bold")
file_menu.add_command(label="📃 Save",command=saveFileSome,font="Garamond 10 bold")
file_menu.add_command(label="📄 SaveAs",command=saveFileSome,font="Times 10")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=lambda:root.destroy())

    # edit menu added

edit_menu=tkinter.Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Edit",menu=edit_menu)

edit_menu.add_command(label="🔎 View",command=None,font="Garamond 10 bold")
edit_menu.add_command(label="❌ Cut",command=None,font="Garamond 10 bold")
edit_menu.add_command(label="Copy",command=None)
edit_menu.add_command(label="Paste",command=None)

    # color menu
color_theme_menu=tkinter.Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Theme",menu=color_theme_menu)

color_theme_menu.add_command(label="Light",command=colorLight)
color_theme_menu.add_command(label="Dark",command=colorDark)
color_theme_menu.add_command(label="Material Ocean Dark",command=colorMODark)
color_theme_menu.add_command(label="Material ocean deep",command=colorMoDeep)
color_theme_menu.add_command(label="Blue",command=colorBlue)

###############################################################################################################################
#################################################################################################################################

#### creating mainframe menu buttons
mainFrame=tkinter.Frame(root,bg="wheat")
mainFrame.pack(fill="x")

fontList1=["Helvetica","Garamond","Times"]
variableFont=StringVar(root)
variableFont.set("Garamond")

InitialFontSize="16"
InitialFont="Garamond"
InitialBold=""
InitialItalic=""
InitialUnderline=""
finalFontFamily=InitialFont+" "+InitialFontSize+" "+InitialBold+" "+InitialItalic+" "+InitialUnderline
isBold=False

def fontTriggerd(event):
    global InitialFont
    global finalFontFamily
    InitialFont=variableFont.get()
    finalFontFamily=InitialFont+" "+InitialFontSize+" "+InitialBold+" "+InitialItalic+" "+InitialUnderline
    textArea.config(font=finalFontFamily)

def makeFontBold():
    global absoluteTheme
    global InitialBold
    global finalFontFamily
    global isBold
    global imageBold
    if InitialBold=="bold":
        isBold=False
        InitialBold=""
        finalFontFamily=InitialFont+" "+InitialFontSize+" "+InitialBold+" "+InitialItalic+" "+InitialUnderline
        textArea.config(font=finalFontFamily)
        if absoluteTheme=="light":
            imageBold=tkinter.PhotoImage(file="images/Icon-bold.png")
            boldFont.config(image=imageBold)
        else:
            imageBold=tkinter.PhotoImage(file="images/Icon-bold-dark.png")
            boldFont.config(image=imageBold)

    else:
        isBold=True
        InitialBold="bold"
        finalFontFamily=InitialFont+" "+InitialFontSize+" "+InitialBold+" "+InitialItalic+" "+InitialUnderline
        textArea.config(font=finalFontFamily)
        imageBold=tkinter.PhotoImage(file="images/Icon-bold-Selected.png")
        boldFont.config(image=imageBold)

def makeFontItalic():
    global InitialItalic
    global finalFontFamily
    global imageItalic
    if InitialItalic=="":
        InitialItalic="italic"
        finalFontFamily=InitialFont+" "+InitialFontSize+" "+InitialBold+" "+InitialItalic+" "+InitialUnderline
        textArea.config(font=finalFontFamily)
        imageItalic=tkinter.PhotoImage(file="images/Icon-italic-Selected.png")
        italicFont.config(image=imageItalic)

    else:
        InitialItalic=""
        finalFontFamily=InitialFont+" "+InitialFontSize+" "+InitialBold+" "+InitialItalic+" "+InitialUnderline
        textArea.config(font=finalFontFamily)
        if absoluteTheme=="light":
            imageItalic=tkinter.PhotoImage(file="images/Icon-italic.png")
            italicFont.config(image=imageItalic)
        else:
            imageItalic=tkinter.PhotoImage(file="images/Icon-italic-dark.png")
            italicFont.config(image=imageItalic)

def makeFontUnderline():
    global InitialUnderline
    global finalFontFamily
    global imageULine
    if InitialUnderline=="":
        InitialUnderline="underline"
        finalFontFamily=InitialFont+" "+InitialFontSize+" "+InitialBold+" "+InitialItalic+" "+InitialUnderline
        textArea.config(font=finalFontFamily)
        imageULine=tkinter.PhotoImage(file="images/Icon-underline-Selected.png")
        underlineFont.config(image=imageULine)

    else:
        InitialUnderline=""
        finalFontFamily=InitialFont+" "+InitialFontSize+" "+InitialBold+" "+InitialItalic+" "+InitialUnderline
        textArea.config(font=finalFontFamily)
        if absoluteTheme=="loght":
            imageULine=tkinter.PhotoImage(file="images/Icon-underline.png")
            underlineFont.config(image=imageULine)
        else:
            imageULine=tkinter.PhotoImage(file="images/Icon-underline-dark.png")
            underlineFont.config(image=imageULine)
    

def makeAlignLeft():
    textArea.tag_configure("left",justify='left')
    textArea.tag_add("left",1.0,END)
    # textArea.config(padx=20)

def makeAlignRight():
    textArea.tag_configure("right",justify='right')
    # textArea.config(justify=)
    textArea.tag_add("right",1.0,END)
    # textArea.config(padx=20)
    textArea.pack()

def makeAlignCenter():
    textArea.tag_configure("center",justify='center')
    textArea.tag_add("center",1.0,END)
    textArea.pack()


fontSelection=tkinter.OptionMenu(mainFrame,variableFont,*fontList1,command=fontTriggerd)
fontSelection.pack(side=LEFT)

imageBold=tkinter.PhotoImage(file="images/Icon-bold.png")

boldFont=tkinter.Button(mainFrame,image=imageBold,command=makeFontBold,relief=GROOVE)
boldFont.pack(side="left")

imageItalic=tkinter.PhotoImage(file="images/Icon-italic.png")

italicFont=tkinter.Button(mainFrame,image=imageItalic,command=makeFontItalic,relief=GROOVE)
italicFont.pack(side="left")

imageULine=tkinter.PhotoImage(file="images/Icon-underline.png")

underlineFont=tkinter.Button(mainFrame,image=imageULine,command=makeFontUnderline,relief=GROOVE)
underlineFont.pack(side="left")

# imgLAlign=Image.open("left-align-icon-10.png","rb")
# tkinter.PhotoImage()

imageLA=tkinter.PhotoImage(file="images/left-align-icon-10.png")

leftAlign=tkinter.Button(mainFrame,image=imageLA,command=makeAlignLeft,relief=GROOVE)
leftAlign.pack(side="left")

imageCA=tkinter.PhotoImage(file="images/center-align.png")

centeralign=tkinter.Button(mainFrame,image=imageCA,command=makeAlignCenter,relief=GROOVE)
centeralign.pack(side="left")

imageRA=tkinter.PhotoImage(file="images/right-align.png")

rightAlign=tkinter.Button(mainFrame,image=imageRA,command=makeAlignRight,relief=GROOVE)
rightAlign.pack(side="left")
# fontSelection.bind()
# l1=tkinter.Label(mainFrame,text="Hello")
# l1.pack(side="left")
############################################################################################################################
############################################################################################################################

#  main textArea
textArea=tkinter.Text(root,font=finalFontFamily)
textArea.pack(fill="both",expand=True)



scroll=tkinter.Scrollbar(textArea)
scroll.pack(side="right",fill="y")

scroll.config(command=textArea.yview)
textArea.config(yscrollcommand=scroll.set)



root.mainloop()