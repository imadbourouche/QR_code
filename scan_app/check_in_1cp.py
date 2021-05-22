import cv2
import numpy
import pyzbar.pyzbar as pyzbar
import pandas as pd
import datetime
import time
from tkinter import *
import tkinter.font as TkFont
from pygame import mixer
from PIL import ImageTk, Image

#tkinter

root = Tk()
root.attributes('-zoomed', True)
#root.iconify()


PATH= "1cp_list.xlsx"
DAY="DAY1"
# Create a frame
app = Frame(root, bg="white")
app.grid()


sf= TkFont.Font(family='Helvetica', size=16)

liste = Listbox(root,width=49,height=24,selectbackground="red",selectmode="SINGLE",font=sf)
liste.grid(row=0, column=1)

# Create a label in the frame
lmain = Label(app)
lmain.grid(row=1, column=0)


#start the video capture
cap = cv2.VideoCapture(0)

# function for video streaming
def video_stream():

    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    frame = cv2.flip(frame, 1)
    ractangle = cv2.rectangle(frame,(200,120),(430,340),(0,0,255),2)
    #the font to display text in the video
    
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    lenn=len(df)
    for obj in decodedObjects:
        #extracte the data from the qrcode
        text= str(obj.data)
        text = text[2:len(text)-1]
        cv2.putText(frame, text, (20,90), font, 2,(0, 0, 255), 3)
        print(int(text))
        if((text.isnumeric())and (int(text)-300<lenn+1)and(int(text)-300>0)):
               #add the element if it's not checked
            if(df.loc[int(text)-301,DAY] == "non") :
                df.loc[int(text)-301, DAY] = str(datetime.date.today()) + " " +str(datetime.datetime.now().time().strftime('%H:%M:%S'))
                df.to_csv(PATH, index=False)
                print(df.loc[int(text)-301,'NOM']+" "+df.loc[int(text)-301,'PRENOM']+df.loc[int(text)-301,'GROUPE']+" "+df.loc[int(text)-301,DAY]+" CHECKED")
                print("------------------")
                liste.insert(END,df.loc[int(text)-301,'NOM']+" | "+df.loc[int(text)-301,'PRENOM']+" | "+df.loc[int(text)-301,'GROUPE'])                
                liste.see(END)
                liste.insert(END,"----------------------------")
                mixer.init()
                mixer.music.load("checked.wav")
                mixer.music.play()

            else:
                #already checked
                cv2.putText(frame, "CHECKED", (20,60), font, 2,(0, 0, 255), 3)

        else:
            cv2.putText(frame, "WrongQR", (20,60), font, 2,(0, 0, 255), 3)


    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    img=img.resize((960,720))
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)




#read the sheet

df = pd.read_csv(PATH)

#check the form of the sheet befor inserting
liste.insert(END," ")
for f in df.values:
    if(f[5]!="non"):
        liste.insert(END,f[2]+" | "+f[3]+" | "+f[4])
        liste.insert(END,"----------------------------")

print("------- START CHECKING --------")

video_stream()
root.mainloop()

