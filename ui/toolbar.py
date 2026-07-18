import customtkinter as ctk


class Toolbar(ctk.CTkFrame):

    def __init__(
        self,
        master,
        on_open=None,
        on_search=None,
        on_recommended=None,
        on_delete=None
    ):
        super().__init__(master)

        self.grid_columnconfigure(1, weight=1)

        # Abrir carpeta
        self.open_button = ctk.CTkButton(
            self,
            text="📂 Abrir carpeta",
            command=on_open
        )
        self.open_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        # ---------------- Buscar ----------------

        self.search_var = ctk.StringVar()

        self.search = ctk.CTkEntry(
            self,
            textvariable=self.search_var,
            placeholder_text="Buscar..."
        )

        self.search.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=10
        )

        if on_search:

            self.search_var.trace_add(
                "write",
                lambda *args: on_search(
                    self.search_var.get()
                )
            )

        # Ejecutar búsqueda al presionar Enter
        if on_search:
            self.search.bind(
                "<Return>",
                lambda event: on_search(self.search.get())
            )

        # Seleccionar recomendadas
        self.auto_button = ctk.CTkButton(
            self,
            text="⭐ Recomendadas",
            command=on_recommended
        )
        self.auto_button.grid(
            row=0,
            column=2,
            padx=10
        )

        # Eliminar
        self.delete_button = ctk.CTkButton(
            self,
            text="🗑 Eliminar",
            fg_color="#C0392B",
            hover_color="#922B21",
            command=on_delete
        )
        self.delete_button.grid(
            row=0,
            column=3,
            padx=10
        )