import sqlite3
import pandas as pd
import os


def create_dataframe(path):
    """
    This function reads in the class.db database at the given path
    and returns all the tables as a single dataframe.

    Parameters
    ----------
    path : string
        Path to the class.db database file.

    Returns
    -------
    DataFrame with columns 'video_id', 'category_id', 'language'
    """
    if not os.path.exists(path):
        raise ValueError('Cannot find a file at ' + str(path))

    connection = sqlite3.connect(path)
    languages = ['US', 'FR', 'GB', 'DE', 'CA']

    dfs = []
    for lang in languages:
        sql_string = 'SELECT video_id, category_id FROM ' + lang + 'videos;'
        df = pd.read_sql(sql_string, connection)
        df['language'] = lang
        dfs.append(df)

    return pd.concat(dfs)
