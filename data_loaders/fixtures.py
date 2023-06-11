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
    year = 2021
    api_key = "6f159f8e4685b2d513dd9b68b3d22806"
    # Create a dictionary with the API key as a parameter
    headers = {'x-apisports-key': api_key}

    url = 'https://v3.football.api-sports.io/fixtures/statistics?fixture=710556&team=42'
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
    
    # df = pd.json_normalize(fixture_data)
    # df['Ball Possession %'] = df['Ball Possession'].str.rstrip('%')
    # df['Passes %'] = df['Passes %'].str.rstrip('%')
    # df['value'] = df['value'].str.replace('%', '')

    #print(df)
    return df#pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
