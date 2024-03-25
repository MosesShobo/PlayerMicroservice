import csv
import os
from flask import Flask

app = Flask(__name__)
# Prevent JSON from being reordered when rendered
app.json.sort_keys = False

#Using os.path.dirname to get the current directory and joining it with the filename (People.csv) to get the absolute file path. 
#I did this because when I tried to run tests from inside the tests directory, I got a file not found error
def get_csv_file_path():
    """
    :return: the absolute filepath of the csv file (People.csv).
    """
    current_working_directory_path = os.path.dirname(os.path.realpath(__file__))
    csv_file_path = os.path.join(current_working_directory_path, 'People.csv')
    return csv_file_path


def get_csv_data(csv_file):
    """
    :param csv_file: contains player records.
    :return: data from the csv file as a list of dictionaries or None if there's an error.
    """
    try:
        with open(csv_file, encoding='utf-8') as csv_file_handler:
            csv_reader = csv.DictReader(csv_file_handler)
            data = [row for row in csv_reader]
            return data
    except Exception:
        # if csv file is not found or error occurred while reading file
        return None


def find_player(playerID, players):
    """
    :param playerID: ID of player that is being searched.
    :param players: data of all players.
    :return: player if found, otherwise None.
    """
    for player in players:
        if player['playerID'].lower() == playerID.lower():
            return player
    return None


@app.route("/")
def home():
    """
    :return: welcome message at home route
    """
    return 'Hello, this is a Player DB Microservice made with Flask'


@app.route('/players', methods=['GET'])
def get_players():
    """
    :return: The records of all players in the csv file.
    """
    players_data = get_csv_data(get_csv_file_path())
    if players_data:
        return players_data, 200
    return 'No Content', 204


@app.route('/players/<string:playerID>', methods=['GET'])
def get_player(playerID):
    """
    :param playerID: ID of player to be returned.
    :return: player's details.
    """
    players_data = get_csv_data(get_csv_file_path())
    if not players_data:
        return 'Internal Server Error', 500
    player = find_player(playerID, players_data)
    if player:
        return player, 200
    return 'Not Found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('HTTP_PORT', '5000')))
