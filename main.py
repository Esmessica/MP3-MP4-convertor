from pygubu_window import Converthot
from pytube import YouTube
import os

pyg_window = Converthot()


class ConverThor(Converthot):
    def on_download_button_click(self):
        super().entry_user_url = self.entry_user_url

        youtube_object = YouTube(self.entry_user_url)
        youtube_object = youtube_object.streams.get_audio_only()

        try:
            file = youtube_object.download()
            base, ext = os.path.splitext(file)
            new_file = base + ".mp3"
            os.rename(file, new_file)
            print("Download has succeed!")

        except:
            print("An error has occured in the process")
