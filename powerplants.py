import pandas as pd
import os
from datetime import datetime

class PowerPlants:
    def __init__(self, database_file='Coding Challenge Database.csv'):
        self.database_file = database_file

    def _standardize_data(self, df):
        df = df.copy()
        df.columns = df.columns.str.strip()  # clean weird column headers
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
        df['date'] = df['Date'].dt.date
        df['updatetime'] = datetime.now()
        df['updatedby'] = 'petroineos'

        country_map = {'FR': 'France', 'GB': 'United Kingdom'}
        df['country'] = df['Country'].map(country_map).fillna(df['Country'])

        return df[['Date', 'Country', 'Technology', 'SiteName', 'Volume', 'country', 'date', 'updatedby', 'updatetime']]

    def load_new_data_from_file(self, file_path: str):
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        return self._standardize_data(df)

    def save_new_data(self, input_data: pd.DataFrame):
        if os.path.exists(self.database_file):
            existing = pd.read_csv(self.database_file, parse_dates=['Date', 'updatetime'])
            combined = pd.concat([existing, input_data], ignore_index=True)
            combined.sort_values('updatetime', ascending=False, inplace=True)
            combined = combined.drop_duplicates(subset=['SiteName', 'date'], keep='first')
        else:
            combined = input_data

        combined.to_csv(self.database_file, index=False)

    def get_data_from_database(self):
        df = pd.read_csv(self.database_file, parse_dates=['Date', 'updatetime'])
        df.sort_values('updatetime', ascending=False, inplace=True)
        latest = df.drop_duplicates(subset=['SiteName'], keep='first')
        return latest

    def aggregate_data_to_monthly(self):
        df = pd.read_csv(self.database_file)
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date'])
        df['Month'] = df['Date'].dt.to_period('M')
        grouped = df.groupby(['SiteName', 'Month'])['Volume'].agg(['mean', 'min', 'max']).reset_index()
        grouped.rename(columns={'mean': 'avg_volume', 'min': 'min_volume', 'max': 'max_volume'}, inplace=True)
        return grouped

    def aggregate_data_to_country(self):
        df = pd.read_csv(self.database_file)
        grouped = df.groupby(['country', 'Technology'])['Volume'].sum().reset_index()
        grouped.rename(columns={'Volume': 'total_production'}, inplace=True)
        return grouped

