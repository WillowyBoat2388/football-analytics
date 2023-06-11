import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    api_key = "6f159f8e4685b2d513dd9b68b3d22806"
    # Create a dictionary with the API key as a parameter
    headers = {'x-apisports-key': api_key}

    url = 'https://v3.football.api-sports.io/teams?country=England&league=39&season=2021'
    response = requests.get(url,headers=headers)
    data = response.json()

    data_body = data['response']


    id = []
    for entry in data_body:            
        for teams, content in entry.items():
            if teams == 'team':
                for item, contents in content.items():
                    if item == 'id':
                        id.append(contents)
    

    df = pd.DataFrame(id, columns=['Team ID'])
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
