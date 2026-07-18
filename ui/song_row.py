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
        self.grid_columnconfigure(3, weight=1)

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

    # ---------------- Recomendación ----------------

        self.recommend_label = ctk.CTkLabel(
            self,
            text="●",
            width=30,
            text_color="#666666",
            font=("Segoe UI", 16)
        )

        self.recommend_label.grid(
            row=0,
            column=1,
            padx=5
        )

        # ---------------- Score ----------------

        self.score_label = ctk.CTkLabel(
            self,
            text="---",
            width=45,
            font=("Segoe UI", 13, "bold"),
            text_color="#AAAAAA"
        )

        self.score_label.grid(
            row=0,
            column=2,
            padx=5
        )

        # ---------------- Nombre ----------------

        self.name_label = ctk.CTkLabel(
            self,
            text=self.song.name,
            anchor="w",
            font=("Segoe UI", 14)
        )

        self.name_label.grid(
            row=0,
            column=3,
            sticky="ew",
            padx=5
        )

    # ---------------- Tamaño ----------------

        self.size_label = ctk.CTkLabel(
            self,
            text=self.format_size(self.song.size),
            width=80
        )

        self.size_label.grid(
            row=0,
            column=4,
            padx=10
        )

    def on_toggle(self):

        self.song.selected = self.checkbox.get() == 1

        if self.on_selection_changed:
         self.on_selection_changed()

    def format_size(self, size):

        mb = size / (1024 * 1024)

        return f"{mb:.2f} MB"
