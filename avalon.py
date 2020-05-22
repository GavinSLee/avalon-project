from GUI import *
from setup import Setup

class Avalon:

    def __init__(self):
        setup = Setup() 
        gui_login = GuiLogin(setup)             

if __name__ == "__main__":
    avalon = Avalon() 