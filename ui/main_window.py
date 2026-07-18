import customtkinter as ctk

from ui.toolbar import Toolbar
from ui.song_list import SongList
from ui.status_bar import StatusBar


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("Music Cleaner")
        self.geometry("1200x720")
        self.minsize(1000, 650)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.toolbar = Toolbar(self)
        self.toolbar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=10,
            pady=(10,5)
        )

        self.song_list = SongList(self)
        self.song_list.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10
        )

        self.status = StatusBar(self)
        self.status.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=10,
            pady=(5,10)
        )