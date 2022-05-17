import json



# Find the total OPS for first basemen, by team they played for
def populate_position_ops_list(player, pos):
    '''
    Given a player and a position, return a dictionary
    that includes their OPS for every team at that position
    '''
    # Initialize an empty dictionary for the player
    player_dict = {}
    for team in player['teams']:
        # Since we calculate stats within a team, reset OPS for each new team
        ops_sum = 0
        plate_app = 0
        for year in team['years']:
            for position in year['positions']:
                # Only modify the OPS given the position matches out input
                if position['position'] == pos:
                    ops_sum = ops_sum + position['ops']*position['pa']
                    plate_app = plate_app + position['pa']
        # Only create an entry in the player dict if there were
        # PAs for the team at the position in question
        if plate_app > 0:
            ops_total = ops_sum / plate_app
            player_dict[team['team']] = ops_total
    # Only return the player dict if there if the player ever appeared at the position
    if player_dict:
        return {f"{player['first_name']} {player['last_name']}": player_dict}

def populate_position_ops_dict(dict, pos):
    for player, player_dict in dict.items():
        print(player)
        name = f"{player_dict['first_name']} {player_dict['last_name']}"
        print(name)
        for team, team_dict in player_dict['team'].items():
            print(team)
            for year, year_dict in team_dict.items():
                print(year)
                print(year_dict)

if __name__ == '__main__':
    first_basemen = {}
    # with open('bb_data_list_maps.json', 'r') as f_list:
    #     json_list_data = json.loads(f_list.read())
    # for p in json_list_data:
    #     print(populate_position_ops_list(p, '1b'))
    
    with open('bb_data_dict.json', 'r') as f_dict:
        json_dict_data = json.load(f_dict)
        print(json_dict_data)
    populate_position_ops_dict(json_dict_data, '1b')

