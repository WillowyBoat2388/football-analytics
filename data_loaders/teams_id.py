import io
import pandas as pd
import requests
from mage_ai.data_preparation.shared.secrets import get_secret_value
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    api_key = get_secret_value('API_Key')
    # Create a dictionary with the API key as a parameter
    headers = {'x-apisports-key': api_key}
    years = ['2021', '2022']
    id = []
    for year in years:
        url = f'https://v3.football.api-sports.io/teams?country=England&league=39&season={year}'
        response = requests.get(url,headers=headers)
        data = response.json()

        data_body = data['response']

        for entry in data_body:            
            for teams, content in entry.items():
                if teams == 'team':
                    for item, contents in content.items():
                        if item == 'id':
                            id.append([contents, year])

    df = pd.DataFrame(id, columns=['Team ID', 'Year'])
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
