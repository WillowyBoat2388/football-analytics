import io
import pandas as pd
import requests
import time
from mage_ai.data_preparation.shared.secrets import get_secret_value
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(dataa, *args, **kwargs):
    """
    Template for loading data from API
    """
    # years = ['2021', '2022']
    # year = 2021
    api_key = get_secret_value('API_Key')
    # Create a dictionary with the API key as a parameter
    headers = {'x-apisports-key': api_key}
    
    # years = dataa['Year'].unique().tolist()
    list_df = []
    i = 0
    for id, year in zip(dataa['Fixture ID'], dataa['Year']):
        i += 1   
        url = f'https://v3.football.api-sports.io/fixtures/statistics?fixture={id}&team=42'
        response = requests.get(url, headers=headers)
        data = response.json()
        
        #team_name = data['response']['team']
        data_body = data['response']
        fixture_data = data_body[0]['statistics']

        columns = [item['type'] for item in fixture_data]
        values = [item['value'] for item in fixture_data]
        #print (values)
        t = {val:valu for val, valu in zip(columns,values)}
        #df = pd.DataFrame.from_records(values, columns=columns, dtype = 'str')
        df = pd.DataFrame(t, index = [0])
        df['Season'] = year
        df['Fixture'] = id
        # df = pd.json_normalize(fixture_data)
        # df['Ball Possession %'] = df['Ball Possession'].str.rstrip('%')
        # df['Passes %'] = df['Passes %'].str.rstrip('%')
        # df['value'] = df['value'].str.replace('%', '')

        #print(df)
        list_df.append(df)
        if i % 10 == 0:
            time.sleep(60)
            i = 0
    fixture_df = pd.concat(list_df, ignore_index=True)
    return fixture_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
