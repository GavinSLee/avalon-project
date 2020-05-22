import fbchat
import time 
import random 
from random import shuffle
from fbchat import Client
from getpass import getpass
from fbchat.models import *

class Setup:
    def __init__(self):
        self.friends_list = []
        self.merlin = False 
        self.morgana = False 
        self.percival = False
        self.oberon = False 
        self.all_roles = []
        self.messages = []
        self.assignments = {}
        self.visible_to_merlin = {}
        self.visible_to_percival = {}
        self.client = None 

    def set_fb_info(self, username, password):
        self.client = fbchat.Client(username, password)

    def get_fb_info(self): 
        return self.username, self.password 

    def get_client(self):
        print("GOT CLIENT")
        return self.client 

    def set_friends(self, friends):
        self.friends_list = friends

    def play_merlin(self):
        self.merlin = True 
    
    def play_morgana(self):
        self.morgana = True 
    
    def play_mordred(self):
        self.mordred = True 
    
    def play_oberon(self):
        self.oberon = True 

    # 5 players = 3 good and 2 evil
    def five_players(self):
        good_roles = ["KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR"]
        evil_roles = ["KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR"]
        self.all_roles = good_roles + evil_roles 

    # 6 players = 4 good and 2 evil
    def six_players(self):
        good_roles = ["KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR"]
        evil_roles = ["MINION OF MORDRED", "MINION OF MORDRED"]
        self.all_roles = good_roles + evil_roles 
    
    # TODO
    # 7 players = 4 good and 3 evil
    def seven_players(self):
        good_roles = ["KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR"]
        evil_roles = ["MINION OF MORDRED", "MINION OF MORDRED"] 
        if self.merlin == True:
            good_roles.append("MERLIN")
        else:
            good_roles.append("KNIGHT OF ARTHUR")
        if self.morgana == True:
            evil_roles.append("MORGANA")
        else:
            evil_roles.append("MINION OF MORDRED")
        self.all_roles = good_roles + evil_roles 

    # 8 players = 5 good and 3 evil
    def eight_players(self):
        good_roles = ["KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR"]
        evil_roles = []

        good_roles, evil_roles = self.set_special_roles(good_roles, evil_roles) 
        self.all_roles = good_roles + evil_roles

    # 9 players = 6 good and 3 evil
    def nine_players(self):
        good_roles = ["KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR"]
        evil_roles = []

        good_roles, evil_roles = self.set_special_roles(good_roles, evil_roles) 
        self.all_roles = good_roles + evil_roles     

    # 10 players = 6 good and 4 evil
    def ten_players(self):
        good_roles = ["KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR", "KNIGHT OF ARTHUR"]
        evil_roles = ["MINION OF MORDRED"]

        good_roles, evil_roles = self.set_special_roles(good_roles, evil_roles)
        self.total_roles = good_roles + evil_roles

    def set_special_roles(self, good_roles, evil_roles):
        if self.merlin == True:
            good_roles.append("MERLIN") 
        else:
            good_roles.append("KNIGHT OF ARTHUR")

        if self.percival == True:
            if self.merlin == False:
                print("You don't have a Merlin in play!")
            else:
                good_roles.append("PERCIVAL") 
        else:
            good_roles.append("KNIGHT OF ARTHUR")
        
        if self.morgana == True:
            if self.merlin == False:
                print("You don't have a Merlin in play!")
            else:
                evil_roles.append("MORGANA") 
        else:
            evil_roles.append("MINION OF MORDRED")

        if self.mordred == True:
            if self.merlin == False:
                print("You don't have a Merlin in play!")
            else:
                evil_roles.append("MORDRED")
        else:
            evil_roles.append("MINION OF MORDRED")

        if self.oberon == True:
            evil_roles.append("OBERON")
        else:
            evil_roles.append("MINION OF MORDRED")  
        
        return good_roles, evil_roles

    def set_roles(self):
        # 5 players = 3 good and 2 evil
        if len(self.friends_list) == 5:
            self.five_players()

        # 6 players = 4 good and 2 evil
        elif len(self.friends_list) == 6:
            self.six_players()

        # 7 players = 4 good and 3 evil
        elif len(self.friends_list) == 7:
            self.seven_players() 

        # 8 players = 5 good and 3 evil
        elif len(self.friends_list) == 8:
            self.eight_players() 

        # 9 players = 6 good and 3 evil
        elif len(self.friends_list) == 9:
            self.nine_players()

        # 10 players = 6 good and 4 evil
        elif len(self.friends_list) == 10:
            self.ten_players()
        else:
            print("There are not enough players to play Resistance: Avalon!")
    
    def assign_roles(self):
        shuffle(self.all_roles)
        shuffle(self.friends_list)
        for i in range(len(self.friends_list)):
            self.assignments[self.friends_list[i]] = self.all_roles[i] 
        # Roles visible to Merlin
        self.visible_to_merlin = {key: value for (key, value) in self.assignments.items() if value == "MINION OF MORDRED" or value == "MORGANA"}
        # Roles visible to Percival
        self.visible_to_percival = {key: value for (key, value) in self.assignments.items() if value == "MERLIN" or value == "MORGANA"}

    def send_roles(self):
        # Loop through friends list
        starting_player = self.friends_list[random.randint(0, len(self.friends_list) - 1)]
        print("Sending out roles...\n")
        counter = 1
        for friend in self.friends_list:
            # Gets all the friends of the name and creates a list
            name_list = self.client.searchForUsers(friend)
            # Gets the first name in that name list
            name = name_list[0]
            role = self.assignments[friend]
            msg_intro = "Hi " + str.split(friend)[0] + "!" + " This is a python script written by Gavin for Resistance: Avalon. Welcome to today's game!"
            print(msg_intro)
            # client.send(fbchat.models.Message(msg_intro), name.uid)
            time.sleep(3.0)
            msg_num_people = "There are " + str(len(self.friends_list)) + " people playing this round."
            print(msg_num_people)
            # client.send(fbchat.models.Message(msg_num_people), name.uid)
            time.sleep(3.0)

            # Message for Vanilla Good
            if role == "KNIGHT OF ARTHUR":
                msg_knight_arthur = "YOUR ROLE: " + role + ". Seek fellow knights and defeat evil!" 
                # print(msg_knight_arthur)
                image_path = r"C:\Users\Gavin Lee\Documents\side_projects\avalon_project\dog.jpg"
                self.client.sendLocalImage(image_path, thread_id = name.uid)
                print("DOGOOGOOGO")
            
            # Message for Merlin
            elif role == "MERLIN":
                msg_merlin = "YOUR ROLE: " + role + ". The following players are evil: " + ', '.join(key for key in visible_to_merlin.keys())
                print(msg_merlin)
                # self.client.send(fbchat.models.Message(msg_merlin), name.uid)
            # Message for Percival
            elif role == "PERCIVAL":
                msg_percival = "YOUR ROLE: " + role + ". The following may be Merlin: " + ", ".join(key for key in visible_to_percival.keys())
                print(msg_percival) 
                # self.client.send(fbchat.models.Message(msg_percival), name.uid)

            # Message for Vanilla Evil
            elif role == "MINION OF MORDRED":
                msg_minion_mordred = "YOUR ROLE: " + role + ". Seek fellow minions and defeat good!"
                print(msg_minion_mordred)
                # self.client.send(fbchat.models.Message(msg_minion_mordred), name.uid)
            
            # Message for Morgana
            elif role == "MORGANA":
                msg_morgana = "YOUR ROLE: " + role + ". You appear to Percival as a clone of Merlin!"
                print(msg_morgana) 
                # self.client.send(fbchat.models.Message(msg_morgana), name.uid)

            # ERROR: One of the roles isn't listed
            else:
                msg_error = "ERROR: The script has a mistake; stop the game and please let Gavin know immediately!"
                print(msg_error)
                # self.client.send(fbchat.models.Message(msg_error), name.uid)
                return 1

            print("Role " + str(counter) + " sent out!\n")
            counter += 1
            time.sleep(5.0)
        
