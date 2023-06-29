from pytube import YouTube


def download(link_of_video):

    youtube_object = YouTube(link_of_video)
    youtube_object = youtube_object.streams.get_audio_only()
    try:
        youtube_object.download(link_of_video)
    except:
        print("An error has occured in the process")
    print("Download has succeed!")

link = input("Put youtube link_of_video here -->  ")

download(link)