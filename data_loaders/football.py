import io
import pandas as pd
import requests
import time
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(dataa, *args, **kwargs):
    """
    Template for loading data from API
    """
    api_key = "6f159f8e4685b2d513dd9b68b3d22806"
    # Create a dictionary with the API key as a parameter
    headers = {'x-apisports-key': api_key}
    df_list = []
    years = dataa['Year'].unique().tolist()
    for year in years:
        i = 0

        for id, yea in zip(dataa['Team ID'], dataa['Year']):
            if yea == year:
                # print (id)
                # continue
                i += 1
                url = f'https://v3.football.api-sports.io/teams/statistics?league=39&season={year}&team={id}'

                response = requests.get(url,headers=headers)
                data = response.json()
                # print (data)

                # Extract the required data from the response body
                team_name = data["response"]["team"]["name"]
                fixtures = data["response"]["fixtures"]
                goals = data["response"]["goals"]
                lineups = data["response"]["lineups"]

                # Formation = []
                # Played_Formation = []
                # for lineup in lineups:
                #     Formation.append(lineup["formation"])
                #     Played_Formation.append(lineup["played"])
                
                Team = [team_name]
                Played_Home = [fixtures["played"]["home"]]
                Played_Away = [fixtures["played"]["away"]]
                Total_Played = [fixtures["played"]["total"]]
                Wins_Home = [fixtures["wins"]["home"]]
                Wins_Away =  [fixtures["wins"]["away"]]
                Total_Wins = [fixtures["wins"]["total"]]
                Draws_Home = [fixtures["draws"]["home"]]
                Draws_Away = [fixtures["draws"]["away"]]
                Total_Draws = [fixtures["draws"]["total"]]
                Losses_Home = [fixtures["loses"]["home"]]
                Losses_Away = [fixtures["loses"]["away"]]
                Total_Losses = [fixtures["loses"]["total"]]
                Goals_For_Home = [goals["for"]["total"]["home"]]
                Goals_For_Away = [goals["for"]["total"]["away"]]
                Total_Goals_For = [goals["for"]["total"]["total"]]
                Goals_Against_Home = [goals["against"]["total"]["home"]]
                Goals_Against_Away = [goals["against"]["total"]["away"]]
                Total_Goals_Against = [goals["against"]["total"]["total"]]
                Formation = tuple([lineup["formation"] for lineup in lineups])
                Played_Formation =  tuple([lineup["played"] for lineup in lineups])

                #print (Formation)
                # max_length = max(len(Formation), len(Played_Formation))

                # Team += [None] * (max_length - len(Team))
                # Played_Home += [None] * (max_length - len(Played_Home))
                # Played_Away += [None] * (max_length - len(Played_Away))
                # Total_Played += [None] * (max_length - len(Total_Played))
                # Wins_Home += [None] * (max_length - len(Wins_Home))
                # Wins_Away +=  [None] * (max_length - len(Wins_Away))
                # Total_Wins += [None] * (max_length - len(Total_Wins))
                # Draws_Home += [None] * (max_length - len(Draws_Home))
                # Draws_Away += [None] * (max_length - len(Draws_Away))
                # Total_Draws += [None] * (max_length - len(Total_Draws))
                # Losses_Home += [None] * (max_length - len(Losses_Home))
                # Losses_Away += [None] * (max_length - len(Losses_Away))
                # Total_Losses += [None] * (max_length - len(Total_Losses))
                # Goals_For_Home += [None] * (max_length - len(Goals_For_Home))
                # Goals_For_Away += [None] * (max_length - len(Goals_For_Away))
                # Total_Goals_For += [None] * (max_length - len(Total_Goals_For))
                # Goals_Against_Home += [None] * (max_length - len(Goals_Against_Home))
                # Goals_Against_Away += [None] * (max_length - len(Goals_Against_Away))
                # Total_Goals_Against += [None] * (max_length - len(Total_Goals_Against))
                
                # print (Team)
                # print (Formation)
                # print (Played_Formation)

                # Create a DataFrame from the extracted data
                df = pd.DataFrame({
                    "Team": Team ,
                    "Played (Home)": Played_Home ,
                    "Played (Away)": Played_Away,
                    "Total Played": Total_Played,
                    "Wins (Home)": Wins_Home,
                    "Wins (Away)": Wins_Away,
                    "Total Wins": Total_Wins,
                    "Draws (Home)": Draws_Home,
                    "Draws (Away)": Draws_Away,
                    "Total Draws":  Total_Draws,
                    "Losses (Home)": Losses_Home,
                    "Losses (Away)": Losses_Away,
                    "Total Losses": Total_Losses,
                    "Goals For (Home)": Goals_For_Home,
                    "Goals For (Away)": Goals_For_Away,
                    "Total Goals For": Total_Goals_For,
                    "Goals Against (Home)": Goals_Against_Home,
                    "Goals Against (Away)": Goals_Against_Away,
                    "Total Goals Against": Total_Goals_Against,
                    "Formation": [Formation],
                    "Games Played (Formation)": [Played_Formation],
                    "Season": [year]
                })
                df_list.append(df)
                if i == 10 or i == 20:
                    time.sleep(60)
    
    full_df = pd.concat(df_list, ignore_index=True)
    return full_df



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
