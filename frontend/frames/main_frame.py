import customtkinter as ctk


class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, submit, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        # self.grid_rowconfigure((0, 1), weight=0)
        # self.grid_rowconfigure((2), weight=1)
        # self.grid_rowconfigure((3), weight=0)

        title_label = ctk.CTkLabel(self, text="Fill in your name :")
        title_label.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="nsew")
        self.title_entry = ctk.CTkEntry(
            self,
            placeholder_text="John Doe",
        )
        self.title_entry.grid(row=2, column=0, padx=20, pady=(0, 0), sticky="nsew")

        self.submit_btn = ctk.CTkButton(self, text="Submit", command=submit)
        self.submit_btn.grid(row=3, column=0, padx=20, pady=(0, 0), sticky="nsew")

        self.greet_label = ctk.CTkLabel(
            self,
            text="Hello World!",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.greet_label.grid(row=4, column=0, padx=20, pady=(20, 0), sticky="nsew")
