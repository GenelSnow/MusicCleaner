import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(
            self,
            text="🎵 0 canciones     ☑ 0 seleccionadas     🗑 0 eliminar"
        )

        self.label.pack(
            padx=10,
            pady=8,
            anchor="w"
        )