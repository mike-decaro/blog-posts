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
    output_dict = {}
    for player in input_list:
        # Initialize an empty dictionary for the player
        player_dict = {}
        name = f"{player['first_name']} {player['last_name']}"
        for team in player['teams']:
            # Since we calculate stats within a team, reset OPS for each new team
            ops_sum = 0
            plate_app = 0
            for year in team['years']:
                for position in year['positions']:
                    # Only modify the OPS given the position matches our input
                    if position['position'] == pos:
                        ops_sum = ops_sum + position['ops'] * position['pa']
                        plate_app = plate_app + position['pa']
            # Only create an entry in the player dict if there were
            # PAs for the team at the position in question
            if plate_app > 0:
                player_dict[team['team']] = ops_sum / plate_app
        output_dict[name] = player_dict
    return output_dict

def populate_position_ops_dict(input_dict, pos):
    '''
    Given a player and a position, return a dictionary
    that includes their OPS for every team at that position
    '''
    output_dict = {}
    for player, player_dict in input_dict.items():
        # Initialize an empty dictionary for the player
        player_output_dict = {}
        name = f"{player_dict['first_name']} {player_dict['last_name']}"
        for team, team_dict in player_dict['team'].items():
            # Since we calculate stats within a team, reset OPS for each new team
            plate_app = 0
            ops_sum = 0
            for year, year_dict in team_dict.items():
                if year_dict.get(pos):
                # Only modify the OPS given the position matches our input
                    plate_app = plate_app + year_dict.get(pos).get('pa')
                    ops_sum = ops_sum + (year_dict.get(pos).get('ops') * year_dict.get(pos).get('pa'))
            # Only create an entry in the player dict if there were
            # PAs for the team at the position in question
            if plate_app > 0:
                player_output_dict[team] = ops_sum / plate_app
        output_dict[name] = player_output_dict
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
