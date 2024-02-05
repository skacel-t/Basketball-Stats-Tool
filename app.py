import constants
import copy
import random


def clean_player_data():
    players = []
    for index, player in enumerate(constants.PLAYERS,0):
        players.append({})
        players[index]['name'] = player['name']
        players[index]['guardians'] = player['guardians'].split(' and ')
        if player['experience'] == 'YES':
            players[index]['experience'] = True
        else:
            players[index]['experience'] = False
        players[index]['height'] = int(player['height'][0:2])
    return players


def experience_sorter(experience):
    new_list = [player for player in players_copy if player['experience'] == experience]
    return new_list


def balance_teams():
    while bool(sorted_players) == True:
        for team in teams_dict:
            #this stops errors in case the number of players is not divisible by number of teams
            if bool(sorted_players) == False:
                break
            teams_dict[team].append(sorted_players.pop())


def display_stats(user_input):
    print(f'\nTeam name: {user_input}')
    print(f'Number of players: {len(teams_dict[user_input])}')
    print(f"Player names: {', '.join([player['name'] for player in teams_dict[user_input]])}")
    num_experienced_players = sum((1 for player in teams_dict[user_input] if player['experience'] == True))
    print(f"Number of experienced players: {num_experienced_players}")
    print(f"Number of inexperienced players: {len(teams_dict[user_input]) - num_experienced_players}")
    average_height = sum((player['height'] for player in teams_dict[user_input]))/len(teams_dict[user_input])
    print(f"Average height: {round(average_height,1)} inches")
    print(f"Guardian names: {', '.join([', '.join(player['guardians']) for player in teams_dict[user_input]])}\n") 


def menu():
    while True:
        print("""------------------------------------------- 
Teams: {}. 
-------------------------------------------""".format(', '.join([team for team in constants.TEAMS])))
        user_input = input('1. To display team stats enter the team name. \n2. Enter QUIT to quit the app. \n')
        user_input = user_input.capitalize()
        if user_input == 'Quit':
                print('Goodbye!')
                break
        try:
            if user_input not in teams_copy:
                raise Exception('\nOh no! Invalid entry, please try again.')
            display_stats(user_input)
        except Exception as err:
            print(err)


#Running the program:
if __name__ == "__main__":
    #create a copy of the teams and players lists and clean them
    teams_copy = [team.capitalize() for team in constants.TEAMS]
    players_copy = clean_player_data()
    #create a dictionary to store team names and the players on those teams
    teams_dict = {team:[] for team in teams_copy}
    #sort players by experience inside of our list, also adding randomness to player assignment
    experienced_players, inexperienced_players = experience_sorter(True), experience_sorter(False)
    random.shuffle(experienced_players)
    random.shuffle(inexperienced_players)
    sorted_players = experienced_players + inexperienced_players
    #distribute the players across teams
    balance_teams()
    #open user interface in console
    menu()
