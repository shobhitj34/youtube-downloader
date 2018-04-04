from Tkinter import *
import tkFileDialog as filedialog
def browse_button():
    global folder_path
    filen = filedialog.askdirectory()
    folder_path.set(filen)
    addrN.insert(0,filen)


tubeDownload=Tk()
tubeDownload.title("tubeDownload")

Label(tubeDownload,text="URL").grid(row=0)
urlN=Entry(tubeDownload)
urlN.grid(row=0,column=1)

folder_path = StringVar()
addrN=Entry(tubeDownload)
addrN.grid(row=2, column=1)
Label(tubeDownload,text="Name").grid(row=3)
NameN=Entry(tubeDownload)
NameN.grid(row=3,column=1)

button2 = Button(text="Browse", command=browse_button)
button2.grid(row=2, column=0)

#progress=Progressbar(tubeDownload,orient=HORIZONTAL,length=100,mode='determinate')

'''
def bar():
    import time
    progress['value']=20
    tubeDownload.update_idletasks()
    time.sleep(1)
    progress['value']=50
    tubeDownload.update_idletasks()
    time.sleep(1)
    progress['value']=80
    tubeDownload.update_idletasks()
    time.sleep(1)
    progress['value']=100

progress.pack()
Button(tubeDownload,text='foo',command=bar).pack()


'''

Button(tubeDownload, text='submit', command=tubeDownload.quit).grid(row=4, column=0, sticky=W, pady=4)
tubeDownload.mainloop()


import pytube
import os
import subprocess
from pytube import YouTube

url=urlN.get()
addr=addrN.get()
yt=YouTube(url)
temp=os.getcwd()
reqFile=yt.streams.first()
reqFile.download(temp)
name=NameN.get()
name=name+".mp3"
addr=addr+"/"+name
default_filename=reqFile.default_filename
subprocess.call(['ffmpeg','-i',os.path.join(temp,default_filename),os.path.join(temp,addr)])
dele="rm "+"*.webm"
os.system(dele)
dele="rm "+"*.mp4"
os.system(dele)
os.system("clear")