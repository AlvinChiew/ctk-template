import os
from dotenv import load_dotenv, dotenv_values
import customtkinter as ctk

from screens.home_screen import HomeScreen
from scripts.logger import getLogger


def main():
    configs = {
        **dotenv_values(".env.shared"),
        **dotenv_values(".env.secret"),
        # **os.environ,
    }

    configs["root_path"] = (
        os.path.abspath(".")
        if configs["APP_ENV"] in ("UAT", "PROD")
        else os.path.join(os.path.abspath("."), "frontend")
    )
    configs["logger"] = getLogger(
        configs["APP_NAME"].replace(" ", ""),
        os.path.join(configs["root_path"], "logs", "outputs.log"),
    )
    configs["size"] = f"{720}x{560}+{100}+{100}"

    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme(
        "green"
    )  # Themes: "blue" (standard), "green", "dark-blue"

    app = HomeScreen(configs)
    app.mainloop()


if __name__ == "__main__":
    load_dotenv(".env.shared", override=True)
    load_dotenv(".env.secret", override=True)

    main()
