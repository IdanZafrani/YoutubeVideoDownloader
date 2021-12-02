from tkinter import *
from pytube import YouTube

window=Tk()
window.geometry("600x700")
window.config(bg="black")
window.title("Youtube Video Downloader")
Label(window,text="Video Downloader",font="architectural 30 bold",bg="lightblue").pack(padx=5,pady=50)
Label(window,text="Please enter the link : ",font=("architectural",18,"bold")).place(x=170,y=150)
video_link=StringVar()
Entry_link=Entry(window,width=50,font=35,textvariable=video_link).place(x=25,y=200)


def video_download():
    video_url=YouTube(str(video_link.get()))
    videos = video_url.streams.first()
    videos.download()
    Label(window,text="Download Completed !! ",font=("architectural",18,"bold"),bg="lightblue",fg="white").place(x=150,y=450)
    Label(window,text="Check out your venv folder in: PycharmProjects !! ",font=("architectural",18,"bold"),bg="lightblue",fg="white").place(x=10,y=500)

Button(window,text="Download",font=("architectural",25,"bold"),bg="lightblue",command=video_download).place(x=190,y=350)
window.mainloop()