"""
    Process data
"""
import os
import pandas as pd


def intermediate_data():
    raw_dir = '../data/raw'
    inter_dir = '../data/interim'
    for file in os.listdir(raw_dir):
        if file.endswith(".csv"):
            dataset = pd.read_csv(f'{raw_dir}/{file}')
            if file == 'device.csv' or file == 'logon.csv':
                dataset.to_csv(f'{inter_dir}/{file}', index=False)
            elif file == 'file.csv':
                dataset.drop(columns='content', inplace=True)
                dataset.to_csv(f'{inter_dir}/{file}', index=False)
            elif file == '2009-12.csv':
                dataset = dataset[['user_id', 'role']]
                dataset.to_csv(f'{inter_dir}/users.csv', index=False)
            elif file == 'r4.1-3.csv':
                dataset = pd.DataFrame(dataset.to_numpy())
                dataset = dataset[[0, 1, 2, 3, 4, 5]]
                dataset = dataset.loc[dataset[0] != 'email'].loc[dataset[0] != 'http'].reset_index(drop=True)
                dataset.rename(columns={0: "type", 1: "id", 2: "date", 3: "user", 4: "pc", 5: "activity"}, inplace=True)
                dataset.to_csv(f'{inter_dir}/insider.csv', index=False)