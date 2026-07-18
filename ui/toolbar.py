import customtkinter as ctk


class Toolbar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(1, weight=1)

        self.open_button = ctk.CTkButton(
            self,
            text="📂 Abrir carpeta"
        )
        self.open_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Buscar..."
        )
        self.search.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=10
        )

        self.auto_button = ctk.CTkButton(
            self,
            text="⭐ Recomendadas"
        )
        self.auto_button.grid(
            row=0,
            column=2,
            padx=10
        )

        self.delete_button = ctk.CTkButton(
            self,
            text="🗑 Eliminar",
            fg_color="#C0392B",
            hover_color="#922B21"
        )
        self.delete_button.grid(
            row=0,
            column=3,
            padx=10
        )