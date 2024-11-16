class Team:
    def __init__(self, name: str, team_size: int, capital: int):
        self.name = name
        self.team_size = team_size
        self.capital = capital

    def show_info(self):
        print(f"Team name: {self.name}, team size: {self.team_size}, capital: {self.capital}")

team1 = Team('OpenAI', 100, 1000000)
team1.show_info()
# Вывод: Team name: OpenAI, team size: 100, capital: 1000000
