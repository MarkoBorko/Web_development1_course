class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg*2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_cm, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_cm)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


frst_name = input("Enter player's first name: ")
lst_name = input("Enter player's last name: ")
hght = int(input("Enter player's height in cm: "))
wght = int(input("Enter player's weight in kg: "))
gls = int(input("Enter the number of player's goals: "))
yllw_crds = int(input("Enter the number of player's yellow cards: "))
rd_crds = int(input("Enter the number of player's red cards: "))

new_player = FootballPlayer(first_name=frst_name, last_name=lst_name, height_cm=hght, weight_kg=wght, goals=gls, yellow_cards=yllw_crds, red_cards=rd_crds)

with open("Football_players.txt", "a") as football_file:
    football_file.write(str(new_player.__dict__))
    football_file.write('\n')

print("Players's data: {0}".format(new_player.__dict__))