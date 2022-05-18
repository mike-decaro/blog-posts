'''
imports
'''
import json



# Find the total OPS for first basemen, by team they played for
def populate_position_ops_list(input_list, pos):
    '''
    Given a player and a position, return a dictionary
    that includes their OPS for every team at that position
    '''
    # Initialize an empty dictionary for the player
    output_dict = {}
    for player in input_list:
        player_dict = {}
        name = f"{player['first_name']} {player['last_name']}"
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
        output_dict[name] = player_dict
    return output_dict

def populate_position_ops_dict(input_dict, pos):
    '''
    A docstring
    '''
    # Initialize an empty dictionary for the player
    output_dict = {}
    for player, player_val in input_dict.items():
        player_dict = {}
        name = f"{player_val['first_name']} {player_val['last_name']}"
        for team, team_dict in player_val['team'].items():
        # Since we calculate stats within a team, reset OPS for each new team
            plate_app = 0
            ops = 0
            for year, year_dict in team_dict.items():
                # Only modify the OPS given the position matches out input
                plate_app = plate_app + year_dict.get(pos).get('pa')
                ops = ops + (year_dict.get(pos).get('ops') * year_dict.get(pos).get('pa'))
            ops_total = ops / plate_app
            player_dict[team] = ops_total
        output_dict[name] = player_dict
    return output_dict

if __name__ == '__main__':
    with open('bb_data_list_maps.json', 'r', encoding = 'utf-8') as f_list:
         json_list_data = json.loads(f_list.read())
    first_basemen_list = populate_position_ops_list(json_list_data, '1b')
    print(first_basemen_list)

    with open('bb_data_dict.json', 'r', encoding = 'utf-8') as f_dict:
        json_dict_data = json.load(f_dict)
    first_basemen_dict = populate_position_ops_dict(json_dict_data, '1b')
    print(first_basemen_dict)
