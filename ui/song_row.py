import customtkinter as ctk

from models.song import Song


class SongRow(ctk.CTkFrame):

    def __init__(
        self,
        master,
        song,
        on_selection_changed=None
    ):
        super().__init__(master)

        self.song = song
        self.on_selection_changed = on_selection_changed

        # Hace que la columna del nombre ocupe todo el espacio
        self.grid_columnconfigure(1, weight=1)

        # ---------------- Checkbox ----------------

        self.checkbox = ctk.CTkCheckBox(
            self,
            text="",
            command=self.on_toggle
        )

        self.checkbox.grid(
            row=0,
            column=0,
            padx=(10, 5),
            pady=8
        )

        if self.song.selected:
            self.checkbox.select()

        # ---------------- Nombre ----------------

        self.name_label = ctk.CTkLabel(
            self,
            text=self.song.name,
            anchor="w",
            font=("Segoe UI", 14)
        )

        self.name_label.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5
        )

        # ---------------- Tamaño ----------------

        self.size_label = ctk.CTkLabel(
            self,
            text=f"{self.song.size_mb:.2f} MB",
            width=80
        )

        self.size_label.grid(
            row=0,
            column=2,
            padx=10
        )

    def on_toggle(self):

        self.song.selected = self.checkbox.get() == 1

        if self.on_selection_changed:
         self.on_selection_changed()