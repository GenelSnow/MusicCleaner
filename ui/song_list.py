import customtkinter as ctk



class SongList(ctk.CTkScrollableFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        # Datos de ejemplo
        for i in range(30):

            cb = ctk.CTkCheckBox(
                self,
                text=f"Canción {i+1}"
            )

            cb.grid(
                row=i,
                column=0,
                sticky="w",
                padx=10,
                pady=5
            )