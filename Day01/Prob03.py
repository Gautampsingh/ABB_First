
class Team:

    teamleader = None

    @classmethod
    def set_team(cls, tname):
        Team.teamleader = tname

    @classmethod
    def get_name(cls):
        return Team.teamleader

tm =  Team()

Team.set_team("Micheal")
print(Team.get_name())
