# data_processing.py
import pandas as pd


def save_data(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def load_data(file_path):
    return pd.read_csv(file_path)

#Calculaing winrate and duration of matches
def calculate_metrics(match_data):
    win_rate = match_data['win'].mean() * 100
#Converting seconds to minutes
    average_duration = (match_data['duration'].mean())/60
#Rounding to 2 decimal places
    average_duration = round(average_duration,2)
    return win_rate, average_duration

def feature_engineering(match_data):
    match_data['kda'] = (match_data['kills'] + match_data['assists']) / (match_data['deaths'].replace(0, 1))
    return match_data