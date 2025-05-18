class Player:

  def __init__(self, name, Team_name):
    self.name = name
    self.xp = 1500
    self.Team_name = Team_name

  # Player 소개
  def inroduce(self):
    print(f"Hello I'm {self.name} and I Play for {self.Team_name}")


class Team:

  def __init__(self, Team_name):
    self.Team_name = Team_name
    self.Players = []

  # Player 추가
  def add_player(self, name):
    new_player = Player(name, self.Team_name)
    self.Players.append(new_player)
  # team Player 소개
  def show_players(self):
    for player in self.Players:
      player.inroduce()
  # Player 삭제
  def delete_player(self, name):
    for player in self.Players:
      if player.name == name:
        self.Players.remove(player)
        print(f"Deleted {name}({self.Team_name})")
        return
    print("Player not found")
  # team_xp 출력
  def team_xp(self):
    team_xp = 0
    for player in self.Players:
      team_xp += player.xp
    print(f"{self.Team_name} xp is {team_xp}")


#team_x 생성 및 Player 추가
team_x = Team("Team X")
team_x.add_player("nico")

#team_blue 생성 및 Player 추가
team_blue = Team("Team Blue")
team_blue.add_player("lynn")

# Player 소개
team_x.show_players()
team_blue.show_players()

# Player 삭제
team_x.delete_player("nico")

# team_xp 출력
team_x.team_xp()
team_blue.team_xp()
