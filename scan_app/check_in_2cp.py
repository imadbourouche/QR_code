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


#Open the excel file that contains the contacts
#You can find an exmeple here : https://docs.google.com/spreadsheets/d/1IXea1Y45zdlFLKj0hYHyh94zLMwl5kHJ6XTPO0VGKYE/edit?usp=sharing



#tkinter
root = Tk()
root.attributes('-zoomed', True)
#root.iconify()


PATH= "2cp_list.csv"
DAY="DAY1"
# Create a frame
app = Frame(root, bg="white")
app.grid(row=0, column=1)


sf= TkFont.Font(family='Helvetica', size=16)
ssf= TkFont.Font(family='Helvetica', size=16,weight="bold")


name_personne = Label(root ,text="Hello",fg='white',background='#26c952',height=3,width=35,font=ssf)
name_personne.place(relx=0.00001,rely=0.02)
 

liste = Listbox(root,width=35,height=23,selectbackground="red",selectmode="SINGLE",font=sf)
liste.grid(row=0, column=0)

# Create a label in the frame
lmain = Label(app)
lmain.grid()
#row=1, column=0

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
        if((text.isnumeric())and (int(text)<lenn+1)and(int(text)>0)):
               #add the element if it's not checked
            if(df.loc[int(text)-1,DAY] == "non") :
                df.loc[int(text)-1, DAY] = str(datetime.date.today()) + " " +str(datetime.datetime.now().time().strftime('%H:%M:%S'))
                df.to_csv(PATH, index=False)
                print(df.loc[int(text)-1,'NOM']+" "+df.loc[int(text)-1,'PRENOM']+df.loc[int(text)-1,'GROUPE']+" "+df.loc[int(text)-1,DAY]+" CHECKED")
                print("------------------")
                name_personne['text'] = df.loc[int(text)-1,'NOM']+" "+df.loc[int(text)-1,'PRENOM']+" "+df.loc[int(text)-1,'GROUPE']
                liste.insert(END,df.loc[int(text)-1,'NOM']+" | "+df.loc[int(text)-1,'PRENOM']+" | "+df.loc[int(text)-1,'GROUPE'])                
                liste.see(END)
                liste.insert(END,"----------------------------")
                mixer.init()
                mixer.music.load("audio.wav")
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
liste.insert(END," ")
for f in df.values:
    if(f[5]!="non"):
        liste.insert(END,f[2]+" | "+f[3]+" | "+f[4])
        liste.insert(END,"----------------------------")

print("------- START CHECKING --------")

video_stream()
root.mainloop()


