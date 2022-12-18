#!/usr/bin/python3
import pathlib
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "window_downloader.ui"


class Converthot:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)
        self.entry_user_url = builder.get_object("entry_user_url")

    def run(self):
        self.mainwindow.mainloop()

    def on_download_button_click(self):
        user_answer = self.entry_user_url.get()



if __name__ == "__main__":
    app = Converthot()
    app.run()
