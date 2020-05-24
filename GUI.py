from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import sys
import time
sys.path.append(".")


class GuiLogin:

    def __init__(self):
        self.root = Tk()
        self.root.title("Avalon Night Phase Simulator")
        self.root.geometry("750x500")
        self.frame = Frame(self.root)
        self.setup_messenger_logo()
        self.setup_welcome_message()
        self.setup_login_info()
        self.setup_login_button()
        self.frame.pack(expand=True, fill=BOTH)
        self.root.mainloop()

    # Messenger Photo
    def setup_messenger_logo(self):
        photo = ImageTk.PhotoImage(Image.open("images/messenger_logo.png"))
        banner_label = Label(self.frame, image=photo)
        banner_label.image = photo
        banner_label.place(relx=.5, rely=.25, anchor="center")

    # Welcome Messages
    def setup_welcome_message(self):
        welcome_label = Label(
            self.frame, text="Welcome to the Avalon Night Phase simulator!")
        welcome_label.place(relx=.5, rely=.55, anchor="center")
        enter_info_label = Label(
            self.frame, text="Please enter your Facebook login info:")
        enter_info_label.place(relx=.5, rely=.60, anchor="center")

    # Login Info Text Boxes
    def setup_login_info(self):

        # Username Info
        username_text = "Username:"
        username_label = Label(self.frame, text=username_text)
        username_label.place(relx=.35, rely=.70, anchor="center")

        self.username_entry = Entry(self.frame, width=35)
        self.username_entry.insert(END, "gavin.lee.12139862")
        self.username_entry.place(relx=.65, rely=.70, anchor="center")

        # Password Info
        password_text = "Password:"
        password_label = Label(self.frame, text=password_text)
        password_label.place(relx=.35, rely=.75, anchor="center")

        self.password_entry = Entry(self.frame, width=35, show="*")
        self.password_entry.place(relx=.65, rely=.75, anchor="center")

    def clear_widgets(self):
        self.frame.destroy()
        self.frame = Frame(self.root)
        self.frame.pack(expand=True, fill=BOTH)

    # TODO: Handle backend logic for logging in
    def login_button_handler(self):

        # self.setup.set_fb_info(self.get_username(), self.get_password())
        self.clear_widgets()
        gui_setup = GuiSetup(self.root, self.frame)
        # if self.setup.get_client().logout() == False:
        #     print("ERROR: Did not successfully logout of client!")
        # else:
        #     print("Successfully logged out of the client!")

    def setup_login_button(self):
        login_button = Button(self.frame, text="Login",
                              command=self.login_button_handler)
        login_button.place(relx=.5, rely=.9, anchor="center")


class GuiSetup:

    def __init__(self, root, frame):
        self.root = root
        self.root.title("Avalon Night Phase Simulator")
        self.root.geometry("470x600")

        self.frame = frame
        self.custom_font = tkFont.Font(family="calibri", size=12)
        self.setup_photo_banner()
        self.setup_welcome_label()
        self.setup_extra_roles()
        self.setup_name_labels()
        self.setup_players()
        self.setup_go_button()
        self.root.mainloop()

    def setup_photo_banner(self):
        photo = ImageTk.PhotoImage(Image.open("images/avalon_banner.jpg"))
        banner_label = Label(self.frame, image=photo)
        banner_label.image = photo
        banner_label.grid(row=0, column=0, columnspan=6)

    def setup_welcome_label(self):
        welcome_label = Label(
            self.frame, text="Welcome to the Avalon Night Phase simulator!", font=self.custom_font)
        welcome_label.grid(row=1, column=0, columnspan=6)

    def setup_extra_roles(self):
        roles_label = Label(self.frame, text = "Please Check which Roles you'd like to play with:", font=self.custom_font)
        roles_label.grid(row = 2, column = 0, columnspan = 6)
        merlin_check = Checkbutton(self.root, text = "Merlin", variable = 1)
        merlin_check.grid(row = 3, column = 0, sticky = W)

    def setup_name_labels(self):
        name_label = Label(
            self.frame, text="Enter the Facebook names of your players here (minimum of 5 players):", font=self.custom_font)
        name_label.grid(row=3, column=0, columnspan=6)

    def setup_players(self):
        for i in range(10):
            player_counter = i + 1
            player_text = "Enter Player " + \
                str(player_counter) + "'s Facebook Name Here: "
            player_label = Label(self.frame, text=player_text)
            player_label.grid(row=i + 4, column=1, columnspan=2)

            # for player entries
            player_entry = Entry(self.frame, width=35)
            player_entry.grid(row=i + 4, column=3,
                              columnspan=2, padx=10, pady=10)

    def setup_go_button(self):
        lets_go_button = Button(self.frame, text="LET'S GO!")
        lets_go_button.grid(row=13, column=0, columnspan=6)


if __name__ == "__main__":
    gui_login = GuiLogin()
