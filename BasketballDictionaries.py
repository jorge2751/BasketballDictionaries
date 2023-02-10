kevin = {
		"name": "Kevin Durant", 
		"age":34, 
		"position": "small forward", 
		"team": "Brooklyn Nets"
}
jason = {
		"name": "Jason Tatum", 
		"age":24, 
		"position": "small forward", 
		"team": "Boston Celtics"
}
kyrie = {
		"name": "Kyrie Irving", 
		"age":32,
		"position": "Point Guard", 
		"team": "Brooklyn Nets"
}

players = [
	{
		"name": "Kevin Durant", 
		"age":34, 
		"position": "small forward", 
		"team": "Brooklyn Nets"
	},
	{
		"name": "Jason Tatum", 
		"age":24, 
		"position": "small forward", 
		"team": "Boston Celtics"
	},
	{
		"name": "Kyrie Irving", 
		"age":32,
		"position": "Point Guard", 
		"team": "Brooklyn Nets"
	},
	{
		"name": "Damian Lillard", 
		"age":33,
		"position": "Point Guard", 
		"team": "Portland Trailblazers"
	},
	{
		"name": "Joel Embiid", 
		"age":32,
		"position": "Power Foward", 
		"team": "Philidelphia 76ers"
	},
	{
		"name": "DeMar DeRozan",
		"age": 32,
		"position": "Shooting Guard",
		"team": "Chicago Bulls"
	}
]




class Player:
    def __init__(self, player_data):
        self.name = player_data["name"]
        self.age = player_data["age"]
        self.position = player_data["position"]
        self.team = player_data["team"]

    @classmethod
    def get_team(cls, team_list):
        team = []
        for player_data in team_list:
            team.append(cls(player_data))
        return team

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

new_team = []
for player_data in players:
    new_team.append(Player(player_data))

for player in new_team:
    print(player.name)

new_team = Player.get_team(players)
for player in new_team:
    print(player.name, player.age, player.position, player.team)