
class Player:

    def __init__(self):
        print("Player Initialized......")

    def get_runs(self):
        print("Runs Scored......")

sachin = Player()       # calls the __init__() implicitly
sourav = Player()
sachin.__init__()

print("-" * 60)
sachin.get_runs()

