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
    years = ['2021', '2022']
    
    api_key = "6f159f8e4685b2d513dd9b68b3d22806"
    # Create a dictionary with the API key as a parameter
    headers = {'x-apisports-key': api_key}
    id = []
    for year in years:    
        url = f'https://v3.football.api-sports.io/fixtures?league=39&season={year}&team=42'
        response = requests.get(url, headers=headers)
        data = response.json()
        
        #team_name = data['response']['team']
        data_body = data['response']

        for response in data_body:
            #print (response)
            for fixtures, content in response.items():
                if fixtures == 'fixture':
                    for item, contents in content.items():
                        if item == 'id':
                            id.append([contents,year])

    df = pd.DataFrame(id, columns=['Fixture ID', 'Year'])
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
