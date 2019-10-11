class Story():
    def __init__(self, player_name):
        self.player_name = player_name

    def main(self):
        player_name = (input("What is your name?: "))
        print("My name is {}.".format(player_name))

"""
decide = True
while decide == True:
    choose = input("Enter:\nA for story 1, \nB for story 2, or \nc for story 3")
"""

class Story1(Story):
    def __init__(self, player_name):
        super().__init__(player_name)

    def start_adventure(self, player_name):
        print("Welcome {}. You are a teenager who is working at a gas station.".format(player_name))



if __name__ == "__main__":
    pass