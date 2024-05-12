import os
import customtkinter as ctk
from PIL import Image


class SidebarFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_rowconfigure((2), weight=1)
        self.grid_rowconfigure((3), weight=0)

        logo = ctk.CTkImage(
            light_image=Image.open(os.getenv("ICON_PATH")),
            dark_image=Image.open(os.getenv("ICON_PATH")),
            size=(56, 56),
        )
        logo_icon_label = ctk.CTkLabel(self, image=logo, text="")
        logo_text_label = ctk.CTkLabel(
            self,
            text=os.getenv("APP_NAME"),
            font=ctk.CTkFont(size=20, weight="bold"),
        )

        self.status_label = ctk.CTkLabel(self, text="Status: READY")
        self.status_progressbar = ctk.CTkProgressBar(
            self, width=120, mode="indeterminate"
        )

        self.stop_btn = ctk.CTkButton(
            self, text="Stop", command="", state="disabled", height=40
        )
        self.reset_btn = ctk.CTkButton(self, text="Reset", command="", height=40)

        appearance_mode_label = ctk.CTkLabel(self, text="Theme:", anchor="w")
        appearance_mode_optionemenu = ctk.CTkOptionMenu(
            self,
            values=[
                "System",
                "Light",
                "Dark",
            ],
            command=self.change_appearance_mode_event,
        )
        scaling_label = ctk.CTkLabel(self, text="Zoom:", anchor="w")
        scaling_optionemenu = ctk.CTkOptionMenu(
            self,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )

        logo_icon_label.grid(row=0, column=0, padx=20, pady=(20, 0))
        logo_text_label.grid(row=1, column=0, padx=20, pady=(20, 0))
        self.status_label.grid(row=3, column=0, padx=20, pady=(30, 0), sticky="s")
        self.status_progressbar.grid(
            row=4,
            column=0,
            padx=20,
            pady=(0, 0),
            sticky="n",
        )

        self.stop_btn.grid(row=5, column=0, padx=20, pady=(10, 0), sticky="s")
        self.reset_btn.grid(row=6, column=0, padx=20, pady=(40, 0), sticky="s")

        appearance_mode_label.grid(row=7, column=0, padx=20, pady=(30, 0))
        appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 0))
        scaling_label.grid(row=9, column=0, padx=20, pady=(20, 0))
        scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        # set default values
        appearance_mode_optionemenu.set("Dark")
        scaling_optionemenu.set("100%")
        ctk.set_widget_scaling(1)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
