from tkinter import filedialog
import customtkinter as ctk

from services.music_library import MusicLibrary
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

        # --------- Datos ---------

        self.library = MusicLibrary()

        # Control del debounce del buscador
        self.search_job = None

        # --------- Grid ---------

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --------- UI ---------

        self.toolbar = Toolbar(
            self,
            on_open=self.open_folder,
            on_search=self.search_song,
            on_recommended=self.select_recommended,
            on_delete=self.delete_selected
        )

        self.toolbar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=10,
            pady=(10, 5)
        )

        self.song_list = SongList(
            self,
            on_selection_changed=self.update_status
        )
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
            pady=(5, 10)
        )

        

    # ==========================
    # Eventos
    # ==========================

    def open_folder(self):

        folder = filedialog.askdirectory()

        if not folder:
            return

        songs = self.library.load(folder)

        self.song_list.load_songs(songs)

        self.status.update_stats(
            total=len(songs),
            selected=0
        )

    def update_status(self):

        self.status.update_stats(
            total=self.library.count(),
            selected=self.library.selected_count()
        )
    def search_song(self, text):

        if self.search_job is not None:
            self.after_cancel(self.search_job)

        self.search_job = self.after(
        300,
        lambda: self.perform_search(text)
        )


    def perform_search(self, text):

        songs = self.library.search(text)

        self.song_list.load_songs(songs)

        self.update_status()

        self.search_job = None

    def select_recommended(self):
        print("Seleccionar recomendadas")

    def delete_selected(self):
        print("Eliminar")

