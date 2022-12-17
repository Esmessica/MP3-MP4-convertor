from pytube import  YouTube
import os

def download_audio(link):

    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_audio_only()

    try:
        file = youtube_object.download()
        base, ext = os.path.splitext(file)
        new_file = base + ".mp3"
        os.rename(file, new_file)
        print("Download has succeed!")

    except:
        print("An error has occured in the process")


link = input("Put youtube link here -->  ")

download_audio(link)