import json


def test_get_players(client):
    """
    Test the '/players' endpoint to retrieve the records of all players.
    :param client: Flask test client
    :return: None
    """
    response = client.get('/players')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    result = json.loads(response.data)
    assert result[1]['playerID'] == 'aaronha01'
    assert result[1898]['birthYear'] == '1931'
    num_records = len(result)
    assert num_records == 19370


def test_get_player(client):
    """
    Test the '/players/{playerID}' endpoint to retrieve a single player by ID.
    :param client: Flask test client
    :return: None
    """
    response = client.get('/players/aardsda01')
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result['nameGiven'] == 'David Allan'


def test_get_player_that_does_not_exist(client):
    """
    Test the '/players/{playerID}' endpoint with a player ID that does not exist.
    :param client: Flask test client
    :return: None
    """
    response = client.get('/players/aardsda01010101')
    assert response.status_code == 404
