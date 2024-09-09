import pandas as pd
import re
from collection import load_data_from_db
from loguru import logger

def prepare_data():
    logger.info("starting up preprocessing pipeline")
    # 1. Load Dataset
    data = load_data_from_db()
    # 2. Encode Categorical Columns
    data_encoded = encode_cat_cols(data)
    # 3. Parse garden column
    df = parse_garden_col(data_encoded)
    return df

def encode_cat_cols(data):
    cols = ['balcony', 'storage', 'parking', 'furnished', 'garage']
    logger.info(f"encoding categorical columns: {cols}")
    return pd.get_dummies(
        data, 
        columns=cols, 
        drop_first=True)

def parse_garden_col(data):
    for i in range(len(data)):
        if data.loc[i, "garden"] == 'Not present':
            data.loc[i, "garden"] = 0
        else:
            data.loc[i, "garden"] = int(re.findall(r'\d+', data.garden[i])[0])
    return data
