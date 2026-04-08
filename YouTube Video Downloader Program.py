import os
import threading
import yt_dlp
from tkinter import *
from tkinter import messagebox, filedialog, ttk

ytvid=Tk()
ytvid.geometry("500x250")
ytvid.config(bg="#b4dce4")
ytvid.title("YouTube Video Downloader")


#-----function to download video----------
def download_video():
    url=tb1.get()
    dp= filedialog.askdirectory()

    if not url:
        messagebox.showerror("Error","Please Enter A YouTube URL")
        return
    if not dp:
        messagebox.showerror("Error","Please Select A Download Directory")
        return

    fopt= fvar.get()
    opts= {'outtmpl':os.path.join(dp,'%(title)s.%(ext)s'), 'progress_hooks':[progress]}

    if fopt == "MP4":
        opts['format']= "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"
    elif fopt == "MP3":
        opts['format']= "bestaudio[ext=m4a]"
        opts['postprocessors']= [{'key':'FFmpegExtractAudio','preferredcodec':'mp3','preferredquality':'192'}]

    threading.Thread(target=run_ytdlp,args=(opts,url),daemon=True).start()

#--------function to track progress--------
def progress(d):
    if d['status']== 'downloading':
        prol.config(text=f"Downloading: {d['_percent_str']} ({d['_speed_str']})")
    elif d['status']== 'finished':
        prol.config(text="Download Completed!")

#--------function to execute yt-dlp--------
def run_ytdlp(opts,url):
    with yt_dlp.YoutubeDL(opts) as ytdl:
        ytdl.download([url])

#--------------software setup---------------
head= Label(ytvid, text="     YOUTUBE VIDEO DOWNLOADER   ",anchor="center", font=("Times New Roman",20,"bold"), fg="#088da5")
head.place(x=0,y=10)
label1= Label(ytvid, text="YouTube URL: ", font=("Times New Roman",12))
label1.place(x=20,y=70)
tb1= Entry(ytvid,width=50)
tb1.place(x=150,y=70)

fvar= StringVar(value="MP4")
flabel= Label(ytvid, text="Select Format: ", font=("Times New Roman",12))
flabel.place(x=20,y=100)
fdrop= OptionMenu(ytvid,fvar,"MP4","MP3")
fdrop.place(x=150,y=100)

dbutton= Button(ytvid, text="Download",command=download_video)
dbutton.place(x=250,y=150)

prol= Label(ytvid,text="")
prol.place(x=20,y=200)

ytvid.mainloop()
