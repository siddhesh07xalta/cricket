from player import Player
from team import Team

def take_team_details():
    try:
        team_1 = {}
        
        for player in range(3):
            player_name = input(f"Enter name for player {player+1}: ").strip()
            print("Select role")
            print("1.Batsman")
            print("2.Bowler")
            print("3.All Rounder")
            print("4.Wicket Keeper")
            print("5.Captain")

            role_choice = input("Enter role number").strip()

            role_dict = {
                "1":"Batsman",
                "2":"Bowler",
                "3":"All Rounder",
                "4":"Wicket Keeper",
                "5":"Captain",
             }

            role = role_dict.get(role_choice)

            player = Player(player_name,role)
            
            team_1[player_name] = player

            # for player in team_1.values():
            #     print(player)

    
        
        team_name = input("Enter team name: ")
        team = Team(team_name, team_1)

        print("following are the team members")
        print(team)


    except Exception as e:
        print(f'Error while taking input for team players, Error is {e}')

def display_main_menu():
    print("----Cricket Game----")
    print("--Play Game--")
    print("--Exit--")


# def display_sub_menu():
#     print("Enter team players")



def validate_input():
    try:
        pass
    except Exception as e:
        print(e)