import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(
            self,
            text=""
        )

        self.label.pack(
            anchor="w",
            padx=10,
            pady=8
        )

        self.update_stats(0, 0)

    def update_stats(self, total, selected):

        self.label.configure(
            text=f"🎵 {total} canciones     ☑ {selected} seleccionadas"
        )