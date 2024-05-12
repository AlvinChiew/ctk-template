import os
from threading import Thread
import time
import customtkinter as ctk

from frames.main_frame import MainFrame
from frames.sidebar_frame import SidebarFrame


class HomeScreen(ctk.CTk):
    def __init__(self, configs):
        super().__init__()

        # States
        self.mode = os.getenv("ENV")

        # Start Application
        self.title(os.getenv("APP_NAME"))
        self.resizable(True, True)
        self.wm_iconbitmap(os.getenv("ICON_PATH"))
        self.log = configs["logger"]
        self.geometry(configs["size"])

        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0), weight=1)

        self.sidebar_frame = SidebarFrame(
            self,
            # fg_color="transparent",
        )
        self.sidebar_frame.grid(
            row=0, column=0, ipadx=0, ipady=20, rowspan=1, sticky="nsew"
        )

        self.main_frame = MainFrame(
            self,
            self.click_submit,
            fg_color="transparent",
        )
        self.main_frame.grid(
            row=0, column=1, ipadx=0, ipady=20, rowspan=1, sticky="nsew"
        )

    def click_submit(self):
        self.sidebar_frame.status_progressbar.start()
        self.sidebar_frame.status_label.configure(text="Status: RUNNING...")
        self.sidebar_frame.stop_btn.configure(state="normal")
        self.sidebar_frame.reset_btn.configure(state="disabled")

        self.main_frame.title_entry.configure(state="disabled")
        self.main_frame.submit_btn.configure(state="disabled")

        thread = Thread(target=self.submit)
        thread.start()

    def submit(self):
        time.sleep(3)

        name = self.main_frame.title_entry.get()

        if name is not None and name.strip() != "":
            self.main_frame.greet_label.configure(text=f"Hello {name}!")

        self.sidebar_frame.status_progressbar.stop()
        self.sidebar_frame.status_label.configure(text="Status: READY")
        self.sidebar_frame.reset_btn.configure(state="normal")
        self.sidebar_frame.stop_btn.configure(state="disabled")

        self.main_frame.title_entry.configure(state="normal")
        self.main_frame.submit_btn.configure(state="normal")
