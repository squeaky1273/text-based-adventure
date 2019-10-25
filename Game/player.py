class Player():
    def __init__(self, player_name):
        self.player_name = player_name

    def player(self):
        player_name = (input("What is your name?: "))
        print("My name is {}.".format(player_name))
