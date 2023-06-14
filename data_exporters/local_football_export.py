from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.file import FileIO
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to filesystem.

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    file_path = path.join(get_repo_path(), 'output/PL_team_statistics_2021&22.csv')
    #filepath = r'C:\Users\Asus\Documents\Github\football-analytics\output\Asenal_statistics.csv'
    FileIO().export(df, file_path)
