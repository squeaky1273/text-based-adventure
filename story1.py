from story import Story

class Story1(Story):
    def __init__(self, player_name):
        super().__init__(player_name)

    def start_adventure(self, player_name):
        print("Welcome {}. You are a teenager who is working at a gas station.".format(player_name))

        

if __name__ == "__main__":
    pass