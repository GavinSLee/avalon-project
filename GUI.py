from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import sys
import time
sys.path.append(".")


class GuiLogin:

    def __init__(self, setup):
        self.setup = setup
        self.root = Tk()
        self.root.title("Avalon Night Phase Simulator")
        self.root.geometry("750x500")
        self.frame = Frame(self.root)
        # self.username_entry = None
        # self.password_entry = None
        self.setup_messenger_logo()
        self.setup_welcome_message()
        self.setup_login_info()
        self.setup_login_button()
        self.frame.pack(expand=True, fill=BOTH)
        self.root.mainloop()

    def setup_messenger_logo(self):
        photo = ImageTk.PhotoImage(Image.open("images/messenger_logo.png"))

        banner_label = Label(self.frame, image=photo)
        banner_label.image = photo
        banner_label.place(relx=.5, rely=.25, anchor="center")

    def setup_welcome_message(self):
        welcome_label = Label(
            self.frame, text="Welcome to the Avalon Night Phase simulator!")
        welcome_label.place(relx=.5, rely=.55, anchor="center")
        enter_info_label = Label(
            self.frame, text="Please enter your Facebook login info:")
        enter_info_label.place(relx=.5, rely=.60, anchor="center")

    def setup_login_info(self):
        username_text = "Username:"
        username_label = Label(self.frame, text=username_text)
        username_label.place(relx=.35, rely=.70, anchor="center")

        # for player entries
        self.username_entry = Entry(self.frame, width=35)
        self.username_entry.insert(END, "gavin.lee.12139862")
        self.username_entry.place(relx=.65, rely=.70, anchor="center")

        password_text = "Password:"
        password_label = Label(self.frame, text=password_text)
        password_label.place(relx=.35, rely=.75, anchor="center")

        # for player entries
        self.password_entry = Entry(self.frame, width=35, show="*")
        self.password_entry.place(relx=.65, rely=.75, anchor="center")

    def get_username(self):
        username = self.username_entry.get()
        return username

    def get_password(self):
        password = self.password_entry.get()
        return password

    def login_button_handler(self):

        self.setup.set_fb_info(self.get_username(), self.get_password())
        self.clear_widgets()
        gui_setup = GuiSetup(self.root, self.frame)
        if self.setup.get_client().logout() == False:
            print("ERROR: Did not successfully logout of client!")
        else:
            print("Successfully logged out of the client!")

    def setup_login_button(self):
        login_button = Button(self.frame, text="Login",
                              command=self.login_button_handler)
        login_button.place(relx=.5, rely=.9, anchor="center")

    def clear_widgets(self):
        self.frame.destroy()
        self.frame = Frame(self.root)
        self.frame.pack(expand=True, fill=BOTH)


class GuiSetup:

    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.root.geometry("1000x1000")
        self.custom_font = tkFont.Font(family="calibri", size=14)
        self.root.title("Avalon Night Phase Simulator")
        self.setup_photo_banner()
        self.setup_welcome_label()
        self.setup_name_labels()
        self.setup_players()
        self.setup_go_button()
        self.root.mainloop()

    def setup_photo_banner(self):
        photo = PhotoImage(file="avalon_banner.png")
        banner_label = Label(self.frame, image=photo)
        banner_label.image = photo
        banner_label.grid(row=0, column=0, columnspan=6)

    def setup_welcome_label(self):
        welcome_label = Label(
            self.frame, text="Welcome to the Avalon Night Phase simulator!", font=self.custom_font)
        welcome_label.grid(row=1, column=0, columnspan=6)

    def setup_name_labels(self):
        name_label = Label(
            self.frame, text="Enter the names of your players here:", font=self.custom_font)
        name_label.grid(row=2, column=0, columnspan=6)

    def setup_players(self):
        for i in range(10):
            # for player text
            player_counter = i + 1
            player_text = "Enter Player " + \
                str(player_counter) + " name's here: "
            player_label = Label(self.frame, text=player_text)
            player_label.grid(row=i + 3, column=1, columnspan=2)

            # for player entries
            player_entry = Entry(self.frame, width=35, borderwidth=5)
            player_entry.grid(row=i + 3, column=3,
                              columnspan=2, padx=10, pady=5)

    def setup_go_button(self):
        lets_go_button = Button(self.frame, text="LET'S GO!")
        lets_go_button.grid(row=13, column=0, columnspan=6)

    # def add_more_players(self):
    #     player_text = "Enter Player " + str(self.player_counter) + " name's here: "
    #     player_label = Label(root, text = player_text)
    #     player_label.grid(row= self.player_counter + 4, column = 1, columnspan = 2)

    #     entry = Entry(root, width=35, borderwidth=5)
    #     entry.grid(row= self.player_counter + 4, column = 3, columnspan = 2, padx = 10, pady = 10)
    #     add_more_players_button.grid(row = self.player_counter + 5, column = 0, columnspan = 6)
    #     lets_go_button(row = self.player_counter + 6, column = 0, columnspan = 6)
    #     self.player_counter += 1
