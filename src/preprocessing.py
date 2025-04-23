"""
Preprocessing module for Market Basket Analysis
- Cleans dataset
- Handles missing values
- Prepares data for association rule mining
"""

import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)
    df['Price'] = df['Price'].astype(str).str.replace(',', '').astype(float)
    df['Country'] = df['Country'].str.strip()
    return df

def encode_transactions(df, item_column='Itemname'):
    transactions = df[item_column].str.split(',')
    all_items = sorted(set(item for sublist in transactions for item in sublist))
    
    encoded_df = pd.DataFrame(0, index=df.index, columns=all_items)
    for idx, items in enumerate(transactions):
        encoded_df.loc[idx, [item for item in items if item in encoded_df.columns]] = 1
    return encoded_df
