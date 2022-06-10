## Structure ##

# Imports
from kats.consts import TimeSeriesData
from kats.detectors.cusum_detection import CUSUMDetector
from kats.detectors.outlier import OutlierDetector
import pandas as pd


# Functions
def import_data(file_path):
    return pd.read_csv(file_path)

def list_of_team_names(data, team_field='Team_Name'):
    return data[team_field].unique().tolist()

def create_team_ts(data, team_name='MINNESOTA TIMBERWOLVES', age_field='Average_Age_by_Total_Min', team_field='Team_Name', date_field='date'):
    data = data[[team_field, age_field, date_field]]
    # reduce to specific team and remove field
    data = data[data[team_field]==team_name]
    data = data[[age_field, date_field]]

    # confirm data is ordered by date
    data[date_field] = data[date_field].astype('datetime64[ns]')
    data = data.sort_values(date_field, ascending=True)

    # set time-series df
    ts = TimeSeriesData(df=data, time_col_name=date_field)
    return ts








if __name__ == '__main__':
    print('execution started')

    # data ingestion
    df = import_data('data/21_22_age_tracking.csv')

    # obtain list of teamn names
    team_names = list_of_team_names(df) #<<<<----- use this to loop later ... maybe loop through. if an anonmaly is detected, i can print the graph and any available summary stats. 
    ####  cont.... I can then loop through each team and each metric. Print each to its own folder ('detected_anomalies/by_minute', 'detected_anomalies/by_usage, 'detected_anomalies/by_age')
    ####  cont....I can also print a quick comparison DF to see if any teams appear in one folder but not another (along with a quick list of what teams are listed in general)
    ####  cont.... eventually, i could implement this into the site possibly?

    # data prep by team / field
    MIN_df = create_team_ts(df, 'MINNESOTA TIMBERWOLVES', 'Average_Age_by_Total_Min')
    print(MIN_df)



