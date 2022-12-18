from pytube import YouTube


def download(link):

    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print("An error has occured in the process")
    print("Download has succeed!")

link = input("Put youtube link here -->  ")

download(link)