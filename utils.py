def validate_input(prompt, data_type, min_value=None, max_value=None, allowed_values=None):

    while True:
        try:
            user_input = input(prompt)
            
            if data_type is int:
                user_input = int(user_input)
            elif data_type is float:
                user_input = float(user_input)
            elif data_type is str:
                if user_input.isalpha():
                    user_input = str(user_input).strip().lower()
                else:
                    raise ValueError

            if min_value is not None and user_input < min_value:
                print(f"Input must be greater than or equal to {min_value}.")
                continue
            if max_value is not None and user_input > max_value:
                print(f"Input must be less than or equal to {max_value}.")
                continue
            if allowed_values is not None and user_input not in allowed_values:
                print(f"Input must be one of: {allowed_values}.")
                continue

            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a value of type {data_type.__name__}.")
        except Exception as e:
             print(f"An unexpected error occurred while taking input: {e}")


def validate_player_selection(players, prompt, players_dict=None):

    while True:
        # Case 1: players is a dict {name: Player}
        if isinstance(players, dict):
            print("Available players:", [player.name for player in players.values()])
            player_name = validate_input(prompt, str)
            if player_name in players:
                return players[player_name]

        # Case 2: players is a list of names, lookup in players_dict
        elif isinstance(players, list):
            print("Available players:", players)
            player_name = validate_input(prompt, str)
            if player_name in players and players_dict and player_name in players_dict:
                return players_dict[player_name]

        print("Invalid player name! Please select a valid player.")



def validate_ball_outcome():
    """Reusable function to validate and process ball outcome."""
    while True:
        outcome = input("Enter runs scored (or 'W' for Wicket, 'WD' for Wide, 'NB' for No ball): ")
        if outcome in ['W', 'WD', 'NB', 'w', 'wd', 'nb']:
            return outcome.upper()
        elif outcome.isdigit() and 0 <= int(outcome) <= 6:
            return int(outcome)
        else:
            print("Invalid input! Please enter a valid outcome.")
