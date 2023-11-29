from tkinter import *
import datetime
import time
import winsound

def ealarm(set_alarm):
    while True:
        time.sleep(1)
        livetime=datetime.datetime.now()
        current_time=livetime.strftime("%H:%M:%S")
        current_date=livetime.strftime("%d/%m/%Y")
        print(current_time,current_date)
        if current_time == set_alarm:
            print("wake up")
            winsound.PlaySound("sound1.wav",winsound.SND_ASYNC)
            break

def e_alarm():
    set_alarm=f"{ehour.get()}:{emin.get()}:{esec.get()}"
    ealarm(set_alarm)

root=Tk()
root.geometry("500x250")
root.title("Alarm Clock")
root.config(bg='#d5dfed')

lb1=Label(root,text="Hour Minute Second",font=('Arial,15,bold'),bg='#d5dfed')
lb1.place(x=175,y=20)
lb2=Label(root,text=("Set Time - "),font=('Arial,15,bold'),bg='#d5dfed')
lb2.place(x=5,y=75)
lb3=Label(root,text=" --Enter Time in 24-Hour Format-- ",font=('Arial,15,bold'),height=2,width=45,bg='#d5dfed',fg='Black')
lb3.place(x=0,y=190)

ehour=StringVar()
emin=StringVar()
esec=StringVar()
Hn=Entry(root,textvariable=ehour,font=('Arial,15,bold'),bg='#D3D3D3',width=4)
Hn.place(x=175,y=75)
Hn=Entry(root,textvariable=emin,font=('Arial,15,bold'),bg='#D3D3D3',width=4)
Hn.place(x=285,y=75)
Hn=Entry(root,textvariable=esec,font=('Arial,15,bold'),bg='#D3D3D3',width=4)
Hn.place(x=405,y=75)

btn=Button(root,text="Set Alarm",font=('Arial,10,bold'),bg='#FDF5E6',bd=4,command=e_alarm)
btn.place(x=200,y=130)

root.mainloop()

