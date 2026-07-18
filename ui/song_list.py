import customtkinter as ctk

from ui.song_row import SongRow


class SongList(ctk.CTkScrollableFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.rows = []

    def load_songs(self, songs):

        # Eliminar filas anteriores
        for row in self.rows:
            row.destroy()

        self.rows.clear()

        # Crear nuevas filas
        for i, song in enumerate(songs):

            row = SongRow(self, song)

            row.grid(
                row=i,
                column=0,
                sticky="ew",
                padx=5,
                pady=2
            )

            self.rows.append(row)