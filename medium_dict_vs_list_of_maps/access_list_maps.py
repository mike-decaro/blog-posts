import json
with open('bb_data_list_maps.json', 'r') as f:
    json_data = json.loads(f.read())


# Find the total OPS for first basemen, by team they played for
def populate_position_ops(pos):
    # print(f"{i['id']}: {i['first_name']} {i['last_name']}")
    player_dict = {}
    for team in i['teams']:
        ops_sum = 0
        plate_app = 0
        for year in team['years']:
            for position in year['positions']:
                if position['position'] == pos:
                    ops_sum = ops_sum + position['ops']*position['pa']
                    plate_app = plate_app + position['pa']
        if plate_app > 0:
            ops_total = ops_sum / plate_app
            player_dict[team['team']] = ops_total
    if player_dict:
        return {f"{i['first_name']} {i['last_name']}": player_dict}

'''
{
    "Jeff Liefer": {
        "Chicago White Sox": ####,
        "Montreal Expos": ####
    }
}
'''

if __name__ == '__main__':
    first_basemen = {}
    for i in json_data:
        print(populate_position_ops('1b'))
