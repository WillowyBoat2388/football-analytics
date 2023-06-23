import io
import pandas as pd
import requests
import json
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
    
    url = 'https://v3.football.api-sports.io/teams/statistics?league=39&season=2021&team=42'

    response = requests.get(url,headers=headers)
    data = response.json()
    data_body = data['response']

    df = pd.DataFrame([data_body])

    return df
    #return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
